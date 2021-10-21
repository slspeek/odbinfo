---
height: 0
name: Plant invoeren
obj_id: '191'
parent_link:
  bookmark: null
  content_type: metadata
  local_id: testdb
subforms:
- allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  cmd: vwPlant
  cmdtype: query
  controls:
  - columns:
    - controlid: control2
      convertemptytonull: 'true'
      datafield: id
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: id
      name: id
      obj_id: '194'
      type: ooo:FormattedField
    - controlid: control3
      convertemptytonull: 'true'
      datafield: naam
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: naam
      name: naam
      obj_id: '195'
      type: ooo:TextField
    name: MainForm_Grid
    obj_id: '193'
    type: Grid
  depth: 0
  detailfields: ''
  link: &id001
    bookmark: null
    content_type: query
    local_id: vwPlant
  masterfields: ''
  name: MainForm
  obj_id: '192'
  subforms: []
title: Plant invoeren
used_by: []
uses:
- *id001
---
