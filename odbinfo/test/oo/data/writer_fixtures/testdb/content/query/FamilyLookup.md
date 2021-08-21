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
  content_type: metadata
  local_id: ./testdb.odb
table_tokens:
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  index: 18
  link: &id002 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: table
    local_id: Family
  obj_id: '88'
  text: '"Family"'
  title: token18.FamilyLookup
  type: 200
title: FamilyLookup
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 0
  text: SELECT
  type: 131
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 1
  text: ' '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 2
  text: '"Name"'
  type: 200
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 3
  text: ','
  type: 5
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 4
  text: '

    '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 5
  text: ' '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 6
  text: ' '
  type: 207
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 10
  text: ' '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 11
  text: ' '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 12
  text: '"FamilyID"'
  type: 200
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 13
  text: '

    '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 14
  text: FROM
  type: 77
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 15
  text: ' '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 16
  text: ' '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 17
  text: ' '
  type: 207
- *id001
used_by:
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  content_type: query
  local_id: DependendQuery
  location_id: '60'
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  content_type: form
  local_id: PlantListbox
  location_id: '142'
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  content_type: basicfunction
  local_id: ReferToQuery.Module1.Library1
  location_id: '467'
uses:
- *id002
---
