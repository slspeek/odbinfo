---
!!python/object:odbinfo.pure.datatype.exec.Module
callables:
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Library1
  module: Module2
  name: CalleeSub
  name_token_index: 5
  obj_id: '655'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module2.Library1
  title: CalleeSub.Module2.Library1
  tokens: []
  used_by:
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: '406'
    content_type: basicfunction
    local_id: CallerSub.Module1.Library1
  uses: []
- !!python/object:odbinfo.pure.datatype.exec.BasicFunction
  library: Library1
  module: Module2
  name: CalleeTwoSub
  name_token_index: 18
  obj_id: '667'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: module
    local_id: Module2.Library1
  title: CalleeTwoSub.Module2.Library1
  tokens: []
  used_by:
  - !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: '430'
    content_type: basicfunction
    local_id: CallerTwo.Module1.Library1
  uses: []
library: Library1
name: Module2
name_indexes:
- 5
- 18
obj_id: '654'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: library
  local_id: Library1
title: Module2.Library1
tokens:
- index: 0
  text: REM  *****  BASIC  *****
  type: 184
- index: 1
  text: '

    '
  type: 183
- index: 2
  text: '

    '
  type: 183
- index: 3
  text: Sub
  type: 125
- index: 4
  text: ' '
  type: 185
- index: 5
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: CalleeSub.Module2.Library1
  obj_id: '684'
  text: CalleeSub
  title: token5.Module2.Library1
  type: 181
- index: 6
  text: (
  type: 157
- index: 7
  text: )
  type: 168
- index: 8
  text: "\n\t"
  type: 183
- index: 9
  text: print
  type: 100
- index: 10
  text: ' '
  type: 185
- index: 11
  text: '"Module2.CalleeSub"'
  type: 172
- index: 12
  text: '

    '
  type: 183
- index: 13
  text: End Sub
  type: 44
- index: 14
  text: '

    '
  type: 183
- index: 15
  text: '

    '
  type: 183
- index: 16
  text: Sub
  type: 125
- index: 17
  text: ' '
  type: 185
- index: 18
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: CalleeTwoSub.Module2.Library1
  obj_id: '697'
  text: CalleeTwoSub
  title: token18.Module2.Library1
  type: 181
- index: 19
  text: (
  type: 157
- index: 20
  text: )
  type: 168
- index: 21
  text: "\n\t"
  type: 183
- index: 22
  text: print
  type: 100
- index: 23
  text: ' '
  type: 185
- index: 24
  text: '"Module2.CalleeTwoSub"'
  type: 172
- index: 25
  text: '

    '
  type: 183
- index: 26
  text: End Sub
  type: 44
used_by: []
uses: []
---
