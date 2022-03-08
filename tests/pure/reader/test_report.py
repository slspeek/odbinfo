""" test report reading """
import dataclasses
from unittest.mock import Mock

import pytest

from odbinfo.pure.reader.common import CONTENT_XML
from odbinfo.pure.reader.report import read_reports
from tests.pure.reader.test_common import OO_NAMESPACES, ZipFileMock


@pytest.mark.slow
def test_read_reports(odbzip, data_regression):
    """ reports """
    data_regression.check(
        [dataclasses.asdict(report) for report in read_reports(odbzip)])


@pytest.mark.slow
def test_read_reports_empty(empty_odbzip):
    """ read no reports """
    assert len(read_reports(empty_odbzip)) == 0


ODB_ELEMENT = f"""<?xml version="1.0" encoding="UTF-8"?>
<office:document-content {OO_NAMESPACES} office:version="1.2">
  <office:scripts/>
  <office:font-face-decls>
    <style:font-face style:name="F" svg:font-family=""/>
  </office:font-face-decls>
  <office:automatic-styles>
    <style:style style:name="co1" style:family="table-column"/>
    <style:style style:name="ce1" style:family="table-cell">
      <style:paragraph-properties fo:text-align="start"/>
    </style:style>
  </office:automatic-styles>
  <office:body>
    <office:database>
      <db:data-source>
        <db:connection-data>
          <db:connection-resource xlink:href="sdbc:embedded:hsqldb" xlink:type="simple"/>
          <db:login db:is-password-required="false"/>
        </db:connection-data>
        <db:driver-settings db:system-driver-settings="" db:base-dn="" db:parameter-name-substitution="false"/>
        <db:application-connection-settings db:is-table-name-length-limited="false" db:append-table-alias-name="false" db:max-row-count="100">
          <db:table-filter>
            <db:table-include-filter>
              <db:table-filter-pattern>%</db:table-filter-pattern>
            </db:table-include-filter>
          </db:table-filter>
          <db:data-source-settings>
            <db:data-source-setting db:data-source-setting-is-list="false" db:data-source-setting-name="Type" db:data-source-setting-type="string">
              <db:data-source-setting-value>simple</db:data-source-setting-value>
            </db:data-source-setting>
          </db:data-source-settings>
        </db:application-connection-settings>
      </db:data-source>
      <db:reports>
        <db:component db:name="Family" xlink:href="reports/Obj11" xlink:type="simple" db:as-template="false"/>
      </db:reports>
      <db:queries>
      </db:queries>
      <db:table-representations>
      </db:table-representations>
    </office:database>
  </office:body>
</office:document-content>
"""

RPT_ELEMENT = f"""<?xml version="1.0" encoding="UTF-8"?>
<office:document-content {OO_NAMESPACES} office:version="1.2">
  <office:font-face-decls>
    <style:font-face style:name="Liberation Sans" svg:font-family="&apos;Liberation Sans&apos;" style:font-family-generic="roman" style:font-pitch="variable"/>
  </office:font-face-decls>
  <office:automatic-styles>
    </office:automatic-styles>
  <office:body>
    <office:report rpt:command-type="table" rpt:command="Family" office:mimetype="application/vnd.oasis.opendocument.text" draw:name="Rapport">
      <rpt:page-header>
        <table:table table:name="Page header" table:style-name="ta1">
          <table:table-columns>
            <table:table-column table:style-name="co1"/>
          </table:table-columns>
          <table:table-row table:style-name="ro1">
            <table:table-cell table:number-columns-spanned="1">
              <text:p/>
            </table:table-cell>
          </table:table-row>
        </table:table>
      </rpt:page-header>
      <rpt:group rpt:sort-ascending="true" rpt:sort-expression="" rpt:group-expression="">
        <rpt:group-header>
          <table:table table:name="Groep koptekst" table:style-name="ta1">
            <table:table-columns>
              <table:table-column table:style-name="co2"/>
              <table:table-column table:style-name="co2"/>
              <table:table-column table:style-name="co2"/>
              <table:table-column table:style-name="co3"/>
            </table:table-columns>
            <table:table-row table:style-name="ro2">
              <table:table-cell table:style-name="ce1">
                <text:p>
                  <rpt:fixed-content>
                    <text:p>FamlilyID</text:p>
                    <rpt:report-element>
                      <rpt:report-component draw:name="Titelveld"/>
                    </rpt:report-element>
                  </rpt:fixed-content>
                </text:p>
              </table:table-cell>
              <table:table-cell table:style-name="ce1">
                <text:p>
                  <rpt:fixed-content>
                    <text:p>Name</text:p>
                    <rpt:report-element>
                      <rpt:report-component draw:name="Titelveld"/>
                    </rpt:report-element>
                  </rpt:fixed-content>
                </text:p>
              </table:table-cell>
              <table:table-cell table:style-name="ce1">
                <text:p>
                  <rpt:fixed-content>
                    <text:p>Desc</text:p>
                    <rpt:report-element>
                      <rpt:report-component draw:name="Titelveld"/>
                    </rpt:report-element>
                  </rpt:fixed-content>
                </text:p>
              </table:table-cell>
              <table:table-cell/>
            </table:table-row>
          </table:table>
        </rpt:group-header>
        <rpt:detail>
          <table:table table:name="Detail" table:style-name="ta1">
            <table:table-columns>
              <table:table-column table:style-name="co2"/>
              <table:table-column table:style-name="co2"/>
              <table:table-column table:style-name="co2"/>
              <table:table-column table:style-name="co3"/>
            </table:table-columns>
            <table:table-row table:style-name="ro2">
              <table:table-cell table:style-name="ce2">
                <text:p>
                  <rpt:formatted-text rpt:formula="field:[FamlilyID]">
                    <rpt:report-element>
                      <rpt:report-component draw:name="Opgemaakt veld"/>
                    </rpt:report-element>
                  </rpt:formatted-text>
                </text:p>
              </table:table-cell>
              <table:table-cell table:style-name="ce3" office:value-type="string">
                <text:p>
                  <rpt:formatted-text rpt:formula="field:[Name]">
                    <rpt:report-element>
                      <rpt:report-component draw:name="Opgemaakt veld"/>
                    </rpt:report-element>
                  </rpt:formatted-text>
                </text:p>
              </table:table-cell>
              <table:table-cell table:number-rows-spanned="2" table:style-name="ce3" office:value-type="string">
                <text:p>
                  <rpt:formatted-text rpt:formula="field:[Desc]">
                    <rpt:report-element>
                      <rpt:report-component draw:name="Opgemaakt veld"/>
                    </rpt:report-element>
                  </rpt:formatted-text>
                </text:p>
              </table:table-cell>
              <table:table-cell/>
            </table:table-row>
            <table:table-row table:style-name="ro3">
              <table:table-cell/>
              <table:table-cell/>
              <table:covered-table-cell/>
              <table:table-cell/>
            </table:table-row>
          </table:table>
        </rpt:detail>
      </rpt:group>
      <rpt:page-footer>
        <table:table table:name="Page footer" table:style-name="ta1">
          <table:table-columns>
            <table:table-column table:style-name="co1"/>
          </table:table-columns>
          <table:table-row table:style-name="ro1">
            <table:table-cell table:number-columns-spanned="1">
              <text:p/>
            </table:table-cell>
          </table:table-row>
        </table:table>
      </rpt:page-footer>
    </office:report>
  </office:body>
</office:document-content>
"""

data = {CONTENT_XML: ODB_ELEMENT, "reports/Obj11/content.xml": RPT_ELEMENT}


def test_reports():
    # pylint:disable=too-few-public-methods
    fakezip = ZipFileMock()

    def read(file: str) -> str:
        return data[file]

    fakezip.read = Mock(side_effect=read)
    assert len(read_reports(fakezip)) == 1


ODB_ELEMENT_NO_REPORTS = f"""<?xml version="1.0" encoding="UTF-8"?>
<office:document-content {OO_NAMESPACES} office:version="1.2">
  <office:scripts/>
  <office:font-face-decls>
    <style:font-face style:name="F" svg:font-family=""/>
  </office:font-face-decls>
  <office:automatic-styles>
    <style:style style:name="co1" style:family="table-column"/>
    <style:style style:name="ce1" style:family="table-cell">
      <style:paragraph-properties fo:text-align="start"/>
    </style:style>
  </office:automatic-styles>
  <office:body>
    <office:database>
      <db:data-source>
        <db:connection-data>
          <db:connection-resource xlink:href="sdbc:embedded:hsqldb" xlink:type="simple"/>
          <db:login db:is-password-required="false"/>
        </db:connection-data>
        <db:driver-settings db:system-driver-settings="" db:base-dn="" db:parameter-name-substitution="false"/>
        <db:application-connection-settings db:is-table-name-length-limited="false" db:append-table-alias-name="false" db:max-row-count="100">
          <db:table-filter>
            <db:table-include-filter>
              <db:table-filter-pattern>%</db:table-filter-pattern>
            </db:table-include-filter>
          </db:table-filter>
          <db:data-source-settings>
            <db:data-source-setting db:data-source-setting-is-list="false" db:data-source-setting-name="Type" db:data-source-setting-type="string">
              <db:data-source-setting-value>simple</db:data-source-setting-value>
            </db:data-source-setting>
          </db:data-source-settings>
        </db:application-connection-settings>
      </db:data-source>
      <db:queries>
      </db:queries>
      <db:table-representations>
      </db:table-representations>
    </office:database>
  </office:body>
</office:document-content>
"""


def test_no_reports():
    # pylint:disable=too-few-public-methods
    fakezip = ZipFileMock()
    fakezip.read = Mock(return_value=ODB_ELEMENT_NO_REPORTS)
    assert len(read_reports(fakezip)) == 0
