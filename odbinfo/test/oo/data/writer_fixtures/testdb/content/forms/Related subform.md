---
height: 1
name: Related subform
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
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
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
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
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
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
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
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
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
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
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
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
    title: txtnaam
    type: TextField
    used_by: []
    uses: []
  depth: 0
  detailfields: ''
  embedded_query: null
  masterfields: ''
  name: MainForm
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
      parent_link:
        bookmark: null
        local_id: SubForm
        object_type: subforms
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
      parent_link:
        bookmark: null
        local_id: SubForm
        object_type: subforms
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
      parent_link:
        bookmark: null
        local_id: SubForm
        object_type: subforms
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
      parent_link:
        bookmark: null
        local_id: SubForm
        object_type: subforms
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
      parent_link:
        bookmark: null
        local_id: SubForm
        object_type: subforms
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
      parent_link:
        bookmark: null
        local_id: SubForm
        object_type: subforms
      title: txtDesc
      type: TextField
      used_by: []
      uses: []
    depth: 1
    detailfields: '"FamilyID"'
    embedded_query: null
    masterfields: '"RFamliyID"'
    name: SubForm
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
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
