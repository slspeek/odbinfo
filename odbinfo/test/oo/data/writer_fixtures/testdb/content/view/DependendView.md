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
  title: id_1.DependendView
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
  title: token2.DependendView
  type: 200
- &id002 !!python/object:odbinfo.pure.datatype.base.Token
  index: 10
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: view1
    object_type: view
  obj_id: '33'
  text: '"view1"'
  title: token10.DependendView
  type: 200
title: DependendView
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 0
  text: SELECT
  title: token0.DependendView
  type: 131
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 1
  text: ' '
  title: token1.DependendView
  type: 207
- *id001
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 3
  text: .
  title: token3.DependendView
  type: 2
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 4
  text: '"id"'
  title: token4.DependendView
  type: 200
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 5
  text: '

    '
  title: token5.DependendView
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 6
  text: FROM
  title: token6.DependendView
  type: 77
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 7
  text: ' '
  title: token7.DependendView
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 8
  text: ' '
  title: token8.DependendView
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 9
  text: ' '
  title: token9.DependendView
  type: 207
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
