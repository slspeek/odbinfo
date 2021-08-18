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
  source: "REM  *****  BASIC  *****\n\nSub UsesDocument()\n\tprint \"Untitled\"\n\
    End Sub\n\nSub UsesDocumentFilename()\n\tprint \"Untitled.odt\"\nEnd Sub\n\nSub\
    \ CalleeOtherLib\n\tprint \"Standard.Module1.CalleeOtherLib\"\nEnd Sub\n\nSub\
    \ ShadowedCallee()\n\tprint \"Standard.Module1.ShadowedCallee\"\nEnd Sub"
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
    obj_id: '275'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module2.Standard
      content_type: module
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
  obj_id: '274'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Standard
    content_type: library
  source: "REM  *****  BASIC  *****\n\nSub Main\n\tPrint \"hello world\"\nEnd Sub"
  title: Module2.Standard
  tokens: []
  used_by: []
  uses: []
name: Standard
obj_id: '175'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: ./testdb.odb
  content_type: metadata
title: Standard
used_by: []
uses:
- *id001
- *id002
- *id001
- *id002
---
