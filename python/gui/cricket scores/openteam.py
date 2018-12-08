# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openteam.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OpenDialog(object):
    def setupUi(self, OpenDialog):
        OpenDialog.setObjectName("OpenDialog")
        OpenDialog.resize(174, 67)
        self.verticalLayout = QtWidgets.QVBoxLayout(OpenDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cmbOpenTeam = QtWidgets.QComboBox(OpenDialog)
        self.cmbOpenTeam.setObjectName("cmbOpenTeam")
        self.verticalLayout.addWidget(self.cmbOpenTeam)
        self.buttonBox = QtWidgets.QDialogButtonBox(OpenDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(OpenDialog)
        self.buttonBox.accepted.connect(OpenDialog.accept)
        self.buttonBox.rejected.connect(OpenDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OpenDialog)

    def retranslateUi(self, OpenDialog):
        _translate = QtCore.QCoreApplication.translate
        OpenDialog.setWindowTitle(_translate("OpenDialog", "Open Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenDialog = QtWidgets.QDialog()
    ui = Ui_OpenDialog()
    ui.setupUi(OpenDialog)
    OpenDialog.show()
    sys.exit(app.exec_())

