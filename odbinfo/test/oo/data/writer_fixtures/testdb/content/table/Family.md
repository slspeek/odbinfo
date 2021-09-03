---
!!python/object:odbinfo.pure.datatype.tabular.Table
columns:
- !!python/object:odbinfo.pure.datatype.tabular.Column
  autoincrement: false
  defaultvalue: ''
  description: null
  name: FamilyID
  nullable: No_Nulls
  obj_id: '4'
  precision: 0
  scale: 0
  tablename: Family
  title: Family.FamilyID
  typename: INTEGER
- !!python/object:odbinfo.pure.datatype.tabular.Column
  autoincrement: false
  defaultvalue: ''
  description: null
  name: Name
  nullable: Nullable
  obj_id: '5'
  precision: 100
  scale: 0
  tablename: Family
  title: Family.Name
  typename: VARCHAR
- !!python/object:odbinfo.pure.datatype.tabular.Column
  autoincrement: false
  defaultvalue: ''
  description: null
  name: Desc
  nullable: Nullable
  obj_id: '6'
  precision: 0
  scale: 0
  tablename: Family
  title: Family.Desc
  typename: LONGVARCHAR
description: ''
indexes:
- !!python/object:odbinfo.pure.datatype.tabular.Index
  catalog: ''
  clustered: false
  columns:
  - FamilyID
  name: SYS_IDX_48
  obj_id: '3'
  primary: false
  title: SYS_IDX_48
  unique: true
keys:
- !!python/object:odbinfo.pure.datatype.tabular.Key
  columns:
  - FamilyID
  delete_rule: Cascade
  name: SYS_PK_49
  obj_id: '2'
  referenced_table: ''
  relatedcolumns:
  - ''
  title: SYS_PK_49
  typename: Primary
  update_rule: Cascade
name: Family
obj_id: '1'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: ./testdb.odb
title: Family
used_by:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '15'
  content_type: table
  local_id: Plant
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '88'
  content_type: query
  local_id: FamilyLookup
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '103'
  content_type: form
  local_id: Family
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '176'
  content_type: form
  local_id: PlantListboxDirectSQL
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: '191'
  content_type: form
  local_id: Related subform
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: report
  local_id: Family
uses: []
---
