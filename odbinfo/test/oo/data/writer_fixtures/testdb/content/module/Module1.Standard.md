---
!!python/object:odbinfo.pure.datatype.exec.Module
callables:
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Standard
  module: Module1
  name: UsesDocument
  name_token_index: 5
  obj_id: '218'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module1.Standard
  title: UsesDocument.Module1.Standard
  tokens: []
  used_by: []
  uses:
  - &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: textdocument
    local_id: Untitled
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Standard
  module: Module1
  name: UsesDocumentFilename
  name_token_index: 18
  obj_id: '230'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module1.Standard
  title: UsesDocumentFilename.Module1.Standard
  tokens: []
  used_by: []
  uses:
  - &id002 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: textdocument
    local_id: Untitled
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Standard
  module: Module1
  name: CalleeOtherLib
  name_token_index: 31
  obj_id: '242'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module1.Standard
  title: CalleeOtherLib.Module1.Standard
  tokens: []
  used_by:
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: '442'
    content_type: basicfunction
    local_id: CallerOtherLib.Module1.Library1
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: '448'
    content_type: basicfunction
    local_id: CallerOtherLib.Module1.Library1
  uses: []
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Standard
  module: Module1
  name: ShadowedCallee
  name_token_index: 42
  obj_id: '252'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module1.Standard
  title: ShadowedCallee.Module1.Standard
  tokens: []
  used_by: []
  uses: []
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Standard
  module: Module1
  name: AddOne
  name_token_index: 55
  obj_id: '264'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module1.Standard
  title: AddOne.Module1.Standard
  tokens: []
  used_by: []
  uses: []
library: Standard
name: Module1
name_indexes:
- 5
- 18
- 31
- 42
- 55
obj_id: '217'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: library
  local_id: Standard
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: UsesDocument.Module1.Standard
  obj_id: '290'
  text: UsesDocument
  title: token5.Module1.Standard
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
  link: *id001
  obj_id: '296'
  text: '"Untitled"'
  title: token11.Module1.Standard
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: UsesDocumentFilename.Module1.Standard
  obj_id: '303'
  text: UsesDocumentFilename
  title: token18.Module1.Standard
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
  link: *id002
  obj_id: '309'
  text: '"Untitled.odt"'
  title: token24.Module1.Standard
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: CalleeOtherLib.Module1.Standard
  obj_id: '316'
  text: CalleeOtherLib
  title: token31.Module1.Standard
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: ShadowedCallee.Module1.Standard
  obj_id: '327'
  text: ShadowedCallee
  title: token42.Module1.Standard
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
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: AddOne.Module1.Standard
  obj_id: '340'
  text: AddOne
  title: token55.Module1.Standard
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
used_by: []
uses:
- *id001
- *id002
- *id001
- *id002
---
