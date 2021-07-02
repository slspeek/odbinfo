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
  local_id: ./testdb.odb
  object_type: metadatas
table_tokens:
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: Plant
    object_type: tables
  obj_id: '101'
  text: '"Plant"'
  type: 197
title: vwPlant
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  text: SELECT
  type: 129
- !!python/object:odbinfo.pure.datatype.base.Token
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  text: '*'
  type: 7
- !!python/object:odbinfo.pure.datatype.base.Token
  text: '

    '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  text: FROM
  type: 75
- !!python/object:odbinfo.pure.datatype.base.Token
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  text: ' '
  type: 204
- *id001
used_by:
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  local_id: DependendQuery
  location_id: '63'
  object_type: queries
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  local_id: vwPlant
  location_id: '174'
  object_type: reports
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  local_id: Plant invoeren
  location_id: '135'
  object_type: forms
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  local_id: Untitled.odt
  location_id: '577'
  object_type: textdocuments
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: Plant
  object_type: tables
---
