---
height: 0
name: Plant invoeren
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
      parent_link:
        bookmark: null
        local_id: MainForm_Grid
        object_type: grids
      title: ''
      type: ooo:FormattedField
      used_by: []
      uses: []
    - controlid: control3
      convertemptytonull: 'true'
      datafield: naam
      eventlisteners: []
      formfor: ''
      inputrequired: 'false'
      label: naam
      name: naam
      parent_link:
        bookmark: null
        local_id: MainForm_Grid
        object_type: grids
      title: ''
      type: ooo:TextField
      used_by: []
      uses: []
    name: MainForm_Grid
    parent_link:
      bookmark: null
      local_id: MainForm
      object_type: subforms
    title: MainForm_Grid
    used_by: []
    uses: []
  depth: 0
  detailfields: ''
  embedded_query: null
  masterfields: ''
  name: MainForm
  parent_link:
    bookmark: null
    local_id: Plant invoeren
    object_type: forms
  subforms: []
  title: MainForm
  used_by: []
  uses: []
title: Plant invoeren
used_by: []
uses: []
---
