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
- text: ' '
- cls: literalvalue
  text: '1'
- text: ','
- text: '

    '
- text: ' '
- text: ' '
- text: ' '
- text: ' '
- text: ' '
- text: ' '
- text: ' '
- cls: literalvalue
  text: '''fourtytwo'''
- text: ','
- text: '

    '
- text: ' '
- text: ' '
- text: ' '
- text: ' '
- text: ' '
- text: ' '
- text: ' '
- text: '"naam"'
- text: '

    '
- text: FROM
- text: ' '
- text: ' '
- text: ' '
- link:
    content_type: table
    local_id: Plant
  obj_id: '118'
  text: '"Plant"'
used_by: []
uses:
- content_type: table
  local_id: Plant
---
