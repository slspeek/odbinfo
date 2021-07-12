---
!!python/object:odbinfo.pure.datatype.tabular.Query
columns:
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: id
  nullable: No_Nulls
  obj_id: '90'
  precision: 100
  readonly: false
  scale: 0
  tablename: Plant
  title: Plant.id
  typename: NUMERIC
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: false
  name: naam
  nullable: Nullable
  obj_id: '91'
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: Plant
  title: Plant.naam
  typename: VARCHAR
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: RFamliyID
  nullable: Nullable
  obj_id: '92'
  precision: 10
  readonly: false
  scale: 0
  tablename: Plant
  title: Plant.RFamliyID
  typename: INTEGER
  writable: true
command: 'SELECT *

  FROM   "Plant"'
name: vwPlant
obj_id: '89'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadata
table_tokens:
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  index: 8
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Plant
    object_type: table
  obj_id: '101'
  text: '"Plant"'
  type: 197
title: vwPlant
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 0
  text: SELECT
  type: 129
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 1
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 2
  text: '*'
  type: 7
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 3
  text: '

    '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 4
  text: FROM
  type: 75
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 5
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 6
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 7
  text: ' '
  type: 204
- *id001
used_by:
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: DependendQuery
  location_id: '63'
  object_type: query
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: vwPlant
  location_id: '174'
  object_type: report
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: Plant invoeren
  location_id: '135'
  object_type: form
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: Untitled
  location_id: '627'
  object_type: textdocument
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: Plant
  object_type: table
---
