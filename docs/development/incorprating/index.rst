========================
Incorporating a new WaNo
========================

.. raw:: html

    <style> .green {color:green} </style>

.. role:: green

Scientific studies are often obtained by chaining the preparation and execution of multiple interoperable packages
one after the other. The scientific process requires the reproducibility of this simulation chain and the reproducibility
of the singular modules. Here we show how to incorporate a new **WaNo** within in **SimStack** framework, including
its Graphical User Interface (GUI), parameters, and execution process.

1. WaNo concept
###############

The Workflow Active Nodes **WaNo** is specified in an ``XML`` file, which **SimStack** interprets and uses to render
the information of the node from the local machine to the HPC resources. It eases the adjustment of input parameters
and files and is displayed on the right side of the client window, as shown in the last figure of the **Installation**
section. In the code lines below, we highlight in yellow the five possible fields. The absence of the first one will
not raise any execution error, but the remaining are mandatory for any implemented **WaNo**.

.. code-block:: XML
 :linenos:
 :emphasize-lines: 2, 13, 15, 18, 20, 22, 24, 26, 28, 30

 <WaNoTemplate>
    <WaNoMeta>
       <Author>
         <Name> Celso R. C. Rego </Name>
         <Email>celsorego@kit.edu</Email>
       </Author>

       <Description>
         This WaNo performs ...
       </Description>

       <Keyword>Some nice words</Keyword>
    </WaNoMeta>

    <WaNoRoot name="TemplateWaNo">
        Load the input files from a given folder
        Define a set of parameters
    </WaNoRoot>

    <WaNoExecCommand>
        Run the simulation
    </WaNoExecCommand>

    <WaNoInputFiles>
        Name of the mandatory files, e.g., scripts.
    </WaNoInputFiles>

    <WaNoOutputFiles>
        Define the expected output files
    </WaNoOutputFiles>
 </WaNoTemplate>

Every element is required to have a name attribute. This name cannot contain "." characters. Below
we give an overview of the meaning for each element inside the ``WaNoTemplate`` in the ``XML`` file above.

- ``WaNoMeta`` This field is dedicated to the developer information and describes the aims of the **WaNo**.
- ``WaNoRoot`` Here is where we define the set of parameters to be exposed and the inputs files of the simulation.
- ``WaNoExecCommand`` This part is a multiline string, which contains the script or program to execute, when the **WaNo** starts.
- ``WaNoInputFiles`` This segment is where we name all static input files, which have to be present in the **WaNo** folder.
- ``WaNoOutputFiles`` Here is where we name all the expected output files in the output directory. If not
  present, your **WaNo** will be shown as aborted (red folder).

2. Morse potential example
##########################

In this example, we want to include a python program in a new **WaNo**. This script computes the `Morse potential <https://en.wikipedia.org/wiki/Morse_potential>`_
:math:`V(r)=D_{e}[1-e^{-a(r-r_{e})}]^2-D_{e}` energy of  a particular diatomic molecule as a function of the intermolecular distance
:math:`(r-r_{e})` using  `Numpy <https://numpy.org/>`_. Here :green:`De` is the well depth energy relative to the atoms apart from each
other. :green:`a` controls the width of the potential, :math:`\color{green}{r_{e}}` gives the minimum potential distance. This
scrip loads ``.yml`` file from where it reads the inputs to compute the Morse potential energy. Via the command line, it is executed as follows:

.. code-block:: bash

 python/intepretor morse.py

2.1 Starting a new **WaNo** project
***********************************

At this point, we want to move from the code line above to a **SimStack** GUI. To incorporate a new tool, first, we create a new directory
with the **WaNo** name (see the code lines below) in the **WaNo** repository directory, see Paths configuration in :ref:`Configuration`
section. The **WaNo** name should be unique. In our example, we name it as *MORSE-pot*.

.. code-block:: bash

 mkdir Morse-Pot
 cd Morse-pot

Next, we create a *Morse-pot.xml* file, and this will specify the GUI elements in this **WaNo**. To give our new **WaNo** an
icon image, we may add an image *Morse-pot.png* directly in the **WaNo** folder. In such a way, the **SimStack** client will
automatically load this image on the node's area. Now, we have to consider what aspect in this simulation project we want to
emphasize, which parameters should be fixed, which are adjustable. For this particular case, we make all Morse potential parameters
flexible. Still, we think of Density Functional Theory, Molecular Dynamics, or Continues model codes, where we have many
parameters, which in principle, we are allowed to change. In a scenario of codes with a considerable number of parameters, exposing
all of them in most cases is unnecessary and not recommended. In this situation, we should focus only on the most relevant ones
for the problems we want to simulate.

The python script here named *morse.py* accepts arguments to define the Morse potential shape and specify inter-molecular
distance. The outputs are written in the ``MOROUT.yml`` file. For more details, see the code lines below.

.. literalinclude:: morse.py
  :linenos:
  :language: python

To get this ``.py`` file up running and take advantage of the GUI with the chosen parameters highlighted in yellow
below, we must put the script inside the ``WaNoInputFile`` tag, lines 31-33.

.. literalinclude:: Morse-pot.xml
  :linenos:
  :emphasize-lines: 18,19, 20, 21
  :language: XML

.. figure:: /assets/wano_edit.png
   :width: 800

**Fig 1** The arrows show the correspondence between the exposed parameter set in the GUI with the ``.xml`` tags.

- The *logical_filename* property in line 32 maps out the input file into the file name when transferred to the **SimStack** server.

- As mentioned above, ``MOROUT.yml`` is the expected output file of the script, and in the ``.xml`` files, it is managed by lines 35-37

- Regarding the adjustable parameters, we add them inside the ``WaNoRoot`` tag as shown in **Fig 1** and highlighted in the ``.py`` file.

- These parameters basically set up the shape of the Morse potential. Every parameter comes with its description.
