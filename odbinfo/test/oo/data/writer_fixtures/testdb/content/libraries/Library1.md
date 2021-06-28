---
!!python/object:odbinfo.pure.datatype.exec.Library
modules:
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id002 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 7
      obj_id: '386'
      text: Error
      type: 49
    - &id003 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 8
      obj_id: '387'
      text: ' '
      type: 185
    - &id001 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 9
      obj_id: '388'
      text: '"Mijn fout"'
      type: 172
    - &id004 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 10
      obj_id: '389'
      text: '

        '
      type: 183
    calls: []
    library: Library1
    module: Module1
    name: Main
    name_token_index: 5
    obj_id: '249'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings:
    - *id001
    title: Main.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 3
      obj_id: '382'
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 4
      obj_id: '383'
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 5
      obj_id: '384'
      text: Main
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 6
      obj_id: '385'
      text: "\n\t"
      type: 183
    - *id002
    - *id003
    - *id001
    - *id004
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 11
      obj_id: '390'
      text: End Sub
      type: 44
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id005 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 20
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: CalleeSub.Module1.Library1
        object_type: basicfunctions
      obj_id: '399'
      text: CalleeSub
      type: 181
    - &id008 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 21
      obj_id: '400'
      text: (
      type: 157
    - &id009 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 22
      obj_id: '401'
      text: )
      type: 168
    - &id010 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 23
      obj_id: '402'
      text: "\n\t"
      type: 183
    - &id006 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 24
      obj_id: '403'
      text: Module2
      type: 181
    - &id011 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 25
      obj_id: '404'
      text: .
      type: 150
    - &id007 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 26
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: CalleeSub.Module2.Library1
        object_type: basicfunctions
      obj_id: '405'
      text: CalleeSub
      type: 181
    - &id012 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 27
      obj_id: '406'
      text: (
      type: 157
    - &id013 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 28
      obj_id: '407'
      text: )
      type: 168
    - &id014 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 29
      obj_id: '408'
      text: '

        '
      type: 183
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: *id005
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: *id006
      name_token: *id007
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
      hidden: false
      index: 14
      obj_id: '393'
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 15
      obj_id: '394'
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 16
      obj_id: '395'
      text: CallerSub
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 17
      obj_id: '396'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 18
      obj_id: '397'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 19
      obj_id: '398'
      text: "\n\t"
      type: 183
    - *id005
    - *id008
    - *id009
    - *id010
    - *id006
    - *id011
    - *id007
    - *id012
    - *id013
    - *id014
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 30
      obj_id: '409'
      text: End Sub
      type: 44
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id016 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 39
      obj_id: '418'
      text: print
      type: 100
    - &id017 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 40
      obj_id: '419'
      text: ' '
      type: 185
    - &id015 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 41
      obj_id: '420'
      text: '"Module1.CalleeSub"'
      type: 172
    - &id018 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 42
      obj_id: '421'
      text: '

        '
      type: 183
    calls: []
    library: Library1
    module: Module1
    name: CalleeSub
    name_token_index: 35
    obj_id: '277'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings:
    - *id015
    title: CalleeSub.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 33
      obj_id: '412'
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 34
      obj_id: '413'
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 35
      obj_id: '414'
      text: CalleeSub
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 36
      obj_id: '415'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 37
      obj_id: '416'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 38
      obj_id: '417'
      text: "\n\t"
      type: 183
    - *id016
    - *id017
    - *id015
    - *id018
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 43
      obj_id: '422'
      text: End Sub
      type: 44
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id019 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 52
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: CalleeTwoSub.Module2.Library1
        object_type: basicfunctions
      obj_id: '431'
      text: CalleeTwoSub
      type: 181
    - &id020 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 53
      obj_id: '432'
      text: (
      type: 157
    - &id021 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 54
      obj_id: '433'
      text: )
      type: 168
    - &id022 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 55
      obj_id: '434'
      text: '

        '
      type: 183
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: *id019
    library: Library1
    module: Module1
    name: CallerTwo
    name_token_index: 48
    obj_id: '289'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings: []
    title: CallerTwo.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 46
      obj_id: '425'
      text: sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 47
      obj_id: '426'
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 48
      obj_id: '427'
      text: CallerTwo
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 49
      obj_id: '428'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 50
      obj_id: '429'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 51
      obj_id: '430'
      text: "\n\t"
      type: 183
    - *id019
    - *id020
    - *id021
    - *id022
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 56
      obj_id: '435'
      text: End Sub
      type: 44
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id023 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 65
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: CalleeOtherLib.Module1.Standard
        object_type: basicfunctions
      obj_id: '444'
      text: CalleeOtherLib
      type: 181
    - &id026 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 66
      obj_id: '445'
      text: (
      type: 157
    - &id027 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 67
      obj_id: '446'
      text: )
      type: 168
    - &id028 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 68
      obj_id: '447'
      text: "\n\t"
      type: 183
    - &id024 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 69
      obj_id: '448'
      text: Module1
      type: 181
    - &id029 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 70
      obj_id: '449'
      text: .
      type: 150
    - &id025 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 71
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: CalleeOtherLib.Module1.Standard
        object_type: basicfunctions
      obj_id: '450'
      text: CalleeOtherLib
      type: 181
    - &id030 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 72
      obj_id: '451'
      text: (
      type: 157
    - &id031 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 73
      obj_id: '452'
      text: )
      type: 168
    - &id032 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 74
      obj_id: '453'
      text: '

        '
      type: 183
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: *id023
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: *id024
      name_token: *id025
    library: Library1
    module: Module1
    name: CallerOtherLib
    name_token_index: 61
    obj_id: '301'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings: []
    title: CallerOtherLib.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 59
      obj_id: '438'
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 60
      obj_id: '439'
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 61
      obj_id: '440'
      text: CallerOtherLib
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 62
      obj_id: '441'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 63
      obj_id: '442'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 64
      obj_id: '443'
      text: "\n\t"
      type: 183
    - *id023
    - *id026
    - *id027
    - *id028
    - *id024
    - *id029
    - *id025
    - *id030
    - *id031
    - *id032
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 75
      obj_id: '454'
      text: End Sub
      type: 44
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id033 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 84
      link: !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: ShadowedCallee.Module1.Library1
        object_type: basicfunctions
      obj_id: '463'
      text: ShadowedCallee
      type: 181
    - &id034 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 85
      obj_id: '464'
      text: (
      type: 157
    - &id035 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 86
      obj_id: '465'
      text: )
      type: 168
    - &id036 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 87
      obj_id: '466'
      text: '

        '
      type: 183
    calls:
    - !!python/object:odbinfo.pure.datatype.exec.BasicCall
      module_token: null
      name_token: *id033
    library: Library1
    module: Module1
    name: CallerShadowedCallee
    name_token_index: 80
    obj_id: '319'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings: []
    title: CallerShadowedCallee.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 78
      obj_id: '457'
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 79
      obj_id: '458'
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 80
      obj_id: '459'
      text: CallerShadowedCallee
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 81
      obj_id: '460'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 82
      obj_id: '461'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 83
      obj_id: '462'
      text: "\n\t"
      type: 183
    - *id033
    - *id034
    - *id035
    - *id036
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 88
      obj_id: '467'
      text: End Sub
      type: 44
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id038 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 97
      obj_id: '476'
      text: print
      type: 100
    - &id039 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 98
      obj_id: '477'
      text: ' '
      type: 185
    - &id037 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 99
      obj_id: '478'
      text: '"Library1.Module1.ShadowedCallee"'
      type: 172
    - &id040 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 100
      obj_id: '479'
      text: '

        '
      type: 183
    calls: []
    library: Library1
    module: Module1
    name: ShadowedCallee
    name_token_index: 93
    obj_id: '331'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings:
    - *id037
    title: ShadowedCallee.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 91
      obj_id: '470'
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 92
      obj_id: '471'
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 93
      obj_id: '472'
      text: ShadowedCallee
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 94
      obj_id: '473'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 95
      obj_id: '474'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 96
      obj_id: '475'
      text: "\n\t"
      type: 183
    - *id038
    - *id039
    - *id037
    - *id040
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 101
      obj_id: '480'
      text: End Sub
      type: 44
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id042 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 110
      obj_id: '489'
      text: print
      type: 100
    - &id043 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 111
      obj_id: '490'
      text: ' '
      type: 185
    - &id041 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 112
      link: &id053 !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: Plant
        object_type: tables
      obj_id: '491'
      text: '"Plant"'
      type: 172
    - &id044 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 113
      obj_id: '492'
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
      object_type: modules
    strings:
    - *id041
    title: ReferToTable.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 104
      obj_id: '483'
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 105
      obj_id: '484'
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 106
      obj_id: '485'
      text: ReferToTable
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 107
      obj_id: '486'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 108
      obj_id: '487'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 109
      obj_id: '488'
      text: "\n\t"
      type: 183
    - *id042
    - *id043
    - *id041
    - *id044
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 114
      obj_id: '493'
      text: End Sub
      type: 44
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id046 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 123
      obj_id: '502'
      text: print
      type: 100
    - &id047 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 124
      obj_id: '503'
      text: ' '
      type: 185
    - &id045 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 125
      link: &id054 !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: view1
        object_type: views
      obj_id: '504'
      text: '"view1"'
      type: 172
    - &id048 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 126
      obj_id: '505'
      text: '

        '
      type: 183
    calls: []
    library: Library1
    module: Module1
    name: ReferToView
    name_token_index: 119
    obj_id: '355'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module1.Library1
      object_type: modules
    strings:
    - *id045
    title: ReferToView.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 117
      obj_id: '496'
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 118
      obj_id: '497'
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 119
      obj_id: '498'
      text: ReferToView
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 120
      obj_id: '499'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 121
      obj_id: '500'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 122
      obj_id: '501'
      text: "\n\t"
      type: 183
    - *id046
    - *id047
    - *id045
    - *id048
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 127
      obj_id: '506'
      text: End Sub
      type: 44
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id050 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 136
      obj_id: '515'
      text: print
      type: 100
    - &id051 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 137
      obj_id: '516'
      text: ' '
      type: 185
    - &id049 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 138
      link: &id055 !!python/object:odbinfo.pure.datatype.base.Identifier
        local_id: FamilyLookup
        object_type: queries
      obj_id: '517'
      text: '"FamilyLookup"'
      type: 172
    - &id052 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 139
      obj_id: '518'
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
    - *id049
    title: ReferToQuery.Module1.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 130
      obj_id: '509'
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 131
      obj_id: '510'
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 132
      obj_id: '511'
      text: ReferToQuery
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 133
      obj_id: '512'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 134
      obj_id: '513'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 135
      obj_id: '514'
      text: "\n\t"
      type: 183
    - *id050
    - *id051
    - *id049
    - *id052
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 140
      obj_id: '519'
      text: End Sub
      type: 44
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
  obj_id: '248'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: Library1
    object_type: libraries
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
    hidden: true
    index: 0
    link: null
    text: REM  *****  BASIC  *****
    type: 184
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 1
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 2
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 3
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 4
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 5
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Main.Module1.Library1
      object_type: basicfunctions
    text: Main
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 6
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 7
    link: null
    text: Error
    type: 49
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 8
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 9
    link: null
    text: '"Mijn fout"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 10
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 11
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 12
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 13
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 14
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 15
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 16
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: CallerSub.Module1.Library1
      object_type: basicfunctions
    text: CallerSub
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 17
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 18
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 19
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 20
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: CalleeSub
      local_id: Module1.Library1
      object_type: modules
    text: CalleeSub
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 21
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 22
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 23
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 24
    link: null
    text: Module2
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 25
    link: null
    text: .
    type: 150
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 26
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: CalleeSub
      local_id: Module2.Library1
      object_type: modules
    text: CalleeSub
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 27
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 28
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 29
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 30
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 31
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 32
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 33
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 34
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 35
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: CalleeSub.Module1.Library1
      object_type: basicfunctions
    text: CalleeSub
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 36
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 37
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 38
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 39
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 40
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 41
    link: null
    text: '"Module1.CalleeSub"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 42
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 43
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 44
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 45
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 46
    link: null
    text: sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 47
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 48
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: CallerTwo.Module1.Library1
      object_type: basicfunctions
    text: CallerTwo
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 49
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 50
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 51
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 52
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: CalleeTwoSub
      local_id: Module2.Library1
      object_type: modules
    text: CalleeTwoSub
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 53
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 54
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 55
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 56
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 57
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 58
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 59
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 60
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 61
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: CallerOtherLib.Module1.Library1
      object_type: basicfunctions
    text: CallerOtherLib
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 62
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 63
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 64
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 65
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: CalleeOtherLib
      local_id: Module1.Standard
      object_type: modules
    text: CalleeOtherLib
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 66
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 67
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 68
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 69
    link: null
    text: Module1
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 70
    link: null
    text: .
    type: 150
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 71
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: CalleeOtherLib
      local_id: Module1.Standard
      object_type: modules
    text: CalleeOtherLib
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 72
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 73
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 74
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 75
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 76
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 77
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 78
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 79
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 80
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: CallerShadowedCallee.Module1.Library1
      object_type: basicfunctions
    text: CallerShadowedCallee
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 81
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 82
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 83
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 84
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      bookmark: ShadowedCallee
      local_id: Module1.Library1
      object_type: modules
    text: ShadowedCallee
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 85
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 86
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 87
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 88
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 89
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 90
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 91
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 92
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 93
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: ShadowedCallee.Module1.Library1
      object_type: basicfunctions
    text: ShadowedCallee
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 94
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 95
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 96
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 97
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 98
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 99
    link: null
    text: '"Library1.Module1.ShadowedCallee"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 100
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 101
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 102
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 103
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 104
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 105
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 106
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: ReferToTable.Module1.Library1
      object_type: basicfunctions
    text: ReferToTable
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 107
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 108
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 109
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 110
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 111
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 112
    link: *id053
    text: '"Plant"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 113
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 114
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 115
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 116
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 117
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 118
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 119
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: ReferToView.Module1.Library1
      object_type: basicfunctions
    text: ReferToView
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 120
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 121
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 122
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 123
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 124
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 125
    link: *id054
    text: '"view1"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 126
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 127
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 128
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 129
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 130
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 131
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 132
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: ReferToQuery.Module1.Library1
      object_type: basicfunctions
    text: ReferToQuery
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 133
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 134
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 135
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 136
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 137
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 138
    link: *id055
    text: '"FamilyLookup"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 139
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 140
    link: null
    text: End Sub
    type: 44
- !!python/object:odbinfo.pure.datatype.exec.Module
  callables:
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id057 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 9
      obj_id: '554'
      text: print
      type: 100
    - &id058 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 10
      obj_id: '555'
      text: ' '
      type: 185
    - &id056 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 11
      obj_id: '556'
      text: '"Module2.CalleeSub"'
      type: 172
    - &id059 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 12
      obj_id: '557'
      text: '

        '
      type: 183
    calls: []
    library: Library1
    module: Module2
    name: CalleeSub
    name_token_index: 5
    obj_id: '521'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module2.Library1
      object_type: modules
    strings:
    - *id056
    title: CalleeSub.Module2.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 3
      obj_id: '548'
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 4
      obj_id: '549'
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 5
      obj_id: '550'
      text: CalleeSub
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 6
      obj_id: '551'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 7
      obj_id: '552'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 8
      obj_id: '553'
      text: "\n\t"
      type: 183
    - *id057
    - *id058
    - *id056
    - *id059
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 13
      obj_id: '558'
      text: End Sub
      type: 44
  - !!python/object:odbinfo.pure.datatype.exec.BasicFunction
    body_tokens:
    - &id061 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 22
      obj_id: '567'
      text: print
      type: 100
    - &id062 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 23
      obj_id: '568'
      text: ' '
      type: 185
    - &id060 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 24
      obj_id: '569'
      text: '"Module2.CalleeTwoSub"'
      type: 172
    - &id063 !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 25
      obj_id: '570'
      text: '

        '
      type: 183
    calls: []
    library: Library1
    module: Module2
    name: CalleeTwoSub
    name_token_index: 18
    obj_id: '533'
    parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: Module2.Library1
      object_type: modules
    strings:
    - *id060
    title: CalleeTwoSub.Module2.Library1
    tokens:
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 16
      obj_id: '561'
      text: Sub
      type: 125
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 17
      obj_id: '562'
      text: ' '
      type: 185
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 18
      obj_id: '563'
      text: CalleeTwoSub
      type: 181
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 19
      obj_id: '564'
      text: (
      type: 157
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 20
      obj_id: '565'
      text: )
      type: 168
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 21
      obj_id: '566'
      text: "\n\t"
      type: 183
    - *id061
    - *id062
    - *id060
    - *id063
    - !!python/object:odbinfo.pure.datatype.base.Token
      hidden: false
      index: 26
      obj_id: '571'
      text: End Sub
      type: 44
  library: Library1
  name: Module2
  name_indexes:
  - 5
  - 18
  obj_id: '520'
  parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
    local_id: Library1
    object_type: libraries
  source: "REM  *****  BASIC  *****\n\nSub CalleeSub()\n\tprint \"Module2.CalleeSub\"\
    \nEnd Sub\n\nSub CalleeTwoSub()\n\tprint \"Module2.CalleeTwoSub\"\nEnd Sub"
  title: Module2.Library1
  tokens:
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: true
    index: 0
    link: null
    text: REM  *****  BASIC  *****
    type: 184
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 1
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 2
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 3
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 4
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 5
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: CalleeSub.Module2.Library1
      object_type: basicfunctions
    text: CalleeSub
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 6
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 7
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 8
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 9
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 10
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 11
    link: null
    text: '"Module2.CalleeSub"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 12
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 13
    link: null
    text: End Sub
    type: 44
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 14
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 15
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 16
    link: null
    text: Sub
    type: 125
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 17
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 18
    link: !!python/object:odbinfo.pure.datatype.base.Identifier
      local_id: CalleeTwoSub.Module2.Library1
      object_type: basicfunctions
    text: CalleeTwoSub
    type: 181
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 19
    link: null
    text: (
    type: 157
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 20
    link: null
    text: )
    type: 168
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 21
    link: null
    text: "\n\t"
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 22
    link: null
    text: print
    type: 100
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 23
    link: null
    text: ' '
    type: 185
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 24
    link: null
    text: '"Module2.CalleeTwoSub"'
    type: 172
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 25
    link: null
    text: '

      '
    type: 183
  - !!python/object:odbinfo.pure.datatype.base.Token
    hidden: false
    index: 26
    link: null
    text: End Sub
    type: 44
name: Library1
obj_id: '247'
parent_link: !!python/object:odbinfo.pure.datatype.base.Identifier
  local_id: ./testdb.odb
  object_type: metadatas
title: Library1
---
