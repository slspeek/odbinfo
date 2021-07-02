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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: Plant
    object_type: tables
  obj_id: '44'
  text: '"Plant"'
  type: 197
title: view1
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  text: SELECT
  type: 129
- !!python/object:odbinfo.pure.datatype.base.Token
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  text: '"id"'
  type: 197
- !!python/object:odbinfo.pure.datatype.base.Token
  text: '

    '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  text: FROM
  type: 75
- !!python/object:odbinfo.pure.datatype.base.Token
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  text: ' '
  type: 204
- *id001
used_by: []
uses: []
---
