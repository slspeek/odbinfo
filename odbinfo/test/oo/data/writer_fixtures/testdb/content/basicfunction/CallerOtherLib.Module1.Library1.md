---
!!python/object:odbinfo.pure.datatype.exec.BasicFunction
library: Library1
module: Module1
name: CallerOtherLib
name_token_index: 61
obj_id: '463'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  content_type: module
  local_id: Module1.Library1
title: CallerOtherLib.Module1.Library1
tokens:
- index: 59
  text: Sub
  type: 125
- index: 60
  text: ' '
  type: 185
- index: 61
  text: CallerOtherLib
  type: 181
- index: 62
  text: (
  type: 157
- index: 63
  text: )
  type: 168
- index: 64
  text: "\n\t"
  type: 183
- index: 65
  link: &id001 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: CalleeOtherLib.Module1.Standard
  obj_id: '470'
  text: CalleeOtherLib
  type: 181
- index: 66
  text: (
  type: 157
- index: 67
  text: )
  type: 168
- index: 68
  text: "\n\t"
  type: 183
- index: 69
  text: Module1
  type: 181
- index: 70
  text: .
  type: 150
- index: 71
  link: &id002 !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    content_type: basicfunction
    local_id: CalleeOtherLib.Module1.Standard
  obj_id: '476'
  text: CalleeOtherLib
  type: 181
- index: 72
  text: (
  type: 157
- index: 73
  text: )
  type: 168
- index: 74
  text: '

    '
  type: 183
- index: 75
  text: End Sub
  type: 44
used_by: []
uses:
- *id001
- *id002
---
