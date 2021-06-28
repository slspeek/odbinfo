---
!!python/object:odbinfo.pure.datatype.tabular.Query
columns:
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: false
  name: Name
  nullable: Nullable
  obj_id: '68'
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: Family
  title: Family.Name
  typename: VARCHAR
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: FamilyID
  nullable: No_Nulls
  obj_id: '69'
  precision: 10
  readonly: false
  scale: 0
  tablename: Family
  title: Family.FamilyID
  typename: INTEGER
  writable: true
command: "SELECT \"Name\",\n       \"FamilyID\"\nFROM   \"Family\""
name: FamilyLookup
obj_id: '67'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: ./testdb.odb
  object_type: metadatas
table_tokens:
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 18
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: Family
    object_type: tables
  obj_id: '88'
  text: '"Family"'
  type: 197
title: FamilyLookup
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 0
  obj_id: '70'
  text: SELECT
  type: 129
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 1
  obj_id: '71'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 2
  obj_id: '72'
  text: '"Name"'
  type: 197
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 3
  obj_id: '73'
  text: ','
  type: 5
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 4
  obj_id: '74'
  text: '

    '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 5
  obj_id: '75'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 6
  obj_id: '76'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 7
  obj_id: '77'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 8
  obj_id: '78'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 9
  obj_id: '79'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 10
  obj_id: '80'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 11
  obj_id: '81'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 12
  obj_id: '82'
  text: '"FamilyID"'
  type: 197
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 13
  obj_id: '83'
  text: '

    '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 14
  obj_id: '84'
  text: FROM
  type: 75
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 15
  obj_id: '85'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 16
  obj_id: '86'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 17
  obj_id: '87'
  text: ' '
  type: 204
- *id001
---
