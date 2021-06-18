---
command:
  link: null
  text: select * from "Plant";
commandtype: command
embedded_query:
  columns:
  - autoincrement: false
    issigned: true
    name: id
    nullable: No_Nulls
    parent_link:
      bookmark: null
      local_id: ReportCommandTypeSQL.Command
      object_type: queries
    precision: 100
    readonly: false
    scale: 0
    tablename: Plant
    title: Plant.id
    typename: NUMERIC
    used_by: []
    uses: []
    writable: true
  - autoincrement: false
    issigned: false
    name: naam
    nullable: Nullable
    parent_link:
      bookmark: null
      local_id: ReportCommandTypeSQL.Command
      object_type: queries
    precision: 2147483647
    readonly: false
    scale: 0
    tablename: Plant
    title: Plant.naam
    typename: VARCHAR
    used_by: []
    uses: []
    writable: true
  - autoincrement: false
    issigned: true
    name: RFamliyID
    nullable: Nullable
    parent_link:
      bookmark: null
      local_id: ReportCommandTypeSQL.Command
      object_type: queries
    precision: 10
    readonly: false
    scale: 0
    tablename: Plant
    title: Plant.RFamliyID
    typename: INTEGER
    used_by: []
    uses: []
    writable: true
  command: 'SELECT *

    FROM   "Plant";'
  name: ReportCommandTypeSQL.Command
  parent_link:
    bookmark: null
    local_id: ./testdb.odb
    object_type: metadatas
  table_tokens:
  - column: 7
    hidden: false
    index: 8
    line: 2
    link:
      bookmark: null
      local_id: Plant
      object_type: tables
    text: '"Plant"'
    type: 197
  title: ReportCommandTypeSQL.Command
  tokens:
  - column: 0
    hidden: false
    index: 0
    line: 1
    link: null
    text: SELECT
    type: 129
  - column: 6
    hidden: true
    index: 1
    line: 1
    link: null
    text: ' '
    type: 204
  - column: 7
    hidden: false
    index: 2
    line: 1
    link: null
    text: '*'
    type: 7
  - column: 8
    hidden: true
    index: 3
    line: 1
    link: null
    text: '

      '
    type: 204
  - column: 0
    hidden: false
    index: 4
    line: 2
    link: null
    text: FROM
    type: 75
  - column: 4
    hidden: true
    index: 5
    line: 2
    link: null
    text: ' '
    type: 204
  - column: 5
    hidden: true
    index: 6
    line: 2
    link: null
    text: ' '
    type: 204
  - column: 6
    hidden: true
    index: 7
    line: 2
    link: null
    text: ' '
    type: 204
  - column: 7
    hidden: false
    index: 8
    line: 2
    link:
      bookmark: null
      local_id: Plant
      object_type: tables
    text: '"Plant"'
    type: 197
  - column: 14
    hidden: false
    index: 9
    line: 2
    link: null
    text: ;
    type: 1
  used_by: []
  uses: []
formulas:
- field:[id]
- field:[naam]
name: ReportCommandTypeSQL
output_type: application/vnd.oasis.opendocument.text
parent_link:
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadatas
title: ReportCommandTypeSQL
used_by: []
uses: []
---
