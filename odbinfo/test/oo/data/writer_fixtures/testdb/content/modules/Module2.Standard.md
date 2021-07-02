---
!!python/object:odbinfo.pure.datatype.exec.Module
callables:
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    text: Print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    text: ' '
    type: 185
  - &id001 !!python/object:odbinfo.pure.datatype.base.Token
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
  - *id001
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
    local_id: Main.Module2.Standard
    object_type: basicfunctions
  text: Main
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: Print
  type: 100
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  link: null
  text: '"hello world"'
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
