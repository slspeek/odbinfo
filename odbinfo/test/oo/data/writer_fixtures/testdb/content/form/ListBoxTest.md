---
!!python/object:odbinfo.pure.datatype.ui.Form
height: 0
name: ListBoxTest
obj_id: '155'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: testdb
subforms:
- !!python/object:odbinfo.pure.datatype.ui.SubForm
  allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  command: vwPlant
  commandtype: query
  controls:
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control1
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control2
    inputrequired: ''
    label: id
    name: id label
    obj_id: '157'
    type: FixedText
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control3
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control4
    inputrequired: ''
    label: naam
    name: naam label
    obj_id: '158'
    type: FixedText
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control5
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control6
    inputrequired: ''
    label: RFamliyID
    name: RFamliyID label
    obj_id: '159'
    type: FixedText
  - !!python/object:odbinfo.pure.datatype.ui.ListBox
    boundcolumn: '1'
    controlid: control2
    convertemptytonull: ''
    datafield: id
    dropdown: 'true'
    embedded_query: !!python/object:odbinfo.pure.datatype.tabular.EmbeddedQuery
      columns: []
      command: "SELECT \"id\",\n       \"naam\"\nFROM   \"Plant\""
      literal_values: []
      name: id.Command
      obj_id: '161'
      table_tokens: []
      tokens:
      - text: SELECT
        type: 131
      - text: ' '
        type: 207
      - text: '"id"'
        type: 200
      - text: ','
        type: 5
      - text: '

          '
        type: 207
      - text: ' '
        type: 207
      - text: ' '
        type: 207
      - text: ' '
        type: 207
      - text: ' '
        type: 207
      - text: ' '
        type: 207
      - text: ' '
        type: 207
      - text: ' '
        type: 207
      - text: '"naam"'
        type: 200
      - text: '

          '
        type: 207
      - text: FROM
        type: 77
      - text: ' '
        type: 207
      - text: ' '
        type: 207
      - text: ' '
        type: 207
      - link: &id002 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          content_type: table
          local_id: Plant
        obj_id: '180'
        text: '"Plant"'
        type: 200
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    listsource: select "id", "naam" from "Plant"
    listsourcetype: sql-pass-through
    name: id
    obj_id: '160'
    type: ListBox
  - !!python/object:odbinfo.pure.datatype.ui.ListBox
    boundcolumn: '1'
    controlid: control4
    convertemptytonull: ''
    datafield: naam
    dropdown: 'true'
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    link: &id003 !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      content_type: table
      local_id: Plant
    listsource: Plant
    listsourcetype: table-fields
    name: naam
    obj_id: '181'
    type: ListBox
  - !!python/object:odbinfo.pure.datatype.ui.ListBox
    boundcolumn: '1'
    controlid: control6
    convertemptytonull: ''
    datafield: RFamliyID
    dropdown: 'true'
    eventlisteners: []
    formfor: ''
    inputrequired: 'true'
    label: ''
    listsource: 1, 2, 3
    listsourcetype: valuelist
    name: ListBoxValuesRFamliyID
    obj_id: '182'
    type: ListBox
  depth: 0
  detailfields: ''
  link: &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: query
    local_id: vwPlant
  masterfields: ''
  name: MainForm
  obj_id: '156'
  subforms: []
title: ListBoxTest
used_by: []
uses:
- *id001
- *id002
- *id003
---
