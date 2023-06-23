# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
                               QDialog, QDialogButtonBox, QFormLayout, QGridLayout,
                               QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QWidget, QVBoxLayout, QStackedWidget, QSpinBox)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(354, 440)
        self.verticalLayout = QVBoxLayout(ConfigureDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout_3 = QFormLayout(self.configGroupBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.lineEditIdentifier = QLineEdit(self.configGroupBox)
        self.lineEditIdentifier.setObjectName(u"lineEditIdentifier")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEditIdentifier)

        self.label_3 = QLabel(self.configGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.prefix_lineEdit = QLineEdit(self.configGroupBox)
        self.prefix_lineEdit.setObjectName(u"prefix_lineEdit")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.prefix_lineEdit)

        self.label1 = QLabel(self.configGroupBox)
        self.label1.setObjectName(u"label1")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditOutputDirectory = QLineEdit(self.configGroupBox)
        self.lineEditOutputDirectory.setObjectName(u"lineEditOutputDirectory")

        self.horizontalLayout.addWidget(self.lineEditOutputDirectory)

        self.pushButtonOutputDirectory = QPushButton(self.configGroupBox)
        self.pushButtonOutputDirectory.setObjectName(u"pushButtonOutputDirectory")

        self.horizontalLayout.addWidget(self.pushButtonOutputDirectory)


        self.formLayout_3.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_5 = QLabel(self.configGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.comboBoxExportType = QComboBox(self.configGroupBox)
        self.comboBoxExportType.addItem("")
        self.comboBoxExportType.addItem("")
        self.comboBoxExportType.addItem("")
        self.comboBoxExportType.setObjectName(u"comboBoxExportType")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.comboBoxExportType)

        self.stackedWidget = QStackedWidget(self.configGroupBox)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setMidLineWidth(-4)
        self.pageWebGL = QWidget()
        self.pageWebGL.setObjectName(u"pageWebGL")
        self.formLayout_2 = QFormLayout(self.pageWebGL)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.checkBoxSplitWebGLOutput = QCheckBox(self.pageWebGL)
        self.checkBoxSplitWebGLOutput.setObjectName(u"checkBoxSplitWebGLOutput")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.checkBoxSplitWebGLOutput)

        self.splitMaxSize_lineEdit = QLineEdit(self.pageWebGL)
        self.splitMaxSize_lineEdit.setObjectName(u"splitMaxSize_lineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.splitMaxSize_lineEdit)

        self.label_6 = QLabel(self.pageWebGL)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.label_4 = QLabel(self.pageWebGL)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.label = QLabel(self.pageWebGL)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.pageWebGL)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.timeSteps_lineEdit = QLineEdit(self.pageWebGL)
        self.timeSteps_lineEdit.setObjectName(u"timeSteps_lineEdit")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.timeSteps_lineEdit)

        self.initialTime_lineEdit = QLineEdit(self.pageWebGL)
        self.initialTime_lineEdit.setObjectName(u"initialTime_lineEdit")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.initialTime_lineEdit)

        self.finishTime_lineEdit = QLineEdit(self.pageWebGL)
        self.finishTime_lineEdit.setObjectName(u"finishTime_lineEdit")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.finishTime_lineEdit)

        self.stackedWidget.addWidget(self.pageWebGL)
        self.pageThumbnail = QWidget()
        self.pageThumbnail.setObjectName(u"pageThumbnail")
        self.stackedWidget.addWidget(self.pageThumbnail)
        self.pageImage = QWidget()
        self.pageImage.setObjectName(u"pageImage")
        self.formLayout = QFormLayout(self.pageImage)
        self.formLayout.setObjectName(u"formLayout")
        self.labelWidth = QLabel(self.pageImage)
        self.labelWidth.setObjectName(u"labelWidth")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelWidth)

        self.spinBoxWidth = QSpinBox(self.pageImage)
        self.spinBoxWidth.setObjectName(u"spinBoxWidth")
        self.spinBoxWidth.setMinimum(18)
        self.spinBoxWidth.setMaximum(9999)
        self.spinBoxWidth.setValue(512)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinBoxWidth)

        self.labelHeight = QLabel(self.pageImage)
        self.labelHeight.setObjectName(u"labelHeight")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelHeight)

        self.spinBoxHeight = QSpinBox(self.pageImage)
        self.spinBoxHeight.setObjectName(u"spinBoxHeight")
        self.spinBoxHeight.setMinimum(18)
        self.spinBoxHeight.setMaximum(9999)
        self.spinBoxHeight.setValue(512)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinBoxHeight)

        self.stackedWidget.addWidget(self.pageImage)

        self.formLayout_3.setWidget(4, QFormLayout.SpanningRole, self.stackedWidget)


        self.verticalLayout.addWidget(self.configGroupBox)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.prefix_lineEdit, self.lineEditOutputDirectory)
        QWidget.setTabOrder(self.lineEditOutputDirectory, self.pushButtonOutputDirectory)

        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        self.comboBoxExportType.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Argon Scene Exporter", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"Identifier:  ", None))
        self.label_3.setText(QCoreApplication.translate("ConfigureDialog", u"Prefix : ", None))
        self.label1.setText(QCoreApplication.translate("ConfigureDialog", u"Output directory:", None))
        self.pushButtonOutputDirectory.setText(QCoreApplication.translate("ConfigureDialog", u"...", None))
        self.label_5.setText(QCoreApplication.translate("ConfigureDialog", u"Export type:", None))
        self.comboBoxExportType.setItemText(0, QCoreApplication.translate("ConfigureDialog", u"webgl", None))
        self.comboBoxExportType.setItemText(1, QCoreApplication.translate("ConfigureDialog", u"thumbnail", None))
        self.comboBoxExportType.setItemText(2, QCoreApplication.translate("ConfigureDialog", u"image", None))

        self.checkBoxSplitWebGLOutput.setText(QCoreApplication.translate("ConfigureDialog", u"Split webGL output", None))
        self.splitMaxSize_lineEdit.setText(QCoreApplication.translate("ConfigureDialog", u"18MiB", None))
        self.label_6.setText(QCoreApplication.translate("ConfigureDialog", u"Split files greater than:", None))
        self.label_4.setText(QCoreApplication.translate("ConfigureDialog", u"Time Steps : ", None))
        self.label.setText(QCoreApplication.translate("ConfigureDialog", u"Initial Time (s) : ", None))
        self.label_2.setText(QCoreApplication.translate("ConfigureDialog", u"Finish Time (s) : ", None))
        self.labelWidth.setText(QCoreApplication.translate("ConfigureDialog", u"Width:", None))
        self.labelHeight.setText(QCoreApplication.translate("ConfigureDialog", u"Height:", None))
    # retranslateUi

