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
- column: 7
  hidden: false
  index: 8
  line: 2
  link:
    bookmark: null
    local_id: FamilyLookup
    object_type: queries
  name: token8
  obj_id: '60'
  text: '"FamilyLookup"'
  type: 197
- column: 23
  hidden: false
  index: 11
  line: 2
  link:
    bookmark: null
    local_id: vwPlant
    object_type: queries
  name: token11
  obj_id: '63'
  text: '"vwPlant"'
  type: 197
- column: 34
  hidden: false
  index: 14
  line: 2
  link:
    bookmark: null
    local_id: view1
    object_type: views
  name: token14
  obj_id: '66'
  text: '"view1"'
  type: 197
title: DependendQuery
tokens:
- column: 0
  hidden: false
  index: 0
  line: 1
  link: null
  name: token0
  obj_id: '52'
  text: SELECT
  type: 129
- column: 6
  hidden: true
  index: 1
  line: 1
  link: null
  name: token1
  obj_id: '53'
  text: ' '
  type: 204
- column: 7
  hidden: false
  index: 2
  line: 1
  link: null
  name: token2
  obj_id: '54'
  text: '*'
  type: 7
- column: 8
  hidden: true
  index: 3
  line: 1
  link: null
  name: token3
  obj_id: '55'
  text: '

    '
  type: 204
- column: 0
  hidden: false
  index: 4
  line: 2
  link: null
  name: token4
  obj_id: '56'
  text: FROM
  type: 75
- column: 4
  hidden: true
  index: 5
  line: 2
  link: null
  name: token5
  obj_id: '57'
  text: ' '
  type: 204
- column: 5
  hidden: true
  index: 6
  line: 2
  link: null
  name: token6
  obj_id: '58'
  text: ' '
  type: 204
- column: 6
  hidden: true
  index: 7
  line: 2
  link: null
  name: token7
  obj_id: '59'
  text: ' '
  type: 204
- column: 7
  hidden: false
  index: 8
  line: 2
  link:
    bookmark: null
    local_id: FamilyLookup
    object_type: queries
  name: token8
  obj_id: '60'
  text: '"FamilyLookup"'
  type: 197
- column: 21
  hidden: false
  index: 9
  line: 2
  link: null
  name: token9
  obj_id: '61'
  text: ','
  type: 5
- column: 22
  hidden: true
  index: 10
  line: 2
  link: null
  name: token10
  obj_id: '62'
  text: ' '
  type: 204
- column: 23
  hidden: false
  index: 11
  line: 2
  link:
    bookmark: null
    local_id: vwPlant
    object_type: queries
  name: token11
  obj_id: '63'
  text: '"vwPlant"'
  type: 197
- column: 32
  hidden: false
  index: 12
  line: 2
  link: null
  name: token12
  obj_id: '64'
  text: ','
  type: 5
- column: 33
  hidden: true
  index: 13
  line: 2
  link: null
  name: token13
  obj_id: '65'
  text: ' '
  type: 204
- column: 34
  hidden: false
  index: 14
  line: 2
  link:
    bookmark: null
    local_id: view1
    object_type: views
  name: token14
  obj_id: '66'
  text: '"view1"'
  type: 197
---
