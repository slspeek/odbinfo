# pylint: disable=too-many-lines
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
"""



CLASSMODULE="""
REM =======================================================================================================================
REM ===						The BaseDocumenter library is an extension to LibreOffice.									===
REM ===			Full documentation is available on http://www.access2base.com/basedocumenter.html						===
REM =======================================================================================================================

Option Compatible
Option ClassModule

Option Explicit

REM -----------------------------------------------------------------------------------------------------------------------
REM --- CRUD ON OBJECTS RECORDS								        														---
REM -----------------------------------------------------------------------------------------------------------------------

REM -----------------------------------------------------------------------------------------------------------------------
REM --- CLASS ROOT FIELDS 								        														---
REM -----------------------------------------------------------------------------------------------------------------------

Const cstRECORD = "OBJECTS"

Private Const kType			= 0
Private Const kName			= 1
Private Const kShortName	= 2
Private Const kParentType	= 3
Private Const kParentIndex	= 4
Private Const kMissing		= 5
Private Const kUses			= 6
Private Const kUsedBy		= 7
Private Const kProperties	= 8

Private DatabaseID		As Long
Private Items()			As Variant		'	Items(i, j) <= (i+1)th field in (j)th row

'	For editing
Private EditMode		As Integer
Private EditedRow		As Long

'	Database fields
Private pType			As Long
Private pName			As String
Private pShortName		As String
Private pParentType		As Long
Private pParentIndex	As Long
Private pMissing		As Boolean
Private pUses			As String
Private pUsedBy			As String
Private pProperties		As Variant

REM -----------------------------------------------------------------------------------------------------------------------
REM --- CONSTRUCTORS / DESTRUCTORS						        														---
REM -----------------------------------------------------------------------------------------------------------------------
Private Sub Class_Initialize()

	DatabaseID = -1
	Items = Array()
	EditMode = dbEditNone
	EditedRow = -1
	_InitRow()

End Sub		'	Constructor

REM -----------------------------------------------------------------------------------------------------------------------
Private Sub Class_Terminate()
	Call Class_Initialize()
End Sub		'	Destructor

REM -----------------------------------------------------------------------------------------------------------------------
Public Sub Dispose()
	Call Class_Terminate()
End Sub		'	Explicit destructor

REM -----------------------------------------------------------------------------------------------------------------------
REM --- CLASS GET/LET/SET PROPERTIES					        														---
REM -----------------------------------------------------------------------------------------------------------------------

REM -----------------------------------------------------------------------------------------------------------------------
REM --- CLASS METHODS	 								        														---
REM -----------------------------------------------------------------------------------------------------------------------

REM -----------------------------------------------------------------------------------------------------------------------
Public Function AddNew() As Boolean
'	Create a new column in Items()

	If UBound(Items, 1) >= 0 Then EditedRow = UBound(Items, 2) + 1 Else EditedRow = 0
	_InitRow()
	Editmode = dbEditAdd
	Addnew = True

End Function	'	AddNew

REM -----------------------------------------------------------------------------------------------------------------------
Public Function Cancel() As Boolean
'	Cancel pending updates

	EditedRow = -1
	_InitRow()
	EditMode = dbEditNone
	Cancel = True

End Function	'	Cancel

REM -----------------------------------------------------------------------------------------------------------------------
Public Function CountMissings() As Long
'	Count missing items

Dim l As Long, lCount As Long

	lCount = 0
	For l = LBound(Items, 2) To UBound(Items, 2)
		If Items(kMissing, l) Then lCount = lCount + 1
	Next l

	CountMissings = lCount

End Function	'	CountType

REM -----------------------------------------------------------------------------------------------------------------------
Public Function CountType(ByVal piType As Integer) As Long
'	Count items having the given type

Dim l As Long, lCount As Long

	lCount = 0
	For l = LBound(Items, 2) To UBound(Items, 2)
		If Items(kType, l) = piType Then lCount = lCount + 1
	Next l

	CountType = lCount

End Function	'	CountType

REM -----------------------------------------------------------------------------------------------------------------------
Public Function Edit(ByVal plIndex As Long) As Boolean
'	Initializes the update of an existing row

	Edit = False
	If UBound(Items, 1) < 0 Then Exit Function
	If plIndex < LBound(Items, 2) Or plIndex > UBound(Items, 2) + 1 Then Exit Function
	'	Copy row to temporary variables
	EditedRow = plIndex - 1
	pType = Items(kType, EditedRow)
	pName = Items(kName, EditedRow)
	pShortName = Items(kShortName, EditedRow)
	pParentType = Items(kParentType, EditedRow)
	pParentIndex = Items(kParentIndex, EditedRow)
	pMissing = Items(kMissing, EditedRow)
	pUses = Items(kUses, EditedRow)
	pUsedBy = Items(kUsedBy, EditedRow)
	pProperties = Items(kProperties, EditedRow)

	EditMode = dbEditInProgress
	Edit = True

End Function	'	Edit

REM -----------------------------------------------------------------------------------------------------------------------
Public Function GetField(ByVal plIndex As Long, ByVal psField As String) As Variant
'	Get a field within the row designated with plIndex

Dim lIndex As Long

	GetField = Empty
	If UBound(Items, 1) < 0 Then Exit Function
	lIndex = plIndex - 1
	If lIndex < LBound(Items, 2) Or lIndex > UBound(Items, 2) Then Exit Function

	Select Case UCase(psField)
		Case "TYPE"			:		GetField = Items(kType, lIndex)
		Case "NAME"			:		GetField = Items(kName, lIndex)
		Case "SHORTNAME"	:		GetField = Items(kShortName, lIndex)
		Case "PARENTTYPE"	:		GetField = Items(kParentType, lIndex)
		Case "PARENTINDEX"	:		GetField = Items(kParentIndex, lIndex)
		Case "MISSING"		:		GetField = Items(kMissing, lIndex)
		Case "USES"			:		GetField = Items(kUses, lIndex)
		Case "USEDBY"		:		GetField = Items(kUsedBy, lIndex)
		Case Else
	End Select

End Function	'	GetField

REM -----------------------------------------------------------------------------------------------------------------------
Public Function GetHomonyms(ByVal plType As Long, ByVal psName As String) As Variant
'	Return an array of indexes referring to objects of the same type having the same name

Dim vIndexes As Variant, i As Long, bTest As Boolean
	vIndexes = Array()
	If UBound(Items, 1) >= 0 Then
		For i = LBound(Items, 2) To UBound(Items, 2)
			'	Tests split to avoid comparing (long) strings when useless
			bTest = ( Items(kType, i) = plType )
			If bTest Then bTest = ( UCase(Items(kName, i)) = UCase(psName) )
			If bTest Then
				ReDim Preserve vIndexes(0 To UBound(vIndexes) + 1)
				vIndexes(UBound(vIndexes)) = i + 1
			End If
		Next i
	End If

	GetHomonyms = vIndexes

End Function	'	GetHomonyms

REM -----------------------------------------------------------------------------------------------------------------------
Public Function GetIndex(ByVal plType As Long, ByVal psName As String, Optional ByVal plParentIndex As Long) As Long
'	Return index in Items of tuple (type,name)
'	Homonyms can exist (e.g. for field names) => Solved with parent index
'		If ParentIndex = 0	=>	No parent
'		If ParentIndex = -1	=>	Compare name with last component only (typically for dialogs)

Dim i As Long, bTest As Boolean
	GetIndex = 0
	If IsMissing(plParentIndex) Then plParentIndex = 0
	If UBound(Items, 1) < 0 Then Exit Function
	For i = LBound(Items, 2) To UBound(Items, 2)
		If plParentIndex = 0 Then	'	Tests split to avoid comparing (long) strings when useless
			bTest = ( Items(kType, i) = plType )
			If bTest Then bTest = ( UCase(Items(kName, i)) = UCase(psName) )
		ElseIf plParentIndex < 0 Then	'	Dialogs = scope.library.dialogname
			bTest = ( Items(kType, i) = plType )
			If bTest Then bTest = ( UCase(Items(kShortName, i)) = UCase(psName) )
		Else
			bTest = ( Items(kType, i) = plType And Items(kParentIndex, i) = plParentIndex )
			If bTest Then bTest = ( UCase(Items(kName, i)) = UCase(psName) )
		End If
		If bTest Then
			GetIndex = i + 1
			Exit For
		End If
	Next i

End Function	'	GetIndex

REM -----------------------------------------------------------------------------------------------------------------------
Public Function GetLastIndex() As Long

	GetLastIndex = UBound(Items, 2)

End Function	'	GetLastIndex

REM -----------------------------------------------------------------------------------------------------------------------
Public Function GetList(Optional ByVal psSql As String) As Variant
'	Return an array of the indexes matching a complete SQL statement or a SQL Where condition
'	The first field should be [INDEX]

Dim vIndexMatrix As Variant, vIndex As Variant, oRs As Object
Dim sSql As String, lSize As Long, i As Long

	GetList = Array()
	lSize = UBound(Items, 2)
	If lSize < 0 Then Exit Function
	If IsMissing(psSql) Then psSql = ""

	If psSql = "" Then		'	Used to build full index
		sSql = "SELECT [INDEX] FROM [OBJECTS] WHERE [DATABASEID]=" & DatabaseID & " ORDER BY UCASE([SHORTNAME])"
	ElseIf Left(psSql, 6) = "SELECT" Then
		'Argument should contain a full and correct SQL statement, including a token for the DatabaseID
		sSql = Replace(psSql, "%DB%", DatabaseID)
	Else
		sSql = "SELECT [INDEX] FROM [OBJECTS] WHERE [DATABASEID]=" & DatabaseID & " AND (" & psSql & ") ORDER BY UCASE([SHORTNAME])"
	End If
	Set oRs = _BD_.Repository.OpenRecordset(sSql, , dbSQLPassThrough, dbReadOnly)
	vIndexMatrix = oRs.GetRows(lSize + 1)		'	Potentially all rows of the OBJECTS table could be returned
	oRs.mClose

	vIndex = Array()
	If UBound(vIndexMatrix, 1) >= 0 Then
		lSize = UBound(vIndexMatrix, 2)
		ReDim vIndex(0 To lSize)
		For i = 0 To lSize
			vIndex(i) = vIndexMatrix(0, i)
		Next i
	End If

	GetList = vIndex
	Exit Function

End Function	'	GetList

REM -----------------------------------------------------------------------------------------------------------------------
Public Function GetParentIndex(ByVal plIndex As Long) As Long
'	Return the parent index of the child index

	GetparentIndex = Items(kParentIndex, plIndex - 1)

End Function

REM -----------------------------------------------------------------------------------------------------------------------
Public Function GetProperty(ByVal plIndex As Long, ByVal psName As String, ByVal Optional pvDefault As Variant) As Variant
'	Return the named property as extracted from Properties

Dim lIndex As Long

	On Local Error GoTo Error_Property

	GetProperty = Empty
	If UBound(Items, 1) < 0 Then Exit Function
	lIndex = plIndex - 1
	If lIndex < LBound(Items, 2) Or lIndex > UBound(Items, 2) Then Exit Function

	If IsMissing(pvDefault) Then pvdefault = Null

	If VarType(Items(kProperties, lIndex)) = vbString Then
		'Convert properties from string to propertyvalues. Fresh load has not converted them yet.
		Items(kProperties, lIndex) = _BD_StrToPropValues(Items(kProperties, lIndex))
	End If

	If Not IsArray(Items(kProperties, lIndex)) Then
		Getproperty = pvdefault
	ElseIf UBound(Items(kProperties, lIndex)) < 0 Then
		Getproperty = pvdefault
	Else
		GetProperty = UtilProperty._GetPropertyValue(Items(kProperties, lIndex), psName, pvDefault)
	End If

Exit_Function:
	Exit Function

Error_Property:
	GetProperty = Empty			'	To workaround A2B bug when property = "(0)"
	GoTo Exit_Function
End Function	'	GetProperty

REM -----------------------------------------------------------------------------------------------------------------------
Public Function Load(plDatabaseID As Long) As Boolean
'	Load whole Items() matrix from repository

Dim l As Long, lSize As Long, oRs As Object, sSql As String, sWhere As String, sProperty As String

	If _ErrorHandler() Then On Local Error GoTo Error_DBAccess

	Load = False
	If plDatabaseID <= 0 Then GoTo Exit_Function
	If plDatabaseID = DatabaseID Then		'	Do nothing if already loaded, e.g. when doc follows scan immediately
		Load = True
		Exit Function
	End If

	With _BD_.Repository
		'Load objects matrix
		sWhere = "DATABASEID=" & CStr(plDatabaseID)
		lSize = .DCount("INDEX", "OBJECTS", sWhere)
		If lSize > 0 Then
			sSql = "SELECT [TYPE], [NAME], [SHORTNAME], [PARENTTYPE], [PARENTINDEX]" _
					& ", [MISSING], [USES], [USEDBY], [PROPERTIES] " _
					& "FROM [OBJECTS] WHERE " & sWhere & " " _
					& "ORDER BY [INDEX]"
			Set oRs = .OpenRecordset(sSql, , dbSQLPassThrough, dbReadOnly)
			Items = oRs.GetRows(lSize)
			lSize = UBound(Items, 2)
			DatabaseID = plDatabaseID
		End If
	End With

	Load = True

Exit_Function:
	Exit Function
Error_DBAccess:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRREPOACCESS))
End Function	'	Load

REM -----------------------------------------------------------------------------------------------------------------------
Public Function SetField(ByVal psName As String, ByVal pvValue As Variant) As Boolean
'	Update a field within the row being updated

	SetField = False
	If EditMode = dbEditNone Then Exit Function

	Select Case UCase(psName)
		Case "TYPE"			:		pType = pvValue
		Case "NAME"			:		pName = pvValue
		Case "SHORTNAME"	:		pShortName = pvValue
		Case "PARENTTYPE"	:		pParentType = pvValue
		Case "PARENTINDEX"	:		pParentIndex = pvValue
		Case "MISSING"		:		pMissing = pvValue
		Case "USES"			:		pUses = _BD_AddToList(pUses, pvValue)
		Case "USEDBY"		:		pUsedBy = _BD_AddToList(pUsedBy, pvValue)
		Case Else
	End Select

	SetField = True

End Function	'	SetField

REM -----------------------------------------------------------------------------------------------------------------------
Public Function SetProperty(ByVal psName As String, ByVal pvValue As Variant) As Boolean
'	Add or replace the named property in pProperties

	SetProperty = False
	If EditMode = dbEditNone Then Exit Function
	UtilProperty._SetPropertyValue(pProperties, psName, pvValue)
	SetProperty = True

End Function	'	SetProperty

REM -----------------------------------------------------------------------------------------------------------------------
Public Function SetPropertyFunc(ByVal psName As String, ByVal pvValue As Variant, ByVal psFunction As String) As Boolean
'	Update a property by applying on its current value the given psFunction
'	Admitted functions are: ADD, CONCAT, MIN (lowest positive non-zero value) and MAX (highest ... )

Dim vNewValue As Variant, vOldValue As Variant

	SetPropertyFunc = False
	If EditMode = dbEditNone Then Exit Function
	vOldValue = UtilProperty._GetPropertyValue(pProperties, psName, Iif(IsNumeric(pvValue), 0, ""))

	Select Case psFunction
		Case "ADD"			:		vNewValue = vOldValue + pvValue
		Case "CONCAT"		:		If Len(vOldValue) > 0 Then vNewValue = vOldValue & vbLf() & pvValue Else vNewValue = pvValue
		Case "MIN"			:		If vOldValue > 0 And pvValue < vOldValue Then vNewValue = pvValue Else vNewValue = vOldValue
		Case "MAX"			:		If vOldValue > 0 And pvValue > vOldValue Then vNewValue = pvValue Else vNewValue = vOldValue
	End Select

	If vNewValue <> vOldValue Then UtilProperty._SetPropertyValue(pProperties, psName, vNewValue)
	SetPropertyFunc = True

End Function	'	SetPropertyFunc

REM -----------------------------------------------------------------------------------------------------------------------
Public Function SetPropertyItem(ByVal psName As String, ByVal pvValue As Variant) As Boolean
'	Add a new array item on top of the named property in pProperties

Dim vValue As Variant, lTop As Long

	SetPropertyItem = False
	If EditMode = dbEditNone Then Exit Function
	If IsArray(pvValue) Then Exit Function		'	Argument should be a number, a string, ...
	vValue = UtilProperty._GetPropertyValue(pProperties, psName, Null)
	If IsNull(vValue) Then
		vValue = Array(pvValue)
	Else
		lTop = UBound(vValue) + 1
		ReDim Preserve vValue(0 To lTop)
		vValue(lTop) = pvValue
	End If
	UtilProperty._SetPropertyValue(pProperties, psName, vValue)
	SetPropertyItem = True

End Function	'	SetPropertyItem

REM -----------------------------------------------------------------------------------------------------------------------
Public Function SetUseRelation(ByVal plUsingIndex As Long, ByVal plType As Long, ByVal psName As String _
						, Optional ByVal plParentType As Long, Optional ByVal psParentName As String _
						) As Long
'	Define a Uses/UsedBy relationship beween plUsingIndex item and (plType, psName) tuple
'	Parent is mandatory for sub-items (like fields, controls, ...)
'	If the used item does not exist, it is created with the MISSING field set to True
'	If its parent is also missing, it is also created with MISSING = True
'	The respective USES and USEDBY fields are updated
'
'	Returns the index of the used object

Dim lUsedIndex As Long, lParentIndex As Long, lUsingIndex As Long
Dim sIndex As String

	'Call between AddNew/Edit and Update is forbidden
	If EditMode <> dbEditNone Then Exit Function
	If plUsingIndex < 1 Or Len(psName) = 0 Then Exit Function

	If IsMissing(plParentType) Then
		lUsedIndex = GetIndex(plType, psName)
		If lUsedIndex = 0 Then lUsedIndex = _InitNewItem(plType, psName)
	Else
		lParentIndex = GetIndex(plParentType, psParentName)
		If lParentIndex = 0 Then lParentIndex = _InitNewItem(plParentType, psParentName)
		lUsedIndex = GetIndex(plType, psName, lParentIndex)
		If lUsedIndex = 0 Then lUsedIndex = _InitNewItem(plType, psName, lParentIndex)
	End If

	'	Store Used index in Using record
	sIndex = CStr(lUsedIndex)
	lUsingIndex = plUsingIndex - 1
	Items(kUses, lUsingIndex) = _BD_AddToList(Items(kUses, lUsingIndex), sIndex)

	'	Store Using index in Used record
	sIndex = CStr(plUsingIndex)
	lUsedIndex = lUsedIndex - 1
	Items(kUsedBy, lUsedIndex) = _BD_AddToList(Items(kUsedBy, lUsedIndex), sIndex)

	SetUseRelation = lUsedIndex + 1

End Function		'	SetUseRelation

REM -----------------------------------------------------------------------------------------------------------------------
Public Function Store() As Boolean
'	Store whole Items() matrix in repository

Dim sSql As String, lIndex As Long

	If _ErrorHandler() Then On Local Error GoTo Error_DBAccess

	Store = False
	If DatabaseID <= 0 Then GoTo Exit_Function
	If UBound(Items, 1) < 0 Then Exit Function

	'Store objects matrix
	'Building a SQL sentence is much more efficient (>25x) than using the insertRow method (via Access2Base AddNew/Update mechanisms)
	For lIndex = LBound(Items, 2) To UBound(Items, 2)
		sSql = "INSERT INTO OBJECTS ([DATABASEID],[INDEX],[TYPE],[NAME],[SHORTNAME],[PARENTTYPE],[PARENTINDEX],[MISSING],[USES],[USEDBY],[PROPERTIES])"
		sSql = sSql & " VALUES (" & DatabaseID _
					& "," & (lIndex + 1) _
					& "," & Items(kType, lIndex) _
					& "," & "'" & Replace(Items(kName, lIndex), "'", "''") & "'" _
					& "," & "'" & Replace(Items(kShortName, lIndex), "'", "''") & "'" _
					& "," & Items(kParentType, lIndex) _
					& "," & Items(kParentIndex, lIndex) _
					& "," & Iif(Items(kMissing, lIndex) = True, "TRUE", "FALSE") _
					& "," & "'" & Items(kUses, lIndex) & "'" _
					& "," & "'" & Items(kUsedBy, lIndex) & "'" _
					& "," & "'" & Replace(_BD_PropValuesToStr(Items(kProperties, lIndex)), "'", "''") & "'" _
					& ");"
		_BD_.Repository.RunSql(sSql, dbSQLPassThrough)
	Next lIndex

	Store = True

Exit_Function:
	Exit Function
Error_DBAccess:
	_BD_ForceExecutionStop(BD_Utils._BD_ErrorMessage(ERRREPOACCESS))
End Function	'	Store

REM -----------------------------------------------------------------------------------------------------------------------
Public Function Update() As Long
'	Finalize a pending update and return the updated row index

	'	Increase buffer if needed
	If EditMode = dbEditAdd Then
		If EditedRow = 0 Then
			ReDim Items(kType To kProperties, 0 To EditedRow)
		Else
			ReDim Preserve Items(kType To kProperties, 0 To EditedRow)
		End If
	End If

	'	Copy temporary variables to row
	Items(kType, EditedRow) = pType
	Items(kName, EditedRow) = pName
	Items(kShortName, EditedRow) = pShortName
	Items(kParentType, EditedRow) = pParentType
	Items(kParentIndex, EditedRow) = pParentIndex
	Items(kMissing, EditedRow) = pMissing
	Items(kUses, EditedRow) = pUses
	Items(kUsedBy, EditedRow) = pUsedBy
	Items(kProperties, EditedRow) = pProperties

	EditMode = dbEditNone
	Update = EditedRow + 1
	EditedRow = -1

End Function'	Update

REM -----------------------------------------------------------------------------------------------------------------------
REM ---		PRIVATE SUBs OR FUNCTIONs																					---
REM -----------------------------------------------------------------------------------------------------------------------

REM -----------------------------------------------------------------------------------------------------------------------
Private Function _InitNewItem(ByVal plType As Long, ByVal psName As String, Optional ByVal plParentIndex As Long) As Long
'	Initilizes new row directly in Items matrix
'	MISSING is set to True
'	When type = Module or Dialog, the Location and Library properties are initialized as well
'	Return the index of the newly created items row

Dim lNewRow As Long, vComponents As Variant

	If UBound(Items) < 0 Then	'	No items yet
		ReDim Items(kType To kProperties, 0 To 0)
	Else
		lNewRow = UBound(Items, 2) + 1
		ReDim Preserve Items(kType To kProperties, 0 To lNewRow)
	End If
	Items(kType, lNewRow) = plType
	Items(kName, lNewRow) = psName
	Items(kShortName, lNewRow) = _BD_Component(psName, "LAST")
	If IsMissing(plParentIndex) Then
		Items(kParentType, lNewRow) = 0
		Items(kParentIndex, lNewRow) = 0
	Else
		Items(kParentType, lNewRow) = Items(kType, plParentIndex - 1)
		Items(kParentIndex, lNewRow) = plParentIndex
	End If
	Items(kMissing, lNewRow) = True
	Items(kUses, lNewRow) = ""
	Items(kUsedBy, lNewRow) = ""
	Items(kProperties, lNewRow) = Array()

	'Initilialize modules and dialogs a bit further
	Select Case plType
		Case bdDialog, bdModule
			vComponents = Split(psName, ".")
			If UBound(vComponents) = 2 Then
				UtilProperty._SetPropertyValue(Items(kProperties, lNewRow), "Location", vComponents(0))
				UtilProperty._SetPropertyValue(Items(kProperties, lNewRow), "Library", vComponents(1))
			End If
		Case Else
	End Select

	_InitNewItem = lNewRow + 1

End Function	'	InitNewItem

REM -----------------------------------------------------------------------------------------------------------------------
Private Sub _InitRow()
'	Initilizes new row for update

	pType = 0
	pName = ""
	pShortName = ""
	pParentType = 0
	pParentIndex = 0
	pMissing = False
	pUses = ""
	pUsedBy = ""
	pProperties = Array()

End Sub
"""

def test_parse():
    " call parse "
    parse("")


def test_parse_module_statements():
    " call parse "
    parse(CODE)
    # print(tree.toStringTree())


def test_parse_base_documenter():
    " call parse select"
    parse(SOURCECODE)
    # print(tree.toStringTree())


def test_parse_base_documenter_object():
    " call parse select"
    parse(CLASSMODULE)


SELECT="""
Sub Foo ()
    Select case Fop(a)
        case 1: a = Foo(0)
        case else
    end select
end sub
"""


def test_parse_select():
    " call parse select"
    parse(SELECT)

GETFIELD="""
Public Function SetField(ByVal psName As String, ByVal pvValue As Variant) As Boolean
	Select Case UCase(psName)
		Case "TYPE"			:pType = pvValue
		Case "NAME"			:		pName = pvValue
		Case "SHORTNAME"	:		pShortName = pvValue
		Case "PARENTTYPE"	:		pParentType = pvValue
		Case "PARENTINDEX"	:		pParentIndex = pvValue
		Case "MISSING"		:		pMissing = pvValue
		Case "USES"			:		pUses = _BD_AddToList(pUses, pvValue)
		Case "USEDBY"		:		pUsedBy = _BD_AddToList(pUsedBy, pvValue)
		Case Else
	End Select

	SetField = True

End Function	'	SetField
"""

def test_parse_getfield():
    " call parse getfield"
    parse(GETFIELD)


def test_for_next():
    "for next loop parsing"
    parse("""
    sub foo()
        for i = 0 to 10
            Print(i)
        next i
    end sub
    """)
