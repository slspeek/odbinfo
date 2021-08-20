---
!!python/object:odbinfo.pure.datatype.ui.Report
command: select * from "Plant";
commandtype: command
embedded_query: !!python/object:odbinfo.pure.datatype.tabular.EmbeddedQuery
  columns: []
  command: 'SELECT *

    FROM   "Plant";'
  name: ReportCommandTypeSQL.Command
  obj_id: '204'
  table_tokens:
  - &id001 !!python/object:odbinfo.pure.datatype.base.Token
    index: 8
    link: &id002 !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      content_type: table
      local_id: Plant
    obj_id: '213'
    text: '"Plant"'
    title: token8.ReportCommandTypeSQL.Command
    type: 200
  title: ReportCommandTypeSQL.Command
  tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 0
    text: SELECT
    type: 131
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 1
    text: ' '
    type: 207
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 2
    text: '*'
    type: 7
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 3
    text: '

      '
    type: 207
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 4
    text: FROM
    type: 77
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 5
    text: ' '
    type: 207
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 6
    text: ' '
    type: 207
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 7
    text: ' '
    type: 207
  - *id001
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 9
    text: ;
    type: 1
formulas:
- field:[id]
- field:[naam]
name: ReportCommandTypeSQL
obj_id: '203'
output_type: application/vnd.oasis.opendocument.text
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: ./testdb.odb
title: ReportCommandTypeSQL
used_by: []
uses:
- *id002
---
