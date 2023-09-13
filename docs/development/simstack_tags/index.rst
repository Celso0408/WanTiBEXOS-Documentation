=====================================
The Simstack tags and functionalities
=====================================

.. raw:: html

    <style> .green {color:green} </style>

.. role:: green

This section presents the functionalities for the most common tags used to build the
GUI displayed by the WaNos. We also introduce the
`Test-WaNo <https://github.com/KIT-Workflows/Test-WaNo>`_ example, where the tags below
and report are implemented.

1. Variables: Float, Integer, and string
########################################

SimStack supports all those variables to represent numbers, strings, and logical terms.

  .. code-block:: XML
    :linenos:

    <WaNoFloat name="var-name" force_disable = "False" description = "describe the meaning of your variable here">float value</WaNoFloat>
    <WaNoInt name="var-name" force_disable = "False" description = "describe the meaning of your variable here">integer value</WaNoInt>
    <WaNoString name="var-name" description = "describe the meaning of your variable here">string</WaNoString>
    <WaNoBool name="var-name" description= "describe the meaning of your variable here">False</WaNoBool>

2. Drop-down list
#################

A drop-down list is a graphical control element allowing users
to choose one value from the options. Here we can use as many
options are necessary. The ``chosen="True"`` define the default value of the list.

  .. code-block:: XML
    :linenos:

    <WaNoDropDown name="var-name" description = "describe the meaning of your variable here">
      <Entry id="0" chosen="True">var-option 1</Entry>
      <Entry id="1">var-option 2</Entry>
      <Entry id="2">var-option 3</Entry>
      <Entry id="3">var-option 4</Entry>
        .
        .
        .
      <Entry id="N">var-option N</Entry>
    </WaNoDropDown>


3. DictBox
#################

``WaNoDictBox`` creates a dialogue box that represents a dictionary of values, and
any modifications made by the end-user are changed in the ``rendered_wano.yml`` file. Below
we show a conditional dictbox, which should be available to the end-user only when
the ``name="var-name-Bool"`` be set to ``True``.

  .. code-block:: XML
    :linenos:

    <WaNoBool name="var-name-Bool" description= "describe the meaning of your variable here">False</WaNoBool>
    <WaNoDictBox name="var-name" visibility_condition="%s == True" visibility_var_path="var-name-Bool">
      <WaNoFloat name="var-name 1">float value</WaNoFloat>
      <WaNoInt name="var-name 2">integer value</WaNoInt>
      <WaNoString name="var-name 3">string</WaNoS>
    </WaNoDictBox>

4. Multiple Of
#################
The ``WaNoMultipleOf`` tag works as a dictbox too and beyond that it allows us to
set up directly on the GUI as many variables as needed.

.. code-block:: XML
  :linenos:

  <WaNoMultipleOf name="var-nanme">
    <Element id="0">
      <WaNoString name="string-name">String</WaNoString>
    </Element>
  </WaNoMultipleOf>

5. Load files
#################
``WaNoFile`` tag shows a box to define the path to a given selected file.

.. code-block:: XML
  :linenos:

  <WaNoFile logical_filename="logical file-name"  name="file-name"> file path </WaNoFile>

6. Generating ``.html`` reports for the WaNos
#############################################

Here we show how to creates reports with ``.html`` files. In this example
(`Test-WaNo <https://github.com/KIT-Workflows/Test-WaNo>`_) the ``logical_filename="report_template.body"`` should be
defined in the ``WaNoInputFile`` tag of ``Test-WaNo.xml`` file as shown below.

.. code-block:: XML
  :linenos:

  <WaNoInputFile logical_filename="report_template.body">report_template.body</WaNoInputFile>

The ``.html`` code below shows the setup for the report in the `Test-WaNo <https://github.com/KIT-Workflows/Test-WaNo>`_ example.

.. code-block:: html
  :linenos:

  <html>
    <h1> Test-Report </h1>
  <p style="color:blue;font-size:24px;">
      The output of this WaNo is the figure.png file; you can download
      it to your computer by simply clicking on it in the output folder.
  </p>

  <p style="color:blue;font-size:24px;">The inputs of this WaNo are displayed below.</p>
  {% for key, value in output_dict.items() %}
    <p style="color:black;font-size:20px;"> {{ key }}: {{value}}</p>
  {% endfor %}

  <figure>
      <img src="figure.png" alt="RDFs" style="width:65%">
      <figcaption> <p style="color:red;font-size:24px;">Fig1. - Example of figure.</p>  </figcaption>
  </figure>
  </html>
