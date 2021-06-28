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
  local_id: ./testdb.odb
  object_type: metadatas
table_tokens:
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 2
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: view1
    object_type: views
  obj_id: '25'
  text: '"view1"'
  type: 197
- &id002 !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 10
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: view1
    object_type: views
  obj_id: '33'
  text: '"view1"'
  type: 197
title: DependendView
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 0
  obj_id: '23'
  text: SELECT
  type: 129
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 1
  obj_id: '24'
  text: ' '
  type: 204
- *id001
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 3
  obj_id: '26'
  text: .
  type: 2
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 4
  obj_id: '27'
  text: '"id"'
  type: 197
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 5
  obj_id: '28'
  text: '

    '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 6
  obj_id: '29'
  text: FROM
  type: 75
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 7
  obj_id: '30'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 8
  obj_id: '31'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 9
  obj_id: '32'
  text: ' '
  type: 204
- *id002
---
