---
callables:
- bookmark: null
  content_type: basicfunction
  local_id: Main.Module1.Library1
- bookmark: null
  content_type: basicfunction
  local_id: CallerSub.Module1.Library1
- bookmark: null
  content_type: basicfunction
  local_id: CalleeSub.Module1.Library1
- bookmark: null
  content_type: basicfunction
  local_id: CallerTwo.Module1.Library1
- bookmark: null
  content_type: basicfunction
  local_id: CallerOtherLib.Module1.Library1
- bookmark: null
  content_type: basicfunction
  local_id: CallerShadowedCallee.Module1.Library1
- bookmark: null
  content_type: basicfunction
  local_id: ShadowedCallee.Module1.Library1
- bookmark: null
  content_type: basicfunction
  local_id: ReferToTable.Module1.Library1
- bookmark: null
  content_type: basicfunction
  local_id: ReferToView.Module1.Library1
- bookmark: null
  content_type: basicfunction
  local_id: ReferToQuery.Module1.Library1
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
obj_id: '445'
parent_link:
  content_type: library
  local_id: Library1
source: "REM  *****  BASIC  *****\n\nSub Main\n\tError \"Mijn fout\"\nEnd Sub\n\n\
  Sub CallerSub()\n\tCalleeSub()\n\tModule2.CalleeSub()\nEnd Sub\n\nSub CalleeSub()\n\
  \tprint \"Module1.CalleeSub\"\nEnd Sub\n\nsub CallerTwo()\n\tCalleeTwoSub()\nEnd\
  \ Sub\n\nSub CallerOtherLib()\n\tCalleeOtherLib()\n\tModule1.CalleeOtherLib()\n\
  End Sub\n\nSub CallerShadowedCallee()\n\tShadowedCallee()\nEnd Sub\n\nSub ShadowedCallee()\n\
  \tprint \"Library1.Module1.ShadowedCallee\"\nEnd Sub\n\nSub ReferToTable()\n\tprint\
  \ \"Plant\"\nEnd Sub\n\nSub ReferToView()\n\tprint \"view1\"\nEnd Sub\n\nSub ReferToQuery()\n\
  \tprint \"FamilyLookup\"\nEnd Sub\t\n\n"
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
  link:
    content_type: basicfunction
    local_id: Main.Module1.Library1
  obj_id: '581'
  text: Main
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
  link:
    content_type: basicfunction
    local_id: CallerSub.Module1.Library1
  obj_id: '592'
  text: CallerSub
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
  link:
    bookmark: CalleeSub
    content_type: module
    local_id: Module1.Library1
  obj_id: '596'
  text: CalleeSub
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
  link:
    bookmark: CalleeSub
    content_type: module
    local_id: Module2.Library1
  obj_id: '602'
  text: CalleeSub
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
  link:
    content_type: basicfunction
    local_id: CalleeSub.Module1.Library1
  obj_id: '611'
  text: CalleeSub
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
  link:
    content_type: basicfunction
    local_id: CallerTwo.Module1.Library1
  obj_id: '624'
  text: CallerTwo
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
  link:
    bookmark: CalleeTwoSub
    content_type: module
    local_id: Module2.Library1
  obj_id: '628'
  text: CalleeTwoSub
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
  link:
    content_type: basicfunction
    local_id: CallerOtherLib.Module1.Library1
  obj_id: '637'
  text: CallerOtherLib
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
  link:
    bookmark: CalleeOtherLib
    content_type: module
    local_id: Module1.Standard
  obj_id: '641'
  text: CalleeOtherLib
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
  link:
    bookmark: CalleeOtherLib
    content_type: module
    local_id: Module1.Standard
  obj_id: '647'
  text: CalleeOtherLib
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
  link:
    content_type: basicfunction
    local_id: CallerShadowedCallee.Module1.Library1
  obj_id: '656'
  text: CallerShadowedCallee
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
  link:
    bookmark: ShadowedCallee
    content_type: module
    local_id: Module1.Library1
  obj_id: '660'
  text: ShadowedCallee
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
  link:
    content_type: basicfunction
    local_id: ShadowedCallee.Module1.Library1
  obj_id: '669'
  text: ShadowedCallee
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
  link:
    content_type: basicfunction
    local_id: ReferToTable.Module1.Library1
  obj_id: '682'
  text: ReferToTable
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
  link:
    content_type: table
    local_id: Plant
  obj_id: '688'
  text: '"Plant"'
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
  link:
    content_type: basicfunction
    local_id: ReferToView.Module1.Library1
  obj_id: '695'
  text: ReferToView
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
  link:
    content_type: view
    local_id: view1
  obj_id: '701'
  text: '"view1"'
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
  link:
    content_type: basicfunction
    local_id: ReferToQuery.Module1.Library1
  obj_id: '708'
  text: ReferToQuery
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
  link:
    content_type: query
    local_id: FamilyLookup
  obj_id: '714'
  text: '"FamilyLookup"'
  type: 172
- index: 139
  text: '

    '
  type: 183
- index: 140
  text: End Sub
  type: 44
- index: 141
  text: "\t\n"
  type: 183
- index: 142
  text: '

    '
  type: 183
---
