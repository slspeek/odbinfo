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
  typename: NUMERIC
  writable: true
command: 'SELECT "id"

  FROM   "Plant"'
name: view1
obj_id: '34'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: testdb
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
  type: 200
used_by:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '25'
  content_type: view
  local_id: DependendView
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '33'
  content_type: view
  local_id: DependendView
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '66'
  content_type: query
  local_id: DependendQuery
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '227'
  content_type: form
  local_id: view1
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '526'
  content_type: basicfunction
  local_id: ReferToView.Module1.Library1
uses:
- *id001
---
