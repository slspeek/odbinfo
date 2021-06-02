---
name: Plant
subforms:
- allowdeletes: 'true'
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
  - controlid: control6
    convertemptytonull: 'true'
    datafield: RFamliyID
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    name: fmtRFamliyID
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
  detailfields: ''
  embedded_query: null
  masterfields: ''
  name: MainForm
  subforms: []
  title: MainForm
title: Plant
---
