---
!!python/object:odbinfo.pure.datatype.exec.Module
callables:
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 7
    text: Error
    type: 49
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 8
    text: ' '
    type: 185
  - &id001 !!python/object:odbinfo.pure.datatype.base.Token
    index: 9
    text: '"Mijn fout"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 10
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
    index: 20
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: CalleeSub.Module1.Library1
      object_type: basicfunctions
    obj_id: '399'
    text: CalleeSub
    type: 181
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
  - &id003 !!python/object:odbinfo.pure.datatype.base.Token
    index: 24
    text: Module2
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 25
    text: .
    type: 150
  - &id004 !!python/object:odbinfo.pure.datatype.base.Token
    index: 26
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: CalleeSub.Module2.Library1
      object_type: basicfunctions
    obj_id: '405'
    text: CalleeSub
    type: 181
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
  uses:
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: CalleeSub.Module1.Library1
    object_type: basicfunctions
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: CalleeSub.Module2.Library1
    object_type: basicfunctions
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 39
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 40
    text: ' '
    type: 185
  - &id005 !!python/object:odbinfo.pure.datatype.base.Token
    index: 41
    text: '"Module1.CalleeSub"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 42
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
  used_by:
  - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
    local_id: CallerSub.Module1.Library1
    location_id: '399'
    object_type: basicfunctions
  uses: []
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens:
  - &id006 !!python/object:odbinfo.pure.datatype.base.Token
    index: 52
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: CalleeTwoSub.Module2.Library1
      object_type: basicfunctions
    obj_id: '431'
    text: CalleeTwoSub
    type: 181
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
  uses:
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: CalleeTwoSub.Module2.Library1
    object_type: basicfunctions
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens:
  - &id007 !!python/object:odbinfo.pure.datatype.base.Token
    index: 65
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: CalleeOtherLib.Module1.Standard
      object_type: basicfunctions
    obj_id: '444'
    text: CalleeOtherLib
    type: 181
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
  - &id008 !!python/object:odbinfo.pure.datatype.base.Token
    index: 69
    text: Module1
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 70
    text: .
    type: 150
  - &id009 !!python/object:odbinfo.pure.datatype.base.Token
    index: 71
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: CalleeOtherLib.Module1.Standard
      object_type: basicfunctions
    obj_id: '450'
    text: CalleeOtherLib
    type: 181
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
  uses:
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: CalleeOtherLib.Module1.Standard
    object_type: basicfunctions
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: CalleeOtherLib.Module1.Standard
    object_type: basicfunctions
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens:
  - &id010 !!python/object:odbinfo.pure.datatype.base.Token
    index: 84
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: ShadowedCallee.Module1.Library1
      object_type: basicfunctions
    obj_id: '463'
    text: ShadowedCallee
    type: 181
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
  uses:
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: ShadowedCallee.Module1.Library1
    object_type: basicfunctions
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 97
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 98
    text: ' '
    type: 185
  - &id011 !!python/object:odbinfo.pure.datatype.base.Token
    index: 99
    text: '"Library1.Module1.ShadowedCallee"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 100
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
  used_by:
  - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
    local_id: CallerShadowedCallee.Module1.Library1
    location_id: '463'
    object_type: basicfunctions
  uses: []
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 110
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 111
    text: ' '
    type: 185
  - &id012 !!python/object:odbinfo.pure.datatype.base.Token
    index: 112
    link: &id015 !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Plant
      object_type: tables
    obj_id: '491'
    text: '"Plant"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 113
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
  uses:
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: Plant
    object_type: tables
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 123
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 124
    text: ' '
    type: 185
  - &id013 !!python/object:odbinfo.pure.datatype.base.Token
    index: 125
    link: &id016 !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: view1
      object_type: views
    obj_id: '504'
    text: '"view1"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 126
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
  uses:
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: view1
    object_type: views
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 136
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 137
    text: ' '
    type: 185
  - &id014 !!python/object:odbinfo.pure.datatype.base.Token
    index: 138
    link: &id017 !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: FamilyLookup
      object_type: queries
    obj_id: '517'
    text: '"FamilyLookup"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 139
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
  uses:
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: FamilyLookup
    object_type: queries
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
  \tprint \"Module1.CalleeSub\"\nEnd Sub\n\nsub CallerTwo()\n\tCalleeTwoSub()\nEnd\
  \ Sub\n\nSub CallerOtherLib()\n\tCalleeOtherLib()\n\tModule1.CalleeOtherLib()\n\
  End Sub\n\nSub CallerShadowedCallee()\n\tShadowedCallee()\nEnd Sub\n\nSub ShadowedCallee()\n\
  \tprint \"Library1.Module1.ShadowedCallee\"\nEnd Sub\n\nSub ReferToTable()\n\tprint\
  \ \"Plant\"\nEnd Sub\n\nSub ReferToView()\n\tprint \"view1\"\nEnd Sub\n\nSub ReferToQuery()\n\
  \tprint \"FamilyLookup\"\nEnd Sub"
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
    local_id: Main.Module1.Library1
    object_type: basicfunctions
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
    local_id: CallerSub.Module1.Library1
    object_type: basicfunctions
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeSub
    local_id: Module1.Library1
    object_type: modules
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeSub
    local_id: Module2.Library1
    object_type: modules
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
    local_id: CalleeSub.Module1.Library1
    object_type: basicfunctions
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
    local_id: CallerTwo.Module1.Library1
    object_type: basicfunctions
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeTwoSub
    local_id: Module2.Library1
    object_type: modules
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
    local_id: CallerOtherLib.Module1.Library1
    object_type: basicfunctions
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeOtherLib
    local_id: Module1.Standard
    object_type: modules
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeOtherLib
    local_id: Module1.Standard
    object_type: modules
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
    local_id: CallerShadowedCallee.Module1.Library1
    object_type: basicfunctions
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: ShadowedCallee
    local_id: Module1.Library1
    object_type: modules
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
    local_id: ShadowedCallee.Module1.Library1
    object_type: basicfunctions
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
    local_id: ReferToTable.Module1.Library1
    object_type: basicfunctions
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
  link: *id015
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
    local_id: ReferToView.Module1.Library1
    object_type: basicfunctions
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
  link: *id016
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
    local_id: ReferToQuery.Module1.Library1
    object_type: basicfunctions
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
  link: *id017
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
---
