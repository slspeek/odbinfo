---
columns:
- autoincrement: false
  issigned: true
  name: id
  nullable: Nullable
  obj_id: '33'
  position: 1
  precision: 100
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  typename: NUMERIC
  writable: true
command: 'SELECT "view1"."id"

  FROM   "view1"'
name: DependendView
obj_id: '21'
parent_link:
  content_type: metadata
  local_id: testdb
title: DependendView
tokens:
- text: SELECT
- text: ' '
- link:
    content_type: view
    local_id: view1
  obj_id: '24'
  text: '"view1"'
- text: .
- text: '"id"'
- text: '

    '
- text: FROM
- text: ' '
- text: ' '
- text: ' '
- link:
    content_type: view
    local_id: view1
  obj_id: '32'
  text: '"view1"'
used_by: []
uses:
- link:
    content_type: view
    local_id: view1
  sources: '24'
- link:
    content_type: view
    local_id: view1
  sources: '32'
---
