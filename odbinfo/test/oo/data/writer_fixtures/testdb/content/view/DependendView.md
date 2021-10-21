---
columns:
- autoincrement: false
  issigned: true
  name: id
  nullable: Nullable
  obj_id: '22'
  position: 1
  precision: 100
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  typename: NUMERIC
  writable: true
command: 'SELECT "view1"."id"

  FROM   "view1"'
literal_values: []
name: DependendView
obj_id: '21'
parent_link:
  bookmark: null
  content_type: metadata
  local_id: testdb
table_tokens:
- index: 2
  link: &id001
    bookmark: null
    content_type: view
    local_id: view1
  obj_id: '25'
  text: '"view1"'
  type: 200
- index: 10
  link: &id002
    bookmark: null
    content_type: view
    local_id: view1
  obj_id: '33'
  text: '"view1"'
  type: 200
title: DependendView
tokens:
- index: 0
  text: SELECT
  type: 131
- index: 1
  text: ' '
  type: 207
- index: 2
  link: *id001
  obj_id: '25'
  text: '"view1"'
  type: 200
- index: 3
  text: .
  type: 2
- index: 4
  text: '"id"'
  type: 200
- index: 5
  text: '

    '
  type: 207
- index: 6
  text: FROM
  type: 77
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
  link: *id002
  obj_id: '33'
  text: '"view1"'
  type: 200
used_by: []
uses:
- *id001
- *id002
---
