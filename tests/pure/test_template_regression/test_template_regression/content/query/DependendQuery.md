---
columns:
- autoincrement: false
  issigned: false
  name: Name
  nullable: Nullable
  obj_id: '61'
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
  obj_id: '62'
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
  obj_id: '63'
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
  obj_id: '64'
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
  obj_id: '65'
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
  obj_id: '66'
  position: 6
  precision: 100
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  typename: NUMERIC
  writable: true
command: 'SELECT *

  FROM   "FamilyLookup", "vwPlant", "view1"'
name: DependendQuery
obj_id: '45'
parent_link:
  content_type: metadata
  local_id: testdb
title: DependendQuery
tokens:
- text: SELECT
- text: ' '
- text: '*'
- text: '

    '
- text: FROM
- text: ' '
- text: ' '
- text: ' '
- link:
    content_type: query
    local_id: FamilyLookup
  obj_id: '54'
  text: '"FamilyLookup"'
- text: ','
- text: ' '
- link:
    content_type: query
    local_id: vwPlant
  obj_id: '57'
  text: '"vwPlant"'
- text: ','
- text: ' '
- link:
    content_type: view
    local_id: view1
  obj_id: '60'
  text: '"view1"'
used_by: []
uses:
- link:
    content_type: query
    local_id: FamilyLookup
  sources: '54'
- link:
    content_type: query
    local_id: vwPlant
  sources: '57'
- link:
    content_type: view
    local_id: view1
  sources: '60'
---
