---
height: 1
name: Formulier1
obj_id: '141'
parent_link:
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
    command: 'SELECT *

      FROM   "Person"'
    name: Formulier.Command
    obj_id: '144'
    tokens:
    - text: SELECT
    - text: ' '
    - text: '*'
    - text: '

        '
    - text: FROM
    - text: ' '
    - text: ' '
    - text: ' '
    - link:
        content_type: table
        local_id: Person
      obj_id: '153'
      text: '"Person"'
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
- link:
    content_type: table
    local_id: Person
  sources: '153'
---
