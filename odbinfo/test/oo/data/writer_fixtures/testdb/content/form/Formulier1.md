---
!!python/object:odbinfo.pure.datatype.ui.Form
height: 1
name: Formulier1
obj_id: '108'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: ./testdb.odb
subforms:
- !!python/object:odbinfo.pure.datatype.ui.SubForm
  allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  command: select * from "Person"
  commandtype: command
  controls: []
  depth: 0
  detailfields: ''
  embedded_query: !!python/object:odbinfo.pure.datatype.tabular.EmbeddedQuery
    columns: []
    command: 'SELECT *

      FROM   "Person"'
    name: Formulier.Command
    obj_id: '111'
    table_tokens:
    - &id001 !!python/object:odbinfo.pure.datatype.base.Token
      index: 8
      link: &id002 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        content_type: table
        local_id: Person
      obj_id: '120'
      text: '"Person"'
      title: token8.Formulier.Command
      type: 200
    title: Formulier.Command
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
  masterfields: ''
  name: Formulier
  obj_id: '109'
  subforms:
  - !!python/object:odbinfo.pure.datatype.ui.SubForm
    allowdeletes: 'true'
    allowinserts: 'true'
    allowupdates: 'true'
    command: ''
    commandtype: table
    controls: []
    depth: 1
    detailfields: ''
    masterfields: ''
    name: Formulier2
    obj_id: '110'
    subforms: []
    title: Formulier2.Formulier.Formulier1
  title: Formulier.Formulier1
- !!python/object:odbinfo.pure.datatype.ui.SubForm
  allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  command: ''
  commandtype: table
  controls: []
  depth: 0
  detailfields: ''
  masterfields: ''
  name: Formulier 1
  obj_id: '121'
  subforms: []
  title: Formulier 1.Formulier1
title: Formulier1
used_by: []
uses:
- *id002
---
