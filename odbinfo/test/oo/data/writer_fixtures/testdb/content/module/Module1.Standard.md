---
!!python/object:odbinfo.pure.datatype.exec.Module
callables:
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens:
  - &id002 !!python/object:odbinfo.pure.datatype.base.Token
    index: 7
    text: print
    type: 100
  - &id003 !!python/object:odbinfo.pure.datatype.base.Token
    index: 8
    text: ' '
    type: 185
  - &id001 !!python/object:odbinfo.pure.datatype.base.Token
    index: 9
    text: '"Standard.Module1.CalleeOtherLib"'
    type: 172
  - &id004 !!python/object:odbinfo.pure.datatype.base.Token
    index: 10
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
    object_type: module
  strings:
  - *id001
  title: CalleeOtherLib.Module1.Standard
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
    text: CalleeOtherLib
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 6
    text: "\n\t"
    type: 183
  - *id002
  - *id003
  - *id001
  - *id004
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 11
    text: End Sub
    type: 44
  used_by:
  - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
    local_id: CallerOtherLib.Module1.Library1
    location_id: '444'
    object_type: basicfunction
  - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
    local_id: CallerOtherLib.Module1.Library1
    location_id: '450'
    object_type: basicfunction
  uses: []
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens:
  - &id006 !!python/object:odbinfo.pure.datatype.base.Token
    index: 20
    text: print
    type: 100
  - &id007 !!python/object:odbinfo.pure.datatype.base.Token
    index: 21
    text: ' '
    type: 185
  - &id005 !!python/object:odbinfo.pure.datatype.base.Token
    index: 22
    text: '"Standard.Module1.ShadowedCallee"'
    type: 172
  - &id008 !!python/object:odbinfo.pure.datatype.base.Token
    index: 23
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
    object_type: module
  strings:
  - *id005
  title: ShadowedCallee.Module1.Standard
  tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 14
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 15
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 16
    text: ShadowedCallee
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 17
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 18
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 19
    text: "\n\t"
    type: 183
  - *id006
  - *id007
  - *id005
  - *id008
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 24
    text: End Sub
    type: 44
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
  object_type: library
source: "REM  *****  BASIC  *****\n\nSub CalleeOtherLib\n\tprint \"Standard.Module1.CalleeOtherLib\"\
  \nEnd Sub\n\nSub ShadowedCallee()\n\tprint \"Standard.Module1.ShadowedCallee\"\n\
  End Sub"
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
    local_id: CalleeOtherLib.Module1.Standard
    object_type: basicfunction
  text: CalleeOtherLib
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 6
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 7
  link: null
  text: print
  type: 100
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 8
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 9
  link: null
  text: '"Standard.Module1.CalleeOtherLib"'
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
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 12
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 13
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 14
  link: null
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 15
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 16
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: ShadowedCallee.Module1.Standard
    object_type: basicfunction
  text: ShadowedCallee
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 17
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 18
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 19
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 20
  link: null
  text: print
  type: 100
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 21
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 22
  link: null
  text: '"Standard.Module1.ShadowedCallee"'
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 23
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 24
  link: null
  text: End Sub
  type: 44
used_by: []
uses: []
---
