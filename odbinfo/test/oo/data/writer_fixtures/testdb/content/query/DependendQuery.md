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
  link: &id004 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: FamilyLookup
    object_type: query
  obj_id: '60'
  text: '"FamilyLookup"'
  title: token8.DependendQuery
  type: 200
- &id002 !!python/object:odbinfo.pure.datatype.base.Token
  index: 11
  link: &id005 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: vwPlant
    object_type: query
  obj_id: '63'
  text: '"vwPlant"'
  title: token11.DependendQuery
  type: 200
- &id003 !!python/object:odbinfo.pure.datatype.base.Token
  index: 14
  link: &id006 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: view1
    object_type: view
  obj_id: '66'
  text: '"view1"'
  title: token14.DependendQuery
  type: 200
title: DependendQuery
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 0
  text: SELECT
  type: 131
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 1
  text: ' '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 2
  text: '*'
  type: 7
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 3
  text: '

    '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 4
  text: FROM
  type: 77
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 5
  text: ' '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 6
  text: ' '
  type: 207
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 7
  text: ' '
  type: 207
- *id001
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 9
  text: ','
  type: 5
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 10
  text: ' '
  type: 207
- *id002
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 12
  text: ','
  type: 5
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 13
  text: ' '
  type: 207
- *id003
used_by: []
uses:
- *id004
- *id005
- *id006
---
