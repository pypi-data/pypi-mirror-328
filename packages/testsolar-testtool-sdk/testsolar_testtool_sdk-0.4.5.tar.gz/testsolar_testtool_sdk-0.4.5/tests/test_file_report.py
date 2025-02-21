import concurrent.futures
import tempfile
from functools import partial
from pathlib import Path

from testsolar_testtool_sdk.file_reader import (
    read_file_load_result,
    read_file_test_result,
)
from testsolar_testtool_sdk.model.test import TestCase
from testsolar_testtool_sdk.model.testresult import (
    ResultType,
)
from testsolar_testtool_sdk.reporter import FileReporter, LOAD_RESULT_FILE_NAME
from .prepare_data import generate_demo_load_result, send_test_result


def test_report_load_result_with_file() -> None:
    # 创建一个Reporter实例

    with tempfile.TemporaryDirectory() as tmpdir:
        result_file_path = Path(tmpdir) / LOAD_RESULT_FILE_NAME
        reporter = FileReporter(result_file_path)
        # 创建一个LoadResult实例
        load_result = generate_demo_load_result()

        # 调用report_load_result方法
        reporter.report_load_result(load_result)

        re = read_file_load_result(result_file_path)

        assert re == load_result


def test_report_run_case_result_with_file():
    # 创建一个Reporter实例
    with tempfile.TemporaryDirectory() as tmpdir:
        reporter = FileReporter(report_path=Path(tmpdir))
        # 创建五个LoadResult实例并发调用report_run_case_result方法
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            send_action = partial(send_test_result, reporter)
            for i in range(5):
                executor.submit(send_action, i)

        for i in range(5):
            r = read_file_test_result(
                Path(tmpdir), TestCase(Name=f"mumu/mu.py/test_case_name_{i}_p1")
            )
            assert r.ResultType == ResultType.SUCCEED


def test_report_run_case_result_with_junit_xml():
    with tempfile.TemporaryDirectory() as tmpdir:
        reporter = FileReporter(report_path=Path(tmpdir))
        xml_file_name = str(Path(__file__).parent.joinpath("testdata/test.xml"))
        reporter.report_junit_xml(xml_file_name)
        r = read_file_test_result(Path(tmpdir), TestCase(Name="test_normal_case?test_success"))
        assert r.ResultType == ResultType.SUCCEED
        assert r.Test.Name == "test_normal_case?test_success"
        r = read_file_test_result(Path(tmpdir), TestCase(Name="test_normal_case?test_failed"))
        assert r.ResultType == ResultType.FAILED
        assert r.Test.Name == "test_normal_case?test_failed"
        assert r.Message
        assert r.Steps[0].Logs[0].Content
        r = read_file_test_result(Path(tmpdir), TestCase(Name="test_normal_case?test_raise_error"))
        assert r.ResultType == ResultType.FAILED
        assert r.Test.Name == "test_normal_case?test_raise_error"
        assert r.Message
