---
columns:
- autoincrement: false
  defaultvalue: ''
  description: null
  name: FamilyID
  nullable: No_Nulls
  parent: null
  precision: 0
  scale: 0
  tablename: Family
  title: Family.FamilyID
  typename: INTEGER
  used_by: []
  uses: []
- autoincrement: false
  defaultvalue: ''
  description: null
  name: Name
  nullable: Nullable
  parent: null
  precision: 100
  scale: 0
  tablename: Family
  title: Family.Name
  typename: VARCHAR
  used_by: []
  uses: []
- autoincrement: false
  defaultvalue: ''
  description: null
  name: Desc
  nullable: Nullable
  parent: null
  precision: 0
  scale: 0
  tablename: Family
  title: Family.Desc
  typename: LONGVARCHAR
  used_by: []
  uses: []
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
parent: null
title: Family
used_by: []
uses: []
---
