---
!!python/object:odbinfo.pure.datatype.tabular.Query
columns:
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: id
  nullable: No_Nulls
  obj_id: '90'
  position: 1
  precision: 100
  readonly: false
  scale: 0
  tablename: Plant
  title: id_1.vwPlant
  typename: NUMERIC
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: false
  name: naam
  nullable: Nullable
  obj_id: '91'
  position: 2
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: Plant
  title: naam_2.vwPlant
  typename: VARCHAR
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: RFamliyID
  nullable: Nullable
  obj_id: '92'
  position: 3
  precision: 10
  readonly: false
  scale: 0
  tablename: Plant
  title: RFamliyID_3.vwPlant
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
  title: token8.vwPlant
  type: 197
title: vwPlant
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 0
  text: SELECT
  title: token0.vwPlant
  type: 129
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 1
  text: ' '
  title: token1.vwPlant
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 2
  text: '*'
  title: token2.vwPlant
  type: 7
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 3
  text: '

    '
  title: token3.vwPlant
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 4
  text: FROM
  title: token4.vwPlant
  type: 75
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 5
  text: ' '
  title: token5.vwPlant
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 6
  text: ' '
  title: token6.vwPlant
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 7
  text: ' '
  title: token7.vwPlant
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
