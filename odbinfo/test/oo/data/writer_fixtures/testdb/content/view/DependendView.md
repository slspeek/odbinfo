---
!!python/object:odbinfo.pure.datatype.tabular.View
columns:
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: id
  nullable: Nullable
  obj_id: '22'
  precision: 100
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.id
  typename: NUMERIC
  writable: true
command: 'SELECT "view1"."id"

  FROM   "view1"'
name: DependendView
obj_id: '21'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadata
table_tokens:
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  index: 2
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: view1
    object_type: view
  obj_id: '25'
  text: '"view1"'
  type: 197
- &id002 !!python/object:odbinfo.pure.datatype.base.Token
  index: 10
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: view1
    object_type: view
  obj_id: '33'
  text: '"view1"'
  type: 197
title: DependendView
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 0
  text: SELECT
  type: 129
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 1
  text: ' '
  type: 204
- *id001
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 3
  text: .
  type: 2
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 4
  text: '"id"'
  type: 197
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 5
  text: '

    '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 6
  text: FROM
  type: 75
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 7
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 8
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 9
  text: ' '
  type: 204
- *id002
used_by: []
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: view1
  object_type: view
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: view1
  object_type: view
---
