---
height: 0
name: PlantListbox
obj_id: '196'
parent_link:
  content_type: metadata
  local_id: testdb
subforms:
- allowdeletes: 'false'
  allowinserts: 'true'
  allowupdates: 'true'
  cmd: Plant
  cmdtype: table
  controls:
  - controlid: control1
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control2
    inputrequired: ''
    isvisible: true
    label: id
    name: lblid
    obj_id: '198'
    type: FixedText
  - controlid: control2
    convertemptytonull: 'true'
    datafield: id
    eventlisteners: []
    formfor: ''
    inputrequired: 'true'
    isvisible: true
    label: ''
    name: fmtid
    obj_id: '199'
    type: FormattedField
  - controlid: control3
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control4
    inputrequired: ''
    isvisible: true
    label: naam
    name: lblnaam
    obj_id: '200'
    type: FixedText
  - controlid: control4
    convertemptytonull: 'true'
    datafield: naam
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    isvisible: true
    label: ''
    name: txtnaam
    obj_id: '201'
    type: TextField
  - controlid: control5
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control6
    inputrequired: ''
    isvisible: true
    label: RFamliyID
    name: lblRFamliyID
    obj_id: '202'
    type: FixedText
  - boundcolumn: '1'
    controlid: control6
    convertemptytonull: ''
    datafield: RFamliyID
    dropdown: 'true'
    eventlisteners: []
    formfor: ''
    inputrequired: 'true'
    isvisible: true
    label: ''
    link:
      content_type: query
      local_id: FamilyLookup
    listsource: FamilyLookup
    listsourcetype: query
    name: fmtRFamliyID
    obj_id: '203'
    type: ListBox
  - controlid: control7
    convertemptytonull: ''
    datafield: ''
    eventlisteners:
    - link:
        content_type: basicfunction
        local_id: Main.Module1.Library1
      name: form:performaction
      obj_id: '205'
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    formfor: ''
    inputrequired: ''
    isvisible: true
    label: Say hello
    name: Knop 1
    obj_id: '204'
    type: CommandButton
  - controlid: control8
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: ''
    inputrequired: ''
    isvisible: true
    label: Knop
    name: Knop 2
    obj_id: '206'
    type: CommandButton
  - controlid: control9
    convertemptytonull: ''
    datafield: ''
    eventlisteners:
    - link:
        content_type: basicfunction
        local_id: Main.Module1.Library1
      name: form:performaction
      obj_id: '208'
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    - link:
        content_type: basicfunction
        local_id: Main.Module1.Library1
      name: form:approveaction
      obj_id: '209'
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    formfor: ''
    inputrequired: ''
    isvisible: true
    label: Call to script
    name: Knop 3
    obj_id: '207'
    type: CommandButton
  depth: 0
  detailfields: ''
  link:
    content_type: table
    local_id: Plant
  masterfields: ''
  name: MainForm
  obj_id: '197'
  subforms: []
title: PlantListbox
used_by: []
uses:
- content_type: table
  local_id: Plant
- content_type: query
  local_id: FamilyLookup
- content_type: basicfunction
  local_id: Main.Module1.Library1
- content_type: basicfunction
  local_id: Main.Module1.Library1
- content_type: basicfunction
  local_id: Main.Module1.Library1
---
