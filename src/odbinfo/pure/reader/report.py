""" reading reports """
from typing import List, Tuple
from xml.dom.minidom import Element
from zipfile import ZipFile

from odbinfo.pure.datatype.ui import Report
from odbinfo.pure.reader.common import attr_default, get_elements_from_href


def office_report_elements(odbzip) -> List[Tuple[str, Element]]:
    """Returns a list off the name and <office:report> element for all reports"""
    db_reports_elements = get_elements_from_href(odbzip, "", "db:reports")
    if not db_reports_elements:
        return []

    db_component_elements = db_reports_elements[0].getElementsByTagName(
        "db:component")

    return [(db_component.getAttribute("db:name"),
             get_elements_from_href(odbzip,
                                    db_component.getAttribute("xlink:href"),
                                    "office:report")[0])
            for db_component in db_component_elements]


def get_report_formulas(office_report_element: Element) -> List[str]:
    """Returns the report formulas in `office_report_element`"""
    return [
        elem.getAttribute("rpt:formula") for elem in
        office_report_element.getElementsByTagName("rpt:formatted-text")
    ]


def read_reports(odbzip: ZipFile) -> List[Report]:
    """ Returns a list of Reports read reports from `odbzip` zipfile """
    reports = []
    for name, office_report_element in office_report_elements(odbzip):
        reports.append(
            Report(
                name, office_report_element.getAttribute("rpt:command"),
                attr_default(office_report_element, "rpt:command-type",
                             "command"),
                office_report_element.getAttribute("office:mimetype"),
                get_report_formulas(office_report_element)))
    return reports
