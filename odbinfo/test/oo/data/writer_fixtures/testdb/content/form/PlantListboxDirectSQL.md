---
!!python/object:odbinfo.pure.datatype.ui.Form
height: 0
name: PlantListboxDirectSQL
obj_id: '177'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: testdb
subforms:
- !!python/object:odbinfo.pure.datatype.ui.SubForm
  allowdeletes: 'false'
  allowinserts: 'true'
  allowupdates: 'true'
  command: Plant
  commandtype: table
  controls:
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control1
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control2
    inputrequired: ''
    label: id
    name: lblid
    obj_id: '179'
    type: FixedText
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control3
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control4
    inputrequired: ''
    label: naam
    name: lblnaam
    obj_id: '180'
    type: FixedText
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control5
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control6
    inputrequired: ''
    label: RFamliyID
    name: lblRFamliyID
    obj_id: '181'
    type: FixedText
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control2
    convertemptytonull: 'true'
    datafield: id
    eventlisteners: []
    formfor: ''
    inputrequired: 'true'
    label: ''
    name: fmtid
    obj_id: '182'
    type: FormattedField
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control4
    convertemptytonull: 'true'
    datafield: naam
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    label: ''
    name: txtnaam
    obj_id: '183'
    type: TextField
  - !!python/object:odbinfo.pure.datatype.ui.ListBox
    boundcolumn: '1'
    controlid: control6
    convertemptytonull: ''
    datafield: RFamliyID
    dropdown: 'true'
    embedded_query: !!python/object:odbinfo.pure.datatype.tabular.EmbeddedQuery
      columns: []
      command: "SELECT \"Name\",\n       \"FamilyID\"\nFROM   \"Family\""
      name: fmtRFamliyID.Command
      obj_id: '185'
      table_tokens: []
      tokens:
      - text: SELECT
        type: 131
      - text: ' '
        type: 207
      - text: '"Name"'
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
      - text: '"FamilyID"'
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
          local_id: Family
        obj_id: '204'
        text: '"Family"'
        type: 200
    eventlisteners: []
    formfor: ''
    inputrequired: 'true'
    label: ''
    listsource: SELECT "Name", "FamilyID" FROM "Family"
    listsourcetype: sql
    name: fmtRFamliyID
    obj_id: '184'
    type: ListBox
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control7
    convertemptytonull: ''
    datafield: ''
    eventlisteners:
    - !!python/object:odbinfo.pure.datatype.ui.EventListener
      link: &id003 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        content_type: basicfunction
        local_id: Main.Module1.Library1
      name: form:performaction
      obj_id: '206'
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    formfor: ''
    inputrequired: ''
    label: Say hello
    name: Knop 1
    obj_id: '205'
    type: CommandButton
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control8
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: ''
    inputrequired: ''
    label: Knop
    name: Knop 2
    obj_id: '207'
    type: CommandButton
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control9
    convertemptytonull: ''
    datafield: ''
    eventlisteners:
    - !!python/object:odbinfo.pure.datatype.ui.EventListener
      link: &id004 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        content_type: basicfunction
        local_id: Main.Module1.Library1
      name: form:performaction
      obj_id: '209'
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    - !!python/object:odbinfo.pure.datatype.ui.EventListener
      link: &id005 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        content_type: basicfunction
        local_id: Main.Module1.Library1
      name: form:approveaction
      obj_id: '210'
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    formfor: ''
    inputrequired: ''
    label: Call to script
    name: Knop 3
    obj_id: '208'
    type: CommandButton
  depth: 0
  detailfields: ''
  link: &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: table
    local_id: Plant
  masterfields: ''
  name: MainForm
  obj_id: '178'
  subforms: []
title: PlantListboxDirectSQL
used_by: []
uses:
- *id001
- *id002
- *id003
- *id004
- *id005
---
