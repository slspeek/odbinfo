---
!!python/object:odbinfo.pure.datatype.tabular.Query
columns:
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: false
  name: Name
  nullable: Nullable
  obj_id: '46'
  position: 1
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: Name_1.DependendQuery
  typename: VARCHAR
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: FamilyID
  nullable: Nullable
  obj_id: '47'
  position: 2
  precision: 10
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: FamilyID_2.DependendQuery
  typename: INTEGER
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: id
  nullable: Nullable
  obj_id: '48'
  position: 3
  precision: 100
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: id_3.DependendQuery
  typename: NUMERIC
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: false
  name: naam
  nullable: Nullable
  obj_id: '49'
  position: 4
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: naam_4.DependendQuery
  typename: VARCHAR
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: RFamliyID
  nullable: Nullable
  obj_id: '50'
  position: 5
  precision: 10
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: RFamliyID_5.DependendQuery
  typename: INTEGER
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: id
  nullable: Nullable
  obj_id: '51'
  position: 6
  precision: 100
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: id_6.DependendQuery
  typename: NUMERIC
  writable: true
command: 'SELECT *

  FROM   "FamilyLookup", "vwPlant", "view1"'
name: DependendQuery
obj_id: '45'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadata
table_tokens:
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  index: 8
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: FamilyLookup
    object_type: query
  obj_id: '60'
  text: '"FamilyLookup"'
  title: token8.DependendQuery
  type: 197
- &id002 !!python/object:odbinfo.pure.datatype.base.Token
  index: 11
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: vwPlant
    object_type: query
  obj_id: '63'
  text: '"vwPlant"'
  title: token11.DependendQuery
  type: 197
- &id003 !!python/object:odbinfo.pure.datatype.base.Token
  index: 14
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: view1
    object_type: view
  obj_id: '66'
  text: '"view1"'
  title: token14.DependendQuery
  type: 197
title: DependendQuery
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 0
  text: SELECT
  title: token0.DependendQuery
  type: 129
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 1
  text: ' '
  title: token1.DependendQuery
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 2
  text: '*'
  title: token2.DependendQuery
  type: 7
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 3
  text: '

    '
  title: token3.DependendQuery
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 4
  text: FROM
  title: token4.DependendQuery
  type: 75
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 5
  text: ' '
  title: token5.DependendQuery
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 6
  text: ' '
  title: token6.DependendQuery
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 7
  text: ' '
  title: token7.DependendQuery
  type: 204
- *id001
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 9
  text: ','
  title: token9.DependendQuery
  type: 5
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 10
  text: ' '
  title: token10.DependendQuery
  type: 204
- *id002
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 12
  text: ','
  title: token12.DependendQuery
  type: 5
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 13
  text: ' '
  title: token13.DependendQuery
  type: 204
- *id003
used_by: []
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: view1
  object_type: view
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: FamilyLookup
  object_type: query
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: vwPlant
  object_type: query
---
