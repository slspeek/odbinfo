---
!!python/object:odbinfo.pure.datatype.tabular.Table
columns:
- !!python/object:odbinfo.pure.datatype.tabular.Column
  autoincrement: false
  defaultvalue: ''
  description: null
  name: Naam
  nullable: No_Nulls
  obj_id: '10'
  precision: 100
  scale: 0
  tablename: Persoon
  title: Persoon.Naam
  typename: VARCHAR
- !!python/object:odbinfo.pure.datatype.tabular.Column
  autoincrement: false
  defaultvalue: ''
  description: Woonadres
  name: Adres
  nullable: No_Nulls
  obj_id: '11'
  precision: 100
  scale: 0
  tablename: Persoon
  title: Persoon.Adres
  typename: VARCHAR
- !!python/object:odbinfo.pure.datatype.tabular.Column
  autoincrement: false
  defaultvalue: ''
  description: null
  name: Leeftijd
  nullable: Nullable
  obj_id: '12'
  precision: 0
  scale: 0
  tablename: Persoon
  title: Persoon.Leeftijd
  typename: INTEGER
description: ''
indexes:
- !!python/object:odbinfo.pure.datatype.tabular.Index
  catalog: ''
  clustered: false
  columns:
  - Naam
  - Adres
  name: SYS_IDX_50
  obj_id: '9'
  primary: false
  title: SYS_IDX_50
  unique: true
keys:
- !!python/object:odbinfo.pure.datatype.tabular.Key
  columns:
  - Adres
  - Naam
  delete_rule: Cascade
  name: SYS_PK_51
  obj_id: '8'
  referenced_table: ''
  relatedcolumns:
  - ''
  - ''
  title: SYS_PK_51
  typename: Primary
  update_rule: Cascade
name: Persoon
obj_id: '7'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: ./testdb.odb
title: Persoon
used_by: []
uses: []
---
