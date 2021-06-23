---
height: 0
name: view1
obj_id: '168'
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
      local_id: view1
      object_type: views
    text: view1
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
    obj_id: '170'
    type: FixedText
  - controlid: control2
    convertemptytonull: 'true'
    datafield: id
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    name: fmtid
    obj_id: '171'
    type: FormattedField
  depth: 0
  detailfields: ''
  embedded_query: null
  masterfields: ''
  name: MainForm
  obj_id: '169'
  parent_link:
    bookmark: null
    local_id: view1
    object_type: forms
  subforms: []
  title: MainForm
title: view1
---
