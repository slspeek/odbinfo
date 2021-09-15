---
!!python/object:odbinfo.pure.datatype.ui.Form
height: 1
name: Formulier1
obj_id: '108'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: testdb
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
    table_tokens: []
    tokens:
    - text: SELECT
      type: 131
    - text: ' '
      type: 207
    - text: '*'
      type: 7
    - text: '

        '
      type: 207
    - text: FROM
      type: 77
    - text: ' '
      type: 207
    - text: ' '
      type: 207
    - text: ' '
      type: 207
    - link: &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        content_type: table
        local_id: Person
      obj_id: '120'
      text: '"Person"'
      type: 200
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
title: Formulier1
used_by: []
uses:
- *id001
---
