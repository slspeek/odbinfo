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
  text: '"Standard.Module1.CalleeOtherLib"'
  type: 172
- &id004 !!python/object:odbinfo.pure.datatype.base.Token
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
  object_type: modules
strings:
- *id001
title: CalleeOtherLib.Module1.Standard
tokens:
- !!python/object:odbinfo.pure.datatype.base.Token
  text: Sub
  type: 125
- !!python/object:odbinfo.pure.datatype.base.Token
  text: ' '
  type: 185
- !!python/object:odbinfo.pure.datatype.base.Token
  text: CalleeOtherLib
  type: 181
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
used_by:
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  local_id: CallerOtherLib.Module1.Library1
  location_id: '444'
  object_type: basicfunctions
- !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
  local_id: CallerOtherLib.Module1.Library1
  location_id: '450'
  object_type: basicfunctions
uses: []
---
