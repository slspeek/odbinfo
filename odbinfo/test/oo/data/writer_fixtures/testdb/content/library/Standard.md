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
    obj_id: '218'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      content_type: module
      local_id: Module1.Standard
    strings:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 11
      link: &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        content_type: textdocument
        local_id: Untitled
      obj_id: '227'
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
    obj_id: '230'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      content_type: module
      local_id: Module1.Standard
    strings:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 24
      link: &id002 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        content_type: textdocument
        local_id: Untitled
      obj_id: '239'
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
    obj_id: '242'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      content_type: module
      local_id: Module1.Standard
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
      content_type: basicfunction
      local_id: CallerOtherLib.Module1.Library1
      location_id: '442'
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      bookmark: null
      content_type: basicfunction
      local_id: CallerOtherLib.Module1.Library1
      location_id: '448'
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Standard
    module: Module1
    name: ShadowedCallee
    name_token_index: 42
    obj_id: '252'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      content_type: module
      local_id: Module1.Standard
    strings:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 48
      text: '"Standard.Module1.ShadowedCallee"'
      type: 172
    title: ShadowedCallee.Module1.Standard
    tokens: []
    used_by: []
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: !!python/object:odbinfo.pure.datatype.base.Token
        index: 60
        text: AddOne
        type: 181
    library: Standard
    module: Module1
    name: AddOne
    name_token_index: 55
    obj_id: '264'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      content_type: module
      local_id: Module1.Standard
    strings: []
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
  source: "REM  *****  BASIC  *****\n\nSub UsesDocument()\n\tprint \"Untitled\"\n\
    End Sub\n\nSub UsesDocumentFilename()\n\tprint \"Untitled.odt\"\nEnd Sub\n\nSub\
    \ CalleeOtherLib\n\tprint \"Standard.Module1.CalleeOtherLib\"\nEnd Sub\n\nSub\
    \ ShadowedCallee()\n\tprint \"Standard.Module1.ShadowedCallee\"\nEnd Sub\n\nFunction\
    \ AddOne(arg)\n\tAddOne() = arg + 1\nEnd Function"
  title: Module1.Standard
  tokens: []
  used_by: []
  uses:
  - *id001
  - *id002
  - *id001
  - *id002
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Standard
    module: Module2
    name: Main
    name_token_index: 5
    obj_id: '359'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      content_type: module
      local_id: Module2.Standard
    strings:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 9
      text: '"hello world"'
      type: 172
    title: Main.Module2.Standard
    tokens: []
    used_by: []
    uses: []
  library: Standard
  name: Module2
  name_indexes:
  - 5
  obj_id: '358'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: library
    local_id: Standard
  source: "REM  *****  BASIC  *****\n\nSub Main\n\tPrint \"hello world\"\nEnd Sub"
  title: Module2.Standard
  tokens: []
  used_by: []
  uses: []
name: Standard
obj_id: '216'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: metadata
  local_id: ./testdb.odb
title: Standard
used_by: []
uses:
- *id001
- *id002
- *id001
- *id002
---
