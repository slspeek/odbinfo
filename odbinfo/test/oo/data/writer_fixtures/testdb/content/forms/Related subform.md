---
height: 1
name: Related subform
parent: null
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
    parent: null
    title: lblid
    type: FixedText
    used_by: []
    uses: []
  - controlid: control9
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control10
    inputrequired: ''
    label: naam
    name: lblnaam
    parent: null
    title: lblnaam
    type: FixedText
    used_by: []
    uses: []
  - controlid: control11
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control12
    inputrequired: ''
    label: RFamliyID
    name: lblRFamliyID
    parent: null
    title: lblRFamliyID
    type: FixedText
    used_by: []
    uses: []
  - controlid: control8
    convertemptytonull: 'true'
    datafield: id
    eventlisteners: []
    formfor: ''
    inputrequired: 'true'
    label: ''
    name: fmtid
    parent: null
    title: fmtid
    type: FormattedField
    used_by: []
    uses: []
  - controlid: control12
    convertemptytonull: 'true'
    datafield: RFamliyID
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    name: fmtRFamliyID
    parent: null
    title: fmtRFamliyID
    type: FormattedField
    used_by: []
    uses: []
  - controlid: control10
    convertemptytonull: 'true'
    datafield: naam
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    name: txtnaam
    parent: null
    title: txtnaam
    type: TextField
    used_by: []
    uses: []
  depth: 0
  detailfields: ''
  embedded_query: null
  masterfields: ''
  name: MainForm
  parent: null
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
      parent: null
      title: lblFamilyID
      type: FixedText
      used_by: []
      uses: []
    - controlid: control3
      convertemptytonull: ''
      datafield: ''
      eventlisteners: []
      formfor: control4
      inputrequired: ''
      label: Name
      name: lblName
      parent: null
      title: lblName
      type: FixedText
      used_by: []
      uses: []
    - controlid: control5
      convertemptytonull: ''
      datafield: ''
      eventlisteners: []
      formfor: control6
      inputrequired: ''
      label: Desc
      name: lblDesc
      parent: null
      title: lblDesc
      type: FixedText
      used_by: []
      uses: []
    - controlid: control2
      convertemptytonull: 'true'
      datafield: FamilyID
      eventlisteners: []
      formfor: ''
      inputrequired: 'true'
      label: ''
      name: fmtFamilyID
      parent: null
      title: fmtFamilyID
      type: FormattedField
      used_by: []
      uses: []
    - controlid: control4
      convertemptytonull: 'true'
      datafield: Name
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: ''
      name: txtName
      parent: null
      title: txtName
      type: TextField
      used_by: []
      uses: []
    - controlid: control6
      convertemptytonull: 'true'
      datafield: Desc
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: ''
      name: txtDesc
      parent: null
      title: txtDesc
      type: TextField
      used_by: []
      uses: []
    depth: 1
    detailfields: '"FamilyID"'
    embedded_query: null
    masterfields: '"RFamliyID"'
    name: SubForm
    parent: null
    subforms: []
    title: SubForm
    used_by: []
    uses: []
  title: MainForm
  used_by: []
  uses: []
title: Related subform
used_by: []
uses: []
---
