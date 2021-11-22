---
columns:
- autoincrement: false
  issigned: true
  name: id
  nullable: No_Nulls
  obj_id: '123'
  position: 1
  precision: 100
  readonly: false
  scale: 0
  tablename: Plant
  typename: NUMERIC
  writable: true
- autoincrement: false
  issigned: false
  name: naam
  nullable: Nullable
  obj_id: '124'
  position: 2
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: Plant
  typename: VARCHAR
  writable: true
- autoincrement: false
  issigned: true
  name: RFamliyID
  nullable: Nullable
  obj_id: '125'
  position: 3
  precision: 10
  readonly: false
  scale: 0
  tablename: Plant
  typename: INTEGER
  writable: true
command: 'SELECT *

  FROM   "Plant"'
literal_values: []
name: vwPlant
obj_id: '122'
parent_link:
  content_type: metadata
  local_id: testdb
table_tokens:
- link:
    content_type: table
    local_id: Plant
  obj_id: '134'
  text: '"Plant"'
  type: 200
title: vwPlant
tokens:
- text: SELECT
  type: 131
- text: ' '
  type: 207
- text: '*'
  type: 7
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
  obj_id: '134'
  text: '"Plant"'
  type: 200
used_by:
- bookmark: '63'
  content_type: query
  local_id: DependendQuery
- bookmark: '156'
  content_type: form
  local_id: ListBoxTest
- bookmark: '192'
  content_type: form
  local_id: Plant invoeren
- content_type: report
  local_id: vwPlant
- bookmark: '778'
  content_type: textdocument
  local_id: Untitled
uses:
- content_type: table
  local_id: Plant
---
