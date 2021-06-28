---
!!python/object:odbinfo.pure.datatype.ui.Form
height: 0
name: Family
obj_id: '116'
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
      local_id: Family
      object_type: tables
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
      type: ooo:TextField
    name: MainForm_Grid
    obj_id: '118'
  depth: 0
  detailfields: ''
  masterfields: ''
  name: MainForm
  obj_id: '117'
  subforms: []
title: Family
---
