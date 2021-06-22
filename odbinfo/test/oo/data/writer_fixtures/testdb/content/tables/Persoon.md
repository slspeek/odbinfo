---
columns:
- autoincrement: false
  defaultvalue: ''
  description: null
  name: Naam
  nullable: No_Nulls
  obj_id: 10
  parent_link:
    bookmark: null
    local_id: Persoon
    object_type: tables
  precision: 100
  scale: 0
  tablename: Persoon
  title: Persoon.Naam
  typename: VARCHAR
  used_by: []
  uses: []
- autoincrement: false
  defaultvalue: ''
  description: Woonadres
  name: Adres
  nullable: No_Nulls
  obj_id: 11
  parent_link:
    bookmark: null
    local_id: Persoon
    object_type: tables
  precision: 100
  scale: 0
  tablename: Persoon
  title: Persoon.Adres
  typename: VARCHAR
  used_by: []
  uses: []
- autoincrement: false
  defaultvalue: ''
  description: null
  name: Leeftijd
  nullable: Nullable
  obj_id: 12
  parent_link:
    bookmark: null
    local_id: Persoon
    object_type: tables
  precision: 0
  scale: 0
  tablename: Persoon
  title: Persoon.Leeftijd
  typename: INTEGER
  used_by: []
  uses: []
description: ''
indexes:
- catalog: ''
  clustered: false
  columns:
  - Naam
  - Adres
  name: SYS_IDX_50
  obj_id: 9
  parent_link:
    bookmark: null
    local_id: Persoon
    object_type: tables
  primary: false
  title: SYS_IDX_50
  unique: true
  used_by: []
  uses: []
keys:
- columns:
  - Adres
  - Naam
  delete_rule: Cascade
  name: SYS_PK_51
  obj_id: 8
  parent_link:
    bookmark: null
    local_id: Persoon
    object_type: tables
  referenced_table:
    link: null
    text: ''
  relatedcolumns:
  - ''
  - ''
  title: SYS_PK_51
  typename: Primary
  update_rule: Cascade
  used_by: []
  uses: []
name: Persoon
obj_id: 7
parent_link:
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadatas
title: Persoon
used_by: []
uses: []
---
