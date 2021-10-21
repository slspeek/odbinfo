---
height: 0
name: ListBoxTest
obj_id: '155'
parent_link:
  bookmark: null
  content_type: metadata
  local_id: testdb
subforms:
- allowdeletes: 'true'
  allowinserts: 'true'
  allowupdates: 'true'
  cmd: vwPlant
  cmdtype: query
  controls:
  - controlid: control1
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control2
    inputrequired: ''
    label: id
    name: id label
    obj_id: '157'
    type: FixedText
  - boundcolumn: '1'
    controlid: control2
    convertemptytonull: ''
    datafield: id
    dropdown: 'true'
    embedded_query:
      columns: []
      command: "SELECT \"id\",\n       \"naam\"\nFROM   \"Plant\""
      literal_values: []
      name: id.Command
      obj_id: '159'
      table_tokens:
      - index: 18
        link: &id001
          bookmark: null
          content_type: table
          local_id: Plant
        obj_id: '178'
        text: '"Plant"'
        type: 200
      tokens:
      - index: 0
        text: SELECT
        type: 131
      - index: 1
        text: ' '
        type: 207
      - index: 2
        text: '"id"'
        type: 200
      - index: 3
        text: ','
        type: 5
      - index: 4
        text: '

          '
        type: 207
      - index: 5
        text: ' '
        type: 207
      - index: 6
        text: ' '
        type: 207
      - index: 7
        text: ' '
        type: 207
      - index: 8
        text: ' '
        type: 207
      - index: 9
        text: ' '
        type: 207
      - index: 10
        text: ' '
        type: 207
      - index: 11
        text: ' '
        type: 207
      - index: 12
        text: '"naam"'
        type: 200
      - index: 13
        text: '

          '
        type: 207
      - index: 14
        text: FROM
        type: 77
      - index: 15
        text: ' '
        type: 207
      - index: 16
        text: ' '
        type: 207
      - index: 17
        text: ' '
        type: 207
      - index: 18
        link: *id001
        obj_id: '178'
        text: '"Plant"'
        type: 200
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    listsource: select "id", "naam" from "Plant"
    listsourcetype: sql-pass-through
    name: id
    obj_id: '158'
    type: ListBox
  - controlid: control3
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control4
    inputrequired: ''
    label: naam
    name: naam label
    obj_id: '179'
    type: FixedText
  - boundcolumn: '1'
    controlid: control4
    convertemptytonull: ''
    datafield: naam
    dropdown: 'true'
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    link: &id003
      bookmark: null
      content_type: table
      local_id: Plant
    listsource: Plant
    listsourcetype: table-fields
    name: naam
    obj_id: '180'
    type: ListBox
  - controlid: control5
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control6
    inputrequired: ''
    label: RFamliyID
    name: RFamliyID label
    obj_id: '181'
    type: FixedText
  - boundcolumn: '1'
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
  link: &id002
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
- *id002
- *id001
- *id003
---
