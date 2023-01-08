Argon Scene Exporter
====================

Overview
--------

The **Argon Scene Exporter** is a MAP Client plugin for exporting an Argon scene.
The plugin uses an Argon document as an input.
The plugin can be configured to export the scene to either webGL or a JPEG thumbnail.

Workflow Connections
--------------------

As shown in :numref:`fig-mcp-argon-scene-exporter-workflow-connections`, the **Argon Scene Exporter** uses 1 input:

1. An Argon Document from a **Argon Viewer** or other plugin. (Port: *https://opencmiss.org/1.0/rdf-schema#ArgonDocument*) 

It does not have a output port, the output of this plugin will be generated in the folder set in config.

.. _fig-mcp-argon-scene-exporter-workflow-connections:

.. figure:: _images/workflow-connections.png
   :alt: Argon Scene Exporter workflow connections.
   :align: center
   :figwidth: 75%

   **Argon Scene Exporter** workflow connections.¶

Configure
---------

As a minimum, to configure the step, set the name of the step, select the export type required, and set the output directory.
The output directory should be located outside the workflow directory.

.. _fig-mcp-argon-scene-exporter-configure-dialog:

.. figure:: _images/step-configuration-dialog.png
   :alt: Step configure dialog

   Argon scene exporter step configuration dialog.

There are four other parameters for configuring the step that are optional:

#. Prefix
#. Time Steps
#. Initial Time
#. Finish Time

The *Prefix* parameter, is a string that is placed as a prefix on all files produced by the type of export selected.
The *Time Steps* parameter, is an integer representing the number of time steps to output the export at between the *Initial Time* and the *Finish Time*.
The *Time Steps* parameter, is currently ignored for the *thumbnail* export, the intention is to output a GIF image in the future.
The *Initial Time* parameter, is the initial time to export the scene from.
The *Finish Time* parameter, is the final time to export the scene to.

The *Time Steps*, *Initial Time*, and *Finish Time* are only appropriate for time varying scenes.
If the scene is not time varying these parameters are ignored.
