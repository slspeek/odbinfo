---
!!python/object:odbinfo.pure.datatype.exec.BasicFunction
body_tokens:
- &id001 !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: CalleeSub.Module1.Library1
    object_type: basicfunctions
  obj_id: '399'
  text: CalleeSub
  type: 181
- &id004 !!python/object:odbinfo.pure.datatype.base.Token
  text: (
  type: 157
- &id005 !!python/object:odbinfo.pure.datatype.base.Token
  text: )
  type: 168
- &id006 !!python/object:odbinfo.pure.datatype.base.Token
  text: "\n\t"
  type: 183
- &id002 !!python/object:odbinfo.pure.datatype.base.Token
  text: Module2
  type: 181
- &id007 !!python/object:odbinfo.pure.datatype.base.Token
  text: .
  type: 150
- &id003 !!python/object:odbinfo.pure.datatype.base.Token
  link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: CalleeSub.Module2.Library1
    object_type: basicfunctions
  obj_id: '405'
  text: CalleeSub
  type: 181
- &id008 !!python/object:odbinfo.pure.datatype.base.Token
  text: (
  type: 157
- &id009 !!python/object:odbinfo.pure.datatype.base.Token
  text: )
  type: 168
- &id010 !!python/object:odbinfo.pure.datatype.base.Token
  text: '

    '
  type: 183
calls:
- !!python/object:odbinfo.pure.datatype.exec.BasicCall
  module_token: null
  name_token: *id001
- !!python/object:odbinfo.pure.datatype.exec.BasicCall
  module_token: *id002
  name_token: *id003
library: Library1
module: Module1
name: CallerSub
name_token_index: 16
obj_id: '259'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: Module1.Library1
  object_type: modules
strings: []
title: CallerSub.Module1.Library1
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  text: CallerSub
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
- *id001
- *id004
- *id005
- *id006
- *id002
- *id007
- *id003
- *id008
- *id009
- *id010
- !!python/object:odbinfo.pure.datatype.base.Token
  text: End Sub
  type: 44
used_by: []
uses:
- !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: CalleeSub.Module1.Library1
  object_type: basicfunctions
- !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: CalleeSub.Module2.Library1
  object_type: basicfunctions
---
