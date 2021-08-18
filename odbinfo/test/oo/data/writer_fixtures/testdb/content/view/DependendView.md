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
  content_type: metadata
  local_id: ./testdb.odb
table_tokens:
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  index: 2
  link: &id003 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: view
    local_id: view1
  obj_id: '25'
  text: '"view1"'
  title: token2.DependendView
  type: 200
- &id002 !!python/object:odbinfo.pure.datatype.base.Token
  index: 10
  link: &id004 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: view
    local_id: view1
  obj_id: '33'
  text: '"view1"'
  title: token10.DependendView
  type: 200
title: DependendView
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 0
  text: SELECT
  type: 131
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 1
  text: ' '
  type: 207
- *id001
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 3
  text: .
  type: 2
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 4
  text: '"id"'
  type: 200
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 5
  text: '

    '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 6
  text: FROM
  type: 77
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 7
  text: ' '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 8
  text: ' '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 9
  text: ' '
  type: 207
- *id002
used_by: []
uses:
- *id003
- *id004
---
