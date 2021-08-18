---
!!python/object:odbinfo.pure.datatype.exec.Module
callables:
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens: []
  calls: []
  library: Standard
  module: Module1
  name: UsesDocument
  name_token_index: 5
  obj_id: '177'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Module1.Standard
    content_type: module
  strings:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 11
    link: &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Untitled
      content_type: textdocument
    obj_id: '186'
    text: '"Untitled"'
    title: token11.UsesDocument.Module1.Standard
    type: 172
  title: UsesDocument.Module1.Standard
  tokens: []
  used_by: []
  uses:
  - *id001
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens: []
  calls: []
  library: Standard
  module: Module1
  name: UsesDocumentFilename
  name_token_index: 18
  obj_id: '189'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Module1.Standard
    content_type: module
  strings:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 24
    link: &id002 !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Untitled
      content_type: textdocument
    obj_id: '198'
    text: '"Untitled.odt"'
    title: token24.UsesDocumentFilename.Module1.Standard
    type: 172
  title: UsesDocumentFilename.Module1.Standard
  tokens: []
  used_by: []
  uses:
  - *id002
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens: []
  calls: []
  library: Standard
  module: Module1
  name: CalleeOtherLib
  name_token_index: 31
  obj_id: '201'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Module1.Standard
    content_type: module
  strings:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 35
    text: '"Standard.Module1.CalleeOtherLib"'
    type: 172
  title: CalleeOtherLib.Module1.Standard
  tokens: []
  used_by:
  - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
    bookmark: null
    local_id: CallerOtherLib.Module1.Library1
    location_id: '358'
    content_type: basicfunction
  - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
    bookmark: null
    local_id: CallerOtherLib.Module1.Library1
    location_id: '364'
    content_type: basicfunction
  uses: []
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens: []
  calls: []
  library: Standard
  module: Module1
  name: ShadowedCallee
  name_token_index: 42
  obj_id: '211'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Module1.Standard
    content_type: module
  strings:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 48
    text: '"Standard.Module1.ShadowedCallee"'
    type: 172
  title: ShadowedCallee.Module1.Standard
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
obj_id: '176'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: Standard
  content_type: library
source: "REM  *****  BASIC  *****\n\nSub UsesDocument()\n\tprint \"Untitled\"\nEnd\
  \ Sub\n\nSub UsesDocumentFilename()\n\tprint \"Untitled.odt\"\nEnd Sub\n\nSub CalleeOtherLib\n\
  \tprint \"Standard.Module1.CalleeOtherLib\"\nEnd Sub\n\nSub ShadowedCallee()\n\t\
  print \"Standard.Module1.ShadowedCallee\"\nEnd Sub"
title: Module1.Standard
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
    local_id: UsesDocument.Module1.Standard
    content_type: basicfunction
  obj_id: '228'
  text: UsesDocument
  title: token5.Module1.Standard
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 6
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 7
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 8
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 9
  text: print
  type: 100
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 10
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 11
  link: *id001
  obj_id: '234'
  text: '"Untitled"'
  title: token11.Module1.Standard
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 12
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 13
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 14
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 15
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 16
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 17
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 18
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: UsesDocumentFilename.Module1.Standard
    content_type: basicfunction
  obj_id: '241'
  text: UsesDocumentFilename
  title: token18.Module1.Standard
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 19
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 20
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 21
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 22
  text: print
  type: 100
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 23
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 24
  link: *id002
  obj_id: '247'
  text: '"Untitled.odt"'
  title: token24.Module1.Standard
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 25
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 26
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 27
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 28
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 29
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 30
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 31
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: CalleeOtherLib.Module1.Standard
    content_type: basicfunction
  obj_id: '254'
  text: CalleeOtherLib
  title: token31.Module1.Standard
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 32
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 33
  text: print
  type: 100
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 34
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 35
  text: '"Standard.Module1.CalleeOtherLib"'
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 36
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 37
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 38
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 39
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 40
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 41
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 42
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: ShadowedCallee.Module1.Standard
    content_type: basicfunction
  obj_id: '265'
  text: ShadowedCallee
  title: token42.Module1.Standard
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 43
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 44
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 45
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 46
  text: print
  type: 100
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 47
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 48
  text: '"Standard.Module1.ShadowedCallee"'
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 49
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 50
  text: End Sub
  type: 44
used_by: []
uses:
- *id001
- *id002
- *id001
- *id002
---
