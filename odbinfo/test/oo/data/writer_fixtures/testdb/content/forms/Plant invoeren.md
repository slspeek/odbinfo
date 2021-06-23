---
height: 0
name: Plant invoeren
obj_id: '134'
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
      obj_id: '137'
      type: ooo:FormattedField
    - controlid: control3
      convertemptytonull: 'true'
      datafield: naam
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: naam
      name: naam
      obj_id: '138'
      type: ooo:TextField
    name: MainForm_Grid
    obj_id: '136'
  depth: 0
  detailfields: ''
  embedded_query: null
  masterfields: ''
  name: MainForm
  obj_id: '135'
  parent_link:
    bookmark: null
    local_id: Plant invoeren
    object_type: forms
  subforms: []
  title: MainForm
title: Plant invoeren
---
