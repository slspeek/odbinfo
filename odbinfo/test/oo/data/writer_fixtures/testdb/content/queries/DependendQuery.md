---
!!python/object:odbinfo.pure.datatype.tabular.Query
columns:
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: false
  name: Name
  nullable: Nullable
  obj_id: '46'
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.Name
  typename: VARCHAR
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: FamilyID
  nullable: Nullable
  obj_id: '47'
  precision: 10
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.FamilyID
  typename: INTEGER
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: id
  nullable: Nullable
  obj_id: '48'
  precision: 100
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.id
  typename: NUMERIC
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: false
  name: naam
  nullable: Nullable
  obj_id: '49'
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.naam
  typename: VARCHAR
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: RFamliyID
  nullable: Nullable
  obj_id: '50'
  precision: 10
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.RFamliyID
  typename: INTEGER
  writable: true
- !!python/object:odbinfo.pure.datatype.tabular.QueryColumn
  autoincrement: false
  issigned: true
  name: id
  nullable: Nullable
  obj_id: '51'
  precision: 100
  readonly: false
  scale: 0
  tablename: SYSTEM_SUBQUERY
  title: SYSTEM_SUBQUERY.id
  typename: NUMERIC
  writable: true
command: 'SELECT *

  FROM   "FamilyLookup", "vwPlant", "view1"'
name: DependendQuery
obj_id: '45'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: ./testdb.odb
  object_type: metadatas
table_tokens:
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 8
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: FamilyLookup
    object_type: queries
  obj_id: '60'
  text: '"FamilyLookup"'
  type: 197
- &id002 !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 11
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: vwPlant
    object_type: queries
  obj_id: '63'
  text: '"vwPlant"'
  type: 197
- &id003 !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 14
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: view1
    object_type: views
  obj_id: '66'
  text: '"view1"'
  type: 197
title: DependendQuery
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 0
  obj_id: '52'
  text: SELECT
  type: 129
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 1
  obj_id: '53'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 2
  obj_id: '54'
  text: '*'
  type: 7
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 3
  obj_id: '55'
  text: '

    '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 4
  obj_id: '56'
  text: FROM
  type: 75
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 5
  obj_id: '57'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 6
  obj_id: '58'
  text: ' '
  type: 204
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 7
  obj_id: '59'
  text: ' '
  type: 204
- *id001
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 9
  obj_id: '61'
  text: ','
  type: 5
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 10
  obj_id: '62'
  text: ' '
  type: 204
- *id002
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 12
  obj_id: '64'
  text: ','
  type: 5
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: true
  index: 13
  obj_id: '65'
  text: ' '
  type: 204
- *id003
---
