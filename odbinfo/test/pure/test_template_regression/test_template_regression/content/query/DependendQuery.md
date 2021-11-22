---
columns:
- autoincrement: false
  issigned: false
  name: Name
  nullable: Nullable
  obj_id: '46'
  position: 1
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  typename: VARCHAR
  writable: true
- autoincrement: false
  issigned: true
  name: FamilyID
  nullable: Nullable
  obj_id: '47'
  position: 2
  precision: 10
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  typename: INTEGER
  writable: true
- autoincrement: false
  issigned: true
  name: id
  nullable: Nullable
  obj_id: '48'
  position: 3
  precision: 100
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  typename: NUMERIC
  writable: true
- autoincrement: false
  issigned: false
  name: naam
  nullable: Nullable
  obj_id: '49'
  position: 4
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  typename: VARCHAR
  writable: true
- autoincrement: false
  issigned: true
  name: RFamliyID
  nullable: Nullable
  obj_id: '50'
  position: 5
  precision: 10
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  typename: INTEGER
  writable: true
- autoincrement: false
  issigned: true
  name: id
  nullable: Nullable
  obj_id: '51'
  position: 6
  precision: 100
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  typename: NUMERIC
  writable: true
command: 'SELECT *

  FROM   "FamilyLookup", "vwPlant", "view1"'
literal_values: []
name: DependendQuery
obj_id: '45'
parent_link:
  content_type: metadata
  local_id: testdb
table_tokens:
- link:
    content_type: query
    local_id: FamilyLookup
  obj_id: '60'
  text: '"FamilyLookup"'
  type: 200
- link:
    content_type: query
    local_id: vwPlant
  obj_id: '63'
  text: '"vwPlant"'
  type: 200
- link:
    content_type: view
    local_id: view1
  obj_id: '66'
  text: '"view1"'
  type: 200
title: DependendQuery
tokens:
- text: SELECT
  type: 131
- text: ' '
  type: 207
- text: '*'
  type: 7
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
    content_type: query
    local_id: FamilyLookup
  obj_id: '60'
  text: '"FamilyLookup"'
  type: 200
- text: ','
  type: 5
- text: ' '
  type: 207
- link:
    content_type: query
    local_id: vwPlant
  obj_id: '63'
  text: '"vwPlant"'
  type: 200
- text: ','
  type: 5
- text: ' '
  type: 207
- link:
    content_type: view
    local_id: view1
  obj_id: '66'
  text: '"view1"'
  type: 200
used_by: []
uses:
- content_type: query
  local_id: FamilyLookup
- content_type: query
  local_id: vwPlant
- content_type: view
  local_id: view1
---
