---
height: 0
name: Family
obj_id: '135'
parent_link:
  content_type: metadata
  local_id: testdb
subforms:
- allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  cmd: Family
  cmdtype: table
  controls:
  - columns:
    - controlid: control2
      convertemptytonull: 'true'
      datafield: FamlilyID
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      isvisible: true
      label: FamlilyID
      name: FamlilyID
      obj_id: '138'
      type: ooo:FormattedField
    - controlid: control3
      convertemptytonull: 'true'
      datafield: Name
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      isvisible: true
      label: Name
      name: Name
      obj_id: '139'
      type: ooo:TextField
    - controlid: control4
      convertemptytonull: 'true'
      datafield: Desc
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      isvisible: true
      label: Desc
      name: Desc
      obj_id: '140'
      type: ooo:TextField
    name: MainForm_Grid
    obj_id: '137'
    type: Grid
  depth: 0
  detailfields: ''
  link:
    content_type: table
    local_id: Family
  masterfields: ''
  name: MainForm
  obj_id: '136'
  subforms: []
title: Family
used_by: []
uses:
- content_type: table
  local_id: Family
---
