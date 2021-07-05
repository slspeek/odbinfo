---
!!python/object:odbinfo.pure.datatype.exec.BasicFunction
body_tokens:
- &id002 !!python/object:odbinfo.pure.datatype.base.Token
  index: 110
  text: print
  type: 100
- &id003 !!python/object:odbinfo.pure.datatype.base.Token
  index: 111
  text: ' '
  type: 185
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  index: 112
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: Plant
    object_type: table
  obj_id: '491'
  text: '"Plant"'
  type: 172
- &id004 !!python/object:odbinfo.pure.datatype.base.Token
  index: 113
  text: '

    '
  type: 183
calls: []
library: Library1
module: Module1
name: ReferToTable
name_token_index: 106
obj_id: '343'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: Module1.Library1
  object_type: module
strings:
- *id001
title: ReferToTable.Module1.Library1
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 104
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 105
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 106
  text: ReferToTable
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 107
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 108
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 109
  text: "\n\t"
  type: 183
- *id002
- *id003
- *id001
- *id004
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 114
  text: End Sub
  type: 44
used_by: []
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: Plant
  object_type: table
---
