---
!!python/object:odbinfo.pure.datatype.exec.Library
modules:
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 7
      obj_id: '206'
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 8
      obj_id: '207'
      text: ' '
      type: 185
    - &id001 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 9
      obj_id: '208'
      text: '"Standard.Module1.CalleeOtherLib"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 10
      obj_id: '209'
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
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 20
      obj_id: '219'
      text: print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 21
      obj_id: '220'
      text: ' '
      type: 185
    - &id002 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 22
      obj_id: '221'
      text: '"Standard.Module1.ShadowedCallee"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 23
      obj_id: '222'
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
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 7
      obj_id: '242'
      text: Print
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 8
      obj_id: '243'
      text: ' '
      type: 185
    - &id003 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 9
      obj_id: '244'
      text: '"hello world"'
      type: 172
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 10
      obj_id: '245'
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
name: Standard
obj_id: '175'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: ./testdb.odb
  object_type: metadatas
title: Standard
---
