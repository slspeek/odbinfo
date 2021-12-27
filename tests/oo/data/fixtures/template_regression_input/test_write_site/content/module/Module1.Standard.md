---
callables:
- content_type: basicfunction
  local_id: UsesDocument.Module1.Standard
- content_type: basicfunction
  local_id: UsesDocumentFilename.Module1.Standard
- content_type: basicfunction
  local_id: CalleeOtherLib.Module1.Standard
- content_type: basicfunction
  local_id: ShadowedCallee.Module1.Standard
- content_type: basicfunction
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
    local_id: UsesDocument.Module1.Standard
  obj_id: '351'
  text: UsesDocument
- index: 6
  text: (
- index: 7
  text: )
- index: 8
  text: "\n\t"
- index: 9
  text: print
- index: 10
  text: ' '
- cls: stringlit
  index: 11
  link:
    content_type: textdocument
    local_id: Untitled
  obj_id: '357'
  text: '"Untitled"'
- index: 12
  text: '

    '
- index: 13
  text: End Sub
- index: 14
  text: '

    '
- index: 15
  text: '

    '
- index: 16
  text: Sub
- index: 17
  text: ' '
- cls: identifier
  index: 18
  link:
    content_type: basicfunction
    local_id: UsesDocumentFilename.Module1.Standard
  obj_id: '364'
  text: UsesDocumentFilename
- index: 19
  text: (
- index: 20
  text: )
- index: 21
  text: "\n\t"
- index: 22
  text: print
- index: 23
  text: ' '
- cls: stringlit
  index: 24
  link:
    content_type: textdocument
    local_id: Untitled
  obj_id: '370'
  text: '"Untitled.odt"'
- index: 25
  text: '

    '
- index: 26
  text: End Sub
- index: 27
  text: '

    '
- index: 28
  text: '

    '
- index: 29
  text: Sub
- index: 30
  text: ' '
- cls: identifier
  index: 31
  link:
    content_type: basicfunction
    local_id: CalleeOtherLib.Module1.Standard
  obj_id: '377'
  text: CalleeOtherLib
- index: 32
  text: "\n\t"
- index: 33
  text: print
- index: 34
  text: ' '
- cls: stringlit
  index: 35
  text: '"Standard.Module1.CalleeOtherLib"'
- index: 36
  text: '

    '
- index: 37
  text: End Sub
- index: 38
  text: '

    '
- index: 39
  text: '

    '
- index: 40
  text: Sub
- index: 41
  text: ' '
- cls: identifier
  index: 42
  link:
    content_type: basicfunction
    local_id: ShadowedCallee.Module1.Standard
  obj_id: '388'
  text: ShadowedCallee
- index: 43
  text: (
- index: 44
  text: )
- index: 45
  text: "\n\t"
- index: 46
  text: print
- index: 47
  text: ' '
- cls: stringlit
  index: 48
  text: '"Standard.Module1.ShadowedCallee"'
- index: 49
  text: '

    '
- index: 50
  text: End Sub
- index: 51
  text: '

    '
- index: 52
  text: '

    '
- index: 53
  text: Function
- index: 54
  text: ' '
- cls: identifier
  index: 55
  link:
    content_type: basicfunction
    local_id: AddOne.Module1.Standard
  obj_id: '401'
  text: AddOne
- index: 56
  text: (
- cls: identifier
  index: 57
  text: arg
- index: 58
  text: )
- index: 59
  text: "\n\t"
- cls: identifier
  index: 60
  text: AddOne
- index: 61
  text: (
- index: 62
  text: )
- index: 63
  text: ' '
- index: 64
  text: '='
- index: 65
  text: ' '
- cls: identifier
  index: 66
  text: arg
- index: 67
  text: ' '
- index: 68
  text: +
- index: 69
  text: ' '
- index: 70
  text: '1'
- index: 71
  text: '

    '
- index: 72
  text: End Function
- index: 73
  text: '

    '
---
