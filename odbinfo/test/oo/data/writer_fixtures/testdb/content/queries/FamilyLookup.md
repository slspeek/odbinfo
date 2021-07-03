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
  index: 0
  text: SELECT
  type: 129
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 1
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 2
  text: '"Name"'
  type: 197
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 3
  text: ','
  type: 5
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 4
  text: '

    '
  type: 204
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 8
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 9
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 10
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 11
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 12
  text: '"FamilyID"'
  type: 197
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 13
  text: '

    '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 14
  text: FROM
  type: 75
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 15
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 16
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 17
  text: ' '
  type: 204
- *id001
used_by:
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  local_id: ReferToQuery.Module1.Library1
  location_id: '517'
  object_type: basicfunctions
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  local_id: DependendQuery
  location_id: '60'
  object_type: queries
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: Family
  object_type: tables
---
