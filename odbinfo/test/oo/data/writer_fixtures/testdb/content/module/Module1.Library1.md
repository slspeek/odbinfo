---
!!python/object:odbinfo.pure.datatype.exec.Module
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
  text: REM  *****  BASIC  *****
  type: 184
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 1
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 2
  text: '

    '
  type: 183
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Main.Module1.Library1
    content_type: basicfunction
  obj_id: '434'
  text: Main
  title: token5.Module1.Library1
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 9
  text: '"Mijn fout"'
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 10
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 11
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 12
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 13
  text: '

    '
  type: 183
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: CallerSub.Module1.Library1
    content_type: basicfunction
  obj_id: '445'
  text: CallerSub
  title: token16.Module1.Library1
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 20
  link: &id010 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeSub
    local_id: Module1.Library1
    content_type: module
  obj_id: '449'
  text: CalleeSub
  title: token20.Module1.Library1
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 24
  text: Module2
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 25
  text: .
  type: 150
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 26
  link: &id011 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeSub
    local_id: Module2.Library1
    content_type: module
  obj_id: '455'
  text: CalleeSub
  title: token26.Module1.Library1
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 30
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 31
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 32
  text: '

    '
  type: 183
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: CalleeSub.Module1.Library1
    content_type: basicfunction
  obj_id: '464'
  text: CalleeSub
  title: token35.Module1.Library1
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 41
  text: '"Module1.CalleeSub"'
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 42
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 43
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 44
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 45
  text: '

    '
  type: 183
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: CallerTwo.Module1.Library1
    content_type: basicfunction
  obj_id: '477'
  text: CallerTwo
  title: token48.Module1.Library1
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 52
  link: &id012 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeTwoSub
    local_id: Module2.Library1
    content_type: module
  obj_id: '481'
  text: CalleeTwoSub
  title: token52.Module1.Library1
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 56
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 57
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 58
  text: '

    '
  type: 183
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: CallerOtherLib.Module1.Library1
    content_type: basicfunction
  obj_id: '490'
  text: CallerOtherLib
  title: token61.Module1.Library1
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 65
  link: &id013 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeOtherLib
    local_id: Module1.Standard
    content_type: module
  obj_id: '494'
  text: CalleeOtherLib
  title: token65.Module1.Library1
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 69
  text: Module1
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 70
  text: .
  type: 150
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 71
  link: &id014 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeOtherLib
    local_id: Module1.Standard
    content_type: module
  obj_id: '500'
  text: CalleeOtherLib
  title: token71.Module1.Library1
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 75
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 76
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 77
  text: '

    '
  type: 183
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: CallerShadowedCallee.Module1.Library1
    content_type: basicfunction
  obj_id: '509'
  text: CallerShadowedCallee
  title: token80.Module1.Library1
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 84
  link: &id015 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: ShadowedCallee
    local_id: Module1.Library1
    content_type: module
  obj_id: '513'
  text: ShadowedCallee
  title: token84.Module1.Library1
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 88
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 89
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 90
  text: '

    '
  type: 183
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: ShadowedCallee.Module1.Library1
    content_type: basicfunction
  obj_id: '522'
  text: ShadowedCallee
  title: token93.Module1.Library1
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 99
  text: '"Library1.Module1.ShadowedCallee"'
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 100
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 101
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 102
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 103
  text: '

    '
  type: 183
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: ReferToTable.Module1.Library1
    content_type: basicfunction
  obj_id: '535'
  text: ReferToTable
  title: token106.Module1.Library1
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 112
  link: *id007
  obj_id: '541'
  text: '"Plant"'
  title: token112.Module1.Library1
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 113
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 114
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 115
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 116
  text: '

    '
  type: 183
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: ReferToView.Module1.Library1
    content_type: basicfunction
  obj_id: '548'
  text: ReferToView
  title: token119.Module1.Library1
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 125
  link: *id008
  obj_id: '554'
  text: '"view1"'
  title: token125.Module1.Library1
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 126
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 127
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 128
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 129
  text: '

    '
  type: 183
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: ReferToQuery.Module1.Library1
    content_type: basicfunction
  obj_id: '561'
  text: ReferToQuery
  title: token132.Module1.Library1
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 138
  link: *id009
  obj_id: '567'
  text: '"FamilyLookup"'
  title: token138.Module1.Library1
  type: 172
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
