---
columns:
- autoincrement: false
  issigned: true
  name: id
  nullable: Nullable
  parent_link:
    bookmark: null
    local_id: DependendView
    object_type: views
  precision: 100
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.id
  typename: NUMERIC
  used_by: []
  uses: []
  writable: true
command: 'SELECT "view1"."id"

  FROM   "view1"'
name: DependendView
parent_link:
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadatas
table_tokens:
- column: 7
  hidden: false
  index: 2
  line: 1
  link:
    bookmark: null
    local_id: view1
    object_type: views
  text: '"view1"'
  type: 197
- column: 7
  hidden: false
  index: 10
  line: 2
  link:
    bookmark: null
    local_id: view1
    object_type: views
  text: '"view1"'
  type: 197
title: DependendView
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
  link:
    bookmark: null
    local_id: view1
    object_type: views
  text: '"view1"'
  type: 197
- column: 14
  hidden: false
  index: 3
  line: 1
  link: null
  text: .
  type: 2
- column: 15
  hidden: false
  index: 4
  line: 1
  link: null
  text: '"id"'
  type: 197
- column: 19
  hidden: true
  index: 5
  line: 1
  link: null
  text: '

    '
  type: 204
- column: 0
  hidden: false
  index: 6
  line: 2
  link: null
  text: FROM
  type: 75
- column: 4
  hidden: true
  index: 7
  line: 2
  link: null
  text: ' '
  type: 204
- column: 5
  hidden: true
  index: 8
  line: 2
  link: null
  text: ' '
  type: 204
- column: 6
  hidden: true
  index: 9
  line: 2
  link: null
  text: ' '
  type: 204
- column: 7
  hidden: false
  index: 10
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