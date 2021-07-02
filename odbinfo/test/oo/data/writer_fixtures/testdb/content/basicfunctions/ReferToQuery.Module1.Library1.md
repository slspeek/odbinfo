---
!!python/object:odbinfo.pure.datatype.exec.BasicFunction
body_tokens:
- &id002 !!python/object:odbinfo.pure.datatype.base.Token
  text: print
  type: 100
- &id003 !!python/object:odbinfo.pure.datatype.base.Token
  text: ' '
  type: 185
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: FamilyLookup
    object_type: queries
  obj_id: '517'
  text: '"FamilyLookup"'
  type: 172
- &id004 !!python/object:odbinfo.pure.datatype.base.Token
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
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  text: ReferToQuery
  type: 181
- !!python/object:odbinfo.pure.datatype.base.Token
  text: (
  type: 157
- !!python/object:odbinfo.pure.datatype.base.Token
  text: )
  type: 168
- !!python/object:odbinfo.pure.datatype.base.Token
  text: "\n\t"
  type: 183
- *id002
- *id003
- *id001
- *id004
- !!python/object:odbinfo.pure.datatype.base.Token
  text: End Sub
  type: 44
used_by: []
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: FamilyLookup
  object_type: queries
---
