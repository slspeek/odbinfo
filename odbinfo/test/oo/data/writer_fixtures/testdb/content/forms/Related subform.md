---
height: 1
name: Related subform
obj_id: '153'
parent_link:
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadatas
subforms:
- allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  command:
    link:
      bookmark: null
      local_id: Plant
      object_type: tables
    text: Plant
  commandtype: table
  controls:
  - controlid: control7
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control8
    inputrequired: ''
    label: id
    name: lblid
    obj_id: '155'
    type: FixedText
  - controlid: control9
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control10
    inputrequired: ''
    label: naam
    name: lblnaam
    obj_id: '156'
    type: FixedText
  - controlid: control11
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control12
    inputrequired: ''
    label: RFamliyID
    name: lblRFamliyID
    obj_id: '157'
    type: FixedText
  - controlid: control8
    convertemptytonull: 'true'
    datafield: id
    eventlisteners: []
    formfor: ''
    inputrequired: 'true'
    label: ''
    name: fmtid
    obj_id: '158'
    type: FormattedField
  - controlid: control12
    convertemptytonull: 'true'
    datafield: RFamliyID
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    name: fmtRFamliyID
    obj_id: '159'
    type: FormattedField
  - controlid: control10
    convertemptytonull: 'true'
    datafield: naam
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    name: txtnaam
    obj_id: '160'
    type: TextField
  depth: 0
  detailfields: ''
  embedded_query: null
  masterfields: ''
  name: MainForm
  obj_id: '154'
  parent_link:
    bookmark: null
    local_id: Related subform
    object_type: forms
  subforms:
  - allowdeletes: 'true'
    allowinserts: 'true'
    allowupdates: 'true'
    command:
      link:
        bookmark: null
        local_id: Family
        object_type: tables
      text: Family
    commandtype: table
    controls:
    - controlid: control1
      convertemptytonull: ''
      datafield: ''
      eventlisteners: []
      formfor: control2
      inputrequired: ''
      label: FamilyID
      name: lblFamilyID
      obj_id: '162'
      type: FixedText
    - controlid: control3
      convertemptytonull: ''
      datafield: ''
      eventlisteners: []
      formfor: control4
      inputrequired: ''
      label: Name
      name: lblName
      obj_id: '163'
      type: FixedText
    - controlid: control5
      convertemptytonull: ''
      datafield: ''
      eventlisteners: []
      formfor: control6
      inputrequired: ''
      label: Desc
      name: lblDesc
      obj_id: '164'
      type: FixedText
    - controlid: control2
      convertemptytonull: 'true'
      datafield: FamilyID
      eventlisteners: []
      formfor: ''
      inputrequired: 'true'
      label: ''
      name: fmtFamilyID
      obj_id: '165'
      type: FormattedField
    - controlid: control4
      convertemptytonull: 'true'
      datafield: Name
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: ''
      name: txtName
      obj_id: '166'
      type: TextField
    - controlid: control6
      convertemptytonull: 'true'
      datafield: Desc
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: ''
      name: txtDesc
      obj_id: '167'
      type: TextField
    depth: 1
    detailfields: '"FamilyID"'
    embedded_query: null
    masterfields: '"RFamliyID"'
    name: SubForm
    obj_id: '161'
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
    subforms: []
    title: SubForm
  title: MainForm
title: Related subform
---
