call C:\Users\ywan787\pyvenv\venv39\Scripts\activate
@REM pyside6-uic -o mapclientplugins\argonviewerstep\ui\ui_argonviewerwidget.py res\designer\argonviewerwidget.ui
pyside6-uic -o mapclientplugins\argonsceneexporterstep\ui_configuredialog.py mapclientplugins\argonsceneexporterstep\qt\configuredialog.ui
pyside6-rcc -o mapclientplugins\argonsceneexporterstep\resources_rc.py mapclientplugins\argonsceneexporterstep\qt\resources.qrc