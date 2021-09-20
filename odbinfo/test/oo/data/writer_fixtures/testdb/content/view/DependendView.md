---
!!python/object:odbinfo.pure.datatype.tabular.View
columns:
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: id
  nullable: Nullable
  obj_id: '22'
  position: 1
  precision: 100
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  typename: NUMERIC
  writable: true
command: 'SELECT "view1"."id"

  FROM   "view1"'
literal_values: []
name: DependendView
obj_id: '21'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: testdb
table_tokens: []
title: DependendView
tokens:
- text: SELECT
  type: 131
- text: ' '
  type: 207
- link: &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: view
    local_id: view1
  obj_id: '25'
  text: '"view1"'
  type: 200
- text: .
  type: 2
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
- link: &id002 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: view
    local_id: view1
  obj_id: '33'
  text: '"view1"'
  type: 200
used_by: []
uses:
- *id001
- *id002
---
