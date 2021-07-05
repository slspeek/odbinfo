---
!!python/object:odbinfo.pure.datatype.tabular.Query
columns:
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: id
  nullable: No_Nulls
  obj_id: '103'
  precision: 100
  readonly: false
  scale: 0
  tablename: Plant
  title: Plant.id
  typename: NUMERIC
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: false
  name: naam
  nullable: Nullable
  obj_id: '104'
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: Plant
  title: Plant.naam
  typename: VARCHAR
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: RFamliyID
  nullable: Nullable
  obj_id: '105'
  precision: 10
  readonly: false
  scale: 0
  tablename: Plant
  title: Plant.RFamliyID
  typename: INTEGER
  writable: true
command: 'SELECT *

  FROM   "Plant";'
name: ReportCommandTypeSQL.Command
obj_id: '102'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: ./testdb.odb
  object_type: metadata
table_tokens:
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  index: 8
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: Plant
    object_type: table
  obj_id: '114'
  text: '"Plant"'
  type: 197
title: ReportCommandTypeSQL.Command
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 0
  text: SELECT
  type: 129
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 1
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 2
  text: '*'
  type: 7
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 3
  text: '

    '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 4
  text: FROM
  type: 75
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 5
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 6
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 7
  text: ' '
  type: 204
- *id001
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 9
  text: ;
  type: 1
used_by: []
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: Plant
  object_type: table
---
