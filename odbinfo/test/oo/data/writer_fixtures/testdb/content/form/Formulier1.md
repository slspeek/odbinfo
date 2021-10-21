---
height: 1
name: Formulier1
obj_id: '141'
parent_link:
  bookmark: null
  content_type: metadata
  local_id: testdb
subforms:
- allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  cmd: select * from "Person"
  cmdtype: command
  controls: []
  depth: 0
  detailfields: ''
  embedded_query:
    columns: []
    command: 'SELECT *

      FROM   "Person"'
    literal_values: []
    name: Formulier.Command
    obj_id: '144'
    table_tokens:
    - index: 8
      link: &id001
        bookmark: null
        content_type: table
        local_id: Person
      obj_id: '153'
      text: '"Person"'
      type: 200
    tokens:
    - index: 0
      text: SELECT
      type: 131
    - index: 1
      text: ' '
      type: 207
    - index: 2
      text: '*'
      type: 7
    - index: 3
      text: '

        '
      type: 207
    - index: 4
      text: FROM
      type: 77
    - index: 5
      text: ' '
      type: 207
    - index: 6
      text: ' '
      type: 207
    - index: 7
      text: ' '
      type: 207
    - index: 8
      link: *id001
      obj_id: '153'
      text: '"Person"'
      type: 200
  masterfields: ''
  name: Formulier
  obj_id: '142'
  subforms:
  - allowdeletes: 'true'
    allowinserts: 'true'
    allowupdates: 'true'
    cmd: ''
    cmdtype: table
    controls: []
    depth: 1
    detailfields: ''
    masterfields: ''
    name: Formulier2
    obj_id: '143'
    subforms: []
- allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  cmd: ''
  cmdtype: table
  controls: []
  depth: 0
  detailfields: ''
  masterfields: ''
  name: Formulier 1
  obj_id: '154'
  subforms: []
title: Formulier1
used_by: []
uses:
- *id001
---
