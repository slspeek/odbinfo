---
height: 0
name: PlantListbox
obj_id: 66
parent_link:
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadatas
subforms:
- allowdeletes: 'false'
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
  - controlid: control1
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control2
    inputrequired: ''
    label: id
    name: lblid
    obj_id: 68
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
    title: lblid
    type: FixedText
    used_by: []
    uses: []
  - controlid: control3
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control4
    inputrequired: ''
    label: naam
    name: lblnaam
    obj_id: 69
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
    title: lblnaam
    type: FixedText
    used_by: []
    uses: []
  - controlid: control5
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control6
    inputrequired: ''
    label: RFamliyID
    name: lblRFamliyID
    obj_id: 70
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
    title: lblRFamliyID
    type: FixedText
    used_by: []
    uses: []
  - controlid: control2
    convertemptytonull: 'true'
    datafield: id
    eventlisteners: []
    formfor: ''
    inputrequired: 'true'
    label: ''
    name: fmtid
    obj_id: 71
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
    title: fmtid
    type: FormattedField
    used_by: []
    uses: []
  - controlid: control4
    convertemptytonull: 'true'
    datafield: naam
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    name: txtnaam
    obj_id: 72
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
    title: txtnaam
    type: TextField
    used_by: []
    uses: []
  - boundcolumn: '1'
    controlid: control6
    convertemptytonull: ''
    datafield: RFamliyID
    dropdown: 'true'
    eventlisteners: []
    formfor: ''
    inputrequired: 'true'
    label: ''
    listsource: FamilyLookup
    listsourcetype: query
    name: fmtRFamliyID
    obj_id: 73
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
    title: fmtRFamliyID
    type: ListBox
    used_by: []
    uses: []
  - controlid: control7
    convertemptytonull: ''
    datafield: ''
    eventlisteners:
    - event: form:performaction
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    formfor: ''
    inputrequired: ''
    label: Say hello
    name: Knop 1
    obj_id: 74
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
    title: Knop 1
    type: CommandButton
    used_by: []
    uses: []
  - controlid: control8
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: ''
    inputrequired: ''
    label: Knop
    name: Knop 2
    obj_id: 75
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
    title: Knop 2
    type: CommandButton
    used_by: []
    uses: []
  - controlid: control9
    convertemptytonull: ''
    datafield: ''
    eventlisteners:
    - event: form:performaction
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    - event: form:approveaction
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    formfor: ''
    inputrequired: ''
    label: Call to script
    name: Knop 3
    obj_id: 76
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
    title: Knop 3
    type: CommandButton
    used_by: []
    uses: []
  depth: 0
  detailfields: ''
  embedded_query: null
  masterfields: ''
  name: MainForm
  obj_id: 67
  parent_link:
    bookmark: null
    local_id: PlantListbox
    object_type: forms
  subforms: []
  title: MainForm
  used_by: []
  uses: []
title: PlantListbox
used_by: []
uses: []
---
