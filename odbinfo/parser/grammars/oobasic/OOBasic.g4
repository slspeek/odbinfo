/*
* Copyright (C) 2017, Ulrich Wolffgang <ulrich.wolffgang@proleap.io>
* All rights reserved.
*
* This software may be modified and distributed under the terms
* of the MIT license. See the LICENSE file for details.
*/

/*
* Visual Basic 6.0 Grammar for ANTLR4
*
* This is a Visual Basic 6.0 grammar, which is part of the Visual Basic 6.0
* parser at https://github.com/uwol/proleap-vb6-parser.
*
* The grammar is derived from the Visual Basic 6.0 language reference
* http://msdn.microsoft.com/en-us/library/aa338033%28v=vs.60%29.aspx
* and has been tested with MSDN VB6 statements as well as several Visual
* Basic 6.0 code repositories.
*/

grammar OOBasic;

// module ----------------------------------

startRule
   : module EOF
   ;

module
   : WS? NEWLINE* (moduleHeader NEWLINE +)? moduleReferences? NEWLINE*  moduleConfig? NEWLINE* moduleOptions? NEWLINE* moduleBody? NEWLINE* WS?
   ;

moduleReferences
   : moduleReference+
   ;

moduleReference
   : OBJECT WS? EQ WS? moduleReferenceValue (SEMICOLON WS? moduleReferenceComponent)? NEWLINE*
   ;

moduleReferenceValue
   : STRINGLITERAL
   ;

moduleReferenceComponent
   : STRINGLITERAL
   ;

moduleHeader
   : VERSION WS DOUBLELITERAL (WS CLASS)?
   ;

moduleConfig
   : BEGIN NEWLINE + moduleConfigElement + END NEWLINE +
   ;

moduleConfigElement
   : ambiguousIdentifier WS? EQ WS? literal NEWLINE
   ;

moduleOptions
   : (moduleOption NEWLINE +) +
   ;

moduleOption
   : OPTION_BASE WS INTEGERLITERAL # optionBaseStmt
   | OPTION_COMPARE WS (BINARY | TEXT) # optionCompareStmt
   | OPTION_EXPLICIT # optionExplicitStmt
   | OPTION_PRIVATE_MODULE # optionPrivateModuleStmt
   | OPTION_COMPATIBLE # optionCompatible
   | OPTION_CLASSMODULE # optionClassModule
   ;

moduleBody
   : moduleBodyElement  (NEWLINE + moduleBodyElement )*
   ;

moduleBodyElement
   : moduleBlock
   | moduleOption
   | functionStmt
   | propertyGetStmt
   | propertySetStmt
   | propertyLetStmt
   | subStmt
   | typeStmt
   ;

// block ----------------------------------

moduleBlock
   : block
   ;


block
   : blockLine (NEWLINE + WS? blockLine)*
   ;

blockLine
   : blockStmt (WS? COLON WS? blockStmt)*
   ;

blockStmt
   : msgBox
   | beepStmt
   | chDirStmt
   | chDriveStmt
   | closeStmt
   | constStmt
   | dateStmt
   | deftypeStmt
   | doLoopStmt
   | endStmt
   | explicitCallStmt
   | errorStmt
   | exitStmt
   | filecopyStmt
   | forEachStmt
   | forNextStmt
   | goToStmt
   | ifThenElseStmt
   | inputStmt
   | letStmt
   | lineInputStmt
   | lineLabel
   | midStmt
   | mkdirStmt
   | nameStmt
   | onErrorStmt
   | onGoToStmt
   | openStmt
   | printStmt
   | putStmt
   | randomizeStmt
   | redimStmt
   | resetStmt
   | resumeStmt
   | rmdirStmt
   | selectCaseStmt
   | setStmt
   | stopStmt
   | timeStmt
   | variableStmt
   | whileWendStmt
   | widthStmt
   | withStmt
   | writeStmt
   | implicitCallStmt_InBlock
   ;

// statements ----------------------------------

beepStmt
   : BEEP
   ;

chDirStmt
   : CHDIR WS valueStmt
   ;

chDriveStmt
   : CHDRIVE WS valueStmt
   ;

closeStmt
   : CLOSE (WS valueStmt (WS? COMMA WS? valueStmt)*)?
   ;

constStmt
   : (publicPrivateGlobalVisibility WS)? CONST WS constSubStmt (WS? COMMA WS? constSubStmt)*
   ;

constSubStmt
   : ambiguousIdentifier typeHint? (WS asTypeClause)? WS? EQ WS? valueStmt
   ;

dateStmt
   : DATE WS? EQ WS? valueStmt
   ;

deftypeStmt
   : (DEFBOOL | DEFBYTE | DEFINT | DEFLNG | DEFCUR | DEFSNG | DEFDBL | DEFDEC | DEFDATE | DEFSTR | DEFOBJ | DEFVAR) WS letterrange (WS? COMMA WS? letterrange)*
   ;

doLoopStmt
   : DO NEWLINE + (block NEWLINE +)? LOOP
   | DO WS (WHILE | UNTIL) WS valueStmt NEWLINE + (block NEWLINE +)? LOOP
   | DO NEWLINE + (block NEWLINE +) LOOP WS (WHILE | UNTIL) WS valueStmt
   ;

endStmt
   : END
   ;

errorStmt
   : ERROR WS valueStmt
   ;

exitStmt
   : EXIT_DO
   | EXIT_FOR
   | EXIT_FUNCTION
   | EXIT_SUB
   ;

filecopyStmt
   : FILECOPY WS valueStmt WS? COMMA WS? valueStmt
   ;

forEachStmt
   : FOR WS EACH WS ambiguousIdentifier typeHint? WS IN WS valueStmt NEWLINE + (block NEWLINE +)? NEXT (WS ambiguousIdentifier)?
   ;

forNextStmt
   : FOR WS iCS_S_VariableOrProcedureCall typeHint? (WS asTypeClause)? WS? EQ WS? valueStmt WS TO WS valueStmt (WS STEP WS valueStmt)?  NEWLINE + (block NEWLINE +)? NEXT (WS ambiguousIdentifier typeHint?)?
   ;

functionStmt
   : (visibility WS)? (STATIC WS)? FUNCTION WS ambiguousIdentifier (WS? argList)? (WS asTypeClause)? NEWLINE + (block NEWLINE +)? END_FUNCTION
   ;


goToStmt
   : GOTO WS valueStmt
   ;

ifThenElseStmt
   : IF WS ifConditionStmt WS THEN WS blockStmt (WS ELSE WS blockStmt)? # inlineIfThenElse
   | ifBlockStmt ifElseIfBlockStmt* ifElseBlockStmt? END_IF # blockIfThenElse
   ;

ifBlockStmt
   : IF WS ifConditionStmt WS THEN WS?  NEWLINE + (block NEWLINE +)?
   ;

ifConditionStmt
   : valueStmt
   ;

ifElseIfBlockStmt
   : ELSEIF WS ifConditionStmt WS THEN WS?  NEWLINE + (block NEWLINE +)?
   ;

ifElseBlockStmt
   : ELSE WS?  NEWLINE + (block NEWLINE +)?
   ;

inputStmt
   : INPUT WS valueStmt (WS? COMMA WS? valueStmt) +
   ;

letStmt
   : (LET WS)? implicitCallStmt_InStmt WS? (ADDNUMERIC | EQ | PLUS_EQ | MINUS_EQ) WS? valueStmt
   ;

lineInputStmt
   : LINE_INPUT WS valueStmt WS? COMMA WS? valueStmt
   ;

midStmt
   : MID WS? LPAREN WS? argsCall WS? RPAREN
   ;

mkdirStmt
   : MKDIR WS valueStmt
   ;

nameStmt
   : NAME WS valueStmt WS AS WS valueStmt
   ;

onErrorStmt
   : (ON_ERROR | ON_LOCAL_ERROR) WS (GOTO WS valueStmt COLON? | RESUME WS NEXT)
   ;

onGoToStmt
   : ON WS valueStmt WS GOTO WS valueStmt (WS? COMMA WS? valueStmt)*
   ;

openStmt
  : OPEN WS valueStmt WS FOR WS (APPEND | BINARY | INPUT | OUTPUT | RANDOM) (WS ACCESS WS (READ | WRITE | READ_WRITE))? (WS (SHARED | LOCK_READ | LOCK_WRITE | LOCK_READ_WRITE))? WS AS WS valueStmt (WS LEN WS? EQ WS? valueStmt)?
  ;

outputList
   : outputList_Expression (WS? (SEMICOLON | COMMA) WS? outputList_Expression?)*
   | outputList_Expression? (WS? (SEMICOLON | COMMA) WS? outputList_Expression?) +
   ;

outputList_Expression
   : (SPC | TAB) (WS? LPAREN WS? argsCall WS? RPAREN)?
   | valueStmt
   ;

printStmt
   : PRINT WS valueStmt (WS? COMMA (WS? outputList)?)?
   | PRINT WS? LPAREN WS? valueStmt (WS? COMMA WS? outputList)? WS? RPAREN
   ;

propertyGetStmt
  : (visibility WS)? (STATIC WS)? PROPERTY_GET WS ambiguousIdentifier typeHint? (WS? argList)? (WS asTypeClause)? NEWLINE + (block NEWLINE +)? END_PROPERTY
  ;

propertySetStmt
  : (visibility WS)? (STATIC WS)? PROPERTY_SET WS ambiguousIdentifier (WS? argList)? NEWLINE + (block NEWLINE +)? END_PROPERTY
  ;

propertyLetStmt
  : (visibility WS)? (STATIC WS)? PROPERTY_LET WS ambiguousIdentifier (WS? argList)? NEWLINE + (block NEWLINE +)? END_PROPERTY
  ;

putStmt
   : PUT WS valueStmt WS? COMMA WS? valueStmt? WS? COMMA WS? valueStmt
   ;

randomizeStmt
   : RANDOMIZE (WS valueStmt)?
   ;

redimStmt
   : REDIM WS (PRESERVE WS)? redimSubStmt (WS? COMMA WS? redimSubStmt)*
   ;

redimSubStmt
   : implicitCallStmt_InStmt WS? LPAREN WS? subscripts WS? RPAREN (WS asTypeClause)?
   ;

resetStmt
   : RESET
   ;

resumeStmt
   : RESUME (WS (NEXT | ambiguousIdentifier))?
   ;

rmdirStmt
   : RMDIR WS valueStmt
   ;

selectCaseStmt
   : SELECT WS CASE WS valueStmt  NEWLINE + sC_Case* WS? END_SELECT
   ;

sC_Case
   : CASE WS sC_Cond WS? (COLON? NEWLINE* | NEWLINE +) (WS? block NEWLINE +)?
   | COMMENT NEWLINE+
   ;

// ELSE first, so that it is not interpreted as a variable call
sC_Cond
   : ELSE # caseCondElse
   | sC_CondExpr (WS? COMMA WS? sC_CondExpr)* #caseCondExpr
   ;

sC_CondExpr
   : valueStmt # caseCondExprValue
   | valueStmt WS TO WS valueStmt # caseCondExprTo
   ;

setStmt
   : SET WS implicitCallStmt_InStmt WS? EQ WS? valueStmt
   ;

stopStmt
   : STOP
   ;

subStmt
   : (visibility WS)? (STATIC WS)? SUB WS ambiguousIdentifier (WS? argList)? NEWLINE + (block NEWLINE +)? END_SUB
   ;

timeStmt
   : TIME WS? EQ WS? valueStmt
   ;

typeStmt
   : (visibility WS)? TYPE WS ambiguousIdentifier NEWLINE + (typeStmt_Element)* END_TYPE
   ;

typeStmt_Element
   : ambiguousIdentifier (WS? LPAREN (WS? subscripts)? WS? RPAREN)? (WS asTypeClause)? NEWLINE +
   ;


// operator precedence is represented by rule order
valueStmt
   : literal                                       # vsLiteral
   | LPAREN WS? valueStmt (WS? COMMA WS? valueStmt)* WS? RPAREN      # vsStruct
   | NEW WS valueStmt                                                # vsNew
   | implicitCallStmt_InStmt WS? ASSIGN WS? valueStmt                # vsAssign
   | valueStmt WS? POW WS? valueStmt                                 # vsPow
   | MINUS WS? valueStmt                                             # vsNegation
   | PLUS WS? valueStmt                                              # vsPlus
   | valueStmt WS? DIV WS? valueStmt                                 # vsDiv
   | valueStmt WS? MULT WS? valueStmt                                # vsMult
   | valueStmt WS? MOD WS? valueStmt                                 # vsMod
   | valueStmt WS? PLUS WS? valueStmt                                # vsAdd
   | valueStmt WS? MINUS WS? valueStmt                               # vsMinus
   | valueStmt WS? AMPERSAND WS? valueStmt   # vsAmp
   | valueStmt WS? EQ WS? valueStmt                                  # vsEq
   | valueStmt WS? NEQ WS? valueStmt                                 # vsNeq
   | valueStmt WS? LT WS? valueStmt                                  # vsLt
   | valueStmt WS? GT WS? valueStmt                                  # vsGt
   | valueStmt WS? LEQ WS? valueStmt                                 # vsLeq
   | valueStmt WS? GEQ WS? valueStmt                                 # vsGeq
   | NOT (WS valueStmt | LPAREN WS? valueStmt WS? RPAREN)            # vsNot
   | valueStmt WS? AND WS? valueStmt                                 # vsAnd
   | valueStmt WS? OR WS? valueStmt                                  # vsOr
   | valueStmt WS? XOR WS? valueStmt                                 # vsXor
   | valueStmt WS? EQV WS? valueStmt                                 # vsEqv
   | valueStmt WS? IMP WS? valueStmt                                 # vsImp
   | implicitCallStmt_InStmt                  # vsICS
   | midStmt                                                         # vsMid
   | msgBox                                                          # vsMsgBox
   ;

variableStmt
   : (DIM | STATIC | visibility) WS variableListStmt
   ;

variableListStmt
   : variableSubStmt (WS? COMMA WS? variableSubStmt)*
   ;

variableSubStmt
   : ambiguousIdentifier typeHint? (WS? LPAREN WS? (subscripts WS?)? RPAREN WS?)? (WS asTypeClause)?
   ;

whileWendStmt
   : WHILE WS valueStmt NEWLINE + block* NEWLINE* WEND
   ;

widthStmt
   : WIDTH WS valueStmt WS? COMMA WS? valueStmt
   ;

withStmt
   : WITH WS (NEW WS)? implicitCallStmt_InStmt NEWLINE + (block NEWLINE +)? END_WITH
   ;

writeStmt
   : WRITE WS valueStmt WS? COMMA (WS? outputList)?
   ;

// complex call statements ----------------------------------
explicitCallStmt
   : eCS_ProcedureCall
   | eCS_MemberProcedureCall
   ;

// parantheses are required in case of args -> empty parantheses are removed
eCS_ProcedureCall
   : CALL WS ambiguousIdentifier typeHint? (WS? LPAREN WS? (argsCall WS?)? RPAREN)?
   ;

// parantheses are required in case of args -> empty parantheses are removed
eCS_MemberProcedureCall
   : CALL WS implicitCallStmt_InStmt? DOT WS? ambiguousIdentifier typeHint? (WS? LPAREN WS? (argsCall WS?)? RPAREN)?
   ;

msgBox
   : MSGBOX WS? LPAREN WS? argsCall WS? RPAREN
   | MSGBOX WS argsCall
   ;

implicitCallStmt_InBlock
   : iCS_B_ProcedureCall
   | iCS_B_MemberProcedureCall
   ;

// certainIdentifier instead of ambiguousIdentifier for preventing ambiguity with statement keywords
iCS_B_ProcedureCall
   : certainIdentifier (WS? LPAREN WS? (argsCall WS?)? RPAREN)?
   | certainIdentifier WS? (argsCall WS?)?
   ;

iCS_B_MemberProcedureCall
   : implicitCallStmt_InStmt? DOT ambiguousIdentifier typeHint? (WS? LPAREN WS? (argsCall WS?)? RPAREN)?
   | implicitCallStmt_InStmt? DOT ambiguousIdentifier typeHint? WS? (argsCall WS?)?
   ;

// iCS_S_MembersCall first, so that member calls are not resolved as separate iCS_S_VariableOrProcedureCalls
implicitCallStmt_InStmt
   : iCS_S_MembersCall
   | iCS_S_VariableOrProcedureCall
   | iCS_S_ProcedureOrArrayCall
   ;

iCS_S_VariableOrProcedureCall
   : ambiguousIdentifier typeHint?
   ;

iCS_S_ProcedureOrArrayCall
   : ambiguousIdentifier helper_rule #icsAmbiguousIdentifier
   | baseType helper_rule            #icsBaseType
   | iCS_S_NestedProcedureCall helper_rule #icsNestedProcedureCall
   ;

helper_rule
    :  typeHint? WS? (LPAREN WS? (argsCall WS?)? RPAREN)+
    ;

iCS_S_NestedProcedureCall
	: ambiguousIdentifier typeHint? WS? LPAREN WS? (argsCall WS?)? RPAREN
	;


iCS_S_MembersCall
   : (iCS_S_VariableOrProcedureCall | iCS_S_ProcedureOrArrayCall)? iCS_S_MemberCall +
   ;

iCS_S_MemberCall
   : WS? DOT (iCS_S_VariableOrProcedureCall | iCS_S_ProcedureOrArrayCall)
   ;

// atomic call statements ----------------------------------

argsCall
   : (argCall? WS? (COMMA | SEMICOLON) WS?)* argCall (WS? (COMMA | SEMICOLON) WS? argCall?)*
   ;

argCall
   : ((BYVAL | BYREF ) WS)? valueStmt
   ;

// atomic rules for statements
argList
   : LPAREN (WS? arg  (WS? COMMA WS? arg WS? )*)? WS? RPAREN
   ;

arg
   : (OPTIONAL WS)? ((BYVAL | BYREF) WS)? (OPTIONAL WS)? ambiguousIdentifier typeHint? (WS? LPAREN WS? RPAREN)? (WS asTypeClause)? (WS? argDefaultValue)?
   ;

argDefaultValue
   : EQ WS? valueStmt
   ;

subscripts
   : subscript (WS? COMMA WS? subscript)*
   ;

subscript
   : (valueStmt WS TO WS)? valueStmt
   ;

// atomic rules ----------------------------------

ambiguousIdentifier
   : (IDENTIFIER | ambiguousKeyword) +
   | L_SQUARE_BRACKET (IDENTIFIER | ambiguousKeyword) + R_SQUARE_BRACKET
   ;

asTypeClause
   : AS WS (NEW WS)? otype (WS fieldLength)?
   ;

baseType
   : BOOLEAN
   | BYTE
   | DATE
   | DOUBLE
   | INTEGER
   | LONG
   | OBJECT
   | STRING
   | VARIANT
   ;

certainIdentifier
   : IDENTIFIER (ambiguousKeyword | IDENTIFIER)*
   | ambiguousKeyword (ambiguousKeyword | IDENTIFIER) +
   ;

comparisonOperator
   : LT
   | LEQ
   | GT
   | GEQ
   | EQ
   | NEQ
   ;

complexType
   : ambiguousIdentifier (DOT ambiguousIdentifier)*
   ;

fieldLength
   : MULT WS? (INTEGERLITERAL | ambiguousIdentifier)
   ;

letterrange
   : certainIdentifier (WS? MINUS WS? certainIdentifier)?
   ;

lineLabel
   : ambiguousIdentifier COLON
   ;

literal
   : COLORLITERAL
   | DATELITERAL
   | (PLUS | MINUS)? DOUBLELITERAL
   | FILENUMBER
   | (PLUS | MINUS)? INTEGERLITERAL
   | (PLUS | MINUS)? OCTALLITERAL
   | STRINGLITERAL
   | TRUE
   | FALSE
   | NOTHING
   | NULL
   ;

publicPrivateVisibility
	: PRIVATE
	| PUBLIC
	;

publicPrivateGlobalVisibility
	: PRIVATE
	| PUBLIC
	| GLOBAL
	;

otype
   : (baseType | complexType) (WS? LPAREN WS? RPAREN)?
   ;

typeHint
   : AMPERSAND
   | AT
   | DOLLAR
   | HASH
   | PERCENT
   ;

visibility
   : PRIVATE
   | PUBLIC
   | GLOBAL
   ;

// ambiguous keywords
ambiguousKeyword
   : ACCESS
   | ALIAS
   | AND
   | APPEND
   | AS
   | BEEP
   | BEGIN
   | BINARY
   | BOOLEAN
   | BYVAL
   | BYREF
   | BYTE
   | CALL
   | CASE
   | CLASS
   | CLOSE
   | CHDIR
   | CHDRIVE
   | CONST
   | DATE
   | DEFBOOL
   | DEFBYTE
   | DEFCUR
   | DEFDBL
   | DEFDATE
   | DEFDEC
   | DEFINT
   | DEFLNG
   | DEFOBJ
   | DEFSNG
   | DEFSTR
   | DEFVAR
   | DIM
   | DO
   | DOUBLE
   | EACH
   | ELSE
   | ELSEIF
   | END
   | EQV
   | ERROR
   | FALSE
   | FILECOPY
   | FOR
   | FUNCTION
   | GLOBAL
   | GOTO
   | IF
   | IMP
   | IN
   | INPUT
   | INTEGER
   | LONG
   | LOOP
   | LEN
   | LET
   | ME
   | MID
   | MKDIR
   | MOD
   | NAME
   | NEXT
   | NEW
   | NOT
   | NOTHING
   | NULL
   | OBJECT
   | ON
   | OPEN
   | OPTIONAL
   | OR
   | OUTPUT
   | PRESERVE
   | PRINT
   | PRIVATE
   | PUBLIC
   | PUT
   | RANDOM
   | RANDOMIZE
   | READ
   | REDIM
   | REM
   | RESET
   | RESUME
   | RMDIR
   | SELECT
   | SET
   | STATIC
   | STEP
   | STOP
   | STRING
   | SUB
   | TAB
   | TEXT
   | THEN
   | TIME
   | TO
   | TRUE
   | TYPE
   | TYPEOF
   | UNTIL
   | VARIANT
   | VERSION
   | WEND
   | WHILE
   | WIDTH
   | WITH
   | WRITE
   | XOR
   ;

// lexer rules --------------------------------------------------------------------------------

// keywords
ACCESS
   : A C C E S S
   ;


ADDNUMERIC
   : '_' A D D N U M E R I C LPAREN RPAREN EQ
   ;

APPEND
   : A P P E N D
   ;


ALIAS
   : A L I A S
   ;


AND
   : A N D
   ;


AS
   : A S
   ;


BEEP
   : B E E P
   ;


BEGIN
   : B E G I N
   ;


BINARY
   : B I N A R Y
   ;


BOOLEAN
   : B O O L E A N
   ;


BYVAL
   : B Y V A L
   ;


BYREF
   : B Y R E F
   ;


BYTE
   : B Y T E
   ;


CASE
   : C A S E
   ;


CHDIR
   : C H D I R
   ;


CHDRIVE
   : C H D R I V E
   ;


CALL
  : C A L L
  ;

CLASS
   : C L A S S
   ;


CLOSE
   : C L O S E
   ;


CONST
   : C O N S T
   ;


DATE
   : D A T E
   ;


DEFBOOL
   : D E F B O O L
   ;


DEFBYTE
   : D E F B Y T E
   ;


DEFDATE
   : D E F D A T E
   ;


DEFDBL
   : D E F D B L
   ;


DEFDEC
   : D E F D E C
   ;


DEFCUR
   : D E F C U R
   ;


DEFINT
   : D E F I N T
   ;


DEFLNG
   : D E F L N G
   ;


DEFOBJ
   : D E F O B J
   ;


DEFSNG
   : D E F S N G
   ;


DEFSTR
   : D E F S T R
   ;


DEFVAR
   : D E F V A R
   ;


DIM
   : D I M
   ;


DO
   : D O
   ;


DOUBLE
   : D O U B L E
   ;


EACH
   : E A C H
   ;


ELSE
   : E L S E
   ;


ELSEIF
   : E L S E I F
   ;


END_FUNCTION
   : E N D ' ' F U N C T I O N
   ;


END_IF
   : E N D ' ' I F
   ;


END_PROPERTY
  : E N D ' ' P R O P E R T Y
  ;



END_SELECT
   : E N D ' ' S E L E C T
   ;


END_SUB
   : E N D ' ' S U B
   ;


END_TYPE
   : E N D ' ' T Y P E
   ;


END_WITH
   : E N D ' ' W I T H
   ;


END
   : E N D
   ;


EQV
   : E Q V
   ;


ERROR
   : E R R O R
   ;


EXIT_DO
   : E X I T ' ' D O
   ;


EXIT_FOR
   : E X I T ' ' F O R
   ;


EXIT_FUNCTION
   : E X I T ' ' F U N C T I O N
   ;


EXIT_SUB
   : E X I T ' ' S U B
   ;


FALSE
   : F A L S E
   ;


FILECOPY
   : F I L E C O P Y
   ;


FOR
   : F O R
   ;


FUNCTION
   : F U N C T I O N
   ;


GLOBAL
   : G L O B A L
   ;


GOTO
   : G O T O
   ;


IF
   : I F
   ;


IMP
   : I M P
   ;


IN
   : I N
   ;


INPUT
   : I N P U T
   ;


INTEGER
   : I N T E G E R
   ;

LOCK
  : L O C K
  ;


LONG
   : L O N G
   ;


LOOP
   : L O O P
   ;


LEN
   : L E N
   ;


LET
   : L E T
   ;


LINE_INPUT
   : L I N E ' ' I N P U T
   ;

LOCK_READ
  : L O C K ' ' R E A D
  ;


LOCK_WRITE
  : L O C K ' ' W R I T E
  ;


LOCK_READ_WRITE
  : L O C K ' ' R E A D ' ' W R I T E
  ;


ME
   : M E
   ;


MSGBOX
   : M S G B O X
   ;

MID
   : M I D
   ;


MKDIR
   : M K D I R
   ;


MOD
   : M O D
   ;


NAME
   : N A M E
   ;


NEXT
   : N E X T
   ;


NEW
   : N E W
   ;


NOT
   : N O T
   ;


NOTHING
   : N O T H I N G
   ;


NULL
   : N U L L
   ;

OBJECT
   : O B J E C T
   ;

ON
   : O N
   ;


ON_ERROR
   : O N ' ' E R R O R
   ;


ON_LOCAL_ERROR
   : O N ' ' L O C A L ' ' E R R O R
   ;


OPEN
   : O P E N
   ;


OPTIONAL
   : O P T I O N A L
   ;


OPTION_BASE
   : O P T I O N ' ' B A S E
   ;


OPTION_EXPLICIT
   : O P T I O N ' ' E X P L I C I T
   ;


OPTION_COMPARE
   : O P T I O N ' ' C O M P A R E
   ;


OPTION_PRIVATE_MODULE
   : O P T I O N ' ' P R I V A T E ' ' M O D U L E
   ;

OPTION_COMPATIBLE
   : O P T I O N ' ' C O M P A T I B L E
   ;

OPTION_CLASSMODULE
   : O P T I O N ' ' C L A S S M O D U L E
   ;

OR
   : O R
   ;


OUTPUT
   : O U T P U T
   ;


PRESERVE
   : P R E S E R V E
   ;


PRINT
   : P R I N T
   ;


PRIVATE
   : P R I V A T E
   ;


PROPERTY_GET
  : P R O P E R T Y ' ' G E T
  ;


PROPERTY_LET
  : P R O P E R T Y ' ' L E T
  ;


PROPERTY_SET
  : P R O P E R T Y ' ' S E T
  ;


PUBLIC
   : P U B L I C
   ;


PUT
   : P U T
   ;


RANDOM
   : R A N D O M
   ;


RANDOMIZE
   : R A N D O M I Z E
   ;


READ
   : R E A D
   ;


READ_WRITE
   : R E A D ' ' W R I T E
   ;


REDIM
   : R E D I M
   ;


REM
   : R E M
   ;


RESET
   : R E S E T
   ;


RESUME
   : R E S U M E
   ;


RETURN
   : R E T U R N
   ;


RMDIR
   : R M D I R
   ;


SELECT
   : S E L E C T
   ;


SHARED
  : S H A R E D
  ;


SET
   : S E T
   ;



SPC
   : S P C
   ;


STATIC
   : S T A T I C
   ;


STEP
   : S T E P
   ;


STOP
   : S T O P
   ;


STRING
   : S T R I N G
   ;


SUB
   : S U B
   ;


TAB
   : T A B
   ;


TEXT
   : T E X T
   ;


THEN
   : T H E N
   ;


TIME
   : T I M E
   ;


TO
   : T O
   ;


TRUE
   : T R U E
   ;


TYPE
   : T Y P E
   ;


TYPEOF
   : T Y P E O F
   ;


UNTIL
   : U N T I L
   ;


VARIANT
   : V A R I A N T
   ;


VERSION
   : V E R S I O N
   ;


WEND
   : W E N D
   ;


WHILE
   : W H I L E
   ;


WIDTH
   : W I D T H
   ;


WITH
   : W I T H
   ;


WRITE
   : W R I T E
   ;


XOR
   : X O R
   ;

// symbols

AMPERSAND
   : '&'
   ;


ASSIGN
   : ':='
   ;


AT
   : '@'
   ;


COLON
   : ':'
   ;


COMMA
   : ','
   ;


DIV
   : '\\' | '/'
   ;


DOLLAR
   : '$'
   ;


DOT
   : '.'
   ;


EQ
   : '='
   ;


GEQ
   : '>='
   ;


GT
   : '>'
   ;


HASH
   : '#'
   ;


LEQ
   : '<='
   ;

LBRACE
	: '{'
	;


LPAREN
   : '('
   ;


LT
   : '<'
   ;


MINUS
   : '-'
   ;


MINUS_EQ
   : '-='
   ;


MULT
   : '*'
   ;


NEQ
   : '<>'
   ;


PERCENT
   : '%'
   ;


PLUS
   : '+'
   ;


PLUS_EQ
   : '+='
   ;


POW
   : '^'
   ;


RBRACE
	: '}'
	;


RPAREN
   : ')'
   ;


SEMICOLON
   : ';'
   ;


L_SQUARE_BRACKET
   : '['
   ;


R_SQUARE_BRACKET
   : ']'
   ;

// literals

STRINGLITERAL
   : '"' (~ ["\r\n] | '""')* '"'
   ;


DATELITERAL
   : HASH (~ [#\r\n])* HASH
   ;


COLORLITERAL
   : '&H' [0-9A-F] + AMPERSAND?
   ;


INTEGERLITERAL
   : ('0' .. '9') + (('e' | 'E') INTEGERLITERAL)* (HASH | AMPERSAND | AT)?
   ;


DOUBLELITERAL
   :  ('0' .. '9')* DOT ('0' .. '9') + (('e' | 'E') (PLUS | MINUS)? ('0' .. '9') +)* (HASH | AMPERSAND | AT)?
   ;


FILENUMBER
   : HASH LETTERORDIGIT +
   ;

OCTALLITERAL
   : '&O' [0-7] + AMPERSAND?
   ;

// misc
FRX_OFFSET
	: COLON [0-9A-F]+
	;

GUID
	: LBRACE [0-9A-F]+ MINUS [0-9A-F]+ MINUS [0-9A-F]+ MINUS [0-9A-F]+ MINUS [0-9A-F]+ RBRACE
	;

// identifier

IDENTIFIER
   : LETTER LETTERORDIGIT*
   ;

// whitespace, line breaks, comments, ...

LINE_CONTINUATION
   : ' ' '_' '\r'? '\n'  -> channel(HIDDEN)
   ;


NEWLINE
   : WS? ('\r'? '\n' | COLON ' ') WS?
   ;


COMMENT
   : WS? ('\'' | COLON? REM (' '|'\t')) (LINE_CONTINUATION | ~ ('\n' | '\r'))* -> channel(HIDDEN)
   ;


WS
   : [ \t] +
   ;

// letters

fragment LETTER
   : [a-zA-Z_äöüÄÖÜáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛàèìòùÀÈÌÒÙãẽĩõũÃẼĨÕŨçÇ]
   ;


fragment LETTERORDIGIT
   : [a-zA-Z0-9_äöüÄÖÜáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛàèìòùÀÈÌÒÙãẽĩõũÃẼĨÕŨçÇ]
   ;

// case insensitive chars

fragment A
   : ('a' | 'A')
   ;


fragment B
   : ('b' | 'B')
   ;


fragment C
   : ('c' | 'C')
   ;


fragment D
   : ('d' | 'D')
   ;


fragment E
   : ('e' | 'E')
   ;


fragment F
   : ('f' | 'F')
   ;


fragment G
   : ('g' | 'G')
   ;


fragment H
   : ('h' | 'H')
   ;


fragment I
   : ('i' | 'I')
   ;


fragment J
   : ('j' | 'J')
   ;


fragment K
   : ('k' | 'K')
   ;


fragment L
   : ('l' | 'L')
   ;


fragment M
   : ('m' | 'M')
   ;


fragment N
   : ('n' | 'N')
   ;


fragment O
   : ('o' | 'O')
   ;


fragment P
   : ('p' | 'P')
   ;


fragment Q
   : ('q' | 'Q')
   ;


fragment R
   : ('r' | 'R')
   ;


fragment S
   : ('s' | 'S')
   ;


fragment T
   : ('t' | 'T')
   ;


fragment U
   : ('u' | 'U')
   ;


fragment V
   : ('v' | 'V')
   ;


fragment W
   : ('w' | 'W')
   ;


fragment X
   : ('x' | 'X')
   ;


fragment Y
   : ('y' | 'Y')
   ;


fragment Z
   : ('z' | 'Z')
   ;
