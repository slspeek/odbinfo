---
height: 0
name: view1
obj_id: '259'
parent_link:
  content_type: metadata
  local_id: testdb
subforms:
- allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  cmd: view1
  cmdtype: table
  controls:
  - controlid: control1
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control2
    inputrequired: ''
    isvisible: true
    label: id
    name: lblid
    obj_id: '261'
    type: FixedText
  - controlid: control2
    convertemptytonull: 'true'
    datafield: id
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    isvisible: true
    label: ''
    name: fmtid
    obj_id: '262'
    type: FormattedField
  depth: 0
  detailfields: ''
  link:
    content_type: view
    local_id: view1
  masterfields: ''
  name: MainForm
  obj_id: '260'
  subforms: []
title: view1
used_by: []
uses:
- link:
    content_type: view
    local_id: view1
  sources: '260'
---
