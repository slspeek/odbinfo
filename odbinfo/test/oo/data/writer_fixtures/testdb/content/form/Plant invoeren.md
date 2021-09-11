---
!!python/object:odbinfo.pure.datatype.ui.Form
height: 0
name: Plant invoeren
obj_id: '130'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: ./testdb.odb
subforms:
- !!python/object:odbinfo.pure.datatype.ui.SubForm
  allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  command: vwPlant
  commandtype: query
  controls:
  - !!python/object:odbinfo.pure.datatype.ui.Grid
    columns:
    - !!python/object:odbinfo.pure.datatype.ui.Control
      controlid: control2
      convertemptytonull: 'true'
      datafield: id
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: id
      name: id
      obj_id: '133'
      title: ''
      type: ooo:FormattedField
    - !!python/object:odbinfo.pure.datatype.ui.Control
      controlid: control3
      convertemptytonull: 'true'
      datafield: naam
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: naam
      name: naam
      obj_id: '134'
      title: ''
      type: ooo:TextField
    name: MainForm_Grid
    obj_id: '132'
    title: MainForm_Grid
    type: Grid
  depth: 0
  detailfields: ''
  link: &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: query
    local_id: vwPlant
  masterfields: ''
  name: MainForm
  obj_id: '131'
  subforms: []
  title: MainForm
title: Plant invoeren
used_by: []
uses:
- *id001
---
