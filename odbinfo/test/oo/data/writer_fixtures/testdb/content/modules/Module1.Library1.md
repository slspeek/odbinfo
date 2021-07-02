---
!!python/object:odbinfo.pure.datatype.exec.Module
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
    link: &id015 !!python/object:odbinfo.pure.datatype.base.Identifier
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
    link: &id016 !!python/object:odbinfo.pure.datatype.base.Identifier
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
    link: &id017 !!python/object:odbinfo.pure.datatype.base.Identifier
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
  \tprint \"Module1.CalleeSub\"\nEnd Sub\n\nsub CallerTwo()\n\tCalleeTwoSub()\nEnd\
  \ Sub\n\nSub CallerOtherLib()\n\tCalleeOtherLib()\n\tModule1.CalleeOtherLib()\n\
  End Sub\n\nSub CallerShadowedCallee()\n\tShadowedCallee()\nEnd Sub\n\nSub ShadowedCallee()\n\
  \tprint \"Library1.Module1.ShadowedCallee\"\nEnd Sub\n\nSub ReferToTable()\n\tprint\
  \ \"Plant\"\nEnd Sub\n\nSub ReferToView()\n\tprint \"view1\"\nEnd Sub\n\nSub ReferToQuery()\n\
  \tprint \"FamilyLookup\"\nEnd Sub"
title: Module1.Library1
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: REM  *****  BASIC  *****
  type: 184
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: Main.Module1.Library1
    object_type: basicfunctions
  text: Main
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: Error
  type: 49
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '"Mijn fout"'
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: CallerSub.Module1.Library1
    object_type: basicfunctions
  text: CallerSub
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeSub
    local_id: Module1.Library1
    object_type: modules
  text: CalleeSub
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: Module2
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: .
  type: 150
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeSub
    local_id: Module2.Library1
    object_type: modules
  text: CalleeSub
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: CalleeSub.Module1.Library1
    object_type: basicfunctions
  text: CalleeSub
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: print
  type: 100
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '"Module1.CalleeSub"'
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: CallerTwo.Module1.Library1
    object_type: basicfunctions
  text: CallerTwo
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeTwoSub
    local_id: Module2.Library1
    object_type: modules
  text: CalleeTwoSub
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: CallerOtherLib.Module1.Library1
    object_type: basicfunctions
  text: CallerOtherLib
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeOtherLib
    local_id: Module1.Standard
    object_type: modules
  text: CalleeOtherLib
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: Module1
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: .
  type: 150
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeOtherLib
    local_id: Module1.Standard
    object_type: modules
  text: CalleeOtherLib
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: CallerShadowedCallee.Module1.Library1
    object_type: basicfunctions
  text: CallerShadowedCallee
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: ShadowedCallee
    local_id: Module1.Library1
    object_type: modules
  text: ShadowedCallee
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: ShadowedCallee.Module1.Library1
    object_type: basicfunctions
  text: ShadowedCallee
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: print
  type: 100
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '"Library1.Module1.ShadowedCallee"'
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: ReferToTable.Module1.Library1
    object_type: basicfunctions
  text: ReferToTable
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: print
  type: 100
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: *id015
  text: '"Plant"'
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: ReferToView.Module1.Library1
    object_type: basicfunctions
  text: ReferToView
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: print
  type: 100
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: *id016
  text: '"view1"'
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: ReferToQuery.Module1.Library1
    object_type: basicfunctions
  text: ReferToQuery
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: print
  type: 100
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: *id017
  text: '"FamilyLookup"'
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: End Sub
  type: 44
used_by: []
uses: []
---
