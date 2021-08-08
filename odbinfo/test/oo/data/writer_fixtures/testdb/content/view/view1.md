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
  link: &id002 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Plant
    object_type: table
  obj_id: '44'
  text: '"Plant"'
  title: token8.view1
  type: 200
title: view1
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
  text: '"id"'
  type: 200
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
  local_id: DependendQuery
  location_id: '66'
  object_type: query
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: view1
  location_id: '169'
  object_type: form
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: ReferToView.Module1.Library1
  location_id: '414'
  object_type: basicfunction
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: Module1.Library1
  location_id: '554'
  object_type: module
uses:
- *id002
---
