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
  link: &id001
    bookmark: null
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
  bookmark: null
  content_type: metadata
  local_id: testdb
title: Plant
used_by:
- bookmark: '44'
  content_type: view
  local_id: view1
- bookmark: '121'
  content_type: query
  local_id: LiteralValueQuery
- bookmark: '134'
  content_type: query
  local_id: vwPlant
- bookmark: '178'
  content_type: form
  local_id: ListBoxTest
- bookmark: '180'
  content_type: form
  local_id: ListBoxTest
- bookmark: '184'
  content_type: form
  local_id: Plant
- bookmark: '197'
  content_type: form
  local_id: PlantListbox
- bookmark: '211'
  content_type: form
  local_id: PlantListboxDirectSQL
- bookmark: '245'
  content_type: form
  local_id: Related subform
- bookmark: '274'
  content_type: report
  local_id: ReportCommandTypeSQL
- bookmark: '549'
  content_type: basicfunction
  local_id: ReferToTable.Module1.Library1
uses:
- *id001
---
