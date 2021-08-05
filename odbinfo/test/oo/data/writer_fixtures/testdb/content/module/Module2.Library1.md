---
!!python/object:odbinfo.pure.datatype.exec.Module
callables:
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens: []
  calls: []
  library: Library1
  module: Module2
  name: CalleeSub
  name_token_index: 5
  obj_id: '571'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Module2.Library1
    object_type: module
  strings:
  - &id001 !!python/object:odbinfo.pure.datatype.base.Token
    index: 11
    text: '"Module2.CalleeSub"'
    type: 172
  title: CalleeSub.Module2.Library1
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
    text: CalleeSub
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
  used_by:
  - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
    bookmark: null
    local_id: CallerSub.Module1.Library1
    location_id: '322'
    object_type: basicfunction
  uses: []
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens: []
  calls: []
  library: Library1
  module: Module2
  name: CalleeTwoSub
  name_token_index: 18
  obj_id: '583'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Module2.Library1
    object_type: module
  strings:
  - &id002 !!python/object:odbinfo.pure.datatype.base.Token
    index: 24
    text: '"Module2.CalleeTwoSub"'
    type: 172
  title: CalleeTwoSub.Module2.Library1
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
    text: CalleeTwoSub
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
  used_by:
  - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
    bookmark: null
    local_id: CallerTwo.Module1.Library1
    location_id: '346'
    object_type: basicfunction
  uses: []
library: Library1
name: Module2
name_indexes:
- 5
- 18
obj_id: '570'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: Library1
  object_type: library
source: "REM  *****  BASIC  *****\n\nSub CalleeSub()\n\tprint \"Module2.CalleeSub\"\
  \nEnd Sub\n\nSub CalleeTwoSub()\n\tprint \"Module2.CalleeTwoSub\"\nEnd Sub"
title: Module2.Library1
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
    local_id: CalleeSub.Module2.Library1
    object_type: basicfunction
  obj_id: '600'
  text: CalleeSub
  title: token5.Module2.Library1
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
  link: null
  text: '"Module2.CalleeSub"'
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
    local_id: CalleeTwoSub.Module2.Library1
    object_type: basicfunction
  obj_id: '613'
  text: CalleeTwoSub
  title: token18.Module2.Library1
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
  link: null
  text: '"Module2.CalleeTwoSub"'
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
used_by: []
uses: []
---
