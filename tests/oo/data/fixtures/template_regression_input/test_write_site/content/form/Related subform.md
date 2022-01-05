---
height: 1
name: Related subform
obj_id: '244'
parent_link:
  content_type: metadata
  local_id: testdb
subforms:
- allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  cmd: Plant
  cmdtype: table
  controls:
  - controlid: control7
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control8
    inputrequired: ''
    isvisible: true
    label: id
    name: lblid
    obj_id: '246'
    type: FixedText
  - controlid: control8
    convertemptytonull: 'true'
    datafield: id
    eventlisteners: []
    formfor: ''
    inputrequired: 'true'
    isvisible: true
    label: ''
    name: fmtid
    obj_id: '247'
    type: FormattedField
  - controlid: control9
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control10
    inputrequired: ''
    isvisible: true
    label: naam
    name: lblnaam
    obj_id: '248'
    type: FixedText
  - controlid: control10
    convertemptytonull: 'true'
    datafield: naam
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    isvisible: true
    label: ''
    name: txtnaam
    obj_id: '249'
    type: TextField
  - controlid: control11
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control12
    inputrequired: ''
    isvisible: true
    label: RFamliyID
    name: lblRFamliyID
    obj_id: '250'
    type: FixedText
  - controlid: control12
    convertemptytonull: 'true'
    datafield: RFamliyID
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    isvisible: true
    label: ''
    name: fmtRFamliyID
    obj_id: '251'
    type: FormattedField
  depth: 0
  detailfields: ''
  link:
    content_type: table
    local_id: Plant
  masterfields: ''
  name: MainForm
  obj_id: '245'
  subforms:
  - allowdeletes: 'true'
    allowinserts: 'true'
    allowupdates: 'true'
    cmd: Family
    cmdtype: table
    controls:
    - controlid: control1
      convertemptytonull: ''
      datafield: ''
      eventlisteners: []
      formfor: control2
      inputrequired: ''
      isvisible: true
      label: FamilyID
      name: lblFamilyID
      obj_id: '253'
      type: FixedText
    - controlid: control2
      convertemptytonull: 'true'
      datafield: FamilyID
      eventlisteners: []
      formfor: ''
      inputrequired: 'true'
      isvisible: true
      label: ''
      name: fmtFamilyID
      obj_id: '254'
      type: FormattedField
    - controlid: control3
      convertemptytonull: ''
      datafield: ''
      eventlisteners: []
      formfor: control4
      inputrequired: ''
      isvisible: true
      label: Name
      name: lblName
      obj_id: '255'
      type: FixedText
    - controlid: control4
      convertemptytonull: 'true'
      datafield: Name
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      isvisible: true
      label: ''
      name: txtName
      obj_id: '256'
      type: TextField
    - controlid: control5
      convertemptytonull: ''
      datafield: ''
      eventlisteners: []
      formfor: control6
      inputrequired: ''
      isvisible: true
      label: Desc
      name: lblDesc
      obj_id: '257'
      type: FixedText
    - controlid: control6
      convertemptytonull: 'true'
      datafield: Desc
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      isvisible: true
      label: ''
      name: txtDesc
      obj_id: '258'
      type: TextField
    depth: 1
    detailfields: '"FamilyID"'
    link:
      content_type: table
      local_id: Family
    masterfields: '"RFamliyID"'
    name: SubForm
    obj_id: '252'
    subforms: []
title: Related subform
used_by: []
uses:
- content_type: table
  local_id: Plant
- content_type: table
  local_id: Family
---
