---
cmd: select * from "Plant";
cmdtype: command
embedded_query:
  columns: []
  command: 'SELECT *

    FROM   "Plant";'
  literal_values: []
  name: ReportCommandTypeSQL.Command
  obj_id: '265'
  table_tokens:
  - index: 8
    link: &id001
      bookmark: null
      content_type: table
      local_id: Plant
    obj_id: '274'
    text: '"Plant"'
    type: 200
  tokens:
  - index: 0
    text: SELECT
    type: 131
  - index: 1
    text: ' '
    type: 207
  - index: 2
    text: '*'
    type: 7
  - index: 3
    text: '

      '
    type: 207
  - index: 4
    text: FROM
    type: 77
  - index: 5
    text: ' '
    type: 207
  - index: 6
    text: ' '
    type: 207
  - index: 7
    text: ' '
    type: 207
  - index: 8
    link: *id001
    obj_id: '274'
    text: '"Plant"'
    type: 200
  - index: 9
    text: ;
    type: 1
formulas:
- field:[id]
- field:[naam]
name: ReportCommandTypeSQL
obj_id: '264'
output_type: application/vnd.oasis.opendocument.text
parent_link:
  bookmark: null
  content_type: metadata
  local_id: testdb
title: ReportCommandTypeSQL
used_by: []
uses:
- *id001
---
