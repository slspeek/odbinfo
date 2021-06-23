---
height: 0
name: Plant
obj_id: '126'
parent_link:
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadatas
subforms:
- allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  command:
    link:
      bookmark: null
      local_id: Plant
      object_type: tables
    text: Plant
  commandtype: table
  controls:
  - controlid: control1
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control2
    inputrequired: ''
    label: id
    name: lblid
    obj_id: '128'
    type: FixedText
  - controlid: control3
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control4
    inputrequired: ''
    label: naam
    name: lblnaam
    obj_id: '129'
    type: FixedText
  - controlid: control5
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control6
    inputrequired: ''
    label: RFamliyID
    name: lblRFamliyID
    obj_id: '130'
    type: FixedText
  - controlid: control2
    convertemptytonull: 'true'
    datafield: id
    eventlisteners: []
    formfor: ''
    inputrequired: 'true'
    label: ''
    name: fmtid
    obj_id: '131'
    type: FormattedField
  - controlid: control6
    convertemptytonull: 'true'
    datafield: RFamliyID
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    name: fmtRFamliyID
    obj_id: '132'
    type: FormattedField
  - controlid: control4
    convertemptytonull: 'true'
    datafield: naam
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    name: txtnaam
    obj_id: '133'
    type: TextField
  depth: 0
  detailfields: ''
  embedded_query: null
  masterfields: ''
  name: MainForm
  obj_id: '127'
  parent_link:
    bookmark: null
    local_id: Plant
    object_type: forms
  subforms: []
  title: MainForm
title: Plant
---
