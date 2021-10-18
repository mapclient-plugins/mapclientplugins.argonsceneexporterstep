"""
Geometric fit model adding visualisations to github.com/ABI-Software/scaffoldfitter
"""
import os
import json

from opencmiss.argon.core.argondocument import ArgonDocument
from opencmiss.argon.core.argonerror import ArgonError
from opencmiss.argon.core.argonlogger import ArgonLogger


class ArgonSceneExporterModel(object):
    """
    Geometric fit model adding visualisations to github.com/ABI-Software/scaffoldfitter
    """

    def __init__(self, input_argon_doc_file, location, identifier):
        """
        :param location: Path to folder for mapclient step name.
        """
        self._location = os.path.join(location, identifier)
        self._identifier = identifier
        self._document = ArgonDocument()
        self._document.initialiseVisualisationContents()
        self._prefix = "ArgonSceneExporter"
        self._numberOfTimeSteps = 10
        self._initialTime = 0.0
        self._finishTime = 1.0
        self._fileLocation = ""
        self.load(input_argon_doc_file)

    def load(self, filename):
        """
        Loads the named Argon file and on success sets filename as the current location.
        Emits documentChange separately if new document loaded, including if existing document cleared due to load failure.
        :return  True on success, otherwise False.
        """
        try:
            with open(filename, 'r') as f:
                state = f.read()
                self._location = None
                if self._document is not None:
                    self._document.freeVisualisationContents()
                self._document = ArgonDocument()
                self._document.initialiseVisualisationContents()
                # set current directory to path from file, to support scripts and fieldml with external resources
                path = os.path.dirname(filename)
                os.chdir(path)
                self._document.deserialize(state)
                self._location = filename
                return True
        except (ArgonError, IOError, ValueError) as e:
            ArgonLogger.getLogger().error("Failed to load Neon model " + filename + ": " + str(e))
        except:
            ArgonLogger.getLogger().error("Failed to load Neon model " + filename + ": Unknown error")

        return False

    def done(self):
        self.exportViewJson()
        self.exportWebGLJson()

    def getIdentifier(self):
        return self._identifier

    def exportViewJson(self):
        """Export sceneviewer parameters to JSON format"""
        sceneviewer = self._document.getSceneviewer()
        viewData = {'farPlane': sceneviewer._far_clipping_plane, 'nearPlane': sceneviewer._near_clipping_plane, 'eyePosition': sceneviewer._eye_position,
                    'targetPosition': sceneviewer._lookat_position, 'upVector': sceneviewer._up_vector}
        f = open(self._prefix + '_view' + '.json', 'w+')
        json.dump(viewData, f)
        f.close()

    def exportWebGLJson(self):
        """
        Export graphics into JSON format, one json export represents one
        surface graphics.
        """
        scene = self._document.getRootRegion().getZincRegion().getScene()
        sceneSR = scene.createStreaminformationScene()
        sceneSR.setIOFormat(sceneSR.IO_FORMAT_THREEJS)
        """
        output frames of the deforming heart between time 0 to 1,
        this matches the number of frame we have read in previously
        """
        sceneSR.setNumberOfTimeSteps(self._numberOfTimeSteps)
        sceneSR.setInitialTime(self._initialTime)
        sceneSR.setFinishTime(self._finishTime)
        """ we want the geometries and colours change overtime """
        sceneSR.setOutputTimeDependentVertices(1)
        sceneSR.setOutputTimeDependentColours(1)
        number = sceneSR.getNumberOfResourcesRequired()
        resources = []
        """Write out each graphics into a json file which can be rendered with ZincJS"""
        for i in range(number):
            resources.append(sceneSR.createStreamresourceMemory())
        scene.write(sceneSR)
        """Write out each resource into their own file"""
        for i in range(number):
            if i == 0:
                f = open(self._fileLocation + '\\' + self._prefix + '_' + 'metadata.json', 'w+')
            else:
                f = open(self._fileLocation + '\\' + self._prefix + '_' + str(i) + '.json', 'w+')
            buffer = resources[i].getBuffer()[1].decode()

            if i == 0:
                for j in range(number - 1):
                    """
                    IMPORTANT: the replace name here is relative to your html page, so adjust it
                    accordingly.
                    """
                    replaceName = '' + self._prefix + '_' + str(j + 1) + '.json'
                    old_name = 'memory_resource' + '_' + str(j + 2)
                    buffer = buffer.replace(old_name, replaceName)
                viewObj = {
                    "Type": "View",
                    "URL": self._prefix + '_view' + '.json'
                }
                obj = json.loads(buffer)
                obj.append(viewObj)
                buffer = json.dumps(obj)
            f.write(buffer)
            f.close()
