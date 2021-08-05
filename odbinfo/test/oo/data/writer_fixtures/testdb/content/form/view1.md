---
!!python/object:odbinfo.pure.datatype.ui.Form
height: 0
name: view1
obj_id: '168'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadata
subforms:
- !!python/object:odbinfo.pure.datatype.ui.SubForm
  allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  command: view1
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
    title: control1.MainForm.view1
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
    title: control2.MainForm.view1
    type: FormattedField
  depth: 0
  detailfields: ''
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: view1
    object_type: view
  masterfields: ''
  name: MainForm
  obj_id: '169'
  subforms: []
  title: MainForm.view1
title: view1
used_by: []
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: view1
  object_type: view
---
