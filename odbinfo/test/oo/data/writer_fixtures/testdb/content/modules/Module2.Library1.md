---
!!python/object:odbinfo.pure.datatype.exec.Module
callables:
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 9
    obj_id: '554'
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 10
    obj_id: '555'
    text: ' '
    type: 185
  - &id001 !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 11
    obj_id: '556'
    text: '"Module2.CalleeSub"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 12
    obj_id: '557'
    text: '

      '
    type: 183
  calls: []
  library: Library1
  module: Module2
  name: CalleeSub
  name_token_index: 5
  obj_id: '521'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: Module2.Library1
    object_type: modules
  strings:
  - *id001
  title: CalleeSub.Module2.Library1
  tokens: []
  used_by: []
  uses: []
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  body_tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 22
    obj_id: '567'
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 23
    obj_id: '568'
    text: ' '
    type: 185
  - &id002 !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 24
    obj_id: '569'
    text: '"Module2.CalleeTwoSub"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 25
    obj_id: '570'
    text: '

      '
    type: 183
  calls: []
  library: Library1
  module: Module2
  name: CalleeTwoSub
  name_token_index: 18
  obj_id: '533'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: Module2.Library1
    object_type: modules
  strings:
  - *id002
  title: CalleeTwoSub.Module2.Library1
  tokens: []
  used_by: []
  uses: []
library: Library1
name: Module2
name_indexes:
- 5
- 18
obj_id: '520'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: Library1
  object_type: libraries
source: "REM  *****  BASIC  *****\n\nSub CalleeSub()\n\tprint \"Module2.CalleeSub\"\
  \nEnd Sub\n\nSub CalleeTwoSub()\n\tprint \"Module2.CalleeTwoSub\"\nEnd Sub"
title: Module2.Library1
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
    local_id: CalleeSub.Module2.Library1
    object_type: basicfunctions
  text: CalleeSub
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 6
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 7
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 8
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 9
  link: null
  text: print
  type: 100
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 10
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 11
  link: null
  text: '"Module2.CalleeSub"'
  type: 172
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
  text: End Sub
  type: 44
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 14
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 15
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 16
  link: null
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 17
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 18
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: CalleeTwoSub.Module2.Library1
    object_type: basicfunctions
  text: CalleeTwoSub
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 19
  link: null
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 20
  link: null
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 21
  link: null
  text: "\n\t"
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 22
  link: null
  text: print
  type: 100
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 23
  link: null
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 24
  link: null
  text: '"Module2.CalleeTwoSub"'
  type: 172
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 25
  link: null
  text: '

    '
  type: 183
- !!python/object:odbinfo.pure.datatype.base.Token
  hidden: false
  index: 26
  link: null
  text: End Sub
  type: 44
used_by: []
uses: []
---
