r"""
This module has templates for some python object used in FreeCAD.

The content of this module is not generated.
If there are errors/inconsistency with FreeCAD,
please report at https://github.com/ostr00000/freecad-stubs/.

The ideal solution would use optional protocol,
but at the moment there is no such feature in Python:
https://www.python.org/dev/peps/pep-0544/#support-optional-protocol-members

Regex used for searching method for this module:
Find regex:
^\s*FC_PY_ELEMENT\((\w+)\)[^\S\n]*\\?
Replace:
    def $1(self):\n        \"\"\"May be implemented in python\"\"\"
"""

# pyright: reportGeneralTypeIssues=false, reportMissingModuleSource=false
from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    import FreeCAD
    import FreeCADGui

    try:
        from qtpy import PYSIDE2, PYSIDE6
    except ImportError:
        # `qtpy` is an optional dependency for this file
        # (to be able easy copy-paste)
        # See: https://github.com/ostr00000/freecad-stubs/issues/8
        PYSIDE2 = PYSIDE6 = False

    if PYSIDE2 or PYSIDE6:
        # This is a check for type checker (`pyright`). See:
        # https://github.com/spyder-ide/qtpy/issues/447
        # https://github.com/microsoft/pyright/blob/110efe8a3baa5657e380198ad126300a0018d983/docs/configuration.md?plain=1#L19

        from qtpy.QtCore import QObject
        from qtpy.QtGui import QIcon
        from qtpy.QtWidgets import QDialogButtonBox, QMenu
    else:
        from PySide.QtCore import QObject  # type: ignore[reportMissingImports]
        from PySide.QtGui import QIcon  # type: ignore[reportMissingImports]
        from PySide.QtWidgets import (  # type: ignore[reportMissingImports]
            QDialogButtonBox,
            QMenu,
        )


# FeaturePython.cpp
class _ProxyPythonGeneral:
    def attach(self, obj: FreeCAD.DocumentObject):
        """FreeCAD call this function if present"""

    def __getstate__(self):
        """FreeCAD call this function if present"""

    def __setstate__(self, value):
        """FreeCAD call this function if present"""

    def onBeforeChangeLabel(self, obj: FreeCAD.DocumentObject, newLabel: str) -> str:
        """FreeCAD call this function if present"""

    def getViewProviderName(self, obj: FreeCAD.DocumentObject) -> str:
        """FreeCAD call this function if present"""

    def getSubObject(
        self,
        obj: FreeCAD.DocumentObject,
        subName: str,
        num: typing.Literal[1, 2],
        matrix: FreeCAD.Matrix,
        transform: bool,
        depth: int,
    ) -> (
        tuple[FreeCAD.DocumentObject | None, FreeCAD.Matrix, typing.Any]
        | tuple[FreeCAD.DocumentObject | None, FreeCAD.Matrix]
        | None
    ):
        """FreeCAD call this function if present"""

    def getSubObjects(
        self, obj: FreeCAD.DocumentObject, reason: int
    ) -> typing.Sequence[str] | None:
        """FreeCAD call this function if present"""

    def getLinkedObject(
        self,
        obj: FreeCAD.DocumentObject,
        recurse: bool,
        matrix: FreeCAD.Matrix,
        transform: bool,
        depth: int,
    ) -> tuple[FreeCAD.DocumentObject | None, FreeCAD.Matrix] | None:
        """FreeCAD call this function if present"""

    def canLinkProperties(self, obj: FreeCAD.DocumentObject) -> bool:
        """FreeCAD call this function if present"""

    def allowDuplicateLabel(self, obj: FreeCAD.DocumentObject) -> bool:
        """FreeCAD call this function if present"""

    def redirectSubName(
        self,
        obj: FreeCAD.DocumentObject,
        ss: str,
        topParent: FreeCAD.DocumentObject | object,
        child: FreeCAD.DocumentObject | object,
    ) -> str | None:
        """FreeCAD call this function if present"""

    def canLoadPartial(self, obj: FreeCAD.DocumentObject) -> int:
        """FreeCAD call this function if present"""

    def hasChildElement(self, obj: FreeCAD.DocumentObject) -> bool:
        """FreeCAD call this function if present"""

    def isElementVisible(self, obj: FreeCAD.DocumentObject, element: str) -> int:
        """FreeCAD call this function if present"""

    def setElementVisible(
        self, obj: FreeCAD.DocumentObject, element: str, visible: bool
    ) -> int:
        """FreeCAD call this function if present"""


class ProxyPython(_ProxyPythonGeneral):
    def execute(self, obj: FreeCAD.DocumentObject):
        """FreeCAD call this function if present"""

    def mustExecute(self, obj: FreeCAD.DocumentObject) -> bool:
        """FreeCAD call this function if present"""

    def onBeforeChange(self, obj: FreeCAD.DocumentObject, propertyName: str):
        """FreeCAD call this function if present"""

    def onChanged(self, obj: FreeCAD.DocumentObject, propertyName: str):
        """FreeCAD call this function if present"""

    def onDocumentRestored(self, obj: FreeCAD.DocumentObject):
        """FreeCAD call this function if present"""


class ProxyPythonObj(_ProxyPythonGeneral):
    """
    This is the same as ProxyPython, but has __object__ attribute.
    Methods defined in this class are called without object argument.
    """

    __object__: FreeCAD.DocumentObject | None = None

    def execute(self):
        """FreeCAD call this function if present"""

    def mustExecute(self) -> bool:
        """FreeCAD call this function if present"""

    def onBeforeChange(self, propertyName: str):
        """FreeCAD call this function if present"""

    def onChanged(self, propertyName: str):
        """FreeCAD call this function if present"""

    def onDocumentRestored(self):
        """FreeCAD call this function if present"""


SoPickedPoint = typing.Annotated[typing.Any, 'pivy.coin.SoPickedPoint']
SoDetail = typing.Annotated[typing.Any, 'pivy.coin.SoDetail']
SoFullPath = typing.Annotated[typing.Any, 'pivy.coin.SoFullPath']


class _ViewProviderPythonGeneral:
    def getIcon(self) -> QIcon | str | None:
        """May be implemented in python"""

    def claimChildren(self) -> typing.Sequence[FreeCAD.DocumentObject]:
        """May be implemented in python"""

    def useNewSelectionModel(self) -> bool:
        """May be implemented in python"""

    def getElementPicked(self, pivyObj: SoPickedPoint) -> str | None:
        """May be implemented in python"""

    def getElement(self, pivyObj: SoDetail) -> str:
        """May be implemented in python"""

    def getDetail(self, name: str) -> SoDetail:
        """May be implemented in python"""

    def getDetailPath(
        self, name: str, pivyObj: SoFullPath, append: bool
    ) -> bool | SoDetail:
        """May be implemented in python"""

    def getSelectionShape(self):  # not redirected
        """May be implemented in python"""

    def setEditViewer(
        self,
        viewObj: FreeCADGui.ViewProviderDocumentObject,
        viewer: FreeCADGui.View3DInventorViewerPy,
        modNum: int,
    ) -> bool:
        """May be implemented in python"""

    def unsetEditViewer(
        self,
        viewObj: FreeCADGui.ViewProviderDocumentObject,
        viewer: FreeCADGui.View3DInventorViewerPy,
    ) -> bool:
        """May be implemented in python"""

    def startRestoring(self):  # not redirected
        """May be implemented in python"""

    def finishRestoring(self):
        """May be implemented in python"""

    def canDelete(self, obj: FreeCAD.DocumentObject) -> bool:
        """May be implemented in python"""

    def isShow(self) -> bool:
        """May be implemented in python"""

    def getDefaultDisplayMode(self) -> str:
        """May be implemented in python"""

    def setDisplayMode(self, modeName: str) -> str:
        """May be implemented in python"""

    def canRemoveChildrenFromRoot(self) -> bool:
        """May be implemented in python"""

    def canDragObjects(self) -> bool:
        """May be implemented in python"""

    def canDragObject(self, obj: FreeCAD.DocumentObject) -> bool:
        """May be implemented in python"""

    def canDropObjects(self) -> bool:
        """May be implemented in python"""

    def canDropObject(self, obj: FreeCAD.DocumentObject) -> bool:
        """May be implemented in python"""

    def canDragAndDropObject(self, obj: FreeCAD.DocumentObject) -> bool:
        """May be implemented in python"""

    def canDropObjectEx(
        self,
        obj: FreeCAD.DocumentObject,
        owner: FreeCAD.DocumentObject | None,
        subName: str,
        elements: tuple[str],
    ) -> bool:
        """May be implemented in python"""

    def dropObjectEx(
        self,
        viewObj: FreeCADGui.ViewProviderDocumentObject,
        obj: FreeCAD.DocumentObject,
        owner: FreeCAD.DocumentObject | object,
        subName: str,
        elements: tuple[str],
    ) -> str | None:
        """May be implemented in python"""

    def canAddToSceneGraph(self) -> bool:
        """May be implemented in python"""

    def getDropPrefix(self) -> str | None:
        """May be implemented in python"""

    def replaceObject(
        self, oldObj: FreeCAD.DocumentObject, newObj: FreeCAD.DocumentObject
    ) -> bool:
        """May be implemented in python"""

    def getLinkedViewProvider(
        self, recursive: bool
    ) -> (
        tuple[FreeCADGui.ViewProviderDocumentObject, str]
        | FreeCADGui.ViewProviderDocumentObject
        | None
    ):
        """May be implemented in python"""


class ViewProviderPython(_ViewProviderPythonGeneral):
    def setEdit(
        self, viewObj: FreeCADGui.ViewProviderDocumentObject, modNum: int
    ) -> bool | None:
        """May be implemented in python"""

    def unsetEdit(
        self, viewObj: FreeCADGui.ViewProviderDocumentObject, modNum: int
    ) -> bool | None:
        """May be implemented in python"""

    def doubleClicked(self, viewObj: FreeCADGui.ViewProviderDocumentObject) -> bool:
        """May be implemented in python"""

    def setupContextMenu(
        self, viewObj: FreeCADGui.ViewProviderDocumentObject, menu: QMenu
    ) -> bool:
        """May be implemented in python"""

    def attach(self, viewObj: FreeCADGui.ViewProviderDocumentObject):
        """May be implemented in python"""

    def updateData(
        self, viewObj: FreeCADGui.ViewProviderDocumentObject, propertyName: str
    ):
        """May be implemented in python"""

    def onChanged(
        self, viewObj: FreeCADGui.ViewProviderDocumentObject, propertyName: str
    ):
        """May be implemented in python"""

    def onDelete(
        self, viewObj: FreeCADGui.ViewProviderDocumentObject, sub: tuple[str, ...]
    ) -> bool:
        """May be implemented in python"""

    def getDisplayModes(
        self, viewObj: FreeCADGui.ViewProviderDocumentObject
    ) -> typing.Sequence[str]:
        """May be implemented in python"""

    def dragObject(
        self,
        viewObj: FreeCADGui.ViewProviderDocumentObject,
        obj: FreeCAD.DocumentObject,
    ):
        """May be implemented in python"""

    def dropObject(
        self,
        viewObj: FreeCADGui.ViewProviderDocumentObject,
        obj: FreeCAD.DocumentObject,
    ):
        """May be implemented in python"""


class ViewProviderPythonObj(_ViewProviderPythonGeneral):
    """
    This is the same as ViewProviderPython, but object must have  __object__ attribute.
    Methods defined in this class are called without view object argument.
    """

    __vobject__: FreeCADGui.ViewProviderDocumentObject

    def setEdit(self, modNum: int) -> bool | None:
        """May be implemented in python"""

    def unsetEdit(self, modNum: int) -> bool | None:
        """May be implemented in python"""

    def doubleClicked(self) -> bool:
        """May be implemented in python"""

    def setupContextMenu(self, menu: QMenu) -> bool:
        """May be implemented in python"""

    def attach(self):
        """May be implemented in python"""

    def updateData(self, propertyName: str):
        """May be implemented in python"""

    def onChanged(self, propertyName: str):
        """May be implemented in python"""

    def onDelete(self, sub: tuple[str, ...]) -> bool:
        """May be implemented in python"""

    def getDisplayModes(self) -> typing.Sequence[str]:
        """May be implemented in python"""

    def dragObject(self, obj: FreeCAD.DocumentObject):
        """May be implemented in python"""

    def dropObject(self, obj: FreeCAD.DocumentObject):
        """May be implemented in python"""


# Gui/Command.cpp
class ResourceDict(typing.TypedDict, total=False):
    CmdType: str
    Pixmap: str
    WhatsThis: str
    MenuText: str
    ToolTip: str
    StatusTip: str
    Accel: str


class CommandPython:
    def GetResources(self) -> ResourceDict:
        """FreeCAD call this function if present"""

    def IsActive(self) -> bool:
        """FreeCAD call this function if present"""

    def Activated(self):
        """FreeCAD call this function if present"""


class CheckableDict(ResourceDict):
    Checkable: bool


class CheckableCommandPython:
    def GetResources(self) -> CheckableDict:
        """FreeCAD call this function if present"""

    def IsActive(self) -> bool:
        """FreeCAD call this function if present"""

    def Activated(self, checked: bool):
        """FreeCAD call this function if present"""


# Gui/DocumentObserverPython.cpp
class DocumentObserverGui:
    """This is template class. You should copy it to your code."""

    def slotCreatedDocument(self, doc: FreeCADGui.Document):
        """FreeCAD call this function if present"""

    def slotDeletedDocument(self, doc: FreeCADGui.Document):
        """FreeCAD call this function if present"""

    def slotRelabelDocument(self, doc: FreeCADGui.Document):
        """FreeCAD call this function if present"""

    def slotRenameDocument(self, doc: FreeCADGui.Document):
        """FreeCAD call this function if present"""

    def slotActivateDocument(self, doc: FreeCADGui.Document):
        """FreeCAD call this function if present"""

    def slotCreatedObject(self, viewProvider: FreeCADGui.ViewProviderDocumentObject):
        """FreeCAD call this function if present"""

    def slotDeletedObject(self, viewProvider: FreeCADGui.ViewProviderDocumentObject):
        """FreeCAD call this function if present"""

    def slotBeforeChangeObject(
        self,
        viewProvider: FreeCADGui.ViewProviderDocumentObject,
        propContainerName: str,
    ):
        """FreeCAD call this function if present"""

    def slotChangedObject(
        self,
        viewProvider: FreeCADGui.ViewProviderDocumentObject,
        propContainerName: str,
    ):
        """FreeCAD call this function if present"""

    def slotInEdit(self, viewProvider: FreeCADGui.ViewProviderDocumentObject):
        """FreeCAD call this function if present"""

    def slotResetEdit(self, viewProvider: FreeCADGui.ViewProviderDocumentObject):
        """FreeCAD call this function if present"""


# App/DocumentObserverPython.cpp
class DocumentObserverApp:
    """This is template class. You should copy it to your code."""

    def slotCreatedDocument(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotDeletedDocument(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotRelabelDocument(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotActivateDocument(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotUndoDocument(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotRedoDocument(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotBeforeChangeDocument(self, doc: FreeCAD.Document, propContainerName: str):
        """FreeCAD call this function if present"""

    def slotChangedDocument(self, obj: FreeCAD.DocumentObject, propContainerName: str):
        """FreeCAD call this function if present"""

    def slotCreatedObject(self, obj: FreeCAD.DocumentObject):
        """FreeCAD call this function if present"""

    def slotDeletedObject(self, obj: FreeCAD.DocumentObject):
        """FreeCAD call this function if present"""

    def slotBeforeChangeObject(
        self, obj: FreeCAD.DocumentObject, propContainerName: str
    ):
        """FreeCAD call this function if present"""

    def slotChangedObject(self, obj: FreeCAD.DocumentObject, propContainerName: str):
        """FreeCAD call this function if present"""

    def slotRecomputedObject(self, obj: FreeCAD.DocumentObject):
        """FreeCAD call this function if present"""

    def slotBeforeRecomputeDocument(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotRecomputedDocument(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotOpenTransaction(self, doc: FreeCAD.Document, name: str):
        """FreeCAD call this function if present"""

    def slotCommitTransaction(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotAbortTransaction(self, doc: FreeCAD.Document):
        """FreeCAD call this function if present"""

    def slotUndo(self):
        """FreeCAD call this function if present"""

    def slotRedo(self):
        """FreeCAD call this function if present"""

    def slotBeforeCloseTransaction(self, abort: bool):
        """FreeCAD call this function if present"""

    def slotCloseTransaction(self, abort: bool):
        """FreeCAD call this function if present"""

    def slotStartSaveDocument(self, doc: FreeCAD.Document, fileName: str):
        """FreeCAD call this function if present"""

    def slotFinishSaveDocument(self, doc: FreeCAD.Document, fileName: str):
        """FreeCAD call this function if present"""

    def slotAppendDynamicProperty(
        self, propContainer: FreeCAD.PropertyContainer, propContainerName: str
    ):
        """FreeCAD call this function if present"""

    def slotRemoveDynamicProperty(
        self, propContainer: FreeCAD.PropertyContainer, propContainerName: str
    ):
        """FreeCAD call this function if present"""

    def slotChangePropertyEditor(
        self, propContainer: FreeCAD.PropertyContainer, propContainerName: str
    ):
        """FreeCAD call this function if present"""

    def slotBeforeAddingDynamicExtension(
        self, extension: FreeCAD.ExtensionContainer, extensionName: str
    ):
        """FreeCAD call this function if present"""

    def slotAddedDynamicExtension(
        self, extension: FreeCAD.ExtensionContainer, extensionName: str
    ):
        """FreeCAD call this function if present"""


class TaskDialog:
    def open(self):
        """
        FreeCAD call this function if present.
        It is called by the framework when the dialog is opened.
        """

    def clicked(self, i: int):
        """
        FreeCAD call this function if present.
        It is called by the framework if a button is clicked which has no accept or reject role.
        """

    def accept(self) -> bool:
        """
        FreeCAD call this function if present.
        It is called by the framework if the dialog is accepted (Ok).
        """

    def reject(self) -> bool:
        """
        FreeCAD call this function if present.
        It is called by the framework if the dialog is rejected (Cancel).
        """

    def helpRequested(self):
        """
        FreeCAD call this function if present.
        It is called by the framework if the user press the help button.
        """

    def getStandardButtons(self) -> int:
        """FreeCAD call this function if present"""

    def modifyStandardButtons(self, buttonBox: QDialogButtonBox):
        """FreeCAD call this function if present"""

    def isAllowedAlterDocument(self) -> bool:
        """
        FreeCAD call this function if present.
        Indicates whether this task dialog allows other commands to modify
        the document while it is open.
        """

    def isAllowedAlterView(self) -> bool:
        """
        FreeCAD call this function if present.
        Indicates whether this task dialog allows other commands to modify
        the 3d view while it is open.
        """

    def isAllowedAlterSelection(self) -> bool:
        """
        FreeCAD call this function if present.
        Indicates whether this task dialog allows other commands to modify
        the selection while it is open.
        """

    def needsFullSpace(self) -> bool:
        """FreeCAD call this function if present"""


class TaskDialogPythonUi(TaskDialog):
    ui: str


class TaskDialogPythonForm(TaskDialog):
    form: list[QObject] | QObject


class SelectionObserver:
    def addSelection(
        self,
        docName: str,
        objectName: str,
        subName: str,
        xyz: tuple[float, float, float],
        /,
    ):
        """May be implemented in python"""

    def clearSelection(self, docName: str, /):
        """May be implemented in python"""

    def pickedListChanged(self):
        """May be implemented in python"""

    def removePreselection(self, docName: str, objectName: str, subName: str, /):
        """May be implemented in python"""

    def removeSelection(self, docName: str, objectName: str, subName: str, /):
        """May be implemented in python"""

    def setPreselection(self, docName: str, objectName: str, subName: str, /):
        """May be implemented in python"""

    def setSelection(self, docName: str, /):
        """May be implemented in python"""
