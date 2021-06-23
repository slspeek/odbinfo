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
  referenced_table:
    link: null
    text: ''
  relatedcolumns:
  - ''
  typename: Primary
  update_rule: Cascade
- columns:
  - RFamliyID
  delete_rule: No_Action
  name: SYS_FK_79
  obj_id: '15'
  referenced_table:
    link:
      bookmark: null
      local_id: Family
      object_type: tables
    text: Family
  relatedcolumns:
  - FamilyID
  typename: Foreign
  update_rule: No_Action
name: Plant
obj_id: '13'
parent_link:
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadatas
title: Plant
---
