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
  content_type: metadata
  local_id: ./testdb.odb
table_tokens: []
title: view1
tokens:
- text: SELECT
  type: 131
- text: ' '
  type: 207
- text: '"id"'
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
  obj_id: '44'
  text: '"Plant"'
  title: token8.view1
  type: 200
used_by:
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  content_type: view
  local_id: DependendView
  location_id: '25'
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  content_type: view
  local_id: DependendView
  location_id: '33'
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  content_type: query
  local_id: DependendQuery
  location_id: '66'
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  content_type: form
  local_id: view1
  location_id: '199'
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  content_type: basicfunction
  local_id: ReferToView.Module1.Library1
  location_id: '498'
uses:
- *id001
---
