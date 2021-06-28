---
!!python/object:odbinfo.pure.datatype.ui.Form
height: 0
name: Plant invoeren
obj_id: '134'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: ./testdb.odb
  object_type: metadatas
subforms:
- !!python/object:odbinfo.pure.datatype.ui.SubForm
  allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  command: !!python/object:odbinfo.pure.datatype.base.LinkedString
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: vwPlant
      object_type: queries
    text: vwPlant
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
      type: ooo:TextField
    name: MainForm_Grid
    obj_id: '136'
  depth: 0
  detailfields: ''
  masterfields: ''
  name: MainForm
  obj_id: '135'
  subforms: []
title: Plant invoeren
---
