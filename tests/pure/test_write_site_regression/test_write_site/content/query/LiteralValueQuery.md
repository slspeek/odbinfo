---
columns:
- autoincrement: false
  issigned: true
  name: ''
  nullable: No_Nulls
  obj_id: '119'
  position: 1
  precision: 10
  readonly: true
  scale: 0
  tablename: ''
  typename: INTEGER
  writable: false
- autoincrement: false
  issigned: false
  name: ''
  nullable: No_Nulls
  obj_id: '120'
  position: 2
  precision: 2147483647
  readonly: true
  scale: 0
  tablename: ''
  typename: VARCHAR
  writable: false
- autoincrement: false
  issigned: false
  name: naam
  nullable: Nullable
  obj_id: '121'
  position: 3
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: Plant
  typename: VARCHAR
  writable: true
command: "SELECT 1,\n       'fourtytwo',\n       \"naam\"\nFROM   \"Plant\""
name: LiteralValueQuery
obj_id: '89'
parent_link:
  content_type: metadata
  local_id: testdb
title: LiteralValueQuery
tokens:
- text: SELECT
  type: 131
- text: ' '
  type: 207
- cls: literalvalue
  text: '1'
  type: 201
- text: ','
  type: 5
- text: '

    '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- cls: literalvalue
  text: '''fourtytwo'''
  type: 203
- text: ','
  type: 5
- text: '

    '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: '"naam"'
  type: 200
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
- link:
    content_type: table
    local_id: Plant
  obj_id: '118'
  text: '"Plant"'
  type: 200
used_by: []
uses:
- content_type: table
  local_id: Plant
---
