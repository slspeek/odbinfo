---
columns:
- autoincrement: false
  issigned: true
  name: ''
  nullable: No_Nulls
  obj_id: '90'
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
  obj_id: '91'
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
  obj_id: '92'
  position: 3
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: Plant
  typename: VARCHAR
  writable: true
command: "SELECT 1,\n       'fourtytwo',\n       \"naam\"\nFROM   \"Plant\""
literal_values:
- cls: literalvalue
  index: 2
  text: '1'
  type: 201
- cls: literalvalue
  index: 12
  text: '''fourtytwo'''
  type: 203
name: LiteralValueQuery
obj_id: '89'
parent_link:
  bookmark: null
  content_type: metadata
  local_id: testdb
table_tokens:
- index: 28
  link: &id001
    bookmark: null
    content_type: table
    local_id: Plant
  obj_id: '121'
  text: '"Plant"'
  type: 200
title: LiteralValueQuery
tokens:
- index: 0
  text: SELECT
  type: 131
- index: 1
  text: ' '
  type: 207
- cls: literalvalue
  index: 2
  text: '1'
  type: 201
- index: 3
  text: ','
  type: 5
- index: 4
  text: '

    '
  type: 207
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
  text: ' '
  type: 207
- index: 9
  text: ' '
  type: 207
- index: 10
  text: ' '
  type: 207
- index: 11
  text: ' '
  type: 207
- cls: literalvalue
  index: 12
  text: '''fourtytwo'''
  type: 203
- index: 13
  text: ','
  type: 5
- index: 14
  text: '

    '
  type: 207
- index: 15
  text: ' '
  type: 207
- index: 16
  text: ' '
  type: 207
- index: 17
  text: ' '
  type: 207
- index: 18
  text: ' '
  type: 207
- index: 19
  text: ' '
  type: 207
- index: 20
  text: ' '
  type: 207
- index: 21
  text: ' '
  type: 207
- index: 22
  text: '"naam"'
  type: 200
- index: 23
  text: '

    '
  type: 207
- index: 24
  text: FROM
  type: 77
- index: 25
  text: ' '
  type: 207
- index: 26
  text: ' '
  type: 207
- index: 27
  text: ' '
  type: 207
- index: 28
  link: *id001
  obj_id: '121'
  text: '"Plant"'
  type: 200
used_by: []
uses:
- *id001
---
