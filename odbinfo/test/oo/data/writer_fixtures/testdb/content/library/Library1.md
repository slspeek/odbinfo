---
!!python/object:odbinfo.pure.datatype.exec.Library
modules:
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Library1
    module: Module1
    name: Main
    name_token_index: 5
    obj_id: '299'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      content_type: module
    strings:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 9
      text: '"Mijn fout"'
      type: 172
    title: Main.Module1.Library1
    tokens: []
    used_by: []
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: !!python/object:odbinfo.pure.datatype.base.Token
        index: 20
        link: &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: CalleeSub.Module1.Library1
          content_type: basicfunction
        obj_id: '316'
        text: CalleeSub
        title: token20.CallerSub.Module1.Library1
        type: 181
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: !!python/object:odbinfo.pure.datatype.base.Token
        index: 24
        text: Module2
        type: 181
      name_token: !!python/object:odbinfo.pure.datatype.base.Token
        index: 26
        link: &id002 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: CalleeSub.Module2.Library1
          content_type: basicfunction
        obj_id: '322'
        text: CalleeSub
        title: token26.CallerSub.Module1.Library1
        type: 181
    library: Library1
    module: Module1
    name: CallerSub
    name_token_index: 16
    obj_id: '309'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      content_type: module
    strings: []
    title: CallerSub.Module1.Library1
    tokens: []
    used_by: []
    uses:
    - *id001
    - *id002
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Library1
    module: Module1
    name: CalleeSub
    name_token_index: 35
    obj_id: '327'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      content_type: module
    strings:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 41
      text: '"Module1.CalleeSub"'
      type: 172
    title: CalleeSub.Module1.Library1
    tokens: []
    used_by:
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      bookmark: null
      local_id: CallerSub.Module1.Library1
      location_id: '316'
      content_type: basicfunction
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: !!python/object:odbinfo.pure.datatype.base.Token
        index: 52
        link: &id003 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: CalleeTwoSub.Module2.Library1
          content_type: basicfunction
        obj_id: '346'
        text: CalleeTwoSub
        title: token52.CallerTwo.Module1.Library1
        type: 181
    library: Library1
    module: Module1
    name: CallerTwo
    name_token_index: 48
    obj_id: '339'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      content_type: module
    strings: []
    title: CallerTwo.Module1.Library1
    tokens: []
    used_by: []
    uses:
    - *id003
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: !!python/object:odbinfo.pure.datatype.base.Token
        index: 65
        link: &id004 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: CalleeOtherLib.Module1.Standard
          content_type: basicfunction
        obj_id: '358'
        text: CalleeOtherLib
        title: token65.CallerOtherLib.Module1.Library1
        type: 181
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: !!python/object:odbinfo.pure.datatype.base.Token
        index: 69
        text: Module1
        type: 181
      name_token: !!python/object:odbinfo.pure.datatype.base.Token
        index: 71
        link: &id005 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: CalleeOtherLib.Module1.Standard
          content_type: basicfunction
        obj_id: '364'
        text: CalleeOtherLib
        title: token71.CallerOtherLib.Module1.Library1
        type: 181
    library: Library1
    module: Module1
    name: CallerOtherLib
    name_token_index: 61
    obj_id: '351'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      content_type: module
    strings: []
    title: CallerOtherLib.Module1.Library1
    tokens: []
    used_by: []
    uses:
    - *id004
    - *id005
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: !!python/object:odbinfo.pure.datatype.base.Token
        index: 84
        link: &id006 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: ShadowedCallee.Module1.Library1
          content_type: basicfunction
        obj_id: '376'
        text: ShadowedCallee
        title: token84.CallerShadowedCallee.Module1.Library1
        type: 181
    library: Library1
    module: Module1
    name: CallerShadowedCallee
    name_token_index: 80
    obj_id: '369'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      content_type: module
    strings: []
    title: CallerShadowedCallee.Module1.Library1
    tokens: []
    used_by: []
    uses:
    - *id006
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Library1
    module: Module1
    name: ShadowedCallee
    name_token_index: 93
    obj_id: '381'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      content_type: module
    strings:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 99
      text: '"Library1.Module1.ShadowedCallee"'
      type: 172
    title: ShadowedCallee.Module1.Library1
    tokens: []
    used_by:
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      bookmark: null
      local_id: CallerShadowedCallee.Module1.Library1
      location_id: '376'
      content_type: basicfunction
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Library1
    module: Module1
    name: ReferToTable
    name_token_index: 106
    obj_id: '393'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      content_type: module
    strings:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 112
      link: &id007 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        local_id: Plant
        content_type: table
      obj_id: '402'
      text: '"Plant"'
      title: token112.ReferToTable.Module1.Library1
      type: 172
    title: ReferToTable.Module1.Library1
    tokens: []
    used_by: []
    uses:
    - *id007
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Library1
    module: Module1
    name: ReferToView
    name_token_index: 119
    obj_id: '405'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      content_type: module
    strings:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 125
      link: &id008 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        local_id: view1
        content_type: view
      obj_id: '414'
      text: '"view1"'
      title: token125.ReferToView.Module1.Library1
      type: 172
    title: ReferToView.Module1.Library1
    tokens: []
    used_by: []
    uses:
    - *id008
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Library1
    module: Module1
    name: ReferToQuery
    name_token_index: 132
    obj_id: '417'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      content_type: module
    strings:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 138
      link: &id009 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        local_id: FamilyLookup
        content_type: query
      obj_id: '426'
      text: '"FamilyLookup"'
      title: token138.ReferToQuery.Module1.Library1
      type: 172
    title: ReferToQuery.Module1.Library1
    tokens: []
    used_by: []
    uses:
    - *id009
  library: Library1
  name: Module1
  name_indexes:
  - 5
  - 16
  - 35
  - 48
  - 61
  - 80
  - 93
  - 106
  - 119
  - 132
  obj_id: '298'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Library1
    content_type: library
  source: "REM  *****  BASIC  *****\n\nSub Main\n\tError \"Mijn fout\"\nEnd Sub\n\n\
    Sub CallerSub()\n\tCalleeSub()\n\tModule2.CalleeSub()\nEnd Sub\n\nSub CalleeSub()\n\
    \tprint \"Module1.CalleeSub\"\nEnd Sub\n\nsub CallerTwo()\n\tCalleeTwoSub()\n\
    End Sub\n\nSub CallerOtherLib()\n\tCalleeOtherLib()\n\tModule1.CalleeOtherLib()\n\
    End Sub\n\nSub CallerShadowedCallee()\n\tShadowedCallee()\nEnd Sub\n\nSub ShadowedCallee()\n\
    \tprint \"Library1.Module1.ShadowedCallee\"\nEnd Sub\n\nSub ReferToTable()\n\t\
    print \"Plant\"\nEnd Sub\n\nSub ReferToView()\n\tprint \"view1\"\nEnd Sub\n\n\
    Sub ReferToQuery()\n\tprint \"FamilyLookup\"\nEnd Sub"
  title: Module1.Library1
  tokens: []
  used_by: []
  uses:
  - *id001
  - *id002
  - *id003
  - *id004
  - *id005
  - *id006
  - *id007
  - *id008
  - *id009
  - &id010 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeSub
    local_id: Module1.Library1
    content_type: module
  - &id011 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeSub
    local_id: Module2.Library1
    content_type: module
  - &id012 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeTwoSub
    local_id: Module2.Library1
    content_type: module
  - &id013 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeOtherLib
    local_id: Module1.Standard
    content_type: module
  - &id014 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeOtherLib
    local_id: Module1.Standard
    content_type: module
  - &id015 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: ShadowedCallee
    local_id: Module1.Library1
    content_type: module
  - *id007
  - *id008
  - *id009
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Library1
    module: Module2
    name: CalleeSub
    name_token_index: 5
    obj_id: '571'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module2.Library1
      content_type: module
    strings:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 11
      text: '"Module2.CalleeSub"'
      type: 172
    title: CalleeSub.Module2.Library1
    tokens: []
    used_by:
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      bookmark: null
      local_id: CallerSub.Module1.Library1
      location_id: '322'
      content_type: basicfunction
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Library1
    module: Module2
    name: CalleeTwoSub
    name_token_index: 18
    obj_id: '583'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module2.Library1
      content_type: module
    strings:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 24
      text: '"Module2.CalleeTwoSub"'
      type: 172
    title: CalleeTwoSub.Module2.Library1
    tokens: []
    used_by:
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      bookmark: null
      local_id: CallerTwo.Module1.Library1
      location_id: '346'
      content_type: basicfunction
    uses: []
  library: Library1
  name: Module2
  name_indexes:
  - 5
  - 18
  obj_id: '570'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Library1
    content_type: library
  source: "REM  *****  BASIC  *****\n\nSub CalleeSub()\n\tprint \"Module2.CalleeSub\"\
    \nEnd Sub\n\nSub CalleeTwoSub()\n\tprint \"Module2.CalleeTwoSub\"\nEnd Sub"
  title: Module2.Library1
  tokens: []
  used_by: []
  uses: []
name: Library1
obj_id: '297'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: ./testdb.odb
  content_type: metadata
title: Library1
used_by: []
uses:
- *id001
- *id002
- *id003
- *id004
- *id005
- *id006
- *id007
- *id008
- *id009
- *id010
- *id011
- *id012
- *id013
- *id014
- *id015
- *id007
- *id008
- *id009
---
