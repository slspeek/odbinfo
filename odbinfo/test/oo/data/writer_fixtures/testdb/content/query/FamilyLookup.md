---
!!python/object:odbinfo.pure.datatype.tabular.Query
columns:
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: false
  name: Name
  nullable: Nullable
  obj_id: '68'
  position: 1
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: Family
  title: Name_1.FamilyLookup
  typename: VARCHAR
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: FamilyID
  nullable: No_Nulls
  obj_id: '69'
  position: 2
  precision: 10
  readonly: false
  scale: 0
  tablename: Family
  title: FamilyID_2.FamilyLookup
  typename: INTEGER
  writable: true
command: "SELECT \"Name\",\n       \"FamilyID\"\nFROM   \"Family\""
name: FamilyLookup
obj_id: '67'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadata
table_tokens:
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  index: 18
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Family
    object_type: table
  obj_id: '88'
  text: '"Family"'
  title: token18.FamilyLookup
  type: 197
title: FamilyLookup
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 0
  text: SELECT
  title: token0.FamilyLookup
  type: 129
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 1
  text: ' '
  title: token1.FamilyLookup
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 2
  text: '"Name"'
  title: token2.FamilyLookup
  type: 197
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 3
  text: ','
  title: token3.FamilyLookup
  type: 5
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 4
  text: '

    '
  title: token4.FamilyLookup
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 5
  text: ' '
  title: token5.FamilyLookup
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 6
  text: ' '
  title: token6.FamilyLookup
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 7
  text: ' '
  title: token7.FamilyLookup
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 8
  text: ' '
  title: token8.FamilyLookup
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 9
  text: ' '
  title: token9.FamilyLookup
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 10
  text: ' '
  title: token10.FamilyLookup
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 11
  text: ' '
  title: token11.FamilyLookup
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 12
  text: '"FamilyID"'
  title: token12.FamilyLookup
  type: 197
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 13
  text: '

    '
  title: token13.FamilyLookup
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 14
  text: FROM
  title: token14.FamilyLookup
  type: 75
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 15
  text: ' '
  title: token15.FamilyLookup
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 16
  text: ' '
  title: token16.FamilyLookup
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 17
  text: ' '
  title: token17.FamilyLookup
  type: 204
- *id001
used_by:
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: ReferToQuery.Module1.Library1
  location_id: '567'
  object_type: basicfunction
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: DependendQuery
  location_id: '60'
  object_type: query
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: Family
  object_type: table
---
