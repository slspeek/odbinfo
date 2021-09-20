---
!!python/object:odbinfo.pure.datatype.tabular.Query
columns:
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: id
  nullable: No_Nulls
  obj_id: '123'
  position: 1
  precision: 100
  readonly: false
  scale: 0
  tablename: Plant
  typename: NUMERIC
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: false
  name: naam
  nullable: Nullable
  obj_id: '124'
  position: 2
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: Plant
  typename: VARCHAR
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: RFamliyID
  nullable: Nullable
  obj_id: '125'
  position: 3
  precision: 10
  readonly: false
  scale: 0
  tablename: Plant
  typename: INTEGER
  writable: true
command: 'SELECT *

  FROM   "Plant"'
literal_values: []
name: vwPlant
obj_id: '122'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: testdb
table_tokens: []
title: vwPlant
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
  obj_id: '134'
  text: '"Plant"'
  type: 200
used_by:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '63'
  content_type: query
  local_id: DependendQuery
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '156'
  content_type: form
  local_id: ListBoxTest
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '192'
  content_type: form
  local_id: Plant invoeren
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: report
  local_id: vwPlant
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '772'
  content_type: textdocument
  local_id: Untitled
uses:
- *id001
---
