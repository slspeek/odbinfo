---
!!python/object:odbinfo.pure.datatype.ui.Form
height: 0
name: view1
obj_id: '168'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: ./testdb.odb
  object_type: metadata
subforms:
- !!python/object:odbinfo.pure.datatype.ui.SubForm
  allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  command: !!python/object:odbinfo.pure.datatype.base.LinkedString
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: view1
      object_type: view
    text: view1
  commandtype: table
  controls:
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control1
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control2
    inputrequired: ''
    label: id
    name: lblid
    obj_id: '170'
    type: FixedText
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control2
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
  masterfields: ''
  name: MainForm
  obj_id: '169'
  subforms: []
title: view1
used_by: []
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: view1
  object_type: view
---
