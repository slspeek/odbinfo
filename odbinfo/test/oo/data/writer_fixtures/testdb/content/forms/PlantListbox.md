---
name: PlantListbox
subforms:
- allowdeletes: 'false'
  allowinserts: 'true'
  allowupdates: 'true'
  command: Plant
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
    type: ooo:com.sun.star.form.component.FixedText
  - controlid: control3
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control4
    inputrequired: ''
    label: naam
    name: lblnaam
    type: ooo:com.sun.star.form.component.FixedText
  - controlid: control5
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control6
    inputrequired: ''
    label: RFamliyID
    name: lblRFamliyID
    type: ooo:com.sun.star.form.component.FixedText
  - controlid: control2
    convertemptytonull: 'true'
    datafield: id
    eventlisteners: []
    formfor: ''
    inputrequired: 'true'
    label: ''
    name: fmtid
    type: ooo:com.sun.star.form.component.FormattedField
  - controlid: control4
    convertemptytonull: 'true'
    datafield: naam
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    name: txtnaam
    type: ooo:com.sun.star.form.component.TextField
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
    type: ooo:com.sun.star.form.component.ListBox
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
    type: ooo:com.sun.star.form.component.CommandButton
  - controlid: control8
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: ''
    inputrequired: ''
    label: Knop
    name: Knop 2
    type: ooo:com.sun.star.form.component.CommandButton
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
    type: ooo:com.sun.star.form.component.CommandButton
  detailfields: ''
  masterfields: ''
  name: MainForm
title: PlantListbox
---
