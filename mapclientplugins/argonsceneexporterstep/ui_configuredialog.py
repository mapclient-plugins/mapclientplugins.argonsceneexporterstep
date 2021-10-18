# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(615, 404)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.lineEditIdentifier = QLineEdit(self.configGroupBox)
        self.lineEditIdentifier.setObjectName(u"lineEditIdentifier")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditIdentifier)

        self.label_3 = QLabel(self.configGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.prefix_lineEdit = QLineEdit(self.configGroupBox)
        self.prefix_lineEdit.setObjectName(u"prefix_lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.prefix_lineEdit)

        self.label_4 = QLabel(self.configGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.timeSteps_lineEdit = QLineEdit(self.configGroupBox)
        self.timeSteps_lineEdit.setObjectName(u"timeSteps_lineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.timeSteps_lineEdit)

        self.label = QLabel(self.configGroupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label)

        self.initialTime_lineEdit = QLineEdit(self.configGroupBox)
        self.initialTime_lineEdit.setObjectName(u"initialTime_lineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.initialTime_lineEdit)

        self.label_2 = QLabel(self.configGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.finishTime_lineEdit = QLineEdit(self.configGroupBox)
        self.finishTime_lineEdit.setObjectName(u"finishTime_lineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.finishTime_lineEdit)

        self.label1 = QLabel(self.configGroupBox)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditOutputDirectory = QLineEdit(self.configGroupBox)
        self.lineEditOutputDirectory.setObjectName(u"lineEditOutputDirectory")

        self.horizontalLayout.addWidget(self.lineEditOutputDirectory)

        self.pushButtonDIrectoryChooser = QPushButton(self.configGroupBox)
        self.pushButtonDIrectoryChooser.setObjectName(u"pushButtonDIrectoryChooser")

        self.horizontalLayout.addWidget(self.pushButtonDIrectoryChooser)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Step", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:  ", None))
        self.label_3.setText(QCoreApplication.translate("ConfigureDialog", u"Prefix : ", None))
        self.label_4.setText(QCoreApplication.translate("ConfigureDialog", u"Time Steps : ", None))
        self.label.setText(QCoreApplication.translate("ConfigureDialog", u"Initial Time : ", None))
        self.label_2.setText(QCoreApplication.translate("ConfigureDialog", u"Finish Time : ", None))
        self.label1.setText(QCoreApplication.translate("ConfigureDialog", u"Output Directory:", None))
        self.pushButtonDIrectoryChooser.setText(QCoreApplication.translate("ConfigureDialog", u"...", None))
    # retranslateUi

