---
!!python/object:odbinfo.pure.datatype.tabular.View
columns:
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: id
  nullable: No_Nulls
  obj_id: '35'
  precision: 100
  readonly: false
  scale: 0
  tablename: Plant
  title: Plant.id
  typename: NUMERIC
  writable: true
command: 'SELECT "id"

  FROM   "Plant"'
name: view1
obj_id: '34'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: ./testdb.odb
  object_type: metadatas
table_tokens:
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 8
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: Plant
    object_type: tables
  obj_id: '44'
  text: '"Plant"'
  type: 197
title: view1
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 0
  obj_id: '36'
  text: SELECT
  type: 129
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 1
  obj_id: '37'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 2
  obj_id: '38'
  text: '"id"'
  type: 197
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 3
  obj_id: '39'
  text: '

    '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 4
  obj_id: '40'
  text: FROM
  type: 75
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 5
  obj_id: '41'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 6
  obj_id: '42'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 7
  obj_id: '43'
  text: ' '
  type: 204
- *id001
---
