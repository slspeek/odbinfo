""" Reading reports from the odb-zipfile """
from typing import List
from xml.dom.minidom import Element
from zipfile import ZipFile

from odbinfo.pure.datatype.ui import Report
from odbinfo.pure.reader.common import attr_default, subdocuments_elements


def get_report_formulas(office_report_element: Element) -> List[str]:
    """Returns the report formulas in `office_report_element`"""
    return [
        elem.getAttribute("rpt:formula") for elem in
        office_report_element.getElementsByTagName("rpt:formatted-text")
    ]


def read_reports(odbzip: ZipFile) -> List[Report]:
    """ Returns a list of Reports read reports from `odbzip` zipfile """
    reports = []
    for name, office_report_element in subdocuments_elements(
            odbzip=odbzip,
            specified_by_tag="db:reports",
            desired_tag="office:report"):
        reports.append(
            Report(name=name,
                   cmd=office_report_element.getAttribute("rpt:command"),
                   cmdtype=attr_default(office_report_element,
                                        "rpt:command-type", "command"),
                   output_type=office_report_element.getAttribute(
                       "office:mimetype"),
                   formulas=get_report_formulas(office_report_element)))
    return reports
