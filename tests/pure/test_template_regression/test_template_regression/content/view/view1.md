---
columns:
- autoincrement: false
  issigned: true
  name: id
  nullable: No_Nulls
  obj_id: '44'
  position: 1
  precision: 100
  readonly: false
  scale: 0
  tablename: Plant
  typename: NUMERIC
  writable: true
command: 'SELECT "id"

  FROM   "Plant"'
name: view1
obj_id: '34'
parent_link:
  content_type: metadata
  local_id: testdb
title: view1
tokens:
- text: SELECT
- text: ' '
- text: '"id"'
- text: '

    '
- text: FROM
- text: ' '
- text: ' '
- text: ' '
- link:
    content_type: table
    local_id: Plant
  obj_id: '43'
  text: '"Plant"'
used_by:
- bookmark: 24,32
  content_type: view
  local_id: DependendView
- bookmark: '60'
  content_type: query
  local_id: DependendQuery
- bookmark: '260'
  content_type: form
  local_id: view1
- bookmark: '561'
  content_type: basicfunction
  local_id: ReferToView.Module1.Library1
uses:
- link:
    content_type: table
    local_id: Plant
  sources: '43'
---
