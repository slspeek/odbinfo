" ui classes test "

from odbinfo.pure.datatype import Report


def test_report_constructor() -> None:
    report = Report("plants_report",
                    "plant",
                    "table",
                    "doc", [])
    assert report
    # print(report)
