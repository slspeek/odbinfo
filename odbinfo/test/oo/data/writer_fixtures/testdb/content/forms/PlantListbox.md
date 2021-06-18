---
height: 0
name: PlantListbox
parent: null
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
    parent: null
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
    parent: null
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
    parent: null
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
    parent: null
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
    parent: null
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
    parent: null
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
    parent: null
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
    parent: null
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
    parent: null
    title: Knop 3
    type: CommandButton
    used_by: []
    uses: []
  depth: 0
  detailfields: ''
  embedded_query: null
  masterfields: ''
  name: MainForm
  parent: null
  subforms: []
  title: MainForm
  used_by: []
  uses: []
title: PlantListbox
used_by: []
uses: []
---
