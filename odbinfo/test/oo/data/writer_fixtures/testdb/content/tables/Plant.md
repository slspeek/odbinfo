---
columns:
- autoincrement: false
  defaultvalue: ''
  description: Unique key for the plant
  name: id
  nullable: No_Nulls
  parent: null
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
  parent: null
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
  parent: null
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
  primary: false
  unique: true
- catalog: ''
  clustered: false
  columns:
  - RFamliyID
  name: SYS_IDX_80
  primary: false
  unique: false
keys:
- columns:
  - id
  delete_rule: Cascade
  name: SYS_PK_47
  referenced_table: ''
  relatedcolumns:
  - ''
  typename: Primary
  update_rule: Cascade
- columns:
  - RFamliyID
  delete_rule: No_Action
  name: SYS_FK_79
  referenced_table: Family
  relatedcolumns:
  - FamilyID
  typename: Foreign
  update_rule: No_Action
name: Plant
parent: null
title: Plant
used_by: []
uses: []
---
