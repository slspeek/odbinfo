---
!!python/object:odbinfo.pure.datatype.ui.Form
height: 1
name: Related subform
obj_id: '153'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadata
subforms:
- !!python/object:odbinfo.pure.datatype.ui.SubForm
  allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  command: Plant
  commandtype: table
  controls:
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control7
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control8
    inputrequired: ''
    label: id
    name: lblid
    obj_id: '155'
    title: control7.MainForm.Related subform
    type: FixedText
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control9
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control10
    inputrequired: ''
    label: naam
    name: lblnaam
    obj_id: '156'
    title: control9.MainForm.Related subform
    type: FixedText
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control11
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control12
    inputrequired: ''
    label: RFamliyID
    name: lblRFamliyID
    obj_id: '157'
    title: control11.MainForm.Related subform
    type: FixedText
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control8
    convertemptytonull: 'true'
    datafield: id
    eventlisteners: []
    formfor: ''
    inputrequired: 'true'
    label: ''
    name: fmtid
    obj_id: '158'
    title: control8.MainForm.Related subform
    type: FormattedField
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control12
    convertemptytonull: 'true'
    datafield: RFamliyID
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    name: fmtRFamliyID
    obj_id: '159'
    title: control12.MainForm.Related subform
    type: FormattedField
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control10
    convertemptytonull: 'true'
    datafield: naam
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    name: txtnaam
    obj_id: '160'
    title: control10.MainForm.Related subform
    type: TextField
  depth: 0
  detailfields: ''
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Plant
    object_type: table
  masterfields: ''
  name: MainForm
  obj_id: '154'
  subforms:
  - !!python/object:odbinfo.pure.datatype.ui.SubForm
    allowdeletes: 'true'
    allowinserts: 'true'
    allowupdates: 'true'
    command: Family
    commandtype: table
    controls:
    - !!python/object:odbinfo.pure.datatype.ui.Control
      controlid: control1
      convertemptytonull: ''
      datafield: ''
      eventlisteners: []
      formfor: control2
      inputrequired: ''
      label: FamilyID
      name: lblFamilyID
      obj_id: '162'
      title: control1.SubForm.MainForm.Related subform
      type: FixedText
    - !!python/object:odbinfo.pure.datatype.ui.Control
      controlid: control3
      convertemptytonull: ''
      datafield: ''
      eventlisteners: []
      formfor: control4
      inputrequired: ''
      label: Name
      name: lblName
      obj_id: '163'
      title: control3.SubForm.MainForm.Related subform
      type: FixedText
    - !!python/object:odbinfo.pure.datatype.ui.Control
      controlid: control5
      convertemptytonull: ''
      datafield: ''
      eventlisteners: []
      formfor: control6
      inputrequired: ''
      label: Desc
      name: lblDesc
      obj_id: '164'
      title: control5.SubForm.MainForm.Related subform
      type: FixedText
    - !!python/object:odbinfo.pure.datatype.ui.Control
      controlid: control2
      convertemptytonull: 'true'
      datafield: FamilyID
      eventlisteners: []
      formfor: ''
      inputrequired: 'true'
      label: ''
      name: fmtFamilyID
      obj_id: '165'
      title: control2.SubForm.MainForm.Related subform
      type: FormattedField
    - !!python/object:odbinfo.pure.datatype.ui.Control
      controlid: control4
      convertemptytonull: 'true'
      datafield: Name
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: ''
      name: txtName
      obj_id: '166'
      title: control4.SubForm.MainForm.Related subform
      type: TextField
    - !!python/object:odbinfo.pure.datatype.ui.Control
      controlid: control6
      convertemptytonull: 'true'
      datafield: Desc
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: ''
      name: txtDesc
      obj_id: '167'
      title: control6.SubForm.MainForm.Related subform
      type: TextField
    depth: 1
    detailfields: '"FamilyID"'
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Family
      object_type: table
    masterfields: '"RFamliyID"'
    name: SubForm
    obj_id: '161'
    subforms: []
    title: SubForm.MainForm.Related subform
  title: MainForm.Related subform
title: Related subform
used_by: []
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: Plant
  object_type: table
- !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: Family
  object_type: table
---
