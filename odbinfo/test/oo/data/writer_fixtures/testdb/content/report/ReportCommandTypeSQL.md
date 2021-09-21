---
!!python/object:odbinfo.pure.datatype.ui.Report
cmd: select * from "Plant";
cmdtype: command
embedded_query: !!python/object:odbinfo.pure.datatype.tabular.EmbeddedQuery
  columns: []
  command: 'SELECT *

    FROM   "Plant";'
  literal_values: []
  name: ReportCommandTypeSQL.Command
  obj_id: '265'
  table_tokens: []
  tokens:
  - text: SELECT
    type: 131
  - text: ' '
    type: 207
  - text: '*'
    type: 7
  - text: '

      '
    type: 207
  - text: FROM
    type: 77
  - text: ' '
    type: 207
  - text: ' '
    type: 207
  - text: ' '
    type: 207
  - link: &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      content_type: table
      local_id: Plant
    obj_id: '274'
    text: '"Plant"'
    type: 200
  - text: ;
    type: 1
formulas:
- field:[id]
- field:[naam]
name: ReportCommandTypeSQL
obj_id: '264'
output_type: application/vnd.oasis.opendocument.text
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: testdb
title: ReportCommandTypeSQL
used_by: []
uses:
- *id001
---
