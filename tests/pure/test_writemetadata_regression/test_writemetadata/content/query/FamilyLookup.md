---
columns:
- autoincrement: false
  issigned: false
  name: Name
  nullable: Nullable
  obj_id: '87'
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
  obj_id: '88'
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
parent_link:
  content_type: metadata
  local_id: testdb
title: FamilyLookup
tokens:
- text: SELECT
- text: ' '
- text: '"Name"'
- text: ','
- text: '

    '
- text: ' '
- text: ' '
- text: ' '
- text: ' '
- text: ' '
- text: ' '
- text: ' '
- text: '"FamilyID"'
- text: '

    '
- text: FROM
- text: ' '
- text: ' '
- text: ' '
- link:
    content_type: table
    local_id: Family
  obj_id: '86'
  text: '"Family"'
used_by:
- bookmark: '54'
  content_type: query
  local_id: DependendQuery
- bookmark: '203'
  content_type: form
  local_id: PlantListbox
- bookmark: '573'
  content_type: basicfunction
  local_id: ReferToQuery.Module1.Library1
uses:
- link:
    content_type: table
    local_id: Family
  sources: '86'
---
