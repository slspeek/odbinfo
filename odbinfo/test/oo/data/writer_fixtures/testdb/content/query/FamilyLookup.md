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
  content_type: metadata
  local_id: testdb
table_tokens:
- link:
    content_type: table
    local_id: Family
  obj_id: '88'
  text: '"Family"'
  type: 200
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
- link:
    content_type: table
    local_id: Family
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
- content_type: table
  local_id: Family
---
