---
height: 0
name: PlantListbox
obj_id: '139'
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
    obj_id: '141'
    type: FixedText
  - controlid: control3
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control4
    inputrequired: ''
    label: naam
    name: lblnaam
    obj_id: '142'
    type: FixedText
  - controlid: control5
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control6
    inputrequired: ''
    label: RFamliyID
    name: lblRFamliyID
    obj_id: '143'
    type: FixedText
  - controlid: control2
    convertemptytonull: 'true'
    datafield: id
    eventlisteners: []
    formfor: ''
    inputrequired: 'true'
    label: ''
    name: fmtid
    obj_id: '144'
    type: FormattedField
  - controlid: control4
    convertemptytonull: 'true'
    datafield: naam
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    name: txtnaam
    obj_id: '145'
    type: TextField
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
    obj_id: '146'
    type: ListBox
  - controlid: control7
    convertemptytonull: ''
    datafield: ''
    eventlisteners:
    - event: form:performaction
      name: ''
      obj_id: '148'
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    formfor: ''
    inputrequired: ''
    label: Say hello
    name: Knop 1
    obj_id: '147'
    type: CommandButton
  - controlid: control8
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: ''
    inputrequired: ''
    label: Knop
    name: Knop 2
    obj_id: '149'
    type: CommandButton
  - controlid: control9
    convertemptytonull: ''
    datafield: ''
    eventlisteners:
    - event: form:performaction
      name: ''
      obj_id: '151'
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    - event: form:approveaction
      name: ''
      obj_id: '152'
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    formfor: ''
    inputrequired: ''
    label: Call to script
    name: Knop 3
    obj_id: '150'
    type: CommandButton
  depth: 0
  detailfields: ''
  embedded_query: null
  masterfields: ''
  name: MainForm
  obj_id: '140'
  parent_link:
    bookmark: null
    local_id: PlantListbox
    object_type: forms
  subforms: []
  title: MainForm
title: PlantListbox
---
