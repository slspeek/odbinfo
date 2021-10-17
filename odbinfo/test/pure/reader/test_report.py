" test report reading "
import dataclasses
from unittest.mock import Mock

import pytest

from odbinfo.pure.reader.report import read_reports
from odbinfo.test.pure.fixtures import empty_odbzip, odbzip


@pytest.mark.slow
def test_read_reports(odbzip, data_regression):
    " reports "
    data_regression.check(list(map(dataclasses.asdict, read_reports(odbzip))))


@pytest.mark.slow
def test_read_reports_empty(empty_odbzip):
    " read no reports "
    assert len(read_reports(empty_odbzip)) == 0


ODB_ELEMENT = """<?xml version="1.0" encoding="UTF-8"?>
<office:document-content xmlns:db="urn:oasis:names:tc:opendocument:xmlns:database:1.0" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:ooo="http://openoffice.org/2004/office" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:rpt="http://openoffice.org/2005/report" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" office:version="1.2">
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

RPT_ELEMENT = """<?xml version="1.0" encoding="UTF-8"?>
<office:document-content xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:rpt="http://openoffice.org/2005/report" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" office:version="1.2">
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

data = {"content.xml": ODB_ELEMENT, "reports/Obj11/content.xml": RPT_ELEMENT}


def test_reports():
    # pylint:disable=too-few-public-methods
    class ZipFileMock:
        def read(self, path):
            pass

    fakezip = ZipFileMock()

    def read(file: str) -> str:
        return data[file]

    fakezip.read = Mock(side_effect=read)
    assert len(read_reports(fakezip)) == 1


ODB_ELEMENT_NO_REPORTS = """<?xml version="1.0" encoding="UTF-8"?>
<office:document-content xmlns:db="urn:oasis:names:tc:opendocument:xmlns:database:1.0" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:ooo="http://openoffice.org/2004/office" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:rpt="http://openoffice.org/2005/report" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" office:version="1.2">
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
    class ZipFileMock:
        def read(self, path):
            pass

    fakezip = ZipFileMock()
    fakezip.read = Mock(return_value=ODB_ELEMENT_NO_REPORTS)
    assert len(read_reports(fakezip)) == 0
