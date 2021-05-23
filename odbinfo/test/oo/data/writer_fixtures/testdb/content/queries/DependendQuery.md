---
columns:
- autoincrement: false
  issigned: false
  name: Name
  nullable: Nullable
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.Name
  typename: VARCHAR
  writable: true
- autoincrement: false
  issigned: true
  name: FamilyID
  nullable: Nullable
  precision: 10
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.FamilyID
  typename: INTEGER
  writable: true
- autoincrement: false
  issigned: true
  name: id
  nullable: Nullable
  precision: 100
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.id
  typename: NUMERIC
  writable: true
- autoincrement: false
  issigned: false
  name: naam
  nullable: Nullable
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.naam
  typename: VARCHAR
  writable: true
- autoincrement: false
  issigned: true
  name: RFamliyID
  nullable: Nullable
  precision: 10
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.RFamliyID
  typename: INTEGER
  writable: true
- autoincrement: false
  issigned: true
  name: id
  nullable: Nullable
  precision: 100
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.id
  typename: NUMERIC
  writable: true
command: 'SELECT *

  FROM   "FamilyLookup", "vwPlant", "view1"'
name: DependendQuery
table_tokens:
- column: 7
  hidden: false
  index: 8
  line: 2
  link:
  - bookmark: null
    local_id: FamilyLookup
    object_type: queries
  text: '"FamilyLookup"'
  type: 184
- column: 23
  hidden: false
  index: 11
  line: 2
  link:
  - bookmark: null
    local_id: vwPlant
    object_type: queries
  text: '"vwPlant"'
  type: 184
- column: 34
  hidden: false
  index: 14
  line: 2
  link:
  - bookmark: null
    local_id: view1
    object_type: views
  text: '"view1"'
  type: 184
title: DependendQuery
tokens:
- column: 0
  hidden: false
  index: 0
  line: 1
  link: []
  text: SELECT
  type: 129
- column: 6
  hidden: true
  index: 1
  line: 1
  link: []
  text: ' '
  type: 191
- column: 7
  hidden: false
  index: 2
  line: 1
  link: []
  text: '*'
  type: 7
- column: 8
  hidden: true
  index: 3
  line: 1
  link: []
  text: '

    '
  type: 191
- column: 0
  hidden: false
  index: 4
  line: 2
  link: []
  text: FROM
  type: 75
- column: 4
  hidden: true
  index: 5
  line: 2
  link: []
  text: ' '
  type: 191
- column: 5
  hidden: true
  index: 6
  line: 2
  link: []
  text: ' '
  type: 191
- column: 6
  hidden: true
  index: 7
  line: 2
  link: []
  text: ' '
  type: 191
- column: 7
  hidden: false
  index: 8
  line: 2
  link:
  - bookmark: null
    local_id: FamilyLookup
    object_type: queries
  text: '"FamilyLookup"'
  type: 184
- column: 21
  hidden: false
  index: 9
  line: 2
  link: []
  text: ','
  type: 5
- column: 22
  hidden: true
  index: 10
  line: 2
  link: []
  text: ' '
  type: 191
- column: 23
  hidden: false
  index: 11
  line: 2
  link:
  - bookmark: null
    local_id: vwPlant
    object_type: queries
  text: '"vwPlant"'
  type: 184
- column: 32
  hidden: false
  index: 12
  line: 2
  link: []
  text: ','
  type: 5
- column: 33
  hidden: true
  index: 13
  line: 2
  link: []
  text: ' '
  type: 191
- column: 34
  hidden: false
  index: 14
  line: 2
  link:
  - bookmark: null
    local_id: view1
    object_type: views
  text: '"view1"'
  type: 184
---
