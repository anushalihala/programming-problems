# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newteam.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewDialog(object):
    def setupUi(self, NewDialog):
        NewDialog.setObjectName("NewDialog")
        NewDialog.resize(174, 72)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewDialog.sizePolicy().hasHeightForWidth())
        NewDialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(NewDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(NewDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.tbNewTeam = QtWidgets.QPlainTextEdit(NewDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbNewTeam.sizePolicy().hasHeightForWidth())
        self.tbNewTeam.setSizePolicy(sizePolicy)
        self.tbNewTeam.setObjectName("tbNewTeam")
        self.gridLayout.addWidget(self.tbNewTeam, 0, 0, 1, 1)

        self.retranslateUi(NewDialog)
        self.buttonBox.accepted.connect(NewDialog.accept)
        self.buttonBox.rejected.connect(NewDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewDialog)

    def retranslateUi(self, NewDialog):
        _translate = QtCore.QCoreApplication.translate
        NewDialog.setWindowTitle(_translate("NewDialog", "New Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewDialog = QtWidgets.QDialog()
    ui = Ui_NewDialog()
    ui.setupUi(NewDialog)
    NewDialog.show()
    sys.exit(app.exec_())

