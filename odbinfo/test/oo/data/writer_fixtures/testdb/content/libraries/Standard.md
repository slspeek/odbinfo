---
!!python/object:odbinfo.pure.datatype.exec.Library
modules:
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: ' '
      type: 185
    - &id001 !!python/object:odbinfo.pure.datatype.base.Token
      text: '"Standard.Module1.CalleeOtherLib"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: '

        '
      type: 183
    calls: []
    library: Standard
    module: Module1
    name: CalleeOtherLib
    name_token_index: 5
    obj_id: '177'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Standard
      object_type: modules
    strings:
    - *id001
    title: CalleeOtherLib.Module1.Standard
    tokens: []
    used_by:
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      local_id: CallerOtherLib.Module1.Library1
      location_id: '444'
      object_type: basicfunctions
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      local_id: CallerOtherLib.Module1.Library1
      location_id: '450'
      object_type: basicfunctions
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: ' '
      type: 185
    - &id002 !!python/object:odbinfo.pure.datatype.base.Token
      text: '"Standard.Module1.ShadowedCallee"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: '

        '
      type: 183
    calls: []
    library: Standard
    module: Module1
    name: ShadowedCallee
    name_token_index: 16
    obj_id: '187'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Standard
      object_type: modules
    strings:
    - *id002
    title: ShadowedCallee.Module1.Standard
    tokens: []
    used_by: []
    uses: []
  library: Standard
  name: Module1
  name_indexes:
  - 5
  - 16
  obj_id: '176'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: Standard
    object_type: libraries
  source: "REM  *****  BASIC  *****\n\nSub CalleeOtherLib\n\tprint \"Standard.Module1.CalleeOtherLib\"\
    \nEnd Sub\n\nSub ShadowedCallee()\n\tprint \"Standard.Module1.ShadowedCallee\"\
    \nEnd Sub"
  title: Module1.Standard
  tokens: []
  used_by: []
  uses: []
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: Print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: ' '
      type: 185
    - &id003 !!python/object:odbinfo.pure.datatype.base.Token
      text: '"hello world"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      text: '

        '
      type: 183
    calls: []
    library: Standard
    module: Module2
    name: Main
    name_token_index: 5
    obj_id: '225'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module2.Standard
      object_type: modules
    strings:
    - *id003
    title: Main.Module2.Standard
    tokens: []
    used_by: []
    uses: []
  library: Standard
  name: Module2
  name_indexes:
  - 5
  obj_id: '224'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: Standard
    object_type: libraries
  source: "REM  *****  BASIC  *****\n\nSub Main\n\tPrint \"hello world\"\nEnd Sub"
  title: Module2.Standard
  tokens: []
  used_by: []
  uses: []
name: Standard
obj_id: '175'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: ./testdb.odb
  object_type: metadatas
title: Standard
used_by: []
uses: []
---
