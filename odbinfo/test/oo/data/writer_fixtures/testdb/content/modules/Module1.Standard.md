---
!!python/object:odbinfo.pure.datatype.exec.Module
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
  used_by: []
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
  \nEnd Sub\n\nSub ShadowedCallee()\n\tprint \"Standard.Module1.ShadowedCallee\"\n\
  End Sub"
title: Module1.Standard
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: REM  *****  BASIC  *****
  type: 184
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: CalleeOtherLib.Module1.Standard
    object_type: basicfunctions
  text: CalleeOtherLib
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: print
  type: 100
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '"Standard.Module1.CalleeOtherLib"'
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: ShadowedCallee.Module1.Standard
    object_type: basicfunctions
  text: ShadowedCallee
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: print
  type: 100
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '"Standard.Module1.ShadowedCallee"'
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: End Sub
  type: 44
used_by: []
uses: []
---
