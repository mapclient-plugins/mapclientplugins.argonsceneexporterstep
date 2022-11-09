import os
import webbrowser

from PySide2 import QtCore, QtWidgets
from mapclientplugins.argonsceneexporterstep.ui_configuredialog import Ui_ConfigureDialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QtWidgets.QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self._workflow_location = None
        self._previousLocation = ''

        self.setWhatsThis('<html>Please read the documentation available \n<a href="https://abi-mapping-tools.readthedocs.io/en/latest/mapclientplugins.argonsceneexporterstep/docs/index.html">here</a> for further details.</html>')

        self._update_ui()
        self._make_connections()

    def event(self, e):
        if e.type() == QtCore.QEvent.Type.WhatsThisClicked:
            webbrowser.open(e.href())
        return super().event(e)

    def _make_connections(self):
        self._ui.lineEditIdentifier.textChanged.connect(self.validate)
        self._ui.pushButtonOutputDirectory.clicked.connect(self._directory_chooser_clicked)
        self._ui.comboBoxExportType.currentTextChanged.connect(self._update_ui)

    def _update_ui(self):
        current_index = self._ui.comboBoxExportType.currentIndex()
        self._ui.stackedWidget.setCurrentIndex(current_index)

    def _output_location(self, location=None):
        if location is None:
            display_path = self._ui.lineEditOutputDirectory.text()
        else:
            display_path = location

        if self._workflow_location and os.path.isabs(display_path):
            display_path = os.path.relpath(display_path, self._workflow_location)

        return display_path

    def accept(self):
        """
        Override the accept method so that we can confirm saving an
        invalid configuration.
        """
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(
                self, 'Invalid Configuration',
                'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def setWorkflowLocation(self, location):
        self._workflow_location = location

    def _directory_valid(self):
        dir_path = self._output_location()

        if self._workflow_location:
            dir_path = os.path.realpath(os.path.join(self._workflow_location, dir_path))

        directory_valid = os.path.isdir(dir_path) and len(self._ui.lineEditOutputDirectory.text())
        self._ui.lineEditOutputDirectory.setStyleSheet(DEFAULT_STYLE_SHEET if directory_valid else INVALID_STYLE_SHEET)

        return directory_valid

    def validate(self):
        """
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the
        overall validity of the configuration.
        """
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEditIdentifier.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEditIdentifier.text())
        if valid:
            self._ui.lineEditIdentifier.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.lineEditIdentifier.setStyleSheet(INVALID_STYLE_SHEET)

        return valid and self._directory_valid()

    def getConfig(self):
        """
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = self._ui.lineEditIdentifier.text()
        config = {'identifier': self._ui.lineEditIdentifier.text(), 'prefix': self._ui.prefix_lineEdit.text(), 'timeSteps': self._ui.timeSteps_lineEdit.text(),
                  'initialTime': self._ui.initialTime_lineEdit.text(), 'finishTime': self._ui.finishTime_lineEdit.text(),
                  'outputDir': self._output_location(), 'exportType': self._ui.comboBoxExportType.currentText(),
                  'splitFiles': self._ui.checkBoxSplitWebGLOutput.isChecked(), 'splitSize': self._ui.splitMaxSize_lineEdit.text(),
                  'width': self._ui.spinBoxWidth.value(), 'height': self._ui.spinBoxHeight.value()}
        if self._previousLocation:
            config['previous_location'] = os.path.relpath(self._previousLocation, self._workflow_location)
        else:
            config['previous_location'] = ''

        return config

    def setConfig(self, config):
        """
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = config['identifier']
        self._ui.lineEditIdentifier.setText(config['identifier'])
        self._ui.prefix_lineEdit.setText(config['prefix'])
        self._ui.timeSteps_lineEdit.setText(config['timeSteps'])
        self._ui.initialTime_lineEdit.setText(config['initialTime'])
        self._ui.finishTime_lineEdit.setText(config['finishTime'])
        self._ui.comboBoxExportType.setCurrentText(config['exportType'])
        self._ui.splitMaxSize_lineEdit.setText(config.get('splitSize', '18 MiB'))
        self._ui.checkBoxSplitWebGLOutput.setChecked(config.get('splitFiles', False))
        self._ui.spinBoxWidth.setValue(config.get('width', 512))
        self._ui.spinBoxHeight.setValue(config.get('height', 512))
        if 'outputDir' in config:
            self._ui.lineEditOutputDirectory.setText(config['outputDir'])
        if 'previous_location' in config:
            self._previousLocation = os.path.join(self._workflow_location, config['previous_location'])

    def _directory_chooser_clicked(self):
        # Second parameter returned is the filter chosen
        location = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Destination for export', self._previousLocation)

        if location:
            self._previousLocation = location
            display_location = self._output_location(location)
            self._ui.lineEditOutputDirectory.setText(display_location)
            self._directory_valid()
