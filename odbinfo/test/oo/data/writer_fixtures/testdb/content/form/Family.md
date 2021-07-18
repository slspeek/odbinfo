---
!!python/object:odbinfo.pure.datatype.ui.Form
height: 0
name: Family
obj_id: '116'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadata
subforms:
- !!python/object:odbinfo.pure.datatype.ui.SubForm
  allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  command: !!python/object:odbinfo.pure.datatype.base.LinkedString
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Family
      object_type: table
    text: Family
  commandtype: table
  controls:
  - !!python/object:odbinfo.pure.datatype.ui.Grid
    columns:
    - !!python/object:odbinfo.pure.datatype.ui.Control
      controlid: control2
      convertemptytonull: 'true'
      datafield: FamlilyID
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: FamlilyID
      name: FamlilyID
      obj_id: '119'
      title: control2.MainForm_Grid.MainForm.Family
      type: ooo:FormattedField
    - !!python/object:odbinfo.pure.datatype.ui.Control
      controlid: control3
      convertemptytonull: 'true'
      datafield: Name
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: Name
      name: Name
      obj_id: '120'
      title: control3.MainForm_Grid.MainForm.Family
      type: ooo:TextField
    - !!python/object:odbinfo.pure.datatype.ui.Control
      controlid: control4
      convertemptytonull: 'true'
      datafield: Desc
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: Desc
      name: Desc
      obj_id: '121'
      title: control4.MainForm_Grid.MainForm.Family
      type: ooo:TextField
    name: MainForm_Grid
    obj_id: '118'
    title: MainForm_Grid.MainForm.Family
  depth: 0
  detailfields: ''
  masterfields: ''
  name: MainForm
  obj_id: '117'
  subforms: []
  title: MainForm.Family
title: Family
used_by: []
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: Family
  object_type: table
---
