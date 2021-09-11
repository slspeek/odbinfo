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
  typename: INTEGER
  writable: true
command: "SELECT \"Name\",\n       \"FamilyID\"\nFROM   \"Family\""
name: FamilyLookup
obj_id: '67'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: ./testdb.odb
table_tokens: []
title: FamilyLookup
tokens:
- text: SELECT
  type: 131
- text: ' '
  type: 207
- text: '"Name"'
  type: 200
- text: ','
  type: 5
- text: '

    '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: '"FamilyID"'
  type: 200
- text: '

    '
  type: 207
- text: FROM
  type: 77
- text: ' '
  type: 207
- text: ' '
  type: 207
- text: ' '
  type: 207
- link: &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: table
    local_id: Family
  obj_id: '88'
  text: '"Family"'
  type: 200
used_by:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '60'
  content_type: query
  local_id: DependendQuery
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '142'
  content_type: form
  local_id: PlantListbox
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '510'
  content_type: basicfunction
  local_id: ReferToQuery.Module1.Library1
uses:
- *id001
---
