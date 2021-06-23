---
columns:
- autoincrement: false
  defaultvalue: ''
  description: null
  name: Naam
  nullable: No_Nulls
  obj_id: '10'
  precision: 100
  scale: 0
  tablename: Persoon
  typename: VARCHAR
- autoincrement: false
  defaultvalue: ''
  description: Woonadres
  name: Adres
  nullable: No_Nulls
  obj_id: '11'
  precision: 100
  scale: 0
  tablename: Persoon
  typename: VARCHAR
- autoincrement: false
  defaultvalue: ''
  description: null
  name: Leeftijd
  nullable: Nullable
  obj_id: '12'
  precision: 0
  scale: 0
  tablename: Persoon
  typename: INTEGER
description: ''
indexes:
- catalog: ''
  clustered: false
  columns:
  - Naam
  - Adres
  name: SYS_IDX_50
  obj_id: '9'
  primary: false
  unique: true
keys:
- columns:
  - Adres
  - Naam
  delete_rule: Cascade
  name: SYS_PK_51
  obj_id: '8'
  referenced_table:
    link: null
    text: ''
  relatedcolumns:
  - ''
  - ''
  typename: Primary
  update_rule: Cascade
name: Persoon
obj_id: '7'
parent_link:
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadatas
title: Persoon
---
