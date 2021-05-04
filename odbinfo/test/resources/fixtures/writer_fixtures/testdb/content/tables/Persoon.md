---
columns:
- autoincrement: false
  defaultvalue: ''
  description: null
  name: Naam
  nullable: No_Nulls
  precision: 100
  scale: 0
  tablename: Persoon
  title: Persoon.Naam
  typename: VARCHAR
- autoincrement: false
  defaultvalue: ''
  description: Woonadres
  name: Adres
  nullable: No_Nulls
  precision: 100
  scale: 0
  tablename: Persoon
  title: Persoon.Adres
  typename: VARCHAR
- autoincrement: false
  defaultvalue: ''
  description: null
  name: Leeftijd
  nullable: Nullable
  precision: 0
  scale: 0
  tablename: Persoon
  title: Persoon.Leeftijd
  typename: INTEGER
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
---
