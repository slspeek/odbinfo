" ui classes test "

from odbinfo.pure.datatype import LinkedString, Report


def test_report_constructor() -> None:
    report = Report("plants_report",
                    LinkedString("plant"),
                    "table",
                    "doc", [])
    assert report
    # print(report)
