" parser tests "
from odbinfo.parser.basic import parse


CODE = """
dim number1, number2 as integer
dim answer as integer

Myfunction("go for it")
console.writeline("enter first number")
number1=int(console.readline())
console.writeline("enter second number")
number2=int(console.readline())
total=number1+number2
console.writeline("the answer is "& answer)

"""

SOURCECODE="""
REM =======================================================================================================================
REM ===						The BaseDocumenter library is an extension to LibreOffice.									===
REM ===			Full documentation is available on http://www.access2base.com/basedocumenter.html						===
REM =======================================================================================================================

Option Explicit

REM -----------------------------------------------------------------------------------------------------------------------
REM ---		EXTERNAL ROUTINES CALLABLE FROM MENU ITEMS
REM -----------------------------------------------------------------------------------------------------------------------

REM -----------------------------------------------------------------------------------------------------------------------
Public Function BD_MENU_Help()
'	Open the help file from the Help menu item

Dim oShell As Object
Const cstHelpUrl = "http://www.access2base.com/basedocumenter"

	On Local Error Resume Next
	Set oShell = createUnoService("com.sun.star.system.SystemShellExecute")
	oShell.execute(cstHelpUrl, "" , com.sun.star.system.SystemShellExecuteFlags.DEFAULTS)
	Set oShell = Nothing

End Function	'	BD_MENU_Help

REM -----------------------------------------------------------------------------------------------------------------------
Public Function BD_MENU_CreateRepository() As Boolean
'	Create a new registered repository - Registered name = 'BaseDocumenter'

Dim sFileName As String, bSuccess As Boolean

	BD_Utils._BD_Initialize(True)	'	Force full reinit

	If MsgBox(_BD_GetLabel("CREATEREPO"), vbYesNo + vbQuestion, BaseDocumenterTitle) = vbNo Then Exit Function

	sFileName = _BD_FilePicker("", "SAVE", "odb", BaseDocumenterTitle & ".odb")
	If sFileName = "" Then Exit Function

	bSuccess = _BD_.CreateRepository(sFileName, True, bdDefaultRepository)

	If bSuccess Then MsgBox Replace(_BD_GetLabel("CREATEREPOOK"), "%0", sFileName), vbOKOnly + vbInformation, BaseDocumenterTitle

	BD_MENU_CreateRepository = bSuccess

Exit_Function:
	Exit Function
End Function	'	BD_MENU_CreateRepository

REM -----------------------------------------------------------------------------------------------------------------------
Public Function BD_MENU_OpenRepository() As Boolean
'	Open the repository linked to the registered name = BASEDOCUMENTER.
'	If not found, display a file picker

Dim sFileName As String, bSuccess As Boolean

	BD_Utils._BD_Initialize(True)	'	Force full reinit

	If _BD_.IsRegistered(bdDefaultRepository) Then
		bSuccess = _BD_.OpenRepository(bdDefaultRepository, "", "")
	Else
		sFileName = _BD_FilePicker("", "OPEN", "odb")
		If sFileName = "" Then Exit Function
		bSuccess = _BD_.OpenRepository(sFileName, "", "")
	End If

	If bSuccess Then MsgBox Replace(_BD_GetLabel("OPENREPOOK"), "%0", sFileName), vbOKOnly + vbInformation, BaseDocumenterTitle

	BD_MENU_OpenRepository = bSuccess

Exit_Function:
	Exit Function
End Function	'	BD_MENU_OpenRepository

REM -----------------------------------------------------------------------------------------------------------------------
Public Function BD_MENU_SetOptions() As Boolean
'	Open the settings dialog and update the default preferences

	BD_Utils._BD_Initialize()
	If Not BD_Utils._BD_IsRepoOpen() Then _BD_.Openrepository(bdDefaultRepository, "", "")		'	Implicit open of registered repository

	BD_MENU_SetOptions = BD_Settings._BD_SetOptions()

Exit_Function:
	Exit Function
End Function	'	BD_MENU_SetOptions

REM -----------------------------------------------------------------------------------------------------------------------
Public Function BD_MENU_DocumentThisDatabase() As Boolean
'	Scan and document the currently open Base document

	BD_Utils._BD_Initialize()

	If Not BD_Utils._BD_IsRepoOpen() Then _BD_.Openrepository(bdDefaultRepository, "", "")		'	Implicit open of registered repository
	If Not BD_Utils._BD_IsBaseDocument Then GoTo Error_NotBase

	'Start scan
	BD_MENU_DocumentThisDatabase = BD_Scan._BD_ScanThisDatabase(False)

Exit_Function:
	Exit Function
Error_NotBase:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRNOTBASEDOCUMENT))
End Function	'	BD_MENU_DocumentThisDatabase

REM -----------------------------------------------------------------------------------------------------------------------
REM ---		APPLICATION PROGRAMMATIC INTERFACE
REM -----------------------------------------------------------------------------------------------------------------------

REM -----------------------------------------------------------------------------------------------------------------------
Public Function BD_CreateRepository(ByVal pvFileName As Variant _
									, ByVal Optional pvRegister As Variant _
									, ByVal Optional pvRegisterName As Variant _
								) As Boolean

Const cstThisSub = "BD_CreateRepository"

	BD_Utils._BD_Initialize(True)	'	Force full reinit

	If IsMissing(pvRegister) Then pvRegister = True
	If Not _CheckArgument(pvFileName, 1, vbString, , False) Then GoTo ErrorArgument
	If Not _CheckArgument(pvRegister, 2, vbBoolean, , False) Then GoTo ErrorArgument
	If IsMissing(pvRegisterName) Then pvRegisterName = Iif(pvRegister, bdDefaultRepository, "")
	If Not _CheckArgument(pvRegisterName, 3, vbString, , False) Then GoTo ErrorArgument
	If pvRegister And Len(pvRegisterName) = 0 Then pvRegisterName = bdDefaultRepository

	If FileExists(ConvertToUrl(pvFileName)) Then GoTo Error_FileExists

	BD_CreateRepository = _BD_.CreateRepository(pvFileName, pvRegister, pvRegisterName)

Exit_Function:
	Exit Function
ErrorArgument:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRWRONGARGUMENT, cstThisSub))
Error_FileExists:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRFILEEXISTS, pvFileName))
End Function	'	BD_CreateRepository

REM -----------------------------------------------------------------------------------------------------------------------
Public Function BD_CloseRepository(ByVal Optional pvCompact As Variant) As Boolean

Const cstThisSub = "BD_CloseRepository"

	BD_Utils._BD_Initialize()

	If IsMissing(pvCompact) Then pvCompact = False
	If Not _CheckArgument(pvCompact, 1, vbBoolean, , False) Then GoTo ErrorArgument
	If Not BD_Utils._BD_IsRepoOpen() Then GoTo Error_RepoNotOpen

	BD_CloseRepository = _BD_.CloseRepository(pvCompact)

Exit_Function:
	Exit Function
ErrorArgument:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRWRONGARGUMENT, cstThisSub))
Error_RepoNotOpen:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRREPONOTOPEN, cstThisSub))
End Function	'	BD_CloseRepository

REM -----------------------------------------------------------------------------------------------------------------------
Public Function BD_OpenRepository(ByVal Optional pvRepository As Variant _
									, ByVal Optional pvUser As Variant _
									, ByVal Optional pvPassword As Variant _
									) As Boolean

Const cstThisSub = "BD_OpenRepository"

	BD_OpenRepository = False

	BD_Utils._BD_Initialize()

	If IsMissing(pvRepository) Then pvRepository = bdDefaultRepository
	If IsMissing(pvUser) Then pvUser = ""
	If IsMissing(pvPassword) Then pvPassword = ""
	If Not _CheckArgument(pvRepository, 1, vbString, , False) Then GoTo ErrorArgument
	If Not _CheckArgument(pvUser, 1, vbString, , False) Then GoTo ErrorArgument
	If Not _CheckArgument(pvPassword, 1, vbString, , False) Then GoTo ErrorArgument

	'Open the repository
	BD_OpenRepository = _BD_.OpenRepository(pvRepository, pvUser, pvPassword)

Exit_Function:
	Exit Function
ErrorArgument:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRWRONGARGUMENT, cstThisSub))
End Function	'	BD_OpenRepository

REM -----------------------------------------------------------------------------------------------------------------------
Public Function BD_SetOptions() As Boolean

Const cstThisSub = "BD_SetOptions"

	BD_Utils._BD_Initialize()
	If Not BD_Utils._BD_IsRepoOpen() Then GoTo Error_RepoNotOpen

	BD_SetOptions = BD_Settings._BD_SetOptions()

Exit_Function:
	Exit Function
Error_RepoNotOpen:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRREPONOTOPEN, cstThisSub))
End Function	'	BD_SetOptions

REM -----------------------------------------------------------------------------------------------------------------------
Public Function BD_ScanThisDatabase() As Boolean

Const cstThisSub = "BD_ScanThisDatabase"

	BD_Utils._BD_Initialize()

	If Not BD_Utils._BD_IsRepoOpen() Then GoTo Error_RepoNotOpen
	If Not BD_Utils._BD_IsBaseDocument() Then GoTo Error_NotBase

	'Start scan
	BD_ScanThisDatabase = BD_Scan._BD_ScanThisDatabase(True)

Exit_Function:
	Exit Function
ErrorArgument:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRWRONGARGUMENT, cstThisSub))
Error_RepoNotOpen:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRREPONOTOPEN, cstThisSub))
Error_NotBase:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRNOTBASEDOCUMENT, cstThisSub))
End Function	'	BD_ScanThisDatabase

REM -----------------------------------------------------------------------------------------------------------------------
Public Function BD_DocumentDatabase(ByVal Optional pvDatabaseName As Variant) As Boolean

Const cstThisSub = "BD_DocumentDatabase"

	BD_Utils._BD_Initialize()

	If IsMissing(pvDatabaseName) Then pvDatabaseName = ""
	If Not _CheckArgument(pvDatabaseName, 1, vbString, , False) Then GoTo ErrorArgument

	If Not BD_Utils._BD_IsRepoOpen() Then GoTo Error_RepoNotOpen

	'Start documentation
	BD_DocumentDatabase = BD_Html._BD_DocumentAllDatabases(pvDatabaseName)

Exit_Function:
	Exit Function
ErrorArgument:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRWRONGARGUMENT, cstThisSub))
Error_RepoNotOpen:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRREPONOTOPEN, cstThisSub))
End Function	'	BD_DocumentDatabase

REM -----------------------------------------------------------------------------------------------------------------------
Public Function BD_ScanAndDocThisDatabase() As Boolean

Const cstThisSub = "BD_ScanAndDocThisDatabase"

	BD_Utils._BD_Initialize()

	If Not BD_Utils._BD_IsRepoOpen() Then GoTo Error_RepoNotOpen
	If Not BD_Utils._BD_IsBaseDocument() Then GoTo Error_NotBase

	'Start scan
	BD_ScanAndDocThisDatabase = BD_Scan._BD_ScanThisDatabase(False)

Exit_Function:
	Exit Function
Error_RepoNotOpen:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRREPONOTOPEN, cstThisSub))
Error_NotBase:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRNOTBASEDOCUMENT, cstThisSub))
End Function	'	BD_ScanAndDocThisDatabase

REM -----------------------------------------------------------------------------------------------------------------------
Public Function BD_ForgetDatabase(ByVal Optional pvDatabaseName As Variant) As Boolean

Const cstThisSub = "BD_ForgetDatabase"

	BD_Utils._BD_Initialize()

	If Not _CheckArgument(pvDatabaseName, 1, vbString, , False) Then GoTo ErrorArgument
	If Not BD_Utils._BD_IsRepoOpen() Then GoTo Error_RepoNotOpen

	BD_ForgetDatabase = _BD_.ForgetDatabase(pvDatabaseName)

Exit_Function:
	Exit Function
ErrorArgument:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRWRONGARGUMENT, cstThisSub))
Error_RepoNotOpen:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRREPONOTOPEN, cstThisSub))
End Function	'	BD_ForgetDatabase

REM -----------------------------------------------------------------------------------------------------------------------
Public Function BD_WithUI(ByVal  Optional pbUI As Boolean) As Boolean

Const cstThisSub = "BD_WithUI"

	BD_Utils._BD_Initialize()

	If IsMissing(pbUI) Then pbUI = True
	If Not _CheckArgument(pbUI, 1, vbBoolean, , False) Then GoTo ErrorArgument

	BD_WithUI = _BD_.SetUI(pbUI)

Exit_Function:
	Exit Function
ErrorArgument:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRWRONGARGUMENT, cstThisSub))
End Function	'	BD_WithUI

REM -----------------------------------------------------------------------------------------------------------------------
REM ---		PRIVATE SUBs OR FUNCTIONs																					---
REM -----------------------------------------------------------------------------------------------------------------------

"""


def test_parse():
    " call parse "
    parse("")


def test_parse_select():
    " call parse select"
    tree = parse(CODE)
    # print(tree.toStringTree())


def test_parse_error():
    " call parse select"
    parse("REM Hi!")
    tree = parse(SOURCECODE)
    # print(tree.toStringTree())
