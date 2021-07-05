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
  unique: true
keys:
- !!python/object:odbinfo.pure.datatype.tabular.Key
  columns:
  - FamilyID
  delete_rule: Cascade
  name: SYS_PK_49
  obj_id: '2'
  referenced_table: !!python/object:odbinfo.pure.datatype.base.LinkedString
    text: ''
  relatedcolumns:
  - ''
  typename: Primary
  update_rule: Cascade
name: Family
obj_id: '1'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: ./testdb.odb
  object_type: metadata
title: Family
used_by:
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  local_id: Plant
  location_id: '15'
  object_type: table
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  local_id: FamilyLookup
  location_id: '88'
  object_type: query
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  local_id: Family
  location_id: '172'
  object_type: report
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  local_id: Family
  location_id: '117'
  object_type: form
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  local_id: Related subform
  location_id: '161'
  object_type: form
uses: []
---
