---
columns:
- autoincrement: false
  defaultvalue: ''
  description: Unique key for the plant
  name: id
  nullable: No_Nulls
  obj_id: 18
  parent_link:
    bookmark: null
    local_id: Plant
    object_type: tables
  precision: 100
  scale: 0
  tablename: Plant
  title: Plant.id
  typename: NUMERIC
  used_by: []
  uses: []
- autoincrement: false
  defaultvalue: ''
  description: Naam aan de plant gegeven
  name: naam
  nullable: Nullable
  obj_id: 19
  parent_link:
    bookmark: null
    local_id: Plant
    object_type: tables
  precision: 100
  scale: 0
  tablename: Plant
  title: Plant.naam
  typename: VARCHAR
  used_by: []
  uses: []
- autoincrement: false
  defaultvalue: ''
  description: null
  name: RFamliyID
  nullable: Nullable
  obj_id: 20
  parent_link:
    bookmark: null
    local_id: Plant
    object_type: tables
  precision: 0
  scale: 0
  tablename: Plant
  title: Plant.RFamliyID
  typename: INTEGER
  used_by: []
  uses: []
description: ''
indexes:
- catalog: ''
  clustered: false
  columns:
  - id
  name: SYS_IDX_46
  obj_id: 16
  parent_link:
    bookmark: null
    local_id: Plant
    object_type: tables
  primary: false
  title: SYS_IDX_46
  unique: true
  used_by: []
  uses: []
- catalog: ''
  clustered: false
  columns:
  - RFamliyID
  name: SYS_IDX_80
  obj_id: 17
  parent_link:
    bookmark: null
    local_id: Plant
    object_type: tables
  primary: false
  title: SYS_IDX_80
  unique: false
  used_by: []
  uses: []
keys:
- columns:
  - id
  delete_rule: Cascade
  name: SYS_PK_47
  obj_id: 14
  parent_link:
    bookmark: null
    local_id: Plant
    object_type: tables
  referenced_table:
    link: null
    text: ''
  relatedcolumns:
  - ''
  title: SYS_PK_47
  typename: Primary
  update_rule: Cascade
  used_by: []
  uses: []
- columns:
  - RFamliyID
  delete_rule: No_Action
  name: SYS_FK_79
  obj_id: 15
  parent_link:
    bookmark: null
    local_id: Plant
    object_type: tables
  referenced_table:
    link:
      bookmark: null
      local_id: Family
      object_type: tables
    text: Family
  relatedcolumns:
  - FamilyID
  title: SYS_FK_79
  typename: Foreign
  update_rule: No_Action
  used_by: []
  uses: []
name: Plant
obj_id: 13
parent_link:
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadatas
title: Plant
used_by: []
uses: []
---
