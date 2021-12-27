---
callables:
- content_type: basicfunction
  local_id: CalleeSub.Module2.Library1
- content_type: basicfunction
  local_id: CalleeTwoSub.Module2.Library1
library: Library1
name: Module2
name_indexes:
- 5
- 18
obj_id: '719'
parent_link:
  content_type: library
  local_id: Library1
source: "REM  *****  BASIC  *****\n\nSub CalleeSub()\n\tprint \"Module2.CalleeSub\"\
  \nEnd Sub\n\nSub CalleeTwoSub()\n\tprint \"Module2.CalleeTwoSub\"\nEnd Sub\n\n"
title: Module2.Library1
tokens:
- cls: comment
  index: 0
  text: REM  *****  BASIC  *****
- index: 1
  text: '

    '
- index: 2
  text: '

    '
- index: 3
  text: Sub
- index: 4
  text: ' '
- cls: identifier
  index: 5
  link:
    content_type: basicfunction
    local_id: CalleeSub.Module2.Library1
  obj_id: '749'
  text: CalleeSub
- index: 6
  text: (
- index: 7
  text: )
- index: 8
  text: "\n\t"
- index: 9
  text: print
- index: 10
  text: ' '
- cls: stringlit
  index: 11
  text: '"Module2.CalleeSub"'
- index: 12
  text: '

    '
- index: 13
  text: End Sub
- index: 14
  text: '

    '
- index: 15
  text: '

    '
- index: 16
  text: Sub
- index: 17
  text: ' '
- cls: identifier
  index: 18
  link:
    content_type: basicfunction
    local_id: CalleeTwoSub.Module2.Library1
  obj_id: '762'
  text: CalleeTwoSub
- index: 19
  text: (
- index: 20
  text: )
- index: 21
  text: "\n\t"
- index: 22
  text: print
- index: 23
  text: ' '
- cls: stringlit
  index: 24
  text: '"Module2.CalleeTwoSub"'
- index: 25
  text: '

    '
- index: 26
  text: End Sub
- index: 27
  text: '

    '
- index: 28
  text: '

    '
---
