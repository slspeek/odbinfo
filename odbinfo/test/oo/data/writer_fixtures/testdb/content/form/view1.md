---
height: 0
name: view1
obj_id: '259'
parent_link:
  bookmark: null
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
    label: ''
    name: fmtid
    obj_id: '262'
    type: FormattedField
  depth: 0
  detailfields: ''
  link: &id001
    bookmark: null
    content_type: view
    local_id: view1
  masterfields: ''
  name: MainForm
  obj_id: '260'
  subforms: []
title: view1
used_by: []
uses:
- *id001
---
