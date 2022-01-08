---
library: Library1
module: Module1
name: CallerSub
name_token_index: 16
obj_id: '456'
parent_link:
  content_type: module
  local_id: Module1.Library1
title: CallerSub.Module1.Library1
tokens:
- index: 14
  text: Sub
- index: 15
  text: ' '
- cls: identifier
  index: 16
  text: CallerSub
- index: 17
  text: (
- index: 18
  text: )
- index: 19
  text: "\n\t"
- cls: identifier
  index: 20
  link:
    content_type: basicfunction
    local_id: CalleeSub.Module1.Library1
  obj_id: '463'
  text: CalleeSub
- index: 21
  text: (
- index: 22
  text: )
- index: 23
  text: "\n\t"
- cls: identifier
  index: 24
  text: Module2
- index: 25
  text: .
- cls: identifier
  index: 26
  link:
    content_type: basicfunction
    local_id: CalleeSub.Module2.Library1
  obj_id: '469'
  text: CalleeSub
- index: 27
  text: (
- index: 28
  text: )
- index: 29
  text: '

    '
- index: 30
  text: End Sub
used_by: []
uses:
- link:
    content_type: basicfunction
    local_id: CalleeSub.Module1.Library1
  sources: '463'
- link:
    content_type: basicfunction
    local_id: CalleeSub.Module2.Library1
  sources: '469'
---
