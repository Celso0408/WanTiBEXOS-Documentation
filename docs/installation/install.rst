============
Installation
============

.. raw:: html

    <style> .red {color: red !important} </style>
    <style> .green {color: green !important} </style>

.. role:: red
.. role:: green


To compile this code, you will need to have OpenMP, the Intel Fortran compiler, and the 
Math Kernel Library (MKL) installed on your computer. Once you have these libraries 
installed, you can follow these steps to install the code:

   1. Download the code at `https://github.com/ac-dias/wantibexos`
   2. Enter the code folder
   3. Edit the makefile if necessary
   4. Open the Linux terminal in the code folder and enter the command: `make all`
   5. All executable files will be located in the `bin` folder


.. note:: In the available makefile, the MKL library is called using the flag 
   "-qmkl" to compile the code. However, in older versions of the Intel 
   Fortran compiler, this library is called using the flag "-mkl".

Executable files
^^^^^^^^^^^^^^^^

   After compiling the code, seven executable files will be generated in the bin folder. 
   Each of them has the following functions:

      * `wtb.x`: This is the main executable file. It can be executed using the command: `wtb.x < input.dat`, where `input.dat` is the main input file. Note: This code does not contain an interface with MPI, so do not try to run it using the `mpirun -np` command.
      * `wtbf.x`: This file is faster than `wtb.x`, but it consumes more RAM memory during BSE calculations.
      * `dirgapf.x`: This post-processing script reads the `band.dat` file and finds both direct and indirect bandgaps. It can be executed using the command: `dirgapf.x nb nocp nk < bands.dat > dirgap.out`, where `nb`, `nocp`, and `nk` are the numbers of wannier projections, occupied states, and `k`-points used to generate the `band.dat` file, respectively.
      * `param_gen.x` or `param_gen_vasp.x`: These pre-processing tools are used to read the `wannier90.win` file and its output files, and then generate the MLWF-TB parameters file named `tb_hr.dat`. They should be executed in the folder containing the DFT and Wannier90 outputs. Before running these scripts, the `Wannier90 input.win` file must be renamed to `wannier90.win`.
      * `nc_nv_finder.x`: This post-processing tool can be used to estimate the number of conduction and valence states (`NBANDSC` and `NBANDSV`) necessary to provide a reliable dielectric function in the interval of `ENSPECI` to `ENSPECF`. To use this tool, enter the command: `nc_nv_finder.x < input.dat >> input.dat`.