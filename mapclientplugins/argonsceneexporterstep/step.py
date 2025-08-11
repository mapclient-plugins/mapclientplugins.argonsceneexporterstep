"""
MAP Client Plugin Step
"""
import os
import json

from PySide6 import QtGui, QtWidgets, QtCore
from cmlibs.argon.argondocument import ArgonDocument

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.argonsceneexporterstep.configuredialog import ConfigureDialog
from mapclientplugins.argonsceneexporterstep.splitter.utilities import convert_to_bytes
from mapclientplugins.argonsceneexporterstep.splitter.json_resource import split_webgl_output, combine_webgl_output

from cmlibs.exporter.flatmapsvg import ArgonSceneExporter as FlatmapSVGExporter
from cmlibs.exporter.webgl import ArgonSceneExporter as WebGLExporter
from cmlibs.exporter.vtk import ArgonSceneExporter as VTKExporter
from cmlibs.exporter.wavefront import ArgonSceneExporter as WavefrontExporter
from cmlibs.exporter.stl import ArgonSceneExporter as STLExporter
from cmlibs.exporter.thumbnail import ArgonSceneExporter as ThumbnailExporter
from cmlibs.exporter.image import ArgonSceneExporter as ImageExporter


class ArgonSceneExporterStep(WorkflowStepMountPoint):
    """
    Export Argon documents to different formats.
    """

    def __init__(self, location):
        super(ArgonSceneExporterStep, self).__init__('Argon Scene Exporter', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Sink'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/argonsceneexporterstep/images/data-sink.png')
        # Ports:
        self.addPort([('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'https://cmlibs.org/1.0/rdf-schema#ArgonDocument'),
                      ('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location')
                      ])
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#directory_location'))
        # Port data:
        self._document = None  # https://opencmiss.org/1.0/rdf-schema#ArgonDocument
        # Config:
        self._config = {'identifier': '', 'exportType': 'webgl', 'prefix': '',
                        'timeSteps': '', 'initialTime': '', 'finishTime': '',
                        'outputDir': '', 'splitSize': '18 MiB', 'splitFiles': False,
                        'combineSize': '703 KiB', 'combineFiles': False}
        self._model = None

    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        # Put your execute step code here before calling the '_doneExecution' method.
        # os.path.join(self._location, self._config['identifier'])
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)
        try:
            output_dir = self._config['outputDir'] if os.path.isabs(self._config['outputDir']) else os.path.join(self._location, self._config['outputDir'])
            output_dir = os.path.realpath(output_dir)
            if self._config['exportType'] == 'webgl':
                self._model = WebGLExporter(output_dir)
                self._model.setLoD(self._config.get("LODs", False))
            elif self._config['exportType'] == 'vtk':
                self._model = VTKExporter(output_dir)
            elif self._config['exportType'] == 'wavefront':
                self._model = WavefrontExporter(output_dir)
            elif self._config['exportType'] == 'stl':
                self._model = STLExporter(output_dir)
            elif self._config['exportType'] == 'flatmapsvg':
                self._model = FlatmapSVGExporter(output_dir)
            elif self._config['exportType'] == 'thumbnail':
                self._model = ThumbnailExporter(output_dir)
            elif self._config['exportType'] == 'image':
                self._model = ImageExporter(self._config['width'], self._config['height'], output_dir)
            else:
                raise NotImplementedError('Current export type selection is not implemented.')

            self._model.set_document(self._document)
            number_of_time_steps = int(self._config['timeSteps']) if self._config['timeSteps'] else None
            initial_time = float(self._config['initialTime']) if self._config['initialTime'] else None
            finish_time = float(self._config['finishTime']) if self._config['finishTime'] else None
            self._model.set_parameters({
                "prefix": self._config['prefix'],
                "numberOfTimeSteps": number_of_time_steps,
                "initialTime": initial_time,
                "finishTime": finish_time,
            })

            self._model.export()
            if self._config['exportType'] == 'webgl':
                if self._config['splitFiles']:
                    split_size = convert_to_bytes(self._config['splitSize'])
                    if split_size != -1:
                        split_webgl_output(self._model.metadata_file(), split_size, True)
                if self._config['combineFiles']:
                    combine_size = convert_to_bytes(self._config['combineSize'])
                    if combine_size != -1:
                        combine_webgl_output(self._model.metadata_file(), combine_size, True)

            self._doneExecution()
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

    def setPortData(self, index, data_in):
        """
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.

        :param index: Index of the port to return.
        :param data_in: The data to set for the port at the given index.
        """
        if isinstance(data_in, str) and os.path.isfile(data_in):
            with open(data_in) as fh:
                content = fh.read()

            document = ArgonDocument()
            document.initialiseVisualisationContents()
            document.deserialize(content, base_path=os.path.dirname(data_in))
            data_in = document

        self._document = data_in  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location

    def getPortData(self, index):
        """
        :param index: Index of the port to return.
        """
        return os.path.realpath(os.path.join(self._location, self._config['outputDir']))

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(self._main_window)
        dlg.setWorkflowLocation(self._location)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.

        :param string: JSON representation of the configuration in a string.
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.setWorkflowLocation(self._location)
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()
