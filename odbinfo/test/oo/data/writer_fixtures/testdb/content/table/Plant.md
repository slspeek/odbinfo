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
  title: Plant.id
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
  title: Plant.naam
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
  title: Plant.RFamliyID
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
  title: SYS_IDX_46
  unique: true
- !!python/object:odbinfo.pure.datatype.tabular.Index
  catalog: ''
  clustered: false
  columns:
  - RFamliyID
  name: SYS_IDX_80
  obj_id: '17'
  primary: false
  title: SYS_IDX_80
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
  title: SYS_PK_47
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
  title: SYS_FK_79
  typename: Foreign
  update_rule: No_Action
name: Plant
obj_id: '13'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: ./testdb.odb
title: Plant
used_by:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '44'
  content_type: view
  local_id: view1
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '101'
  content_type: query
  local_id: vwPlant
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '123'
  content_type: form
  local_id: Plant
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '136'
  content_type: form
  local_id: PlantListbox
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '150'
  content_type: form
  local_id: PlantListboxDirectSQL
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '184'
  content_type: form
  local_id: Related subform
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '213'
  content_type: report
  local_id: ReportCommandTypeSQL
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '486'
  content_type: basicfunction
  local_id: ReferToTable.Module1.Library1
uses:
- *id001
---
