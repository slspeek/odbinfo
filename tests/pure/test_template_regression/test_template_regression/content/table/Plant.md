---
columns:
- autoincrement: false
  defaultvalue: ''
  description: Unique key for the plant
  name: id
  nullable: No_Nulls
  obj_id: '18'
  precision: 100
  scale: 0
  tablename: Plant
  typename: NUMERIC
- autoincrement: false
  defaultvalue: ''
  description: Naam aan de plant gegeven
  name: naam
  nullable: Nullable
  obj_id: '19'
  precision: 100
  scale: 0
  tablename: Plant
  typename: VARCHAR
- autoincrement: false
  defaultvalue: ''
  description: null
  name: RFamliyID
  nullable: Nullable
  obj_id: '20'
  precision: 0
  scale: 0
  tablename: Plant
  typename: INTEGER
description: ''
indexes:
- catalog: ''
  clustered: false
  columns:
  - id
  name: SYS_IDX_46
  obj_id: '16'
  primary: false
  unique: true
- catalog: ''
  clustered: false
  columns:
  - RFamliyID
  name: SYS_IDX_80
  obj_id: '17'
  primary: false
  unique: false
keys:
- columns:
  - id
  delete_rule: Cascade
  name: SYS_PK_47
  obj_id: '14'
  referenced_table: ''
  relatedcolumns:
  - ''
  typename: Primary
  update_rule: Cascade
- columns:
  - RFamliyID
  delete_rule: No_Action
  link:
    content_type: table
    local_id: Family
  name: SYS_FK_79
  obj_id: '15'
  referenced_table: Family
  relatedcolumns:
  - FamilyID
  typename: Foreign
  update_rule: No_Action
name: Plant
obj_id: '13'
parent_link:
  content_type: metadata
  local_id: testdb
title: Plant
used_by:
- content_type: view
  local_id: view1
- content_type: query
  local_id: LiteralValueQuery
- content_type: query
  local_id: vwPlant
- content_type: form
  local_id: ListBoxTest
- content_type: form
  local_id: Plant
- content_type: form
  local_id: PlantListbox
- content_type: form
  local_id: PlantListboxDirectSQL
- content_type: form
  local_id: Related subform
- content_type: report
  local_id: ReportCommandTypeSQL
- content_type: basicfunction
  local_id: ReferToTable.Module1.Library1
uses:
- content_type: table
  local_id: Family
---
