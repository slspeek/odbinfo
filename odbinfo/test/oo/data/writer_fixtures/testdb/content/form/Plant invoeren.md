---
!!python/object:odbinfo.pure.datatype.ui.Form
height: 0
name: Plant invoeren
obj_id: '134'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadata
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
      obj_id: '137'
      title: control2.MainForm_Grid.MainForm.Plant invoeren
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
      obj_id: '138'
      title: control3.MainForm_Grid.MainForm.Plant invoeren
      type: ooo:TextField
    name: MainForm_Grid
    obj_id: '136'
    title: MainForm_Grid.MainForm.Plant invoeren
  depth: 0
  detailfields: ''
  link: &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: vwPlant
    object_type: query
  masterfields: ''
  name: MainForm
  obj_id: '135'
  subforms: []
  title: MainForm.Plant invoeren
title: Plant invoeren
used_by: []
uses:
- *id001
---
