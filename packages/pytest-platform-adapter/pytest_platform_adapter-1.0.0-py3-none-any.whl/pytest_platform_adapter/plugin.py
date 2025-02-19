import asyncio
import json
import os
from typing import List, Optional

import requests
from allure_pytest.utils import allure_title
import logging
import pytest

logger = logging.getLogger('pytest-platform-adapter')
logger.setLevel(logging.INFO)

# 全局变量用于统计测试用例状态
test_stats = {
    'total': 0,
    'passed': 0,
    'failed': 0,
    'skipped': 0,
    'current': 0  # 当前已执行的用例数
}
milestone_counter = 10  # 里程碑计数器
failed_cases = set()  # 记录已标记为失败的用例
skipped_cases = set()  # 记录已标记为跳过的用例
cases_ids = set()  # 存放所有用例ID，用来检查是否有重复的
scan_enable = False  # 记录是否扫描模式，默认为False非扫描模式，True为扫描模式
platform_ip = None
platform_port = None
platform_path = None
pipeline_name = None
build_number = None
platform_use_https = False


def pytest_addoption(parser):
    group = parser.getgroup('platform-adapter', '自动化平台插件')
    group.addoption(
        '--case_ids',
        action='store',
        default=None,
        help='要执行的测试用例ID列表，使用逗号分隔，例如：19936,19930'
    )
    group.addoption(
        '--case_ids_file',
        action='store',
        default=None,
        help='包含测试用例ID的文件路径，文件中每行一个ID'
    )
    group.addoption(
        '--scan',
        action='store_true',
        default=False,
        help='扫描模式：快速生成 Allure 报告而不实际执行测试'
    )
    parser.addini(
        'platform_ip',
        help='自动化平台API IP',
        default=None
    )
    parser.addini(
        'platform_port',
        help='自动化平台API端口',
        default=None
    )
    parser.addini(
        'platform_path',
        help='自动化平台API Path',
        default='/api/autoplatform/task/refresh_data_count'
    )
    parser.addini(
        'platform_use_https',
        help='上报自动化平台时启用HTTPS，默认不启用',
        default=False
    )


def pytest_collection_modifyitems(config, items):
    """
    hook收集用例的过程，给--case_ids和--case_ids_file提供支持
    修改测试用例集合，根据提供的测试用例ID过滤测试用例
    """
    target_ids = get_target_test_ids(config)
    if not target_ids:
        test_stats['total'] = len(items)  # 更新总用例数
        return
    selected = []
    deselected = []
    for item in items:
        title = allure_title(item)
        test_id = get_test_id_from_title(title)
        if test_id in target_ids:
            selected.append(item)
        else:
            deselected.append(item)
        # 检测 ID 是否有重复，只是单纯的检查一下，不影响执行
        if test_id in cases_ids:
            # 为 None 在这里就不用打印log了，因为在 get_test_id_from_title 里面就会报错一次
            if test_id is None:
                continue
            logger.warning(f"测试用例ID {test_id} 重复")
        else:
            cases_ids.add(test_id)
    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = selected
    selected_ids = [get_test_id_from_title(allure_title(item)) for item in selected]
    test_stats['total'] = len(selected)  # 更新总用例数
    logger.info("目标测试用例ID (%d个): %s", len(target_ids), target_ids)
    logger.info("实际执行用例ID (%d个): %s", len(selected_ids), selected_ids)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    if item.config.getoption('--scan'):
        # logger.info(f"扫描模式：跳过执行测试用例 {allure_title(item)}")
        pytest.skip("扫描模式已启动，跳过执行测试用例")
    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup(item):
    if item.config.getoption('--scan'):
        # logger.info(f"扫描模式：跳过测试用例 {allure_title(item)}前置")
        pytest.skip("扫描模式已启动，跳过测试用例前置")
    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown(item):
    if item.config.getoption('--scan'):
        # logger.info(f"扫描模式：跳过测试用例 {allure_title(item)}后置")
        pytest.skip("扫描模式已启动，跳过测试用例后置")
    yield


@pytest.hookimpl
def pytest_runtest_logreport(report):
    """
    hook测试用例执行结果的输出过程
    """
    global milestone_counter, scan_enable, platform_ip, platform_port, platform_path, platform_use_https
    global pipeline_name, build_number
    # config = pytest.Config
    # my_option = config.getini("my_option")
    # 使用 report.nodeid 作为唯一标识
    nodeid = report.nodeid

    if report.when in ['setup', 'call', 'teardown']:
        # 记录失败状态，如果该用例任意阶段失败，则添加到 failed_cases
        if report.failed:
            failed_cases.add(nodeid)

        # 记录跳过状态，仅在 setup 阶段处理
        if report.skipped and report.when == 'setup':
            skipped_cases.add(nodeid)
            test_stats['skipped'] += 1

        # 仅在 teardown 阶段完成统计更新
        if report.when == 'teardown':
            test_stats['current'] += 1
            # 检查用例是否为失败、跳过或通过
            if nodeid in failed_cases:
                # TODO Xfail 应该计算为失败，但是不太对
                test_stats['failed'] += 1
            elif nodeid in skipped_cases:
                # 如果用例已跳过，不计为通过
                pass
            else:
                test_stats['passed'] += 1

            # 打印进度和统计信息
            progress = (test_stats['current'] / test_stats['total']) * 100 if test_stats['total'] != 0 else 0
            pass_rate = (test_stats['passed'] / (test_stats['total'] - test_stats['skipped'])) * 100 if (
                    (test_stats['total'] - test_stats['skipped']) != 0) else 0
            logger.info(
                f"pipeline_name:{pipeline_name}, build_number: {build_number}"
                f"用例进度: 总数 {test_stats['total']}, 跳过 {test_stats['skipped']}, 已执行 {test_stats['current']}, "
                f"失败 {test_stats['failed']}, 通过 {test_stats['passed']}, 进度 {progress:.2f}%, 通过率 {pass_rate:.2f}%"
            )

            # 当没有启用扫描模式、同时配置了平台的IP和端口的时候才回报给自动化平台
            if not scan_enable and platform_ip and platform_port:
                # 在执行前10个用例的时候，进度立即回报给平台进度。之后就是每隔10个用例再回报一次
                if test_stats['current'] <= 10 or test_stats['current'] % 10 == 0:
                    json_data = None
                    url = f"http://{platform_ip}:{platform_port}{platform_path}" if not platform_use_https \
                        else f"https://{platform_ip}:{platform_port}{platform_path}"
                    try:
                        json_data = {
                            'pipeline': pipeline_name,
                            'build_number': build_number,
                            'passed_case_count': test_stats['passed'],
                            'skipped_case_count': test_stats['skipped'],
                            'failed_case_count': test_stats['failed'],
                            'selected_case': test_stats['total'] }
                        headers = {'Content-Type': 'application/json'}
                        response = requests.post(url, data=json.dumps(json_data), headers=headers, timeout=3)
                        logger.info(f"已将数据回报给 {url}，"
                                    f"平台返回状态码：{response.status_code}，"
                                    f"响应体：{response.text}，请求体：{json_data}")
                    except Exception as e:
                        logger.info(f"将请求发送到 {url}"
                                    f"，请求体：{json_data} 错误信息：{e}")


def pytest_configure(config):
    global scan_enable, platform_ip, platform_port, platform_path
    global pipeline_name, build_number
    scan_enable, platform_ip, platform_port, platform_path, platform_use_https = config.getoption(
        '--scan'), config.getini('platform_ip'), config.getini('platform_port'), config.getini(
        'platform_path'), config.getini('platform_use_https')
    pipeline_name = os.environ.get("JOB_NAME")
    build_number = os.environ.get("BUILD_NUMBER")
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('自动化平台插件 - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    config.addinivalue_line(
        "markers",
        "allure_title: 使用allure标题标记测试用例"
    )


def get_test_ids_from_file(file_path: str) -> List[str]:
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def get_test_ids_from_option(ids_string: str) -> List[str]:
    case_id = []
    for id_ in ids_string.strip(',').split(','):
        id_strip = id_.strip()
        if not id_strip.isdigit():
            logger.error(f'存在无效的测试用例ID：{id_}')
            continue
        else:
            case_id.append(id_strip)
    return case_id


def get_target_test_ids(config) -> Optional[List[str]]:
    case_ids = config.getoption('--case_ids')
    case_ids_file = config.getoption('--case_ids_file')
    if case_ids:
        logger.info(f"接收到case_ids入参为：'{case_ids}'")
        return get_test_ids_from_option(case_ids)
    elif case_ids_file:
        logger.info(f"接收到case_ids_file入参为：'{case_ids_file}'")
        return get_test_ids_from_file(case_ids_file)
    return None


def get_test_id_from_title(title: Optional[str]) -> Optional[str]:
    if not title:
        return None
    match = title.split('-', 1)
    if len(match) != 2:
        logger.error(f'存在无法解析用例ID的用例，用例标题为：{title}')
        return None
    if match[0].isdigit():
        return match[0]
    else:
        logger.error(f'存在无法解析用例ID的用例，用例标题为：{title}')
        return None
