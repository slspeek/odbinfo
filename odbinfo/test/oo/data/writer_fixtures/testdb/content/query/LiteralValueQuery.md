---
!!python/object:odbinfo.pure.datatype.tabular.Query
columns:
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
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
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
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
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
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
- !!python/object:odbinfo.pure.datatype.base.Token
  cls: literalvalue
  text: '1'
  type: 201
- !!python/object:odbinfo.pure.datatype.base.Token
  cls: literalvalue
  text: '''fourtytwo'''
  type: 203
name: LiteralValueQuery
obj_id: '89'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: testdb
table_tokens: []
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
- link: &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: table
    local_id: Plant
  obj_id: '121'
  text: '"Plant"'
  type: 200
used_by: []
uses:
- *id001
---
