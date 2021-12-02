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
  content_type: metadata
  local_id: testdb
table_tokens:
- link:
    content_type: view
    local_id: view1
  obj_id: '25'
  text: '"view1"'
  type: 200
- link:
    content_type: view
    local_id: view1
  obj_id: '33'
  text: '"view1"'
  type: 200
title: DependendView
tokens:
- text: SELECT
  type: 131
- text: ' '
  type: 207
- link:
    content_type: view
    local_id: view1
  obj_id: '25'
  text: '"view1"'
  type: 200
- text: .
  type: 2
- text: '"id"'
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
    content_type: view
    local_id: view1
  obj_id: '33'
  text: '"view1"'
  type: 200
used_by: []
uses:
- content_type: view
  local_id: view1
- content_type: view
  local_id: view1
---
