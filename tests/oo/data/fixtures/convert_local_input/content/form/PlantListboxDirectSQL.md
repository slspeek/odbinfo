---
height: 0
name: PlantListboxDirectSQL
obj_id: '210'
parent_link:
  content_type: metadata
  local_id: testdb
subforms:
- allowdeletes: 'false'
  allowinserts: 'true'
  allowupdates: 'true'
  cmd: Plant
  cmdtype: table
  controls:
  - controlid: control1
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control2
    inputrequired: ''
    isvisible: true
    label: id
    name: lblid
    obj_id: '212'
    type: FixedText
  - controlid: control2
    convertemptytonull: 'true'
    datafield: id
    eventlisteners: []
    formfor: ''
    inputrequired: 'true'
    isvisible: true
    label: ''
    name: fmtid
    obj_id: '213'
    type: FormattedField
  - controlid: control3
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control4
    inputrequired: ''
    isvisible: true
    label: naam
    name: lblnaam
    obj_id: '214'
    type: FixedText
  - controlid: control4
    convertemptytonull: 'true'
    datafield: naam
    eventlisteners: []
    formfor: ''
    inputrequired: 'false'
    isvisible: true
    label: ''
    name: txtnaam
    obj_id: '215'
    type: TextField
  - controlid: control5
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: control6
    inputrequired: ''
    isvisible: true
    label: RFamliyID
    name: lblRFamliyID
    obj_id: '216'
    type: FixedText
  - boundcolumn: '1'
    controlid: control6
    convertemptytonull: ''
    datafield: RFamliyID
    dropdown: 'true'
    embedded_query:
      command: "SELECT \"Name\",\n       \"FamilyID\"\nFROM   \"Family\""
      name: fmtRFamliyID.Command
      obj_id: '218'
      tokens:
      - text: SELECT
      - text: ' '
      - text: '"Name"'
      - text: ','
      - text: '

          '
      - text: ' '
      - text: ' '
      - text: ' '
      - text: ' '
      - text: ' '
      - text: ' '
      - text: ' '
      - text: '"FamilyID"'
      - text: '

          '
      - text: FROM
      - text: ' '
      - text: ' '
      - text: ' '
      - link:
          content_type: table
          local_id: Family
        obj_id: '237'
        text: '"Family"'
    eventlisteners: []
    formfor: ''
    inputrequired: 'true'
    isvisible: true
    label: ''
    listsource: SELECT "Name", "FamilyID" FROM "Family"
    listsourcetype: sql
    name: fmtRFamliyID
    obj_id: '217'
    type: ListBox
  - controlid: control7
    convertemptytonull: ''
    datafield: ''
    eventlisteners:
    - link:
        content_type: basicfunction
        local_id: Main.Module1.Library1
      name: form:performaction
      obj_id: '239'
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    formfor: ''
    inputrequired: ''
    isvisible: true
    label: Say hello
    name: Knop 1
    obj_id: '238'
    type: CommandButton
  - controlid: control8
    convertemptytonull: ''
    datafield: ''
    eventlisteners: []
    formfor: ''
    inputrequired: ''
    isvisible: true
    label: Knop
    name: Knop 2
    obj_id: '240'
    type: CommandButton
  - controlid: control9
    convertemptytonull: ''
    datafield: ''
    eventlisteners:
    - link:
        content_type: basicfunction
        local_id: Main.Module1.Library1
      name: form:performaction
      obj_id: '242'
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    - link:
        content_type: basicfunction
        local_id: Main.Module1.Library1
      name: form:approveaction
      obj_id: '243'
      script: vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document
    formfor: ''
    inputrequired: ''
    isvisible: true
    label: Call to script
    name: Knop 3
    obj_id: '241'
    type: CommandButton
  depth: 0
  detailfields: ''
  link:
    content_type: table
    local_id: Plant
  masterfields: ''
  name: MainForm
  obj_id: '211'
  subforms: []
title: PlantListboxDirectSQL
used_by: []
uses:
- link:
    content_type: table
    local_id: Plant
  sources: '211'
- link:
    content_type: table
    local_id: Family
  sources: '237'
- link:
    content_type: basicfunction
    local_id: Main.Module1.Library1
  sources: '239'
- link:
    content_type: basicfunction
    local_id: Main.Module1.Library1
  sources: '242'
- link:
    content_type: basicfunction
    local_id: Main.Module1.Library1
  sources: '243'
---
