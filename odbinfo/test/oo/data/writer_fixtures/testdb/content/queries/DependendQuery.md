---
columns:
- autoincrement: false
  issigned: false
  name: Name
  nullable: Nullable
  obj_id: '46'
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
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadatas
table_tokens:
- hidden: false
  index: 8
  link:
    bookmark: null
    local_id: FamilyLookup
    object_type: queries
  obj_id: '60'
  text: '"FamilyLookup"'
  type: 197
- hidden: false
  index: 11
  link:
    bookmark: null
    local_id: vwPlant
    object_type: queries
  obj_id: '63'
  text: '"vwPlant"'
  type: 197
- hidden: false
  index: 14
  link:
    bookmark: null
    local_id: view1
    object_type: views
  obj_id: '66'
  text: '"view1"'
  type: 197
title: DependendQuery
tokens:
- hidden: false
  index: 0
  link: null
  obj_id: '52'
  text: SELECT
  type: 129
- hidden: true
  index: 1
  link: null
  obj_id: '53'
  text: ' '
  type: 204
- hidden: false
  index: 2
  link: null
  obj_id: '54'
  text: '*'
  type: 7
- hidden: true
  index: 3
  link: null
  obj_id: '55'
  text: '

    '
  type: 204
- hidden: false
  index: 4
  link: null
  obj_id: '56'
  text: FROM
  type: 75
- hidden: true
  index: 5
  link: null
  obj_id: '57'
  text: ' '
  type: 204
- hidden: true
  index: 6
  link: null
  obj_id: '58'
  text: ' '
  type: 204
- hidden: true
  index: 7
  link: null
  obj_id: '59'
  text: ' '
  type: 204
- hidden: false
  index: 8
  link:
    bookmark: null
    local_id: FamilyLookup
    object_type: queries
  obj_id: '60'
  text: '"FamilyLookup"'
  type: 197
- hidden: false
  index: 9
  link: null
  obj_id: '61'
  text: ','
  type: 5
- hidden: true
  index: 10
  link: null
  obj_id: '62'
  text: ' '
  type: 204
- hidden: false
  index: 11
  link:
    bookmark: null
    local_id: vwPlant
    object_type: queries
  obj_id: '63'
  text: '"vwPlant"'
  type: 197
- hidden: false
  index: 12
  link: null
  obj_id: '64'
  text: ','
  type: 5
- hidden: true
  index: 13
  link: null
  obj_id: '65'
  text: ' '
  type: 204
- hidden: false
  index: 14
  link:
    bookmark: null
    local_id: view1
    object_type: views
  obj_id: '66'
  text: '"view1"'
  type: 197
---
