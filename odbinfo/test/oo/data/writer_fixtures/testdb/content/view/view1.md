---
!!python/object:odbinfo.pure.datatype.tabular.View
columns:
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: id
  nullable: No_Nulls
  obj_id: '35'
  position: 1
  precision: 100
  readonly: false
  scale: 0
  tablename: Plant
  title: id_1.view1
  typename: NUMERIC
  writable: true
command: 'SELECT "id"

  FROM   "Plant"'
name: view1
obj_id: '34'
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
  obj_id: '44'
  text: '"Plant"'
  title: token8.view1
  type: 197
title: view1
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 0
  text: SELECT
  title: token0.view1
  type: 129
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 1
  text: ' '
  title: token1.view1
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 2
  text: '"id"'
  title: token2.view1
  type: 197
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 3
  text: '

    '
  title: token3.view1
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 4
  text: FROM
  title: token4.view1
  type: 75
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 5
  text: ' '
  title: token5.view1
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 6
  text: ' '
  title: token6.view1
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 7
  text: ' '
  title: token7.view1
  type: 204
- *id001
used_by:
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: ReferToView.Module1.Library1
  location_id: '554'
  object_type: basicfunction
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: DependendQuery
  location_id: '66'
  object_type: query
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: DependendView
  location_id: '25'
  object_type: view
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: DependendView
  location_id: '33'
  object_type: view
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: view1
  location_id: '169'
  object_type: form
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: Plant
  object_type: table
---
