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
      object_type: module
    strings:
    - &id001 !!python/object:odbinfo.pure.datatype.base.Token
      index: 9
      text: '"Mijn fout"'
      type: 172
    title: Main.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 3
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 4
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 5
      text: Main
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 6
      text: "\n\t"
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 7
      text: Error
      type: 49
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 8
      text: ' '
      type: 185
    - *id001
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 10
      text: '

        '
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 11
      text: End Sub
      type: 44
    used_by: []
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: &id002 !!python/object:odbinfo.pure.datatype.base.Token
        index: 20
        link: &id015 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: CalleeSub.Module1.Library1
          object_type: basicfunction
        obj_id: '449'
        text: CalleeSub
        type: 181
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: &id003 !!python/object:odbinfo.pure.datatype.base.Token
        index: 24
        text: Module2
        type: 181
      name_token: &id004 !!python/object:odbinfo.pure.datatype.base.Token
        index: 26
        link: &id016 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: CalleeSub.Module2.Library1
          object_type: basicfunction
        obj_id: '455'
        text: CalleeSub
        type: 181
    library: Library1
    module: Module1
    name: CallerSub
    name_token_index: 16
    obj_id: '309'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      object_type: module
    strings: []
    title: CallerSub.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 14
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 15
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 16
      text: CallerSub
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 17
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 18
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 19
      text: "\n\t"
      type: 183
    - *id002
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 21
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 22
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 23
      text: "\n\t"
      type: 183
    - *id003
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 25
      text: .
      type: 150
    - *id004
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 27
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 28
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 29
      text: '

        '
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 30
      text: End Sub
      type: 44
    used_by: []
    uses:
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeSub.Module1.Library1
      object_type: basicfunction
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeSub.Module2.Library1
      object_type: basicfunction
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
      object_type: module
    strings:
    - &id005 !!python/object:odbinfo.pure.datatype.base.Token
      index: 41
      text: '"Module1.CalleeSub"'
      type: 172
    title: CalleeSub.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 33
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 34
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 35
      text: CalleeSub
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 36
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 37
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 38
      text: "\n\t"
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 39
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 40
      text: ' '
      type: 185
    - *id005
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 42
      text: '

        '
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 43
      text: End Sub
      type: 44
    used_by:
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      bookmark: null
      local_id: CallerSub.Module1.Library1
      location_id: '449'
      object_type: basicfunction
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: &id006 !!python/object:odbinfo.pure.datatype.base.Token
        index: 52
        link: &id017 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: CalleeTwoSub.Module2.Library1
          object_type: basicfunction
        obj_id: '481'
        text: CalleeTwoSub
        type: 181
    library: Library1
    module: Module1
    name: CallerTwo
    name_token_index: 48
    obj_id: '339'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      object_type: module
    strings: []
    title: CallerTwo.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 46
      text: sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 47
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 48
      text: CallerTwo
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 49
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 50
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 51
      text: "\n\t"
      type: 183
    - *id006
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 53
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 54
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 55
      text: '

        '
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 56
      text: End Sub
      type: 44
    used_by: []
    uses:
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeTwoSub.Module2.Library1
      object_type: basicfunction
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: &id007 !!python/object:odbinfo.pure.datatype.base.Token
        index: 65
        link: &id018 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: CalleeOtherLib.Module1.Standard
          object_type: basicfunction
        obj_id: '494'
        text: CalleeOtherLib
        type: 181
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: &id008 !!python/object:odbinfo.pure.datatype.base.Token
        index: 69
        text: Module1
        type: 181
      name_token: &id009 !!python/object:odbinfo.pure.datatype.base.Token
        index: 71
        link: &id019 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: CalleeOtherLib.Module1.Standard
          object_type: basicfunction
        obj_id: '500'
        text: CalleeOtherLib
        type: 181
    library: Library1
    module: Module1
    name: CallerOtherLib
    name_token_index: 61
    obj_id: '351'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      object_type: module
    strings: []
    title: CallerOtherLib.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 59
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 60
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 61
      text: CallerOtherLib
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 62
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 63
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 64
      text: "\n\t"
      type: 183
    - *id007
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 66
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 67
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 68
      text: "\n\t"
      type: 183
    - *id008
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 70
      text: .
      type: 150
    - *id009
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 72
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 73
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 74
      text: '

        '
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 75
      text: End Sub
      type: 44
    used_by: []
    uses:
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeOtherLib.Module1.Standard
      object_type: basicfunction
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeOtherLib.Module1.Standard
      object_type: basicfunction
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: &id010 !!python/object:odbinfo.pure.datatype.base.Token
        index: 84
        link: &id020 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: ShadowedCallee.Module1.Library1
          object_type: basicfunction
        obj_id: '513'
        text: ShadowedCallee
        type: 181
    library: Library1
    module: Module1
    name: CallerShadowedCallee
    name_token_index: 80
    obj_id: '369'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      object_type: module
    strings: []
    title: CallerShadowedCallee.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 78
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 79
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 80
      text: CallerShadowedCallee
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 81
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 82
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 83
      text: "\n\t"
      type: 183
    - *id010
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 85
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 86
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 87
      text: '

        '
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 88
      text: End Sub
      type: 44
    used_by: []
    uses:
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: ShadowedCallee.Module1.Library1
      object_type: basicfunction
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
      object_type: module
    strings:
    - &id011 !!python/object:odbinfo.pure.datatype.base.Token
      index: 99
      text: '"Library1.Module1.ShadowedCallee"'
      type: 172
    title: ShadowedCallee.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 91
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 92
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 93
      text: ShadowedCallee
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 94
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 95
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 96
      text: "\n\t"
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 97
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 98
      text: ' '
      type: 185
    - *id011
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 100
      text: '

        '
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 101
      text: End Sub
      type: 44
    used_by:
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      bookmark: null
      local_id: CallerShadowedCallee.Module1.Library1
      location_id: '513'
      object_type: basicfunction
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
      object_type: module
    strings:
    - &id012 !!python/object:odbinfo.pure.datatype.base.Token
      index: 112
      link: &id021 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        local_id: Plant
        object_type: table
      obj_id: '541'
      text: '"Plant"'
      type: 172
    title: ReferToTable.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 104
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 105
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 106
      text: ReferToTable
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 107
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 108
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 109
      text: "\n\t"
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 110
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 111
      text: ' '
      type: 185
    - *id012
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 113
      text: '

        '
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 114
      text: End Sub
      type: 44
    used_by: []
    uses:
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Plant
      object_type: table
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
      object_type: module
    strings:
    - &id013 !!python/object:odbinfo.pure.datatype.base.Token
      index: 125
      link: &id022 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        local_id: view1
        object_type: view
      obj_id: '554'
      text: '"view1"'
      type: 172
    title: ReferToView.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 117
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 118
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 119
      text: ReferToView
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 120
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 121
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 122
      text: "\n\t"
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 123
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 124
      text: ' '
      type: 185
    - *id013
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 126
      text: '

        '
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 127
      text: End Sub
      type: 44
    used_by: []
    uses:
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: view1
      object_type: view
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
      object_type: module
    strings:
    - &id014 !!python/object:odbinfo.pure.datatype.base.Token
      index: 138
      link: &id023 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        local_id: FamilyLookup
        object_type: query
      obj_id: '567'
      text: '"FamilyLookup"'
      type: 172
    title: ReferToQuery.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 130
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 131
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 132
      text: ReferToQuery
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 133
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 134
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 135
      text: "\n\t"
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 136
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 137
      text: ' '
      type: 185
    - *id014
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 139
      text: '

        '
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 140
      text: End Sub
      type: 44
    used_by: []
    uses:
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: FamilyLookup
      object_type: query
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
    object_type: library
  source: "REM  *****  BASIC  *****\n\nSub Main\n\tError \"Mijn fout\"\nEnd Sub\n\n\
    Sub CallerSub()\n\tCalleeSub()\n\tModule2.CalleeSub()\nEnd Sub\n\nSub CalleeSub()\n\
    \tprint \"Module1.CalleeSub\"\nEnd Sub\n\nsub CallerTwo()\n\tCalleeTwoSub()\n\
    End Sub\n\nSub CallerOtherLib()\n\tCalleeOtherLib()\n\tModule1.CalleeOtherLib()\n\
    End Sub\n\nSub CallerShadowedCallee()\n\tShadowedCallee()\nEnd Sub\n\nSub ShadowedCallee()\n\
    \tprint \"Library1.Module1.ShadowedCallee\"\nEnd Sub\n\nSub ReferToTable()\n\t\
    print \"Plant\"\nEnd Sub\n\nSub ReferToView()\n\tprint \"view1\"\nEnd Sub\n\n\
    Sub ReferToQuery()\n\tprint \"FamilyLookup\"\nEnd Sub"
  title: Module1.Library1
  tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 0
    link: null
    text: REM  *****  BASIC  *****
    type: 184
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 1
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 2
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 3
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 4
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 5
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Main.Module1.Library1
      object_type: basicfunction
    text: Main
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 6
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 7
    link: null
    text: Error
    type: 49
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 8
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 9
    link: null
    text: '"Mijn fout"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 10
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 11
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 12
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 13
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 14
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 15
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 16
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CallerSub.Module1.Library1
      object_type: basicfunction
    text: CallerSub
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 17
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 18
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 19
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 20
    link: *id015
    text: CalleeSub
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 21
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 22
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 23
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 24
    link: null
    text: Module2
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 25
    link: null
    text: .
    type: 150
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 26
    link: *id016
    text: CalleeSub
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 27
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 28
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 29
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 30
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 31
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 32
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 33
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 34
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 35
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeSub.Module1.Library1
      object_type: basicfunction
    text: CalleeSub
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 36
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 37
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 38
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 39
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 40
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 41
    link: null
    text: '"Module1.CalleeSub"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 42
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 43
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 44
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 45
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 46
    link: null
    text: sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 47
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 48
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CallerTwo.Module1.Library1
      object_type: basicfunction
    text: CallerTwo
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 49
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 50
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 51
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 52
    link: *id017
    text: CalleeTwoSub
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 53
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 54
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 55
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 56
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 57
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 58
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 59
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 60
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 61
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CallerOtherLib.Module1.Library1
      object_type: basicfunction
    text: CallerOtherLib
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 62
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 63
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 64
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 65
    link: *id018
    text: CalleeOtherLib
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 66
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 67
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 68
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 69
    link: null
    text: Module1
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 70
    link: null
    text: .
    type: 150
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 71
    link: *id019
    text: CalleeOtherLib
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 72
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 73
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 74
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 75
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 76
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 77
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 78
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 79
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 80
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CallerShadowedCallee.Module1.Library1
      object_type: basicfunction
    text: CallerShadowedCallee
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 81
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 82
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 83
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 84
    link: *id020
    text: ShadowedCallee
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 85
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 86
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 87
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 88
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 89
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 90
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 91
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 92
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 93
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: ShadowedCallee.Module1.Library1
      object_type: basicfunction
    text: ShadowedCallee
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 94
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 95
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 96
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 97
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 98
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 99
    link: null
    text: '"Library1.Module1.ShadowedCallee"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 100
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 101
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 102
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 103
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 104
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 105
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 106
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: ReferToTable.Module1.Library1
      object_type: basicfunction
    text: ReferToTable
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 107
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 108
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 109
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 110
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 111
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 112
    link: *id021
    text: '"Plant"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 113
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 114
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 115
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 116
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 117
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 118
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 119
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: ReferToView.Module1.Library1
      object_type: basicfunction
    text: ReferToView
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 120
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 121
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 122
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 123
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 124
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 125
    link: *id022
    text: '"view1"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 126
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 127
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 128
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 129
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 130
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 131
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 132
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: ReferToQuery.Module1.Library1
      object_type: basicfunction
    text: ReferToQuery
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 133
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 134
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 135
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 136
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 137
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 138
    link: *id023
    text: '"FamilyLookup"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 139
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 140
    link: null
    text: End Sub
    type: 44
  used_by: []
  uses: []
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
      object_type: module
    strings:
    - &id024 !!python/object:odbinfo.pure.datatype.base.Token
      index: 11
      text: '"Module2.CalleeSub"'
      type: 172
    title: CalleeSub.Module2.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 3
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 4
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 5
      text: CalleeSub
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 6
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 7
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 8
      text: "\n\t"
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 9
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 10
      text: ' '
      type: 185
    - *id024
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 12
      text: '

        '
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 13
      text: End Sub
      type: 44
    used_by:
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      bookmark: null
      local_id: CallerSub.Module1.Library1
      location_id: '455'
      object_type: basicfunction
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
      object_type: module
    strings:
    - &id025 !!python/object:odbinfo.pure.datatype.base.Token
      index: 24
      text: '"Module2.CalleeTwoSub"'
      type: 172
    title: CalleeTwoSub.Module2.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 16
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 17
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 18
      text: CalleeTwoSub
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 19
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 20
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 21
      text: "\n\t"
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 22
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 23
      text: ' '
      type: 185
    - *id025
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 25
      text: '

        '
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 26
      text: End Sub
      type: 44
    used_by:
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      bookmark: null
      local_id: CallerTwo.Module1.Library1
      location_id: '481'
      object_type: basicfunction
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
    object_type: library
  source: "REM  *****  BASIC  *****\n\nSub CalleeSub()\n\tprint \"Module2.CalleeSub\"\
    \nEnd Sub\n\nSub CalleeTwoSub()\n\tprint \"Module2.CalleeTwoSub\"\nEnd Sub"
  title: Module2.Library1
  tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 0
    link: null
    text: REM  *****  BASIC  *****
    type: 184
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 1
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 2
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 3
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 4
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 5
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeSub.Module2.Library1
      object_type: basicfunction
    text: CalleeSub
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 6
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 7
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 8
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 9
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 10
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 11
    link: null
    text: '"Module2.CalleeSub"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 12
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 13
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 14
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 15
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 16
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 17
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 18
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeTwoSub.Module2.Library1
      object_type: basicfunction
    text: CalleeTwoSub
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 19
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 20
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 21
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 22
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 23
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 24
    link: null
    text: '"Module2.CalleeTwoSub"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 25
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 26
    link: null
    text: End Sub
    type: 44
  used_by: []
  uses: []
name: Library1
obj_id: '297'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadata
title: Library1
used_by: []
uses: []
---
