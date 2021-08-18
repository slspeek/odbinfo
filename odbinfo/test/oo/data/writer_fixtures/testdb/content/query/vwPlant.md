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
  content_type: metadata
  local_id: ./testdb.odb
table_tokens:
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  index: 8
  link: &id002 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: table
    local_id: Plant
  obj_id: '101'
  text: '"Plant"'
  title: token8.vwPlant
  type: 200
title: vwPlant
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 0
  text: SELECT
  type: 131
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 1
  text: ' '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 2
  text: '*'
  type: 7
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 3
  text: '

    '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 4
  text: FROM
  type: 77
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 5
  text: ' '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 6
  text: ' '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 7
  text: ' '
  type: 207
- *id001
used_by:
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  content_type: query
  local_id: DependendQuery
  location_id: '63'
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  content_type: form
  local_id: Plant invoeren
  location_id: '121'
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  content_type: report
  local_id: vwPlant
  location_id: '174'
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  content_type: textdocument
  local_id: Untitled
  location_id: '627'
uses:
- *id002
---
