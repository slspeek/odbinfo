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
  referenced_table: !!python/object:odbinfo.pure.datatype.base.LinkedString
    text: ''
  relatedcolumns:
  - ''
  title: SYS_PK_47
  typename: Primary
  update_rule: Cascade
- !!python/object:odbinfo.pure.datatype.tabular.Key
  columns:
  - RFamliyID
  delete_rule: No_Action
  name: SYS_FK_79
  obj_id: '15'
  referenced_table: !!python/object:odbinfo.pure.datatype.base.LinkedString
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Family
      object_type: table
    text: Family
  relatedcolumns:
  - FamilyID
  title: SYS_FK_79
  typename: Foreign
  update_rule: No_Action
name: Plant
obj_id: '13'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadata
title: Plant
used_by:
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: ReferToTable.Module1.Library1
  location_id: '541'
  object_type: basicfunction
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: vwPlant
  location_id: '101'
  object_type: query
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: ReportCommandTypeSQL.Command
  location_id: '114'
  object_type: query
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: view1
  location_id: '44'
  object_type: view
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: Plant
  location_id: '127'
  object_type: form
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: PlantListbox
  location_id: '140'
  object_type: form
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  bookmark: null
  local_id: Related subform
  location_id: '154'
  object_type: form
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: Family
  object_type: table
---
