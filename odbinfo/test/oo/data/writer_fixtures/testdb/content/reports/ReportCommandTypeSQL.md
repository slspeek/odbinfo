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
    obj_id: '103'
    precision: 100
    readonly: false
    scale: 0
    tablename: Plant
    typename: NUMERIC
    writable: true
  - autoincrement: false
    issigned: false
    name: naam
    nullable: Nullable
    obj_id: '104'
    precision: 2147483647
    readonly: false
    scale: 0
    tablename: Plant
    typename: VARCHAR
    writable: true
  - autoincrement: false
    issigned: true
    name: RFamliyID
    nullable: Nullable
    obj_id: '105'
    precision: 10
    readonly: false
    scale: 0
    tablename: Plant
    typename: INTEGER
    writable: true
  command: 'SELECT *

    FROM   "Plant";'
  name: ReportCommandTypeSQL.Command
  obj_id: '102'
  parent_link:
    bookmark: null
    local_id: ./testdb.odb
    object_type: metadatas
  table_tokens:
  - hidden: false
    index: 8
    link:
      bookmark: null
      local_id: Plant
      object_type: tables
    obj_id: '114'
    text: '"Plant"'
    type: 197
  title: ReportCommandTypeSQL.Command
  tokens:
  - hidden: false
    index: 0
    link: null
    obj_id: '106'
    text: SELECT
    type: 129
  - hidden: true
    index: 1
    link: null
    obj_id: '107'
    text: ' '
    type: 204
  - hidden: false
    index: 2
    link: null
    obj_id: '108'
    text: '*'
    type: 7
  - hidden: true
    index: 3
    link: null
    obj_id: '109'
    text: '

      '
    type: 204
  - hidden: false
    index: 4
    link: null
    obj_id: '110'
    text: FROM
    type: 75
  - hidden: true
    index: 5
    link: null
    obj_id: '111'
    text: ' '
    type: 204
  - hidden: true
    index: 6
    link: null
    obj_id: '112'
    text: ' '
    type: 204
  - hidden: true
    index: 7
    link: null
    obj_id: '113'
    text: ' '
    type: 204
  - hidden: false
    index: 8
    link:
      bookmark: null
      local_id: Plant
      object_type: tables
    obj_id: '114'
    text: '"Plant"'
    type: 197
  - hidden: false
    index: 9
    link: null
    obj_id: '115'
    text: ;
    type: 1
formulas:
- field:[id]
- field:[naam]
name: ReportCommandTypeSQL
obj_id: '173'
output_type: application/vnd.oasis.opendocument.text
parent_link:
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadatas
title: ReportCommandTypeSQL
---
