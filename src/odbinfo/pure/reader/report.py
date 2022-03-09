""" reading reports """
from typing import List, Tuple
from xml.dom.minidom import Element

from odbinfo.pure.datatype.ui import Report
from odbinfo.pure.reader.common import (CONTENT_XML, attr_default,
                                        document_element)


def _reports(odbzip) -> List[Tuple[str, Element]]:
    odb_elem = document_element(odbzip, CONTENT_XML)
    db_report_elements = odb_elem.getElementsByTagName("db:reports")
    if not db_report_elements:
        return []
    db_reports = db_report_elements[0].getElementsByTagName("db:component")

    def report(rpt_elem) -> Tuple[str, Element]:
        relpath = rpt_elem.getAttribute("xlink:href") + "/content.xml"
        return (rpt_elem.getAttribute("db:name"),
                document_element(
                    odbzip, relpath).getElementsByTagName("office:report")[0])

    return [report(rpt_elem) for rpt_elem in db_reports]


def _read_report_formulas(rpt_doc: Element) -> List[str]:
    return [
        elem.getAttribute("rpt:formula")
        for elem in rpt_doc.getElementsByTagName("rpt:formatted-text")
    ]


def read_reports(odbzip) -> List[Report]:
    """ Read reports from odb file """
    reports = []
    for name, rpt_doc in _reports(odbzip):
        reports.append(
            Report(name, rpt_doc.getAttribute("rpt:command"),
                   attr_default(rpt_doc, "rpt:command-type", "command"),
                   rpt_doc.getAttribute("office:mimetype"),
                   _read_report_formulas(rpt_doc)))
    return reports
