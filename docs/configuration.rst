.. _mcp-argonsceneexporter-configuration:

Configuration
-------------

As a minimum, to configure the step, set the name of the step, select the export type required, and set the output directory.
The output directory should be located outside the workflow directory.

.. _fig-mcp-argon-scene-exporter-configure-dialog:

.. figure:: _images/step-configuration-dialog.png
   :alt: Step configure dialog

   Argon scene exporter step configuration dialog.

There is one parameter for configuring the step that is optional.
The optional parameter is the *prefix* parameter.
It is however a good idea to set the *prefix*, the *prefix* is used in formulating the output filename.
There are also parameters that are dependent on the exporter chosen.
The *webGL* exporter has the following optional parameters:

#. Time Steps
#. Initial Time
#. Finish Time

The *thumbnail* exporter does not have any optional parameters.
The *image* exporter has the following optional parameters:

#. Width, [min. 18, max. 9999]
#. Height, [min. 18, max. 9999]

The *Prefix* parameter, is a string that is placed as a prefix on all files produced by the type of export selected.
The *Time Steps* parameter, is an integer representing the number of time steps to output the export at between the *Initial Time* and the *Finish Time*.
The *Time Steps* parameter, is currently ignored for the *thumbnail* export, the intention is to output a GIF image in the future.
The *Initial Time* parameter, is the initial time to export the scene from.
The *Finish Time* parameter, is the final time to export the scene to.
The *Width* parameter, is an integer that sets the width of the exported image.
The *Height* parameter, is an integer that sets the height of the exported image.

The *Time Steps*, *Initial Time*, and *Finish Time* are only appropriate for time varying scenes.
If the scene is not time varying these parameters are ignored.
