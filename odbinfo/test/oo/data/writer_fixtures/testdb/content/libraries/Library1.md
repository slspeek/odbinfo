---
!!python/object:odbinfo.pure.datatype.exec.Library
modules:
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: Error
      type: 49
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: ' '
      type: 185
    - &id001 !!python/object:odbinfo.pure.datatype.base.Token
      text: '"Mijn fout"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: '

        '
      type: 183
    calls: []
    library: Library1
    module: Module1
    name: Main
    name_token_index: 5
    obj_id: '249'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings:
    - *id001
    title: Main.Module1.Library1
    tokens: []
    used_by: []
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id002 !!python/object:odbinfo.pure.datatype.base.Token
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: CalleeSub.Module1.Library1
        object_type: basicfunctions
      obj_id: '399'
      text: CalleeSub
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: "\n\t"
      type: 183
    - &id003 !!python/object:odbinfo.pure.datatype.base.Token
      text: Module2
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: .
      type: 150
    - &id004 !!python/object:odbinfo.pure.datatype.base.Token
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: CalleeSub.Module2.Library1
        object_type: basicfunctions
      obj_id: '405'
      text: CalleeSub
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: '

        '
      type: 183
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: *id002
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: *id003
      name_token: *id004
    library: Library1
    module: Module1
    name: CallerSub
    name_token_index: 16
    obj_id: '259'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings: []
    title: CallerSub.Module1.Library1
    tokens: []
    used_by: []
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: ' '
      type: 185
    - &id005 !!python/object:odbinfo.pure.datatype.base.Token
      text: '"Module1.CalleeSub"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: '

        '
      type: 183
    calls: []
    library: Library1
    module: Module1
    name: CalleeSub
    name_token_index: 35
    obj_id: '277'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings:
    - *id005
    title: CalleeSub.Module1.Library1
    tokens: []
    used_by: []
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id006 !!python/object:odbinfo.pure.datatype.base.Token
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: CalleeTwoSub.Module2.Library1
        object_type: basicfunctions
      obj_id: '431'
      text: CalleeTwoSub
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: '

        '
      type: 183
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: *id006
    library: Library1
    module: Module1
    name: CallerTwo
    name_token_index: 48
    obj_id: '289'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings: []
    title: CallerTwo.Module1.Library1
    tokens: []
    used_by: []
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id007 !!python/object:odbinfo.pure.datatype.base.Token
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: CalleeOtherLib.Module1.Standard
        object_type: basicfunctions
      obj_id: '444'
      text: CalleeOtherLib
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: "\n\t"
      type: 183
    - &id008 !!python/object:odbinfo.pure.datatype.base.Token
      text: Module1
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: .
      type: 150
    - &id009 !!python/object:odbinfo.pure.datatype.base.Token
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: CalleeOtherLib.Module1.Standard
        object_type: basicfunctions
      obj_id: '450'
      text: CalleeOtherLib
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: '

        '
      type: 183
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: *id007
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: *id008
      name_token: *id009
    library: Library1
    module: Module1
    name: CallerOtherLib
    name_token_index: 61
    obj_id: '301'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings: []
    title: CallerOtherLib.Module1.Library1
    tokens: []
    used_by: []
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id010 !!python/object:odbinfo.pure.datatype.base.Token
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: ShadowedCallee.Module1.Library1
        object_type: basicfunctions
      obj_id: '463'
      text: ShadowedCallee
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: '

        '
      type: 183
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: *id010
    library: Library1
    module: Module1
    name: CallerShadowedCallee
    name_token_index: 80
    obj_id: '319'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings: []
    title: CallerShadowedCallee.Module1.Library1
    tokens: []
    used_by: []
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: ' '
      type: 185
    - &id011 !!python/object:odbinfo.pure.datatype.base.Token
      text: '"Library1.Module1.ShadowedCallee"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: '

        '
      type: 183
    calls: []
    library: Library1
    module: Module1
    name: ShadowedCallee
    name_token_index: 93
    obj_id: '331'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings:
    - *id011
    title: ShadowedCallee.Module1.Library1
    tokens: []
    used_by: []
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: ' '
      type: 185
    - &id012 !!python/object:odbinfo.pure.datatype.base.Token
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: Plant
        object_type: tables
      obj_id: '491'
      text: '"Plant"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: '

        '
      type: 183
    calls: []
    library: Library1
    module: Module1
    name: ReferToTable
    name_token_index: 106
    obj_id: '343'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings:
    - *id012
    title: ReferToTable.Module1.Library1
    tokens: []
    used_by: []
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: ' '
      type: 185
    - &id013 !!python/object:odbinfo.pure.datatype.base.Token
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: view1
        object_type: views
      obj_id: '504'
      text: '"view1"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: '

        '
      type: 183
    calls: []
    library: Library1
    module: Module1
    name: ReferToView
    name_token_index: 119
    obj_id: '355'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings:
    - *id013
    title: ReferToView.Module1.Library1
    tokens: []
    used_by: []
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: ' '
      type: 185
    - &id014 !!python/object:odbinfo.pure.datatype.base.Token
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: FamilyLookup
        object_type: queries
      obj_id: '517'
      text: '"FamilyLookup"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: '

        '
      type: 183
    calls: []
    library: Library1
    module: Module1
    name: ReferToQuery
    name_token_index: 132
    obj_id: '367'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings:
    - *id014
    title: ReferToQuery.Module1.Library1
    tokens: []
    used_by: []
    uses: []
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
  obj_id: '248'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: Library1
    object_type: libraries
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
  uses: []
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: ' '
      type: 185
    - &id015 !!python/object:odbinfo.pure.datatype.base.Token
      text: '"Module2.CalleeSub"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: '

        '
      type: 183
    calls: []
    library: Library1
    module: Module2
    name: CalleeSub
    name_token_index: 5
    obj_id: '521'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module2.Library1
      object_type: modules
    strings:
    - *id015
    title: CalleeSub.Module2.Library1
    tokens: []
    used_by: []
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: ' '
      type: 185
    - &id016 !!python/object:odbinfo.pure.datatype.base.Token
      text: '"Module2.CalleeTwoSub"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: '

        '
      type: 183
    calls: []
    library: Library1
    module: Module2
    name: CalleeTwoSub
    name_token_index: 18
    obj_id: '533'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module2.Library1
      object_type: modules
    strings:
    - *id016
    title: CalleeTwoSub.Module2.Library1
    tokens: []
    used_by: []
    uses: []
  library: Library1
  name: Module2
  name_indexes:
  - 5
  - 18
  obj_id: '520'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: Library1
    object_type: libraries
  source: "REM  *****  BASIC  *****\n\nSub CalleeSub()\n\tprint \"Module2.CalleeSub\"\
    \nEnd Sub\n\nSub CalleeTwoSub()\n\tprint \"Module2.CalleeTwoSub\"\nEnd Sub"
  title: Module2.Library1
  tokens: []
  used_by: []
  uses: []
name: Library1
obj_id: '247'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: ./testdb.odb
  object_type: metadatas
title: Library1
used_by: []
uses: []
---
