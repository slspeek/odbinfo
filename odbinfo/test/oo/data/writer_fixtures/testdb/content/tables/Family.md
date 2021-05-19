---
columns:
- autoincrement: false
  defaultvalue: ''
  description: null
  name: FamilyID
  nullable: No_Nulls
  precision: 0
  scale: 0
  tablename: Family
  title: Family.FamilyID
  typename: INTEGER
- autoincrement: false
  defaultvalue: ''
  description: null
  name: Name
  nullable: Nullable
  precision: 100
  scale: 0
  tablename: Family
  title: Family.Name
  typename: VARCHAR
- autoincrement: false
  defaultvalue: ''
  description: null
  name: Desc
  nullable: Nullable
  precision: 0
  scale: 0
  tablename: Family
  title: Family.Desc
  typename: LONGVARCHAR
description: ''
indexes:
- catalog: ''
  clustered: false
  columns:
  - FamilyID
  name: SYS_IDX_48
  primary: false
  unique: true
keys:
- columns:
  - FamilyID
  delete_rule: Cascade
  name: SYS_PK_49
  referenced_table: ''
  relatedcolumns:
  - ''
  typename: Primary
  update_rule: Cascade
name: Family
title: Family
---
