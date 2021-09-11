---
!!python/object:odbinfo.pure.datatype.ui.Form
height: 0
name: PlantListbox
obj_id: '135'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: ./testdb.odb
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
    obj_id: '137'
    title: lblid
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
    obj_id: '138'
    title: lblnaam
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
    obj_id: '139'
    title: lblRFamliyID
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
    obj_id: '140'
    title: fmtid
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
    obj_id: '141'
    title: txtnaam
    type: TextField
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
    link: &id002 !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      content_type: query
      local_id: FamilyLookup
    listsource: FamilyLookup
    listsourcetype: query
    name: fmtRFamliyID
    obj_id: '142'
    title: fmtRFamliyID
    type: ListBox
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control7
    convertemptytonull: ''
    datafield: ''
    eventlisteners:
    - !!python/object:odbinfo.pure.datatype.ui.EventListener
      event: form:performaction
      link: &id003 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        content_type: basicfunction
        local_id: Main.Module1.Library1
      obj_id: '144'
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    formfor: ''
    inputrequired: ''
    label: Say hello
    name: Knop 1
    obj_id: '143'
    title: Knop 1
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
    obj_id: '145'
    title: Knop 2
    type: CommandButton
  - !!python/object:odbinfo.pure.datatype.ui.Control
    controlid: control9
    convertemptytonull: ''
    datafield: ''
    eventlisteners:
    - !!python/object:odbinfo.pure.datatype.ui.EventListener
      event: form:performaction
      link: &id004 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        content_type: basicfunction
        local_id: Main.Module1.Library1
      obj_id: '147'
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    - !!python/object:odbinfo.pure.datatype.ui.EventListener
      event: form:approveaction
      link: &id005 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        content_type: basicfunction
        local_id: Main.Module1.Library1
      obj_id: '148'
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    formfor: ''
    inputrequired: ''
    label: Call to script
    name: Knop 3
    obj_id: '146'
    title: Knop 3
    type: CommandButton
  depth: 0
  detailfields: ''
  link: &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: table
    local_id: Plant
  masterfields: ''
  name: MainForm
  obj_id: '136'
  subforms: []
  title: MainForm
title: PlantListbox
used_by: []
uses:
- *id001
- *id002
- *id003
- *id004
- *id005
---
