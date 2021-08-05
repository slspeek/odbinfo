---
!!python/object:odbinfo.pure.datatype.exec.Library
modules:
- !!python/object:odbinfo.pure.datatype.exec.Module
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
      object_type: module
    strings:
    - &id001 !!python/object:odbinfo.pure.datatype.base.Token
      index: 11
      link: &id005 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        local_id: Untitled
        object_type: textdocument
      obj_id: '186'
      text: '"Untitled"'
      title: token11.UsesDocument.Module1.Standard
      type: 172
    title: UsesDocument.Module1.Standard
    tokens:
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
      text: UsesDocument
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
    - *id001
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 12
      text: '

        '
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 13
      text: End Sub
      type: 44
    used_by: []
    uses:
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Untitled
      object_type: textdocument
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
      object_type: module
    strings:
    - &id002 !!python/object:odbinfo.pure.datatype.base.Token
      index: 24
      link: &id006 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        local_id: Untitled
        object_type: textdocument
      obj_id: '198'
      text: '"Untitled.odt"'
      title: token24.UsesDocumentFilename.Module1.Standard
      type: 172
    title: UsesDocumentFilename.Module1.Standard
    tokens:
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
      text: UsesDocumentFilename
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
    - *id002
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 25
      text: '

        '
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 26
      text: End Sub
      type: 44
    used_by: []
    uses:
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Untitled
      object_type: textdocument
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
      object_type: module
    strings:
    - &id003 !!python/object:odbinfo.pure.datatype.base.Token
      index: 35
      text: '"Standard.Module1.CalleeOtherLib"'
      type: 172
    title: CalleeOtherLib.Module1.Standard
    tokens:
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
      text: CalleeOtherLib
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
    - *id003
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 36
      text: '

        '
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 37
      text: End Sub
      type: 44
    used_by:
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      bookmark: null
      local_id: CallerOtherLib.Module1.Library1
      location_id: '358'
      object_type: basicfunction
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      bookmark: null
      local_id: CallerOtherLib.Module1.Library1
      location_id: '364'
      object_type: basicfunction
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
      object_type: module
    strings:
    - &id004 !!python/object:odbinfo.pure.datatype.base.Token
      index: 48
      text: '"Standard.Module1.ShadowedCallee"'
      type: 172
    title: ShadowedCallee.Module1.Standard
    tokens:
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
      text: ShadowedCallee
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
    - *id004
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
    object_type: library
  source: "REM  *****  BASIC  *****\n\nSub UsesDocument()\n\tprint \"Untitled\"\n\
    End Sub\n\nSub UsesDocumentFilename()\n\tprint \"Untitled.odt\"\nEnd Sub\n\nSub\
    \ CalleeOtherLib\n\tprint \"Standard.Module1.CalleeOtherLib\"\nEnd Sub\n\nSub\
    \ ShadowedCallee()\n\tprint \"Standard.Module1.ShadowedCallee\"\nEnd Sub"
  title: Module1.Standard
  tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 0
    link: null
    text: REM  *****  BASIC  *****
    type: 184
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 1
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 2
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 3
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 4
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 5
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: UsesDocument.Module1.Standard
      object_type: basicfunction
    obj_id: '228'
    text: UsesDocument
    title: token5.Module1.Standard
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 6
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 7
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 8
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 9
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 10
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 11
    link: *id005
    obj_id: '234'
    text: '"Untitled"'
    title: token11.Module1.Standard
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 12
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 13
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 14
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 15
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 16
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 17
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 18
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: UsesDocumentFilename.Module1.Standard
      object_type: basicfunction
    obj_id: '241'
    text: UsesDocumentFilename
    title: token18.Module1.Standard
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 19
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 20
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 21
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 22
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 23
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 24
    link: *id006
    obj_id: '247'
    text: '"Untitled.odt"'
    title: token24.Module1.Standard
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 25
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 26
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 27
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 28
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 29
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 30
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 31
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeOtherLib.Module1.Standard
      object_type: basicfunction
    obj_id: '254'
    text: CalleeOtherLib
    title: token31.Module1.Standard
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 32
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 33
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 34
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 35
    link: null
    text: '"Standard.Module1.CalleeOtherLib"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 36
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 37
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 38
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 39
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 40
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 41
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 42
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: ShadowedCallee.Module1.Standard
      object_type: basicfunction
    obj_id: '265'
    text: ShadowedCallee
    title: token42.Module1.Standard
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 43
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 44
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 45
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 46
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 47
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 48
    link: null
    text: '"Standard.Module1.ShadowedCallee"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 49
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 50
    link: null
    text: End Sub
    type: 44
  used_by: []
  uses: []
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Standard
    module: Module2
    name: Main
    name_token_index: 5
    obj_id: '275'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module2.Standard
      object_type: module
    strings:
    - &id007 !!python/object:odbinfo.pure.datatype.base.Token
      index: 9
      text: '"hello world"'
      type: 172
    title: Main.Module2.Standard
    tokens:
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
      text: Main
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 6
      text: "\n\t"
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 7
      text: Print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 8
      text: ' '
      type: 185
    - *id007
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 10
      text: '

        '
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 11
      text: End Sub
      type: 44
    used_by: []
    uses: []
  library: Standard
  name: Module2
  name_indexes:
  - 5
  obj_id: '274'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Standard
    object_type: library
  source: "REM  *****  BASIC  *****\n\nSub Main\n\tPrint \"hello world\"\nEnd Sub"
  title: Module2.Standard
  tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 0
    link: null
    text: REM  *****  BASIC  *****
    type: 184
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 1
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 2
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 3
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 4
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 5
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Main.Module2.Standard
      object_type: basicfunction
    obj_id: '290'
    text: Main
    title: token5.Module2.Standard
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 6
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 7
    link: null
    text: Print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 8
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 9
    link: null
    text: '"hello world"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 10
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 11
    link: null
    text: End Sub
    type: 44
  used_by: []
  uses: []
name: Standard
obj_id: '175'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadata
title: Standard
used_by: []
uses: []
---
