---
!!python/object:odbinfo.pure.datatype.exec.Module
callables:
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Library1
  module: Module1
  name: Main
  name_token_index: 5
  obj_id: '383'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module1.Library1
  title: Main.Module1.Library1
  tokens: []
  used_by:
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: '144'
    content_type: form
    local_id: PlantListbox
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: '147'
    content_type: form
    local_id: PlantListbox
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: '148'
    content_type: form
    local_id: PlantListbox
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: '178'
    content_type: form
    local_id: PlantListboxDirectSQL
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: '181'
    content_type: form
    local_id: PlantListboxDirectSQL
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: '182'
    content_type: form
    local_id: PlantListboxDirectSQL
  uses: []
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Library1
  module: Module1
  name: CallerSub
  name_token_index: 16
  obj_id: '393'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module1.Library1
  title: CallerSub.Module1.Library1
  tokens: []
  used_by: []
  uses:
  - &id004 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: CalleeSub.Module1.Library1
  - &id005 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: CalleeSub.Module2.Library1
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Library1
  module: Module1
  name: CalleeSub
  name_token_index: 35
  obj_id: '411'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module1.Library1
  title: CalleeSub.Module1.Library1
  tokens: []
  used_by:
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: '400'
    content_type: basicfunction
    local_id: CallerSub.Module1.Library1
  uses: []
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Library1
  module: Module1
  name: CallerTwo
  name_token_index: 48
  obj_id: '423'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module1.Library1
  title: CallerTwo.Module1.Library1
  tokens: []
  used_by: []
  uses:
  - &id006 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: CalleeTwoSub.Module2.Library1
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Library1
  module: Module1
  name: CallerOtherLib
  name_token_index: 61
  obj_id: '435'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module1.Library1
  title: CallerOtherLib.Module1.Library1
  tokens: []
  used_by: []
  uses:
  - &id007 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: CalleeOtherLib.Module1.Standard
  - &id008 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: CalleeOtherLib.Module1.Standard
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Library1
  module: Module1
  name: CallerShadowedCallee
  name_token_index: 80
  obj_id: '453'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module1.Library1
  title: CallerShadowedCallee.Module1.Library1
  tokens: []
  used_by: []
  uses:
  - &id009 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: ShadowedCallee.Module1.Library1
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Library1
  module: Module1
  name: ShadowedCallee
  name_token_index: 93
  obj_id: '465'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module1.Library1
  title: ShadowedCallee.Module1.Library1
  tokens: []
  used_by:
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: '460'
    content_type: basicfunction
    local_id: CallerShadowedCallee.Module1.Library1
  uses: []
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Library1
  module: Module1
  name: ReferToTable
  name_token_index: 106
  obj_id: '477'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module1.Library1
  title: ReferToTable.Module1.Library1
  tokens: []
  used_by: []
  uses:
  - &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: table
    local_id: Plant
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Library1
  module: Module1
  name: ReferToView
  name_token_index: 119
  obj_id: '489'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module1.Library1
  title: ReferToView.Module1.Library1
  tokens: []
  used_by: []
  uses:
  - &id002 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: view
    local_id: view1
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Library1
  module: Module1
  name: ReferToQuery
  name_token_index: 132
  obj_id: '501'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module1.Library1
  title: ReferToQuery.Module1.Library1
  tokens: []
  used_by: []
  uses:
  - &id003 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: query
    local_id: FamilyLookup
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
obj_id: '382'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: library
  local_id: Library1
title: Module1.Library1
tokens:
- index: 0
  text: REM  *****  BASIC  *****
  type: 184
- index: 1
  text: '

    '
  type: 183
- index: 2
  text: '

    '
  type: 183
- index: 3
  text: Sub
  type: 125
- index: 4
  text: ' '
  type: 185
- index: 5
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: Main.Module1.Library1
  obj_id: '518'
  text: Main
  title: token5.Module1.Library1
  type: 181
- index: 6
  text: "\n\t"
  type: 183
- index: 7
  text: Error
  type: 49
- index: 8
  text: ' '
  type: 185
- index: 9
  text: '"Mijn fout"'
  type: 172
- index: 10
  text: '

    '
  type: 183
- index: 11
  text: End Sub
  type: 44
- index: 12
  text: '

    '
  type: 183
- index: 13
  text: '

    '
  type: 183
- index: 14
  text: Sub
  type: 125
- index: 15
  text: ' '
  type: 185
- index: 16
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: CallerSub.Module1.Library1
  obj_id: '529'
  text: CallerSub
  title: token16.Module1.Library1
  type: 181
- index: 17
  text: (
  type: 157
- index: 18
  text: )
  type: 168
- index: 19
  text: "\n\t"
  type: 183
- index: 20
  link: &id010 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeSub
    content_type: module
    local_id: Module1.Library1
  obj_id: '533'
  text: CalleeSub
  title: token20.Module1.Library1
  type: 181
- index: 21
  text: (
  type: 157
- index: 22
  text: )
  type: 168
- index: 23
  text: "\n\t"
  type: 183
- index: 24
  text: Module2
  type: 181
- index: 25
  text: .
  type: 150
- index: 26
  link: &id011 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeSub
    content_type: module
    local_id: Module2.Library1
  obj_id: '539'
  text: CalleeSub
  title: token26.Module1.Library1
  type: 181
- index: 27
  text: (
  type: 157
- index: 28
  text: )
  type: 168
- index: 29
  text: '

    '
  type: 183
- index: 30
  text: End Sub
  type: 44
- index: 31
  text: '

    '
  type: 183
- index: 32
  text: '

    '
  type: 183
- index: 33
  text: Sub
  type: 125
- index: 34
  text: ' '
  type: 185
- index: 35
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: CalleeSub.Module1.Library1
  obj_id: '548'
  text: CalleeSub
  title: token35.Module1.Library1
  type: 181
- index: 36
  text: (
  type: 157
- index: 37
  text: )
  type: 168
- index: 38
  text: "\n\t"
  type: 183
- index: 39
  text: print
  type: 100
- index: 40
  text: ' '
  type: 185
- index: 41
  text: '"Module1.CalleeSub"'
  type: 172
- index: 42
  text: '

    '
  type: 183
- index: 43
  text: End Sub
  type: 44
- index: 44
  text: '

    '
  type: 183
- index: 45
  text: '

    '
  type: 183
- index: 46
  text: sub
  type: 125
- index: 47
  text: ' '
  type: 185
- index: 48
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: CallerTwo.Module1.Library1
  obj_id: '561'
  text: CallerTwo
  title: token48.Module1.Library1
  type: 181
- index: 49
  text: (
  type: 157
- index: 50
  text: )
  type: 168
- index: 51
  text: "\n\t"
  type: 183
- index: 52
  link: &id012 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeTwoSub
    content_type: module
    local_id: Module2.Library1
  obj_id: '565'
  text: CalleeTwoSub
  title: token52.Module1.Library1
  type: 181
- index: 53
  text: (
  type: 157
- index: 54
  text: )
  type: 168
- index: 55
  text: '

    '
  type: 183
- index: 56
  text: End Sub
  type: 44
- index: 57
  text: '

    '
  type: 183
- index: 58
  text: '

    '
  type: 183
- index: 59
  text: Sub
  type: 125
- index: 60
  text: ' '
  type: 185
- index: 61
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: CallerOtherLib.Module1.Library1
  obj_id: '574'
  text: CallerOtherLib
  title: token61.Module1.Library1
  type: 181
- index: 62
  text: (
  type: 157
- index: 63
  text: )
  type: 168
- index: 64
  text: "\n\t"
  type: 183
- index: 65
  link: &id013 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeOtherLib
    content_type: module
    local_id: Module1.Standard
  obj_id: '578'
  text: CalleeOtherLib
  title: token65.Module1.Library1
  type: 181
- index: 66
  text: (
  type: 157
- index: 67
  text: )
  type: 168
- index: 68
  text: "\n\t"
  type: 183
- index: 69
  text: Module1
  type: 181
- index: 70
  text: .
  type: 150
- index: 71
  link: &id014 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: CalleeOtherLib
    content_type: module
    local_id: Module1.Standard
  obj_id: '584'
  text: CalleeOtherLib
  title: token71.Module1.Library1
  type: 181
- index: 72
  text: (
  type: 157
- index: 73
  text: )
  type: 168
- index: 74
  text: '

    '
  type: 183
- index: 75
  text: End Sub
  type: 44
- index: 76
  text: '

    '
  type: 183
- index: 77
  text: '

    '
  type: 183
- index: 78
  text: Sub
  type: 125
- index: 79
  text: ' '
  type: 185
- index: 80
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: CallerShadowedCallee.Module1.Library1
  obj_id: '593'
  text: CallerShadowedCallee
  title: token80.Module1.Library1
  type: 181
- index: 81
  text: (
  type: 157
- index: 82
  text: )
  type: 168
- index: 83
  text: "\n\t"
  type: 183
- index: 84
  link: &id015 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: ShadowedCallee
    content_type: module
    local_id: Module1.Library1
  obj_id: '597'
  text: ShadowedCallee
  title: token84.Module1.Library1
  type: 181
- index: 85
  text: (
  type: 157
- index: 86
  text: )
  type: 168
- index: 87
  text: '

    '
  type: 183
- index: 88
  text: End Sub
  type: 44
- index: 89
  text: '

    '
  type: 183
- index: 90
  text: '

    '
  type: 183
- index: 91
  text: Sub
  type: 125
- index: 92
  text: ' '
  type: 185
- index: 93
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: ShadowedCallee.Module1.Library1
  obj_id: '606'
  text: ShadowedCallee
  title: token93.Module1.Library1
  type: 181
- index: 94
  text: (
  type: 157
- index: 95
  text: )
  type: 168
- index: 96
  text: "\n\t"
  type: 183
- index: 97
  text: print
  type: 100
- index: 98
  text: ' '
  type: 185
- index: 99
  text: '"Library1.Module1.ShadowedCallee"'
  type: 172
- index: 100
  text: '

    '
  type: 183
- index: 101
  text: End Sub
  type: 44
- index: 102
  text: '

    '
  type: 183
- index: 103
  text: '

    '
  type: 183
- index: 104
  text: Sub
  type: 125
- index: 105
  text: ' '
  type: 185
- index: 106
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: ReferToTable.Module1.Library1
  obj_id: '619'
  text: ReferToTable
  title: token106.Module1.Library1
  type: 181
- index: 107
  text: (
  type: 157
- index: 108
  text: )
  type: 168
- index: 109
  text: "\n\t"
  type: 183
- index: 110
  text: print
  type: 100
- index: 111
  text: ' '
  type: 185
- index: 112
  link: *id001
  obj_id: '625'
  text: '"Plant"'
  title: token112.Module1.Library1
  type: 172
- index: 113
  text: '

    '
  type: 183
- index: 114
  text: End Sub
  type: 44
- index: 115
  text: '

    '
  type: 183
- index: 116
  text: '

    '
  type: 183
- index: 117
  text: Sub
  type: 125
- index: 118
  text: ' '
  type: 185
- index: 119
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: ReferToView.Module1.Library1
  obj_id: '632'
  text: ReferToView
  title: token119.Module1.Library1
  type: 181
- index: 120
  text: (
  type: 157
- index: 121
  text: )
  type: 168
- index: 122
  text: "\n\t"
  type: 183
- index: 123
  text: print
  type: 100
- index: 124
  text: ' '
  type: 185
- index: 125
  link: *id002
  obj_id: '638'
  text: '"view1"'
  title: token125.Module1.Library1
  type: 172
- index: 126
  text: '

    '
  type: 183
- index: 127
  text: End Sub
  type: 44
- index: 128
  text: '

    '
  type: 183
- index: 129
  text: '

    '
  type: 183
- index: 130
  text: Sub
  type: 125
- index: 131
  text: ' '
  type: 185
- index: 132
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: ReferToQuery.Module1.Library1
  obj_id: '645'
  text: ReferToQuery
  title: token132.Module1.Library1
  type: 181
- index: 133
  text: (
  type: 157
- index: 134
  text: )
  type: 168
- index: 135
  text: "\n\t"
  type: 183
- index: 136
  text: print
  type: 100
- index: 137
  text: ' '
  type: 185
- index: 138
  link: *id003
  obj_id: '651'
  text: '"FamilyLookup"'
  title: token138.Module1.Library1
  type: 172
- index: 139
  text: '

    '
  type: 183
- index: 140
  text: End Sub
  type: 44
used_by: []
uses:
- *id004
- *id005
- *id006
- *id007
- *id008
- *id009
- *id001
- *id002
- *id003
- *id010
- *id011
- *id012
- *id013
- *id014
- *id015
- *id001
- *id002
- *id003
---
