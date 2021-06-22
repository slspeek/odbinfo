---
columns:
- autoincrement: false
  defaultvalue: ''
  description: null
  name: FamilyID
  nullable: No_Nulls
  obj_id: 4
  parent_link:
    bookmark: null
    local_id: Family
    object_type: tables
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
  obj_id: 5
  parent_link:
    bookmark: null
    local_id: Family
    object_type: tables
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
  obj_id: 6
  parent_link:
    bookmark: null
    local_id: Family
    object_type: tables
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
  obj_id: 3
  parent_link:
    bookmark: null
    local_id: Family
    object_type: tables
  primary: false
  title: SYS_IDX_48
  unique: true
  used_by: []
  uses: []
keys:
- columns:
  - FamilyID
  delete_rule: Cascade
  name: SYS_PK_49
  obj_id: 2
  parent_link:
    bookmark: null
    local_id: Family
    object_type: tables
  referenced_table:
    link: null
    text: ''
  relatedcolumns:
  - ''
  title: SYS_PK_49
  typename: Primary
  update_rule: Cascade
  used_by: []
  uses: []
name: Family
obj_id: 1
parent_link:
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadatas
title: Family
used_by: []
uses: []
---
