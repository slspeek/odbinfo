---
name: Plant invoeren
subforms:
- allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  command: vwPlant
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
      type: ooo:FormattedField
    - controlid: control3
      convertemptytonull: 'true'
      datafield: naam
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: naam
      name: naam
      type: ooo:TextField
    name: MainForm_Grid
  detailfields: ''
  masterfields: ''
  name: MainForm
---
