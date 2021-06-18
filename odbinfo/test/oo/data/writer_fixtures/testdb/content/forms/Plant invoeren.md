---
height: 0
name: Plant invoeren
subforms:
- allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  command:
    link:
      bookmark: null
      local_id: vwPlant
      object_type: queries
    text: vwPlant
  commandtype: query
  controls:
  - columns:
    - controlid: control2
      convertemptytonull: 'true'
      datafield: id
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: id
      name: id
      title: ''
      type: ooo:FormattedField
    - controlid: control3
      convertemptytonull: 'true'
      datafield: naam
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: naam
      name: naam
      title: ''
      type: ooo:TextField
    name: MainForm_Grid
    title: MainForm_Grid
  depth: 0
  detailfields: ''
  embedded_query: null
  masterfields: ''
  name: MainForm
  subforms: []
  title: MainForm
title: Plant invoeren
---
