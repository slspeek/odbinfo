---
!!python/object:odbinfo.pure.datatype.exec.BasicFunction
body_tokens:
- &id002 !!python/object:odbinfo.pure.datatype.base.Token
  index: 136
  text: print
  type: 100
- &id003 !!python/object:odbinfo.pure.datatype.base.Token
  index: 137
  text: ' '
  type: 185
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  index: 138
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: FamilyLookup
    object_type: queries
  obj_id: '517'
  text: '"FamilyLookup"'
  type: 172
- &id004 !!python/object:odbinfo.pure.datatype.base.Token
  index: 139
  text: '

    '
  type: 183
calls: []
library: Library1
module: Module1
name: ReferToQuery
name_token_index: 132
obj_id: '367'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: Module1.Library1
  object_type: modules
strings:
- *id001
title: ReferToQuery.Module1.Library1
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 130
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 131
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 132
  text: ReferToQuery
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 133
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 134
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 135
  text: "\n\t"
  type: 183
- *id002
- *id003
- *id001
- *id004
- !!python/object:odbinfo.pure.datatype.base.Token
  index: 140
  text: End Sub
  type: 44
used_by: []
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: FamilyLookup
  object_type: queries
---
