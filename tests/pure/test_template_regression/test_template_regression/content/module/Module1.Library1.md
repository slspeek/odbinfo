---
callables:
- content_type: basicfunction
  local_id: Main.Module1.Library1
- content_type: basicfunction
  local_id: CallerSub.Module1.Library1
- content_type: basicfunction
  local_id: CalleeSub.Module1.Library1
- content_type: basicfunction
  local_id: CallerTwo.Module1.Library1
- content_type: basicfunction
  local_id: CallerOtherLib.Module1.Library1
- content_type: basicfunction
  local_id: CallerShadowedCallee.Module1.Library1
- content_type: basicfunction
  local_id: ShadowedCallee.Module1.Library1
- content_type: basicfunction
  local_id: ReferToTable.Module1.Library1
- content_type: basicfunction
  local_id: ReferToView.Module1.Library1
- content_type: basicfunction
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
- cls: comment
  index: 0
  text: REM  *****  BASIC  *****
- index: 1
  text: '

    '
- index: 2
  text: '

    '
- index: 3
  text: Sub
- index: 4
  text: ' '
- cls: identifier
  index: 5
  link:
    content_type: basicfunction
    local_id: Main.Module1.Library1
  obj_id: '581'
  text: Main
- index: 6
  text: "\n\t"
- index: 7
  text: Error
- index: 8
  text: ' '
- cls: stringlit
  index: 9
  text: '"Mijn fout"'
- index: 10
  text: '

    '
- index: 11
  text: End Sub
- index: 12
  text: '

    '
- index: 13
  text: '

    '
- index: 14
  text: Sub
- index: 15
  text: ' '
- cls: identifier
  index: 16
  link:
    content_type: basicfunction
    local_id: CallerSub.Module1.Library1
  obj_id: '592'
  text: CallerSub
- index: 17
  text: (
- index: 18
  text: )
- index: 19
  text: "\n\t"
- cls: identifier
  index: 20
  link:
    bookmark: CalleeSub
    content_type: module
    local_id: Module1.Library1
  obj_id: '596'
  text: CalleeSub
- index: 21
  text: (
- index: 22
  text: )
- index: 23
  text: "\n\t"
- cls: identifier
  index: 24
  text: Module2
- index: 25
  text: .
- cls: identifier
  index: 26
  link:
    bookmark: CalleeSub
    content_type: module
    local_id: Module2.Library1
  obj_id: '602'
  text: CalleeSub
- index: 27
  text: (
- index: 28
  text: )
- index: 29
  text: '

    '
- index: 30
  text: End Sub
- index: 31
  text: '

    '
- index: 32
  text: '

    '
- index: 33
  text: Sub
- index: 34
  text: ' '
- cls: identifier
  index: 35
  link:
    content_type: basicfunction
    local_id: CalleeSub.Module1.Library1
  obj_id: '611'
  text: CalleeSub
- index: 36
  text: (
- index: 37
  text: )
- index: 38
  text: "\n\t"
- index: 39
  text: print
- index: 40
  text: ' '
- cls: stringlit
  index: 41
  text: '"Module1.CalleeSub"'
- index: 42
  text: '

    '
- index: 43
  text: End Sub
- index: 44
  text: '

    '
- index: 45
  text: '

    '
- index: 46
  text: sub
- index: 47
  text: ' '
- cls: identifier
  index: 48
  link:
    content_type: basicfunction
    local_id: CallerTwo.Module1.Library1
  obj_id: '624'
  text: CallerTwo
- index: 49
  text: (
- index: 50
  text: )
- index: 51
  text: "\n\t"
- cls: identifier
  index: 52
  link:
    bookmark: CalleeTwoSub
    content_type: module
    local_id: Module2.Library1
  obj_id: '628'
  text: CalleeTwoSub
- index: 53
  text: (
- index: 54
  text: )
- index: 55
  text: '

    '
- index: 56
  text: End Sub
- index: 57
  text: '

    '
- index: 58
  text: '

    '
- index: 59
  text: Sub
- index: 60
  text: ' '
- cls: identifier
  index: 61
  link:
    content_type: basicfunction
    local_id: CallerOtherLib.Module1.Library1
  obj_id: '637'
  text: CallerOtherLib
- index: 62
  text: (
- index: 63
  text: )
- index: 64
  text: "\n\t"
- cls: identifier
  index: 65
  link:
    bookmark: CalleeOtherLib
    content_type: module
    local_id: Module1.Standard
  obj_id: '641'
  text: CalleeOtherLib
- index: 66
  text: (
- index: 67
  text: )
- index: 68
  text: "\n\t"
- cls: identifier
  index: 69
  text: Module1
- index: 70
  text: .
- cls: identifier
  index: 71
  link:
    bookmark: CalleeOtherLib
    content_type: module
    local_id: Module1.Standard
  obj_id: '647'
  text: CalleeOtherLib
- index: 72
  text: (
- index: 73
  text: )
- index: 74
  text: '

    '
- index: 75
  text: End Sub
- index: 76
  text: '

    '
- index: 77
  text: '

    '
- index: 78
  text: Sub
- index: 79
  text: ' '
- cls: identifier
  index: 80
  link:
    content_type: basicfunction
    local_id: CallerShadowedCallee.Module1.Library1
  obj_id: '656'
  text: CallerShadowedCallee
- index: 81
  text: (
- index: 82
  text: )
- index: 83
  text: "\n\t"
- cls: identifier
  index: 84
  link:
    bookmark: ShadowedCallee
    content_type: module
    local_id: Module1.Library1
  obj_id: '660'
  text: ShadowedCallee
- index: 85
  text: (
- index: 86
  text: )
- index: 87
  text: '

    '
- index: 88
  text: End Sub
- index: 89
  text: '

    '
- index: 90
  text: '

    '
- index: 91
  text: Sub
- index: 92
  text: ' '
- cls: identifier
  index: 93
  link:
    content_type: basicfunction
    local_id: ShadowedCallee.Module1.Library1
  obj_id: '669'
  text: ShadowedCallee
- index: 94
  text: (
- index: 95
  text: )
- index: 96
  text: "\n\t"
- index: 97
  text: print
- index: 98
  text: ' '
- cls: stringlit
  index: 99
  text: '"Library1.Module1.ShadowedCallee"'
- index: 100
  text: '

    '
- index: 101
  text: End Sub
- index: 102
  text: '

    '
- index: 103
  text: '

    '
- index: 104
  text: Sub
- index: 105
  text: ' '
- cls: identifier
  index: 106
  link:
    content_type: basicfunction
    local_id: ReferToTable.Module1.Library1
  obj_id: '682'
  text: ReferToTable
- index: 107
  text: (
- index: 108
  text: )
- index: 109
  text: "\n\t"
- index: 110
  text: print
- index: 111
  text: ' '
- cls: stringlit
  index: 112
  link:
    content_type: table
    local_id: Plant
  obj_id: '688'
  text: '"Plant"'
- index: 113
  text: '

    '
- index: 114
  text: End Sub
- index: 115
  text: '

    '
- index: 116
  text: '

    '
- index: 117
  text: Sub
- index: 118
  text: ' '
- cls: identifier
  index: 119
  link:
    content_type: basicfunction
    local_id: ReferToView.Module1.Library1
  obj_id: '695'
  text: ReferToView
- index: 120
  text: (
- index: 121
  text: )
- index: 122
  text: "\n\t"
- index: 123
  text: print
- index: 124
  text: ' '
- cls: stringlit
  index: 125
  link:
    content_type: view
    local_id: view1
  obj_id: '701'
  text: '"view1"'
- index: 126
  text: '

    '
- index: 127
  text: End Sub
- index: 128
  text: '

    '
- index: 129
  text: '

    '
- index: 130
  text: Sub
- index: 131
  text: ' '
- cls: identifier
  index: 132
  link:
    content_type: basicfunction
    local_id: ReferToQuery.Module1.Library1
  obj_id: '708'
  text: ReferToQuery
- index: 133
  text: (
- index: 134
  text: )
- index: 135
  text: "\n\t"
- index: 136
  text: print
- index: 137
  text: ' '
- cls: stringlit
  index: 138
  link:
    content_type: query
    local_id: FamilyLookup
  obj_id: '714'
  text: '"FamilyLookup"'
- index: 139
  text: '

    '
- index: 140
  text: End Sub
- index: 141
  text: "\t\n"
- index: 142
  text: '

    '
---
