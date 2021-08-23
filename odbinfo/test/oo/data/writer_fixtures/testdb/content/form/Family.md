---
!!python/object:odbinfo.pure.datatype.ui.Form
height: 0
name: Family
obj_id: '102'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: ./testdb.odb
subforms:
- !!python/object:odbinfo.pure.datatype.ui.SubForm
  allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  command: Family
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
      obj_id: '105'
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
      obj_id: '106'
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
      obj_id: '107'
      title: control4.MainForm_Grid.MainForm.Family
      type: ooo:TextField
    name: MainForm_Grid
    obj_id: '104'
    title: MainForm_Grid.MainForm.Family
    type: Grid
  depth: 0
  detailfields: ''
  link: &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: table
    local_id: Family
  masterfields: ''
  name: MainForm
  obj_id: '103'
  subforms: []
  title: MainForm.Family
title: Family
used_by: []
uses:
- *id001
---
