from datetime import datetime, timedelta
import random
from testsolar_testtool_sdk.model.load import LoadResult, LoadError
from testsolar_testtool_sdk.model.test import TestCase
from testsolar_testtool_sdk.model.testresult import (
    TestResult,
    ResultType,
    TestCaseLog,
    LogLevel,
    TestCaseAssertError,
    TestCaseStep,
)
from testsolar_testtool_sdk.reporter import BaseReporter
from xml.etree.ElementTree import Element, SubElement, tostring


def generate_demo_load_result() -> LoadResult:
    r: LoadResult = LoadResult(Tests=[], LoadErrors=[])

    for x in range(40):
        r.Tests.append(TestCase(Name=f"mumu/mu.py/test_case_name_{x}_p1", Attributes={"tag": "P1"}))

    for x in range(20):
        r.LoadErrors.append(
            LoadError(
                name=f"load error {x}",
                message="""
文件读取失败。可能的原因包括：文件不存在、文件损坏、
不正确的编码方式或其他未知错误。请检查文件路径和内容的正确性，
确保文件具有正确的编码格式。如果问题仍然存在，可能需要尝试其他解决方法

"en": "File not found. Please check the file path and try again.",
"zh": "文件未找到。请检查文件路径，然后重试。",
"ja": "ファイルが見つかりません。ファイルパスを確認して、もう一度試してください。",
"ko": "파일을 찾을 수 없습니다. 파일 경로를 확인하고 다시 시도하십시오.",
"it": "File non trovato. Controlla il percorso del file e riprova.",
"ar": "الملف غير موجود. يرجى التحقق من مسار الملف والمحاولة مرة أخرى.",
"th": "ไม่พบไฟล์ โปรดตรวจสอบเส้นทางไฟล์และลองอีกครั้ง",
        """,
            )
        )
    return r


def generate_test_result(index: int) -> TestResult:
    start: datetime = datetime.utcnow() - timedelta(seconds=40)
    _tr = TestResult(
        Test=TestCase(Name=f"mumu/mu.py/test_case_name_{index}_p1", Attributes={}),
        StartTime=start,
        EndTime=datetime.utcnow(),
        ResultType=ResultType.SUCCEED,
        Message="ファイルが見つかりません。ファイルパスを確認して、もう一度試してください。",
        Steps=[generate_testcase_step(f"{index}_{x}") for x in range(10)],
    )

    return _tr


def generate_testcase_log(index: str) -> TestCaseLog:
    start: datetime = datetime.utcnow() - timedelta(seconds=15)

    return TestCaseLog(
        Time=start,
        Level=LogLevel.INFO,
        Attachments=[
            # Attachment(
            #     Name=f"access.log_{index}",
            #     Url=str(Path(__file__).parent.resolve().joinpath("test_access.log")),
            #     AttachmentType=AttachmentType.FILE,
            # ),
        ],
        AssertError=TestCaseAssertError(Expect="AAA", Actual="BBB", Message="AAA is not BBB"),
        Content=f"采集器：coll-imrv6szb当前状态为0，预期状态为1，状态不一致（0:处理中,1:正常） -> {get_random_unicode(20)}",
    )


def generate_testcase_step(index: str) -> TestCaseStep:
    start: datetime = datetime.utcnow() - timedelta(seconds=10)
    return TestCaseStep(
        StartTime=start,
        EndTime=datetime.utcnow(),
        Title=get_random_unicode(100),
        Logs=[generate_testcase_log(f"{index}_{x}") for x in range(100)],
        ResultType=ResultType.SUCCEED,
    )


def get_random_unicode(length) -> str:
    get_char = chr

    # Update this to include code point ranges to be sampled
    include_ranges = [
        (0x0021, 0x0021),
        (0x0023, 0x0026),
        (0x0028, 0x007E),
        (0x00A1, 0x00AC),
        (0x00AE, 0x00FF),
        (0x0100, 0x017F),
        (0x0180, 0x024F),
        (0x2C60, 0x2C7F),
        (0x16A0, 0x16F0),
        (0x0370, 0x0377),
        (0x037A, 0x037E),
        (0x0384, 0x038A),
        (0x038C, 0x038C),
    ]

    alphabet = [
        get_char(code_point)
        for current_range in include_ranges
        for code_point in range(current_range[0], current_range[1] + 1)
    ]
    return "".join(random.choice(alphabet) for i in range(length))


def send_test_result(reporter: BaseReporter, index=0):
    test_results = []
    run_case_result = generate_test_result(index)
    test_results.append(run_case_result)
    reporter.report_case_result(run_case_result)


def generate_junit_xml(file_path: str):
    root = Element("testsuite")
    testcase = SubElement(root, "testcase", classname="path.to.case", name="Test01", time="0.123")
    failure = SubElement(testcase, "failure", message="Test failed", type="AssertionError")
    failure.text = "Failure details"
    xml_data = tostring(root).decode()
    with open(file_path, "w") as f:
        f.write(xml_data)
