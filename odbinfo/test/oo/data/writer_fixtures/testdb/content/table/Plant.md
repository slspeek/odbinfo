---
!!python/object:odbinfo.pure.datatype.tabular.Table
columns:
- !!python/object:odbinfo.pure.datatype.tabular.Column
  autoincrement: false
  defaultvalue: ''
  description: Unique key for the plant
  name: id
  nullable: No_Nulls
  obj_id: '18'
  precision: 100
  scale: 0
  tablename: Plant
  typename: NUMERIC
- !!python/object:odbinfo.pure.datatype.tabular.Column
  autoincrement: false
  defaultvalue: ''
  description: Naam aan de plant gegeven
  name: naam
  nullable: Nullable
  obj_id: '19'
  precision: 100
  scale: 0
  tablename: Plant
  typename: VARCHAR
- !!python/object:odbinfo.pure.datatype.tabular.Column
  autoincrement: false
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
- !!python/object:odbinfo.pure.datatype.tabular.Index
  catalog: ''
  clustered: false
  columns:
  - id
  name: SYS_IDX_46
  obj_id: '16'
  primary: false
  unique: true
- !!python/object:odbinfo.pure.datatype.tabular.Index
  catalog: ''
  clustered: false
  columns:
  - RFamliyID
  name: SYS_IDX_80
  obj_id: '17'
  primary: false
  unique: false
keys:
- !!python/object:odbinfo.pure.datatype.tabular.Key
  columns:
  - id
  delete_rule: Cascade
  name: SYS_PK_47
  obj_id: '14'
  referenced_table: ''
  relatedcolumns:
  - ''
  typename: Primary
  update_rule: Cascade
- !!python/object:odbinfo.pure.datatype.tabular.Key
  columns:
  - RFamliyID
  delete_rule: No_Action
  link: &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
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
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: testdb
title: Plant
used_by:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '44'
  content_type: view
  local_id: view1
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '121'
  content_type: query
  local_id: LiteralValueQuery
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '134'
  content_type: query
  local_id: vwPlant
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '180'
  content_type: form
  local_id: ListBoxTest
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '181'
  content_type: form
  local_id: ListBoxTest
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '184'
  content_type: form
  local_id: Plant
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '197'
  content_type: form
  local_id: PlantListbox
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '211'
  content_type: form
  local_id: PlantListboxDirectSQL
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '245'
  content_type: form
  local_id: Related subform
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '274'
  content_type: report
  local_id: ReportCommandTypeSQL
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '547'
  content_type: basicfunction
  local_id: ReferToTable.Module1.Library1
uses:
- *id001
---
