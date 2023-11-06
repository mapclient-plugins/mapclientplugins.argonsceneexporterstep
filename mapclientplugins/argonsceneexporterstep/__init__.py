
"""
MAP Client Plugin
"""

__version__ = '0.5.0'
__author__ = 'Kay Wang'
__stepname__ = 'Argon Scene Exporter'
__location__ = 'https://github.com/mapclient-plugins/mapclientplugins.argonsceneexporterstep.git'

# import class that derives itself from the step mountpoint.
from mapclientplugins.argonsceneexporterstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc
