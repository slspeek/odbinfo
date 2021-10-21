---
columns:
- autoincrement: false
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
- autoincrement: false
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
literal_values: []
name: FamilyLookup
obj_id: '67'
parent_link:
  bookmark: null
  content_type: metadata
  local_id: testdb
table_tokens:
- index: 18
  link: &id001
    bookmark: null
    content_type: table
    local_id: Family
  obj_id: '88'
  text: '"Family"'
  type: 200
title: FamilyLookup
tokens:
- index: 0
  text: SELECT
  type: 131
- index: 1
  text: ' '
  type: 207
- index: 2
  text: '"Name"'
  type: 200
- index: 3
  text: ','
  type: 5
- index: 4
  text: '

    '
  type: 207
- index: 5
  text: ' '
  type: 207
- index: 6
  text: ' '
  type: 207
- index: 7
  text: ' '
  type: 207
- index: 8
  text: ' '
  type: 207
- index: 9
  text: ' '
  type: 207
- index: 10
  text: ' '
  type: 207
- index: 11
  text: ' '
  type: 207
- index: 12
  text: '"FamilyID"'
  type: 200
- index: 13
  text: '

    '
  type: 207
- index: 14
  text: FROM
  type: 77
- index: 15
  text: ' '
  type: 207
- index: 16
  text: ' '
  type: 207
- index: 17
  text: ' '
  type: 207
- index: 18
  link: *id001
  obj_id: '88'
  text: '"Family"'
  type: 200
used_by:
- bookmark: '60'
  content_type: query
  local_id: DependendQuery
- bookmark: '203'
  content_type: form
  local_id: PlantListbox
- bookmark: '573'
  content_type: basicfunction
  local_id: ReferToQuery.Module1.Library1
uses:
- *id001
---
