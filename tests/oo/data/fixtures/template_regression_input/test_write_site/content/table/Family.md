---
columns:
- autoincrement: false
  defaultvalue: ''
  description: Primary key
  name: FamilyID
  nullable: No_Nulls
  obj_id: '4'
  precision: 0
  scale: 0
  tablename: Family
  typename: INTEGER
- autoincrement: false
  defaultvalue: ''
  description: Family name
  name: Name
  nullable: Nullable
  obj_id: '5'
  precision: 100
  scale: 0
  tablename: Family
  typename: VARCHAR
- autoincrement: false
  defaultvalue: ''
  description: Description of the family
  name: Desc
  nullable: Nullable
  obj_id: '6'
  precision: 0
  scale: 0
  tablename: Family
  typename: LONGVARCHAR
description: ''
indexes:
- catalog: ''
  clustered: false
  columns:
  - FamilyID
  name: SYS_IDX_48
  obj_id: '3'
  primary: false
  unique: true
keys:
- columns:
  - FamilyID
  delete_rule: Cascade
  name: SYS_PK_49
  obj_id: '2'
  referenced_table: ''
  relatedcolumns:
  - ''
  typename: Primary
  update_rule: Cascade
name: Family
obj_id: '1'
parent_link:
  content_type: metadata
  local_id: testdb
title: Family
used_by:
- bookmark: '15'
  content_type: table
  local_id: Plant
- bookmark: '88'
  content_type: query
  local_id: FamilyLookup
- bookmark: '136'
  content_type: form
  local_id: Family
- bookmark: '237'
  content_type: form
  local_id: PlantListboxDirectSQL
- bookmark: '252'
  content_type: form
  local_id: Related subform
- content_type: report
  local_id: Family
uses: []
---
