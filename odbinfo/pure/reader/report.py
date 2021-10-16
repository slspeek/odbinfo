" reading reports "
from typing import List

from odbinfo.pure.datatype import Report
from odbinfo.pure.reader.common import (_body_elem, _collect_attribute,
                                        mapiflist)


def _reports(odbzip):
    index = _body_elem(odbzip, "content.xml")["office:database"]
    if "db:reports" not in index:
        return []
    index = index["db:reports"]
    dbcomponent = index["db:component"]

    def report(rpt):
        relpath = rpt["@xlink:href"] + "/content.xml"
        info = _body_elem(odbzip, relpath)["office:report"]
        return (rpt["@db:name"], info)

    return mapiflist(report, dbcomponent)


def read_reports(odbzip) -> List[Report]:
    " Read reports from odb file "
    reports = []
    for name, info in _reports(odbzip):
        reports.append(Report(name,
                              info["@rpt:command"],
                              info.get("@rpt:command-type", "command"),
                              info.get("@office:mimetype", ""),
                              _read_report_formulas(info))
                       )
    return reports


def _read_report_formulas(info) -> List[str]:
    return _collect_attribute(info, "@rpt:formula")
