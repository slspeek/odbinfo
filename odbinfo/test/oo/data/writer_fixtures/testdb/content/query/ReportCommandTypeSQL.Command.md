---
!!python/object:odbinfo.pure.datatype.tabular.Query
columns:
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: id
  nullable: No_Nulls
  obj_id: '103'
  position: 1
  precision: 100
  readonly: false
  scale: 0
  tablename: Plant
  title: id_1.ReportCommandTypeSQL.Command
  typename: NUMERIC
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: false
  name: naam
  nullable: Nullable
  obj_id: '104'
  position: 2
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: Plant
  title: naam_2.ReportCommandTypeSQL.Command
  typename: VARCHAR
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: RFamliyID
  nullable: Nullable
  obj_id: '105'
  position: 3
  precision: 10
  readonly: false
  scale: 0
  tablename: Plant
  title: RFamliyID_3.ReportCommandTypeSQL.Command
  typename: INTEGER
  writable: true
command: 'SELECT *

  FROM   "Plant";'
name: ReportCommandTypeSQL.Command
obj_id: '102'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadata
table_tokens:
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  index: 8
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Plant
    object_type: table
  obj_id: '114'
  text: '"Plant"'
  title: token8.ReportCommandTypeSQL.Command
  type: 200
title: ReportCommandTypeSQL.Command
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 0
  text: SELECT
  title: token0.ReportCommandTypeSQL.Command
  type: 131
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 1
  text: ' '
  title: token1.ReportCommandTypeSQL.Command
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 2
  text: '*'
  title: token2.ReportCommandTypeSQL.Command
  type: 7
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 3
  text: '

    '
  title: token3.ReportCommandTypeSQL.Command
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 4
  text: FROM
  title: token4.ReportCommandTypeSQL.Command
  type: 77
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 5
  text: ' '
  title: token5.ReportCommandTypeSQL.Command
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 6
  text: ' '
  title: token6.ReportCommandTypeSQL.Command
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 7
  text: ' '
  title: token7.ReportCommandTypeSQL.Command
  type: 207
- *id001
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 9
  text: ;
  title: token9.ReportCommandTypeSQL.Command
  type: 1
used_by: []
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: Plant
  object_type: table
---
