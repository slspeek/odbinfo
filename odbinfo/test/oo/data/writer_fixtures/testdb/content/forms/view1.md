---
height: 0
name: view1
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
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
    title: lblid
    type: FixedText
    used_by: []
    uses: []
  - controlid: control2
    convertemptytonull: 'true'
    datafield: id
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    name: fmtid
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
    title: fmtid
    type: FormattedField
    used_by: []
    uses: []
  depth: 0
  detailfields: ''
  embedded_query: null
  masterfields: ''
  name: MainForm
  parent_link:
    bookmark: null
    local_id: view1
    object_type: forms
  subforms: []
  title: MainForm
  used_by: []
  uses: []
title: view1
used_by: []
uses: []
---
