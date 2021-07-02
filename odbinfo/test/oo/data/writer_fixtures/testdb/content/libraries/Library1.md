---
!!python/object:odbinfo.pure.datatype.exec.Library
modules:
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 7
      obj_id: '386'
      text: Error
      type: 49
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 8
      obj_id: '387'
      text: ' '
      type: 185
    - &id001 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 9
      obj_id: '388'
      text: '"Mijn fout"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 10
      obj_id: '389'
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
      hidden: false
      index: 20
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: CalleeSub.Module1.Library1
        object_type: basicfunctions
      obj_id: '399'
      text: CalleeSub
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 21
      obj_id: '400'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 22
      obj_id: '401'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 23
      obj_id: '402'
      text: "\n\t"
      type: 183
    - &id003 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 24
      obj_id: '403'
      text: Module2
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 25
      obj_id: '404'
      text: .
      type: 150
    - &id004 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 26
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: CalleeSub.Module2.Library1
        object_type: basicfunctions
      obj_id: '405'
      text: CalleeSub
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 27
      obj_id: '406'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 28
      obj_id: '407'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 29
      obj_id: '408'
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
      hidden: false
      index: 39
      obj_id: '418'
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 40
      obj_id: '419'
      text: ' '
      type: 185
    - &id005 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 41
      obj_id: '420'
      text: '"Module1.CalleeSub"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 42
      obj_id: '421'
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
      hidden: false
      index: 52
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: CalleeTwoSub.Module2.Library1
        object_type: basicfunctions
      obj_id: '431'
      text: CalleeTwoSub
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 53
      obj_id: '432'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 54
      obj_id: '433'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 55
      obj_id: '434'
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
      hidden: false
      index: 65
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: CalleeOtherLib.Module1.Standard
        object_type: basicfunctions
      obj_id: '444'
      text: CalleeOtherLib
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 66
      obj_id: '445'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 67
      obj_id: '446'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 68
      obj_id: '447'
      text: "\n\t"
      type: 183
    - &id008 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 69
      obj_id: '448'
      text: Module1
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 70
      obj_id: '449'
      text: .
      type: 150
    - &id009 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 71
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: CalleeOtherLib.Module1.Standard
        object_type: basicfunctions
      obj_id: '450'
      text: CalleeOtherLib
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 72
      obj_id: '451'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 73
      obj_id: '452'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 74
      obj_id: '453'
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
      hidden: false
      index: 84
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: ShadowedCallee.Module1.Library1
        object_type: basicfunctions
      obj_id: '463'
      text: ShadowedCallee
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 85
      obj_id: '464'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 86
      obj_id: '465'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 87
      obj_id: '466'
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
      hidden: false
      index: 97
      obj_id: '476'
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 98
      obj_id: '477'
      text: ' '
      type: 185
    - &id011 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 99
      obj_id: '478'
      text: '"Library1.Module1.ShadowedCallee"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 100
      obj_id: '479'
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
      hidden: false
      index: 110
      obj_id: '489'
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 111
      obj_id: '490'
      text: ' '
      type: 185
    - &id012 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 112
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: Plant
        object_type: tables
      obj_id: '491'
      text: '"Plant"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 113
      obj_id: '492'
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
      hidden: false
      index: 123
      obj_id: '502'
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 124
      obj_id: '503'
      text: ' '
      type: 185
    - &id013 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 125
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: view1
        object_type: views
      obj_id: '504'
      text: '"view1"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 126
      obj_id: '505'
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
      hidden: false
      index: 136
      obj_id: '515'
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 137
      obj_id: '516'
      text: ' '
      type: 185
    - &id014 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 138
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: FamilyLookup
        object_type: queries
      obj_id: '517'
      text: '"FamilyLookup"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 139
      obj_id: '518'
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
      hidden: false
      index: 9
      obj_id: '554'
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 10
      obj_id: '555'
      text: ' '
      type: 185
    - &id015 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 11
      obj_id: '556'
      text: '"Module2.CalleeSub"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 12
      obj_id: '557'
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
      hidden: false
      index: 22
      obj_id: '567'
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 23
      obj_id: '568'
      text: ' '
      type: 185
    - &id016 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 24
      obj_id: '569'
      text: '"Module2.CalleeTwoSub"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 25
      obj_id: '570'
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
