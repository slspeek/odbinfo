---
columns:
- autoincrement: false
  issigned: false
  name: Name
  nullable: Nullable
  parent_link:
    bookmark: null
    local_id: DependendQuery
    object_type: queries
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.Name
  typename: VARCHAR
  used_by: []
  uses: []
  writable: true
- autoincrement: false
  issigned: true
  name: FamilyID
  nullable: Nullable
  parent_link:
    bookmark: null
    local_id: DependendQuery
    object_type: queries
  precision: 10
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.FamilyID
  typename: INTEGER
  used_by: []
  uses: []
  writable: true
- autoincrement: false
  issigned: true
  name: id
  nullable: Nullable
  parent_link:
    bookmark: null
    local_id: DependendQuery
    object_type: queries
  precision: 100
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.id
  typename: NUMERIC
  used_by: []
  uses: []
  writable: true
- autoincrement: false
  issigned: false
  name: naam
  nullable: Nullable
  parent_link:
    bookmark: null
    local_id: DependendQuery
    object_type: queries
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.naam
  typename: VARCHAR
  used_by: []
  uses: []
  writable: true
- autoincrement: false
  issigned: true
  name: RFamliyID
  nullable: Nullable
  parent_link:
    bookmark: null
    local_id: DependendQuery
    object_type: queries
  precision: 10
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.RFamliyID
  typename: INTEGER
  used_by: []
  uses: []
  writable: true
- autoincrement: false
  issigned: true
  name: id
  nullable: Nullable
  parent_link:
    bookmark: null
    local_id: DependendQuery
    object_type: queries
  precision: 100
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.id
  typename: NUMERIC
  used_by: []
  uses: []
  writable: true
command: 'SELECT *

  FROM   "FamilyLookup", "vwPlant", "view1"'
name: DependendQuery
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
  text: '"view1"'
  type: 197
title: DependendQuery
tokens:
- column: 0
  hidden: false
  index: 0
  line: 1
  link: null
  text: SELECT
  type: 129
- column: 6
  hidden: true
  index: 1
  line: 1
  link: null
  text: ' '
  type: 204
- column: 7
  hidden: false
  index: 2
  line: 1
  link: null
  text: '*'
  type: 7
- column: 8
  hidden: true
  index: 3
  line: 1
  link: null
  text: '

    '
  type: 204
- column: 0
  hidden: false
  index: 4
  line: 2
  link: null
  text: FROM
  type: 75
- column: 4
  hidden: true
  index: 5
  line: 2
  link: null
  text: ' '
  type: 204
- column: 5
  hidden: true
  index: 6
  line: 2
  link: null
  text: ' '
  type: 204
- column: 6
  hidden: true
  index: 7
  line: 2
  link: null
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
  text: '"FamilyLookup"'
  type: 197
- column: 21
  hidden: false
  index: 9
  line: 2
  link: null
  text: ','
  type: 5
- column: 22
  hidden: true
  index: 10
  line: 2
  link: null
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
  text: '"vwPlant"'
  type: 197
- column: 32
  hidden: false
  index: 12
  line: 2
  link: null
  text: ','
  type: 5
- column: 33
  hidden: true
  index: 13
  line: 2
  link: null
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
  text: '"view1"'
  type: 197
used_by: []
uses: []
---
