---
!!python/object:odbinfo.pure.datatype.exec.Library
modules:
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id002 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 7
      obj_id: '206'
      text: print
      type: 100
    - &id003 !!python/object:odbinfo.pure.datatype.base.Token
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
    - &id004 !!python/object:odbinfo.pure.datatype.base.Token
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
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 3
      obj_id: '202'
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 4
      obj_id: '203'
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 5
      obj_id: '204'
      text: CalleeOtherLib
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 6
      obj_id: '205'
      text: "\n\t"
      type: 183
    - *id002
    - *id003
    - *id001
    - *id004
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 11
      obj_id: '210'
      text: End Sub
      type: 44
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id006 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 20
      obj_id: '219'
      text: print
      type: 100
    - &id007 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 21
      obj_id: '220'
      text: ' '
      type: 185
    - &id005 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 22
      obj_id: '221'
      text: '"Standard.Module1.ShadowedCallee"'
      type: 172
    - &id008 !!python/object:odbinfo.pure.datatype.base.Token
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
    - *id005
    title: ShadowedCallee.Module1.Standard
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 14
      obj_id: '213'
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 15
      obj_id: '214'
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 16
      obj_id: '215'
      text: ShadowedCallee
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 17
      obj_id: '216'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 18
      obj_id: '217'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 19
      obj_id: '218'
      text: "\n\t"
      type: 183
    - *id006
    - *id007
    - *id005
    - *id008
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 24
      obj_id: '223'
      text: End Sub
      type: 44
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
  tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: true
    index: 0
    link: null
    text: REM  *****  BASIC  *****
    type: 184
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 1
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 2
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 3
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 4
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 5
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: CalleeOtherLib.Module1.Standard
      object_type: basicfunctions
    text: CalleeOtherLib
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 6
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 7
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 8
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 9
    link: null
    text: '"Standard.Module1.CalleeOtherLib"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 10
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 11
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 12
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 13
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 14
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 15
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 16
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: ShadowedCallee.Module1.Standard
      object_type: basicfunctions
    text: ShadowedCallee
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 17
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 18
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 19
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 20
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 21
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 22
    link: null
    text: '"Standard.Module1.ShadowedCallee"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 23
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 24
    link: null
    text: End Sub
    type: 44
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id010 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 7
      obj_id: '242'
      text: Print
      type: 100
    - &id011 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 8
      obj_id: '243'
      text: ' '
      type: 185
    - &id009 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 9
      obj_id: '244'
      text: '"hello world"'
      type: 172
    - &id012 !!python/object:odbinfo.pure.datatype.base.Token
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
    - *id009
    title: Main.Module2.Standard
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 3
      obj_id: '238'
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 4
      obj_id: '239'
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 5
      obj_id: '240'
      text: Main
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 6
      obj_id: '241'
      text: "\n\t"
      type: 183
    - *id010
    - *id011
    - *id009
    - *id012
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 11
      obj_id: '246'
      text: End Sub
      type: 44
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
  tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: true
    index: 0
    link: null
    text: REM  *****  BASIC  *****
    type: 184
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 1
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 2
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 3
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 4
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 5
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Main.Module2.Standard
      object_type: basicfunctions
    text: Main
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 6
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 7
    link: null
    text: Print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 8
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 9
    link: null
    text: '"hello world"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 10
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 11
    link: null
    text: End Sub
    type: 44
name: Standard
obj_id: '175'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: ./testdb.odb
  object_type: metadatas
title: Standard
---
