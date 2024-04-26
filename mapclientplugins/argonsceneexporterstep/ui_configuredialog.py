# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
    QDialog, QDialogButtonBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(377, 444)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
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
        self.comboBoxExportType.addItem("")
        self.comboBoxExportType.addItem("")
        self.comboBoxExportType.addItem("")
        self.comboBoxExportType.addItem("")
        self.comboBoxExportType.setObjectName(u"comboBoxExportType")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.comboBoxExportType)

        self.stackedWidget = QStackedWidget(self.configGroupBox)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setMidLineWidth(-4)
        self.pageFlatmapSVG = QWidget()
        self.pageFlatmapSVG.setObjectName(u"pageFlatmapSVG")
        self.stackedWidget.addWidget(self.pageFlatmapSVG)
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
        self.pageSTL = QWidget()
        self.pageSTL.setObjectName(u"pageSTL")
        self.stackedWidget.addWidget(self.pageSTL)
        self.pageThumbnail = QWidget()
        self.pageThumbnail.setObjectName(u"pageThumbnail")
        self.stackedWidget.addWidget(self.pageThumbnail)
        self.pageVTK = QWidget()
        self.pageVTK.setObjectName(u"pageVTK")
        self.stackedWidget.addWidget(self.pageVTK)
        self.pageWavefront = QWidget()
        self.pageWavefront.setObjectName(u"pageWavefront")
        self.stackedWidget.addWidget(self.pageWavefront)
        self.pageWebGL = QWidget()
        self.pageWebGL.setObjectName(u"pageWebGL")
        self.gridLayout_2 = QGridLayout(self.pageWebGL)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.pageWebGL)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.frame = QFrame(self.pageWebGL)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.frame.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBoxSplitWebGLOutput = QCheckBox(self.frame)
        self.checkBoxSplitWebGLOutput.setObjectName(u"checkBoxSplitWebGLOutput")

        self.horizontalLayout_3.addWidget(self.checkBoxSplitWebGLOutput)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.splitMaxSize_lineEdit = QLineEdit(self.frame)
        self.splitMaxSize_lineEdit.setObjectName(u"splitMaxSize_lineEdit")

        self.horizontalLayout_3.addWidget(self.splitMaxSize_lineEdit)


        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)

        self.label_8 = QLabel(self.pageWebGL)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.pageWebGL)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBoxLODs = QCheckBox(self.frame_2)
        self.checkBoxLODs.setObjectName(u"checkBoxLODs")

        self.horizontalLayout_2.addWidget(self.checkBoxLODs)


        self.gridLayout_2.addWidget(self.frame_2, 1, 1, 1, 1)

        self.label_4 = QLabel(self.pageWebGL)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.timeSteps_lineEdit = QLineEdit(self.pageWebGL)
        self.timeSteps_lineEdit.setObjectName(u"timeSteps_lineEdit")

        self.gridLayout_2.addWidget(self.timeSteps_lineEdit, 2, 1, 1, 1)

        self.label = QLabel(self.pageWebGL)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)

        self.initialTime_lineEdit = QLineEdit(self.pageWebGL)
        self.initialTime_lineEdit.setObjectName(u"initialTime_lineEdit")

        self.gridLayout_2.addWidget(self.initialTime_lineEdit, 3, 1, 1, 1)

        self.label_2 = QLabel(self.pageWebGL)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)

        self.finishTime_lineEdit = QLineEdit(self.pageWebGL)
        self.finishTime_lineEdit.setObjectName(u"finishTime_lineEdit")

        self.gridLayout_2.addWidget(self.finishTime_lineEdit, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer, 5, 1, 1, 1)

        self.stackedWidget.addWidget(self.pageWebGL)

        self.formLayout_3.setWidget(4, QFormLayout.SpanningRole, self.stackedWidget)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        QWidget.setTabOrder(self.prefix_lineEdit, self.lineEditOutputDirectory)
        QWidget.setTabOrder(self.lineEditOutputDirectory, self.pushButtonOutputDirectory)

        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        self.comboBoxExportType.setCurrentIndex(6)
        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Argon Scene Exporter", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"Identifier :", None))
        self.label_3.setText(QCoreApplication.translate("ConfigureDialog", u"Prefix :", None))
        self.label1.setText(QCoreApplication.translate("ConfigureDialog", u"Output directory :", None))
        self.pushButtonOutputDirectory.setText(QCoreApplication.translate("ConfigureDialog", u"...", None))
        self.label_5.setText(QCoreApplication.translate("ConfigureDialog", u"Export type :", None))
        self.comboBoxExportType.setItemText(0, QCoreApplication.translate("ConfigureDialog", u"flatmapsvg", None))
        self.comboBoxExportType.setItemText(1, QCoreApplication.translate("ConfigureDialog", u"image", None))
        self.comboBoxExportType.setItemText(2, QCoreApplication.translate("ConfigureDialog", u"stl", None))
        self.comboBoxExportType.setItemText(3, QCoreApplication.translate("ConfigureDialog", u"thumbnail", None))
        self.comboBoxExportType.setItemText(4, QCoreApplication.translate("ConfigureDialog", u"vtk", None))
        self.comboBoxExportType.setItemText(5, QCoreApplication.translate("ConfigureDialog", u"wavefront", None))
        self.comboBoxExportType.setItemText(6, QCoreApplication.translate("ConfigureDialog", u"webgl", None))

        self.labelWidth.setText(QCoreApplication.translate("ConfigureDialog", u"Width:", None))
        self.labelHeight.setText(QCoreApplication.translate("ConfigureDialog", u"Height:", None))
        self.label_6.setText(QCoreApplication.translate("ConfigureDialog", u"Split output files :", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSplitWebGLOutput.setToolTip(QCoreApplication.translate("ConfigureDialog", u"If checked, splits the output files to be at most the size specified.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSplitWebGLOutput.setText("")
        self.label_7.setText(QCoreApplication.translate("ConfigureDialog", u"@", None))
        self.splitMaxSize_lineEdit.setText(QCoreApplication.translate("ConfigureDialog", u"18MiB", None))
        self.label_8.setText(QCoreApplication.translate("ConfigureDialog", u"Level of detail :", None))
#if QT_CONFIG(tooltip)
        self.checkBoxLODs.setToolTip(QCoreApplication.translate("ConfigureDialog", u"If checked, outputs additional files with lower tessellations.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxLODs.setText("")
        self.label_4.setText(QCoreApplication.translate("ConfigureDialog", u"Time Steps :", None))
        self.label.setText(QCoreApplication.translate("ConfigureDialog", u"Initial Time (s) :", None))
        self.label_2.setText(QCoreApplication.translate("ConfigureDialog", u"Finish Time (s) :", None))
    # retranslateUi

