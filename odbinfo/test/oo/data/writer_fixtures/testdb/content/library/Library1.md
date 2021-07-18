---
!!python/object:odbinfo.pure.datatype.exec.Library
modules:
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Library1
    module: Module1
    name: Main
    name_token_index: 5
    obj_id: '299'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      object_type: module
    strings:
    - &id001 !!python/object:odbinfo.pure.datatype.base.Token
      index: 9
      text: '"Mijn fout"'
      title: token9.Main.Module1.Library1.Main.Module1.Library1
      type: 172
    title: Main.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 3
      text: Sub
      title: token3.Main.Module1.Library1.Main.Module1.Library1
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 4
      text: ' '
      title: token4.Main.Module1.Library1.Main.Module1.Library1
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 5
      text: Main
      title: token5.Main.Module1.Library1.Main.Module1.Library1
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 6
      text: "\n\t"
      title: token6.Main.Module1.Library1.Main.Module1.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 7
      text: Error
      title: token7.Main.Module1.Library1.Main.Module1.Library1
      type: 49
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 8
      text: ' '
      title: token8.Main.Module1.Library1.Main.Module1.Library1
      type: 185
    - *id001
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 10
      text: '

        '
      title: token10.Main.Module1.Library1.Main.Module1.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 11
      text: End Sub
      title: token11.Main.Module1.Library1.Main.Module1.Library1
      type: 44
    used_by: []
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: &id002 !!python/object:odbinfo.pure.datatype.base.Token
        index: 20
        link: &id015 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: CalleeSub.Module1.Library1
          object_type: basicfunction
        obj_id: '449'
        text: CalleeSub
        title: token20.CallerSub.Module1.Library1.CallerSub.Module1.Library1
        type: 181
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: &id003 !!python/object:odbinfo.pure.datatype.base.Token
        index: 24
        text: Module2
        title: token24.CallerSub.Module1.Library1.CallerSub.Module1.Library1
        type: 181
      name_token: &id004 !!python/object:odbinfo.pure.datatype.base.Token
        index: 26
        link: &id016 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: CalleeSub.Module2.Library1
          object_type: basicfunction
        obj_id: '455'
        text: CalleeSub
        title: token26.CallerSub.Module1.Library1.CallerSub.Module1.Library1
        type: 181
    library: Library1
    module: Module1
    name: CallerSub
    name_token_index: 16
    obj_id: '309'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      object_type: module
    strings: []
    title: CallerSub.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 14
      text: Sub
      title: token14.CallerSub.Module1.Library1.CallerSub.Module1.Library1
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 15
      text: ' '
      title: token15.CallerSub.Module1.Library1.CallerSub.Module1.Library1
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 16
      text: CallerSub
      title: token16.CallerSub.Module1.Library1.CallerSub.Module1.Library1
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 17
      text: (
      title: token17.CallerSub.Module1.Library1.CallerSub.Module1.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 18
      text: )
      title: token18.CallerSub.Module1.Library1.CallerSub.Module1.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 19
      text: "\n\t"
      title: token19.CallerSub.Module1.Library1.CallerSub.Module1.Library1
      type: 183
    - *id002
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 21
      text: (
      title: token21.CallerSub.Module1.Library1.CallerSub.Module1.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 22
      text: )
      title: token22.CallerSub.Module1.Library1.CallerSub.Module1.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 23
      text: "\n\t"
      title: token23.CallerSub.Module1.Library1.CallerSub.Module1.Library1
      type: 183
    - *id003
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 25
      text: .
      title: token25.CallerSub.Module1.Library1.CallerSub.Module1.Library1
      type: 150
    - *id004
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 27
      text: (
      title: token27.CallerSub.Module1.Library1.CallerSub.Module1.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 28
      text: )
      title: token28.CallerSub.Module1.Library1.CallerSub.Module1.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 29
      text: '

        '
      title: token29.CallerSub.Module1.Library1.CallerSub.Module1.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 30
      text: End Sub
      title: token30.CallerSub.Module1.Library1.CallerSub.Module1.Library1
      type: 44
    used_by: []
    uses:
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeSub.Module1.Library1
      object_type: basicfunction
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeSub.Module2.Library1
      object_type: basicfunction
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Library1
    module: Module1
    name: CalleeSub
    name_token_index: 35
    obj_id: '327'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      object_type: module
    strings:
    - &id005 !!python/object:odbinfo.pure.datatype.base.Token
      index: 41
      text: '"Module1.CalleeSub"'
      title: token41.CalleeSub.Module1.Library1.CalleeSub.Module1.Library1
      type: 172
    title: CalleeSub.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 33
      text: Sub
      title: token33.CalleeSub.Module1.Library1.CalleeSub.Module1.Library1
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 34
      text: ' '
      title: token34.CalleeSub.Module1.Library1.CalleeSub.Module1.Library1
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 35
      text: CalleeSub
      title: token35.CalleeSub.Module1.Library1.CalleeSub.Module1.Library1
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 36
      text: (
      title: token36.CalleeSub.Module1.Library1.CalleeSub.Module1.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 37
      text: )
      title: token37.CalleeSub.Module1.Library1.CalleeSub.Module1.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 38
      text: "\n\t"
      title: token38.CalleeSub.Module1.Library1.CalleeSub.Module1.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 39
      text: print
      title: token39.CalleeSub.Module1.Library1.CalleeSub.Module1.Library1
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 40
      text: ' '
      title: token40.CalleeSub.Module1.Library1.CalleeSub.Module1.Library1
      type: 185
    - *id005
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 42
      text: '

        '
      title: token42.CalleeSub.Module1.Library1.CalleeSub.Module1.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 43
      text: End Sub
      title: token43.CalleeSub.Module1.Library1.CalleeSub.Module1.Library1
      type: 44
    used_by:
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      bookmark: null
      local_id: CallerSub.Module1.Library1
      location_id: '449'
      object_type: basicfunction
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: &id006 !!python/object:odbinfo.pure.datatype.base.Token
        index: 52
        link: &id017 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: CalleeTwoSub.Module2.Library1
          object_type: basicfunction
        obj_id: '481'
        text: CalleeTwoSub
        title: token52.CallerTwo.Module1.Library1.CallerTwo.Module1.Library1
        type: 181
    library: Library1
    module: Module1
    name: CallerTwo
    name_token_index: 48
    obj_id: '339'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      object_type: module
    strings: []
    title: CallerTwo.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 46
      text: sub
      title: token46.CallerTwo.Module1.Library1.CallerTwo.Module1.Library1
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 47
      text: ' '
      title: token47.CallerTwo.Module1.Library1.CallerTwo.Module1.Library1
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 48
      text: CallerTwo
      title: token48.CallerTwo.Module1.Library1.CallerTwo.Module1.Library1
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 49
      text: (
      title: token49.CallerTwo.Module1.Library1.CallerTwo.Module1.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 50
      text: )
      title: token50.CallerTwo.Module1.Library1.CallerTwo.Module1.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 51
      text: "\n\t"
      title: token51.CallerTwo.Module1.Library1.CallerTwo.Module1.Library1
      type: 183
    - *id006
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 53
      text: (
      title: token53.CallerTwo.Module1.Library1.CallerTwo.Module1.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 54
      text: )
      title: token54.CallerTwo.Module1.Library1.CallerTwo.Module1.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 55
      text: '

        '
      title: token55.CallerTwo.Module1.Library1.CallerTwo.Module1.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 56
      text: End Sub
      title: token56.CallerTwo.Module1.Library1.CallerTwo.Module1.Library1
      type: 44
    used_by: []
    uses:
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeTwoSub.Module2.Library1
      object_type: basicfunction
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: &id007 !!python/object:odbinfo.pure.datatype.base.Token
        index: 65
        link: &id018 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: CalleeOtherLib.Module1.Standard
          object_type: basicfunction
        obj_id: '494'
        text: CalleeOtherLib
        title: token65.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
        type: 181
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: &id008 !!python/object:odbinfo.pure.datatype.base.Token
        index: 69
        text: Module1
        title: token69.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
        type: 181
      name_token: &id009 !!python/object:odbinfo.pure.datatype.base.Token
        index: 71
        link: &id019 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: CalleeOtherLib.Module1.Standard
          object_type: basicfunction
        obj_id: '500'
        text: CalleeOtherLib
        title: token71.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
        type: 181
    library: Library1
    module: Module1
    name: CallerOtherLib
    name_token_index: 61
    obj_id: '351'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      object_type: module
    strings: []
    title: CallerOtherLib.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 59
      text: Sub
      title: token59.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 60
      text: ' '
      title: token60.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 61
      text: CallerOtherLib
      title: token61.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 62
      text: (
      title: token62.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 63
      text: )
      title: token63.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 64
      text: "\n\t"
      title: token64.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
      type: 183
    - *id007
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 66
      text: (
      title: token66.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 67
      text: )
      title: token67.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 68
      text: "\n\t"
      title: token68.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
      type: 183
    - *id008
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 70
      text: .
      title: token70.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
      type: 150
    - *id009
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 72
      text: (
      title: token72.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 73
      text: )
      title: token73.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 74
      text: '

        '
      title: token74.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 75
      text: End Sub
      title: token75.CallerOtherLib.Module1.Library1.CallerOtherLib.Module1.Library1
      type: 44
    used_by: []
    uses:
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeOtherLib.Module1.Standard
      object_type: basicfunction
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeOtherLib.Module1.Standard
      object_type: basicfunction
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: &id010 !!python/object:odbinfo.pure.datatype.base.Token
        index: 84
        link: &id020 !!python/object:odbinfo.pure.datatype.base.Identifier
          bookmark: null
          local_id: ShadowedCallee.Module1.Library1
          object_type: basicfunction
        obj_id: '513'
        text: ShadowedCallee
        title: token84.CallerShadowedCallee.Module1.Library1.CallerShadowedCallee.Module1.Library1
        type: 181
    library: Library1
    module: Module1
    name: CallerShadowedCallee
    name_token_index: 80
    obj_id: '369'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      object_type: module
    strings: []
    title: CallerShadowedCallee.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 78
      text: Sub
      title: token78.CallerShadowedCallee.Module1.Library1.CallerShadowedCallee.Module1.Library1
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 79
      text: ' '
      title: token79.CallerShadowedCallee.Module1.Library1.CallerShadowedCallee.Module1.Library1
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 80
      text: CallerShadowedCallee
      title: token80.CallerShadowedCallee.Module1.Library1.CallerShadowedCallee.Module1.Library1
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 81
      text: (
      title: token81.CallerShadowedCallee.Module1.Library1.CallerShadowedCallee.Module1.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 82
      text: )
      title: token82.CallerShadowedCallee.Module1.Library1.CallerShadowedCallee.Module1.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 83
      text: "\n\t"
      title: token83.CallerShadowedCallee.Module1.Library1.CallerShadowedCallee.Module1.Library1
      type: 183
    - *id010
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 85
      text: (
      title: token85.CallerShadowedCallee.Module1.Library1.CallerShadowedCallee.Module1.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 86
      text: )
      title: token86.CallerShadowedCallee.Module1.Library1.CallerShadowedCallee.Module1.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 87
      text: '

        '
      title: token87.CallerShadowedCallee.Module1.Library1.CallerShadowedCallee.Module1.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 88
      text: End Sub
      title: token88.CallerShadowedCallee.Module1.Library1.CallerShadowedCallee.Module1.Library1
      type: 44
    used_by: []
    uses:
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: ShadowedCallee.Module1.Library1
      object_type: basicfunction
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Library1
    module: Module1
    name: ShadowedCallee
    name_token_index: 93
    obj_id: '381'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      object_type: module
    strings:
    - &id011 !!python/object:odbinfo.pure.datatype.base.Token
      index: 99
      text: '"Library1.Module1.ShadowedCallee"'
      title: token99.ShadowedCallee.Module1.Library1.ShadowedCallee.Module1.Library1
      type: 172
    title: ShadowedCallee.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 91
      text: Sub
      title: token91.ShadowedCallee.Module1.Library1.ShadowedCallee.Module1.Library1
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 92
      text: ' '
      title: token92.ShadowedCallee.Module1.Library1.ShadowedCallee.Module1.Library1
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 93
      text: ShadowedCallee
      title: token93.ShadowedCallee.Module1.Library1.ShadowedCallee.Module1.Library1
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 94
      text: (
      title: token94.ShadowedCallee.Module1.Library1.ShadowedCallee.Module1.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 95
      text: )
      title: token95.ShadowedCallee.Module1.Library1.ShadowedCallee.Module1.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 96
      text: "\n\t"
      title: token96.ShadowedCallee.Module1.Library1.ShadowedCallee.Module1.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 97
      text: print
      title: token97.ShadowedCallee.Module1.Library1.ShadowedCallee.Module1.Library1
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 98
      text: ' '
      title: token98.ShadowedCallee.Module1.Library1.ShadowedCallee.Module1.Library1
      type: 185
    - *id011
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 100
      text: '

        '
      title: token100.ShadowedCallee.Module1.Library1.ShadowedCallee.Module1.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 101
      text: End Sub
      title: token101.ShadowedCallee.Module1.Library1.ShadowedCallee.Module1.Library1
      type: 44
    used_by:
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      bookmark: null
      local_id: CallerShadowedCallee.Module1.Library1
      location_id: '513'
      object_type: basicfunction
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Library1
    module: Module1
    name: ReferToTable
    name_token_index: 106
    obj_id: '393'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      object_type: module
    strings:
    - &id012 !!python/object:odbinfo.pure.datatype.base.Token
      index: 112
      link: &id021 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        local_id: Plant
        object_type: table
      obj_id: '541'
      text: '"Plant"'
      title: token112.ReferToTable.Module1.Library1.ReferToTable.Module1.Library1
      type: 172
    title: ReferToTable.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 104
      text: Sub
      title: token104.ReferToTable.Module1.Library1.ReferToTable.Module1.Library1
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 105
      text: ' '
      title: token105.ReferToTable.Module1.Library1.ReferToTable.Module1.Library1
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 106
      text: ReferToTable
      title: token106.ReferToTable.Module1.Library1.ReferToTable.Module1.Library1
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 107
      text: (
      title: token107.ReferToTable.Module1.Library1.ReferToTable.Module1.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 108
      text: )
      title: token108.ReferToTable.Module1.Library1.ReferToTable.Module1.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 109
      text: "\n\t"
      title: token109.ReferToTable.Module1.Library1.ReferToTable.Module1.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 110
      text: print
      title: token110.ReferToTable.Module1.Library1.ReferToTable.Module1.Library1
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 111
      text: ' '
      title: token111.ReferToTable.Module1.Library1.ReferToTable.Module1.Library1
      type: 185
    - *id012
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 113
      text: '

        '
      title: token113.ReferToTable.Module1.Library1.ReferToTable.Module1.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 114
      text: End Sub
      title: token114.ReferToTable.Module1.Library1.ReferToTable.Module1.Library1
      type: 44
    used_by: []
    uses:
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Plant
      object_type: table
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Library1
    module: Module1
    name: ReferToView
    name_token_index: 119
    obj_id: '405'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      object_type: module
    strings:
    - &id013 !!python/object:odbinfo.pure.datatype.base.Token
      index: 125
      link: &id022 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        local_id: view1
        object_type: view
      obj_id: '554'
      text: '"view1"'
      title: token125.ReferToView.Module1.Library1.ReferToView.Module1.Library1
      type: 172
    title: ReferToView.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 117
      text: Sub
      title: token117.ReferToView.Module1.Library1.ReferToView.Module1.Library1
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 118
      text: ' '
      title: token118.ReferToView.Module1.Library1.ReferToView.Module1.Library1
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 119
      text: ReferToView
      title: token119.ReferToView.Module1.Library1.ReferToView.Module1.Library1
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 120
      text: (
      title: token120.ReferToView.Module1.Library1.ReferToView.Module1.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 121
      text: )
      title: token121.ReferToView.Module1.Library1.ReferToView.Module1.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 122
      text: "\n\t"
      title: token122.ReferToView.Module1.Library1.ReferToView.Module1.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 123
      text: print
      title: token123.ReferToView.Module1.Library1.ReferToView.Module1.Library1
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 124
      text: ' '
      title: token124.ReferToView.Module1.Library1.ReferToView.Module1.Library1
      type: 185
    - *id013
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 126
      text: '

        '
      title: token126.ReferToView.Module1.Library1.ReferToView.Module1.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 127
      text: End Sub
      title: token127.ReferToView.Module1.Library1.ReferToView.Module1.Library1
      type: 44
    used_by: []
    uses:
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: view1
      object_type: view
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Library1
    module: Module1
    name: ReferToQuery
    name_token_index: 132
    obj_id: '417'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module1.Library1
      object_type: module
    strings:
    - &id014 !!python/object:odbinfo.pure.datatype.base.Token
      index: 138
      link: &id023 !!python/object:odbinfo.pure.datatype.base.Identifier
        bookmark: null
        local_id: FamilyLookup
        object_type: query
      obj_id: '567'
      text: '"FamilyLookup"'
      title: token138.ReferToQuery.Module1.Library1.ReferToQuery.Module1.Library1
      type: 172
    title: ReferToQuery.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 130
      text: Sub
      title: token130.ReferToQuery.Module1.Library1.ReferToQuery.Module1.Library1
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 131
      text: ' '
      title: token131.ReferToQuery.Module1.Library1.ReferToQuery.Module1.Library1
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 132
      text: ReferToQuery
      title: token132.ReferToQuery.Module1.Library1.ReferToQuery.Module1.Library1
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 133
      text: (
      title: token133.ReferToQuery.Module1.Library1.ReferToQuery.Module1.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 134
      text: )
      title: token134.ReferToQuery.Module1.Library1.ReferToQuery.Module1.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 135
      text: "\n\t"
      title: token135.ReferToQuery.Module1.Library1.ReferToQuery.Module1.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 136
      text: print
      title: token136.ReferToQuery.Module1.Library1.ReferToQuery.Module1.Library1
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 137
      text: ' '
      title: token137.ReferToQuery.Module1.Library1.ReferToQuery.Module1.Library1
      type: 185
    - *id014
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 139
      text: '

        '
      title: token139.ReferToQuery.Module1.Library1.ReferToQuery.Module1.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 140
      text: End Sub
      title: token140.ReferToQuery.Module1.Library1.ReferToQuery.Module1.Library1
      type: 44
    used_by: []
    uses:
    - !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: FamilyLookup
      object_type: query
  library: Library1
  name: Module1
  name_indexes:
  - 5
  - 16
  - 35
  - 48
  - 61
  - 80
  - 93
  - 106
  - 119
  - 132
  obj_id: '298'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Library1
    object_type: library
  source: "REM  *****  BASIC  *****\n\nSub Main\n\tError \"Mijn fout\"\nEnd Sub\n\n\
    Sub CallerSub()\n\tCalleeSub()\n\tModule2.CalleeSub()\nEnd Sub\n\nSub CalleeSub()\n\
    \tprint \"Module1.CalleeSub\"\nEnd Sub\n\nsub CallerTwo()\n\tCalleeTwoSub()\n\
    End Sub\n\nSub CallerOtherLib()\n\tCalleeOtherLib()\n\tModule1.CalleeOtherLib()\n\
    End Sub\n\nSub CallerShadowedCallee()\n\tShadowedCallee()\nEnd Sub\n\nSub ShadowedCallee()\n\
    \tprint \"Library1.Module1.ShadowedCallee\"\nEnd Sub\n\nSub ReferToTable()\n\t\
    print \"Plant\"\nEnd Sub\n\nSub ReferToView()\n\tprint \"view1\"\nEnd Sub\n\n\
    Sub ReferToQuery()\n\tprint \"FamilyLookup\"\nEnd Sub"
  title: Module1.Library1
  tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 0
    link: null
    text: REM  *****  BASIC  *****
    title: token0
    type: 184
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 1
    link: null
    text: '

      '
    title: token1
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 2
    link: null
    text: '

      '
    title: token2
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 3
    link: null
    text: Sub
    title: token3
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 4
    link: null
    text: ' '
    title: token4
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 5
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Main.Module1.Library1
      object_type: basicfunction
    text: Main
    title: token5
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 6
    link: null
    text: "\n\t"
    title: token6
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 7
    link: null
    text: Error
    title: token7
    type: 49
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 8
    link: null
    text: ' '
    title: token8
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 9
    link: null
    text: '"Mijn fout"'
    title: token9
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 10
    link: null
    text: '

      '
    title: token10
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 11
    link: null
    text: End Sub
    title: token11
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 12
    link: null
    text: '

      '
    title: token12
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 13
    link: null
    text: '

      '
    title: token13
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 14
    link: null
    text: Sub
    title: token14
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 15
    link: null
    text: ' '
    title: token15
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 16
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CallerSub.Module1.Library1
      object_type: basicfunction
    text: CallerSub
    title: token16
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 17
    link: null
    text: (
    title: token17
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 18
    link: null
    text: )
    title: token18
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 19
    link: null
    text: "\n\t"
    title: token19
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 20
    link: *id015
    text: CalleeSub
    title: token20
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 21
    link: null
    text: (
    title: token21
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 22
    link: null
    text: )
    title: token22
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 23
    link: null
    text: "\n\t"
    title: token23
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 24
    link: null
    text: Module2
    title: token24
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 25
    link: null
    text: .
    title: token25
    type: 150
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 26
    link: *id016
    text: CalleeSub
    title: token26
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 27
    link: null
    text: (
    title: token27
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 28
    link: null
    text: )
    title: token28
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 29
    link: null
    text: '

      '
    title: token29
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 30
    link: null
    text: End Sub
    title: token30
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 31
    link: null
    text: '

      '
    title: token31
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 32
    link: null
    text: '

      '
    title: token32
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 33
    link: null
    text: Sub
    title: token33
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 34
    link: null
    text: ' '
    title: token34
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 35
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeSub.Module1.Library1
      object_type: basicfunction
    text: CalleeSub
    title: token35
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 36
    link: null
    text: (
    title: token36
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 37
    link: null
    text: )
    title: token37
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 38
    link: null
    text: "\n\t"
    title: token38
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 39
    link: null
    text: print
    title: token39
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 40
    link: null
    text: ' '
    title: token40
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 41
    link: null
    text: '"Module1.CalleeSub"'
    title: token41
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 42
    link: null
    text: '

      '
    title: token42
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 43
    link: null
    text: End Sub
    title: token43
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 44
    link: null
    text: '

      '
    title: token44
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 45
    link: null
    text: '

      '
    title: token45
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 46
    link: null
    text: sub
    title: token46
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 47
    link: null
    text: ' '
    title: token47
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 48
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CallerTwo.Module1.Library1
      object_type: basicfunction
    text: CallerTwo
    title: token48
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 49
    link: null
    text: (
    title: token49
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 50
    link: null
    text: )
    title: token50
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 51
    link: null
    text: "\n\t"
    title: token51
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 52
    link: *id017
    text: CalleeTwoSub
    title: token52
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 53
    link: null
    text: (
    title: token53
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 54
    link: null
    text: )
    title: token54
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 55
    link: null
    text: '

      '
    title: token55
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 56
    link: null
    text: End Sub
    title: token56
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 57
    link: null
    text: '

      '
    title: token57
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 58
    link: null
    text: '

      '
    title: token58
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 59
    link: null
    text: Sub
    title: token59
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 60
    link: null
    text: ' '
    title: token60
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 61
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CallerOtherLib.Module1.Library1
      object_type: basicfunction
    text: CallerOtherLib
    title: token61
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 62
    link: null
    text: (
    title: token62
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 63
    link: null
    text: )
    title: token63
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 64
    link: null
    text: "\n\t"
    title: token64
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 65
    link: *id018
    text: CalleeOtherLib
    title: token65
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 66
    link: null
    text: (
    title: token66
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 67
    link: null
    text: )
    title: token67
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 68
    link: null
    text: "\n\t"
    title: token68
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 69
    link: null
    text: Module1
    title: token69
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 70
    link: null
    text: .
    title: token70
    type: 150
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 71
    link: *id019
    text: CalleeOtherLib
    title: token71
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 72
    link: null
    text: (
    title: token72
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 73
    link: null
    text: )
    title: token73
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 74
    link: null
    text: '

      '
    title: token74
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 75
    link: null
    text: End Sub
    title: token75
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 76
    link: null
    text: '

      '
    title: token76
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 77
    link: null
    text: '

      '
    title: token77
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 78
    link: null
    text: Sub
    title: token78
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 79
    link: null
    text: ' '
    title: token79
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 80
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CallerShadowedCallee.Module1.Library1
      object_type: basicfunction
    text: CallerShadowedCallee
    title: token80
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 81
    link: null
    text: (
    title: token81
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 82
    link: null
    text: )
    title: token82
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 83
    link: null
    text: "\n\t"
    title: token83
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 84
    link: *id020
    text: ShadowedCallee
    title: token84
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 85
    link: null
    text: (
    title: token85
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 86
    link: null
    text: )
    title: token86
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 87
    link: null
    text: '

      '
    title: token87
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 88
    link: null
    text: End Sub
    title: token88
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 89
    link: null
    text: '

      '
    title: token89
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 90
    link: null
    text: '

      '
    title: token90
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 91
    link: null
    text: Sub
    title: token91
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 92
    link: null
    text: ' '
    title: token92
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 93
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: ShadowedCallee.Module1.Library1
      object_type: basicfunction
    text: ShadowedCallee
    title: token93
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 94
    link: null
    text: (
    title: token94
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 95
    link: null
    text: )
    title: token95
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 96
    link: null
    text: "\n\t"
    title: token96
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 97
    link: null
    text: print
    title: token97
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 98
    link: null
    text: ' '
    title: token98
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 99
    link: null
    text: '"Library1.Module1.ShadowedCallee"'
    title: token99
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 100
    link: null
    text: '

      '
    title: token100
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 101
    link: null
    text: End Sub
    title: token101
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 102
    link: null
    text: '

      '
    title: token102
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 103
    link: null
    text: '

      '
    title: token103
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 104
    link: null
    text: Sub
    title: token104
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 105
    link: null
    text: ' '
    title: token105
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 106
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: ReferToTable.Module1.Library1
      object_type: basicfunction
    text: ReferToTable
    title: token106
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 107
    link: null
    text: (
    title: token107
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 108
    link: null
    text: )
    title: token108
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 109
    link: null
    text: "\n\t"
    title: token109
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 110
    link: null
    text: print
    title: token110
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 111
    link: null
    text: ' '
    title: token111
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 112
    link: *id021
    text: '"Plant"'
    title: token112
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 113
    link: null
    text: '

      '
    title: token113
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 114
    link: null
    text: End Sub
    title: token114
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 115
    link: null
    text: '

      '
    title: token115
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 116
    link: null
    text: '

      '
    title: token116
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 117
    link: null
    text: Sub
    title: token117
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 118
    link: null
    text: ' '
    title: token118
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 119
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: ReferToView.Module1.Library1
      object_type: basicfunction
    text: ReferToView
    title: token119
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 120
    link: null
    text: (
    title: token120
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 121
    link: null
    text: )
    title: token121
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 122
    link: null
    text: "\n\t"
    title: token122
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 123
    link: null
    text: print
    title: token123
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 124
    link: null
    text: ' '
    title: token124
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 125
    link: *id022
    text: '"view1"'
    title: token125
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 126
    link: null
    text: '

      '
    title: token126
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 127
    link: null
    text: End Sub
    title: token127
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 128
    link: null
    text: '

      '
    title: token128
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 129
    link: null
    text: '

      '
    title: token129
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 130
    link: null
    text: Sub
    title: token130
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 131
    link: null
    text: ' '
    title: token131
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 132
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: ReferToQuery.Module1.Library1
      object_type: basicfunction
    text: ReferToQuery
    title: token132
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 133
    link: null
    text: (
    title: token133
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 134
    link: null
    text: )
    title: token134
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 135
    link: null
    text: "\n\t"
    title: token135
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 136
    link: null
    text: print
    title: token136
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 137
    link: null
    text: ' '
    title: token137
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 138
    link: *id023
    text: '"FamilyLookup"'
    title: token138
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 139
    link: null
    text: '

      '
    title: token139
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 140
    link: null
    text: End Sub
    title: token140
    type: 44
  used_by: []
  uses: []
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Library1
    module: Module2
    name: CalleeSub
    name_token_index: 5
    obj_id: '571'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module2.Library1
      object_type: module
    strings:
    - &id024 !!python/object:odbinfo.pure.datatype.base.Token
      index: 11
      text: '"Module2.CalleeSub"'
      title: token11.CalleeSub.Module2.Library1.CalleeSub.Module2.Library1
      type: 172
    title: CalleeSub.Module2.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 3
      text: Sub
      title: token3.CalleeSub.Module2.Library1.CalleeSub.Module2.Library1
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 4
      text: ' '
      title: token4.CalleeSub.Module2.Library1.CalleeSub.Module2.Library1
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 5
      text: CalleeSub
      title: token5.CalleeSub.Module2.Library1.CalleeSub.Module2.Library1
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 6
      text: (
      title: token6.CalleeSub.Module2.Library1.CalleeSub.Module2.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 7
      text: )
      title: token7.CalleeSub.Module2.Library1.CalleeSub.Module2.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 8
      text: "\n\t"
      title: token8.CalleeSub.Module2.Library1.CalleeSub.Module2.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 9
      text: print
      title: token9.CalleeSub.Module2.Library1.CalleeSub.Module2.Library1
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 10
      text: ' '
      title: token10.CalleeSub.Module2.Library1.CalleeSub.Module2.Library1
      type: 185
    - *id024
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 12
      text: '

        '
      title: token12.CalleeSub.Module2.Library1.CalleeSub.Module2.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 13
      text: End Sub
      title: token13.CalleeSub.Module2.Library1.CalleeSub.Module2.Library1
      type: 44
    used_by:
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      bookmark: null
      local_id: CallerSub.Module1.Library1
      location_id: '455'
      object_type: basicfunction
    uses: []
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens: []
    calls: []
    library: Library1
    module: Module2
    name: CalleeTwoSub
    name_token_index: 18
    obj_id: '583'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: Module2.Library1
      object_type: module
    strings:
    - &id025 !!python/object:odbinfo.pure.datatype.base.Token
      index: 24
      text: '"Module2.CalleeTwoSub"'
      title: token24.CalleeTwoSub.Module2.Library1.CalleeTwoSub.Module2.Library1
      type: 172
    title: CalleeTwoSub.Module2.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 16
      text: Sub
      title: token16.CalleeTwoSub.Module2.Library1.CalleeTwoSub.Module2.Library1
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 17
      text: ' '
      title: token17.CalleeTwoSub.Module2.Library1.CalleeTwoSub.Module2.Library1
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 18
      text: CalleeTwoSub
      title: token18.CalleeTwoSub.Module2.Library1.CalleeTwoSub.Module2.Library1
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 19
      text: (
      title: token19.CalleeTwoSub.Module2.Library1.CalleeTwoSub.Module2.Library1
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 20
      text: )
      title: token20.CalleeTwoSub.Module2.Library1.CalleeTwoSub.Module2.Library1
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 21
      text: "\n\t"
      title: token21.CalleeTwoSub.Module2.Library1.CalleeTwoSub.Module2.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 22
      text: print
      title: token22.CalleeTwoSub.Module2.Library1.CalleeTwoSub.Module2.Library1
      type: 100
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 23
      text: ' '
      title: token23.CalleeTwoSub.Module2.Library1.CalleeTwoSub.Module2.Library1
      type: 185
    - *id025
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 25
      text: '

        '
      title: token25.CalleeTwoSub.Module2.Library1.CalleeTwoSub.Module2.Library1
      type: 183
    - !!python/object:odbinfo.pure.datatype.base.Token
      index: 26
      text: End Sub
      title: token26.CalleeTwoSub.Module2.Library1.CalleeTwoSub.Module2.Library1
      type: 44
    used_by:
    - !!python/object:odbinfo.pure.datatype.base.SourceIdentifier
      bookmark: null
      local_id: CallerTwo.Module1.Library1
      location_id: '481'
      object_type: basicfunction
    uses: []
  library: Library1
  name: Module2
  name_indexes:
  - 5
  - 18
  obj_id: '570'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    bookmark: null
    local_id: Library1
    object_type: library
  source: "REM  *****  BASIC  *****\n\nSub CalleeSub()\n\tprint \"Module2.CalleeSub\"\
    \nEnd Sub\n\nSub CalleeTwoSub()\n\tprint \"Module2.CalleeTwoSub\"\nEnd Sub"
  title: Module2.Library1
  tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 0
    link: null
    text: REM  *****  BASIC  *****
    title: token0
    type: 184
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 1
    link: null
    text: '

      '
    title: token1
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 2
    link: null
    text: '

      '
    title: token2
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 3
    link: null
    text: Sub
    title: token3
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 4
    link: null
    text: ' '
    title: token4
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 5
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeSub.Module2.Library1
      object_type: basicfunction
    text: CalleeSub
    title: token5
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 6
    link: null
    text: (
    title: token6
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 7
    link: null
    text: )
    title: token7
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 8
    link: null
    text: "\n\t"
    title: token8
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 9
    link: null
    text: print
    title: token9
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 10
    link: null
    text: ' '
    title: token10
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 11
    link: null
    text: '"Module2.CalleeSub"'
    title: token11
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 12
    link: null
    text: '

      '
    title: token12
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 13
    link: null
    text: End Sub
    title: token13
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 14
    link: null
    text: '

      '
    title: token14
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 15
    link: null
    text: '

      '
    title: token15
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 16
    link: null
    text: Sub
    title: token16
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 17
    link: null
    text: ' '
    title: token17
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 18
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: null
      local_id: CalleeTwoSub.Module2.Library1
      object_type: basicfunction
    text: CalleeTwoSub
    title: token18
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 19
    link: null
    text: (
    title: token19
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 20
    link: null
    text: )
    title: token20
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 21
    link: null
    text: "\n\t"
    title: token21
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 22
    link: null
    text: print
    title: token22
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 23
    link: null
    text: ' '
    title: token23
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 24
    link: null
    text: '"Module2.CalleeTwoSub"'
    title: token24
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 25
    link: null
    text: '

      '
    title: token25
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    index: 26
    link: null
    text: End Sub
    title: token26
    type: 44
  used_by: []
  uses: []
name: Library1
obj_id: '297'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  bookmark: null
  local_id: ./testdb.odb
  object_type: metadata
title: Library1
used_by: []
uses: []
---
