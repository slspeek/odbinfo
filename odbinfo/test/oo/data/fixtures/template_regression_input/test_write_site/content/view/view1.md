---
columns:
- autoincrement: false
  issigned: true
  name: id
  nullable: No_Nulls
  obj_id: '35'
  position: 1
  precision: 100
  readonly: false
  scale: 0
  tablename: Plant
  typename: NUMERIC
  writable: true
command: 'SELECT "id"

  FROM   "Plant"'
literal_values: []
name: view1
obj_id: '34'
parent_link:
  content_type: metadata
  local_id: testdb
table_tokens:
- link:
    content_type: table
    local_id: Plant
  obj_id: '44'
  text: '"Plant"'
  type: 200
title: view1
tokens:
- text: SELECT
  type: 131
- text: ' '
  type: 207
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
    content_type: table
    local_id: Plant
  obj_id: '44'
  text: '"Plant"'
  type: 200
used_by:
- bookmark: '25'
  content_type: view
  local_id: DependendView
- bookmark: '33'
  content_type: view
  local_id: DependendView
- bookmark: '66'
  content_type: query
  local_id: DependendQuery
- bookmark: '260'
  content_type: form
  local_id: view1
- bookmark: '561'
  content_type: basicfunction
  local_id: ReferToView.Module1.Library1
uses:
- content_type: table
  local_id: Plant
---