---
columns:
- autoincrement: false
  defaultvalue: ''
  description: null
  name: Naam
  nullable: No_Nulls
  parent_link: null
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
  parent_link: null
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
  parent_link: null
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
  primary: false
  unique: true
keys:
- columns:
  - Adres
  - Naam
  delete_rule: Cascade
  name: SYS_PK_51
  referenced_table: ''
  relatedcolumns:
  - ''
  - ''
  typename: Primary
  update_rule: Cascade
name: Persoon
parent_link:
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadatas
title: Persoon
used_by: []
uses: []
---
