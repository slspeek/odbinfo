---
cmd: select * from "Plant";
cmdtype: command
embedded_query:
  command: 'SELECT *

    FROM   "Plant";'
  name: ReportCommandTypeSQL.Command
  obj_id: '265'
  tokens:
  - text: SELECT
  - text: ' '
  - text: '*'
  - text: '

      '
  - text: FROM
  - text: ' '
  - text: ' '
  - text: ' '
  - link:
      content_type: table
      local_id: Plant
    obj_id: '274'
    text: '"Plant"'
  - text: ;
formulas:
- field:[id]
- field:[naam]
name: ReportCommandTypeSQL
obj_id: '264'
output_type: application/vnd.oasis.opendocument.text
parent_link:
  content_type: metadata
  local_id: testdb
title: ReportCommandTypeSQL
used_by: []
uses:
- content_type: table
  local_id: Plant
---
