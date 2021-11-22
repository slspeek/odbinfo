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
  link: null
  text: REM  *****  BASIC  *****
  type: 184
- index: 1
  link: null
  text: '

    '
  type: 183
- index: 2
  link: null
  text: '

    '
  type: 183
- index: 3
  link: null
  text: Sub
  type: 125
- index: 4
  link: null
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
  link: null
  text: (
  type: 157
- index: 7
  link: null
  text: )
  type: 168
- index: 8
  link: null
  text: "\n\t"
  type: 183
- index: 9
  link: null
  text: print
  type: 100
- index: 10
  link: null
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
  link: null
  text: '

    '
  type: 183
- index: 13
  link: null
  text: End Sub
  type: 44
- index: 14
  link: null
  text: '

    '
  type: 183
- index: 15
  link: null
  text: '

    '
  type: 183
- index: 16
  link: null
  text: Sub
  type: 125
- index: 17
  link: null
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
  link: null
  text: (
  type: 157
- index: 20
  link: null
  text: )
  type: 168
- index: 21
  link: null
  text: "\n\t"
  type: 183
- index: 22
  link: null
  text: print
  type: 100
- index: 23
  link: null
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
  link: null
  text: '

    '
  type: 183
- index: 26
  link: null
  text: End Sub
  type: 44
- index: 27
  link: null
  text: '

    '
  type: 183
- index: 28
  link: null
  text: '

    '
  type: 183
- index: 29
  link: null
  text: Sub
  type: 125
- index: 30
  link: null
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
  link: null
  text: "\n\t"
  type: 183
- index: 33
  link: null
  text: print
  type: 100
- index: 34
  link: null
  text: ' '
  type: 185
- index: 35
  link: null
  text: '"Standard.Module1.CalleeOtherLib"'
  type: 172
- index: 36
  link: null
  text: '

    '
  type: 183
- index: 37
  link: null
  text: End Sub
  type: 44
- index: 38
  link: null
  text: '

    '
  type: 183
- index: 39
  link: null
  text: '

    '
  type: 183
- index: 40
  link: null
  text: Sub
  type: 125
- index: 41
  link: null
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
  link: null
  text: (
  type: 157
- index: 44
  link: null
  text: )
  type: 168
- index: 45
  link: null
  text: "\n\t"
  type: 183
- index: 46
  link: null
  text: print
  type: 100
- index: 47
  link: null
  text: ' '
  type: 185
- index: 48
  link: null
  text: '"Standard.Module1.ShadowedCallee"'
  type: 172
- index: 49
  link: null
  text: '

    '
  type: 183
- index: 50
  link: null
  text: End Sub
  type: 44
- index: 51
  link: null
  text: '

    '
  type: 183
- index: 52
  link: null
  text: '

    '
  type: 183
- index: 53
  link: null
  text: Function
  type: 57
- index: 54
  link: null
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
  link: null
  text: (
  type: 157
- index: 57
  link: null
  text: arg
  type: 181
- index: 58
  link: null
  text: )
  type: 168
- index: 59
  link: null
  text: "\n\t"
  type: 183
- index: 60
  link: null
  text: AddOne
  type: 181
- index: 61
  link: null
  text: (
  type: 157
- index: 62
  link: null
  text: )
  type: 168
- index: 63
  link: null
  text: ' '
  type: 185
- index: 64
  link: null
  text: '='
  type: 151
- index: 65
  link: null
  text: ' '
  type: 185
- index: 66
  link: null
  text: arg
  type: 181
- index: 67
  link: null
  text: ' '
  type: 185
- index: 68
  link: null
  text: +
  type: 164
- index: 69
  link: null
  text: ' '
  type: 185
- index: 70
  link: null
  text: '1'
  type: 175
- index: 71
  link: null
  text: '

    '
  type: 183
- index: 72
  link: null
  text: End Function
  type: 40
- index: 73
  link: null
  text: '

    '
  type: 183
---
