#!/bin/bash
pyside2-uic -o mapclientplugins/argonsceneexporterstep/ui_configuredialog.py mapclientplugins/argonsceneexporterstep/qt/configuredialog.ui
pyside2-rcc -o mapclientplugins/argonsceneexporterstep/resources_rc.py mapclientplugins/argonsceneexporterstep/qt/resources.qrc
