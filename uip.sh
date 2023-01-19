#!/bin/bash
pyside6-uic -o mapclientplugins/argonsceneexporterstep/ui_configuredialog.py mapclientplugins/argonsceneexporterstep/qt/configuredialog.ui
pyside6-rcc -o mapclientplugins/argonsceneexporterstep/resources_rc.py mapclientplugins/argonsceneexporterstep/qt/resources.qrc
