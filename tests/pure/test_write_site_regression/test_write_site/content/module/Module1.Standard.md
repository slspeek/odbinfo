---
callables:
- bookmark: null
  content_type: basicfunction
  local_id: UsesDocument.Module1.Standard
- bookmark: null
  content_type: basicfunction
  local_id: UsesDocumentFilename.Module1.Standard
- bookmark: null
  content_type: basicfunction
  local_id: CalleeOtherLib.Module1.Standard
- bookmark: null
  content_type: basicfunction
  local_id: ShadowedCallee.Module1.Standard
- bookmark: null
  content_type: basicfunction
  local_id: AddOne.Module1.Standard
library: Standard
name: Module1
name_indexes:
- 5
- 18
- 31
- 42
- 55
obj_id: '278'
parent_link:
  content_type: library
  local_id: Standard
source: "REM  *****  BASIC  *****\n\nSub UsesDocument()\n\tprint \"Untitled\"\nEnd\
  \ Sub\n\nSub UsesDocumentFilename()\n\tprint \"Untitled.odt\"\nEnd Sub\n\nSub CalleeOtherLib\n\
  \tprint \"Standard.Module1.CalleeOtherLib\"\nEnd Sub\n\nSub ShadowedCallee()\n\t\
  print \"Standard.Module1.ShadowedCallee\"\nEnd Sub\n\nFunction AddOne(arg)\n\tAddOne()\
  \ = arg + 1\nEnd Function\n"
title: Module1.Standard
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
    local_id: UsesDocument.Module1.Standard
  obj_id: '351'
  text: UsesDocument
  type: 181
- index: 6
  text: (
  type: 157
- index: 7
  text: )
  type: 168
- index: 8
  text: "\n\t"
  type: 183
- index: 9
  text: print
  type: 100
- index: 10
  text: ' '
  type: 185
- index: 11
  link:
    content_type: textdocument
    local_id: Untitled
  obj_id: '357'
  text: '"Untitled"'
  type: 172
- index: 12
  text: '

    '
  type: 183
- index: 13
  text: End Sub
  type: 44
- index: 14
  text: '

    '
  type: 183
- index: 15
  text: '

    '
  type: 183
- index: 16
  text: Sub
  type: 125
- index: 17
  text: ' '
  type: 185
- index: 18
  link:
    content_type: basicfunction
    local_id: UsesDocumentFilename.Module1.Standard
  obj_id: '364'
  text: UsesDocumentFilename
  type: 181
- index: 19
  text: (
  type: 157
- index: 20
  text: )
  type: 168
- index: 21
  text: "\n\t"
  type: 183
- index: 22
  text: print
  type: 100
- index: 23
  text: ' '
  type: 185
- index: 24
  link:
    content_type: textdocument
    local_id: Untitled
  obj_id: '370'
  text: '"Untitled.odt"'
  type: 172
- index: 25
  text: '

    '
  type: 183
- index: 26
  text: End Sub
  type: 44
- index: 27
  text: '

    '
  type: 183
- index: 28
  text: '

    '
  type: 183
- index: 29
  text: Sub
  type: 125
- index: 30
  text: ' '
  type: 185
- index: 31
  link:
    content_type: basicfunction
    local_id: CalleeOtherLib.Module1.Standard
  obj_id: '377'
  text: CalleeOtherLib
  type: 181
- index: 32
  text: "\n\t"
  type: 183
- index: 33
  text: print
  type: 100
- index: 34
  text: ' '
  type: 185
- index: 35
  text: '"Standard.Module1.CalleeOtherLib"'
  type: 172
- index: 36
  text: '

    '
  type: 183
- index: 37
  text: End Sub
  type: 44
- index: 38
  text: '

    '
  type: 183
- index: 39
  text: '

    '
  type: 183
- index: 40
  text: Sub
  type: 125
- index: 41
  text: ' '
  type: 185
- index: 42
  link:
    content_type: basicfunction
    local_id: ShadowedCallee.Module1.Standard
  obj_id: '388'
  text: ShadowedCallee
  type: 181
- index: 43
  text: (
  type: 157
- index: 44
  text: )
  type: 168
- index: 45
  text: "\n\t"
  type: 183
- index: 46
  text: print
  type: 100
- index: 47
  text: ' '
  type: 185
- index: 48
  text: '"Standard.Module1.ShadowedCallee"'
  type: 172
- index: 49
  text: '

    '
  type: 183
- index: 50
  text: End Sub
  type: 44
- index: 51
  text: '

    '
  type: 183
- index: 52
  text: '

    '
  type: 183
- index: 53
  text: Function
  type: 57
- index: 54
  text: ' '
  type: 185
- index: 55
  link:
    content_type: basicfunction
    local_id: AddOne.Module1.Standard
  obj_id: '401'
  text: AddOne
  type: 181
- index: 56
  text: (
  type: 157
- index: 57
  text: arg
  type: 181
- index: 58
  text: )
  type: 168
- index: 59
  text: "\n\t"
  type: 183
- index: 60
  text: AddOne
  type: 181
- index: 61
  text: (
  type: 157
- index: 62
  text: )
  type: 168
- index: 63
  text: ' '
  type: 185
- index: 64
  text: '='
  type: 151
- index: 65
  text: ' '
  type: 185
- index: 66
  text: arg
  type: 181
- index: 67
  text: ' '
  type: 185
- index: 68
  text: +
  type: 164
- index: 69
  text: ' '
  type: 185
- index: 70
  text: '1'
  type: 175
- index: 71
  text: '

    '
  type: 183
- index: 72
  text: End Function
  type: 40
- index: 73
  text: '

    '
  type: 183
---
