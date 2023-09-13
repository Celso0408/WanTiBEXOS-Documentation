============
Hamiltonian
============

.. raw:: html

    <style> .red {color: red !important} </style>
    <style> .green {color: green !important} </style>

.. role:: red
.. role:: green


The orthogonal tight-binding Hamiltonian, :math:`H(\mathbf{k})`, obtained via the Wannier90 framework [Arash2008]_ can be 
written as follows,

.. math::
   :label: eq:hamiltonian

   \begin{equation}
        H(\mathbf{k}) = H_{0}+ \sum_{i=1}^{N} e^{i \mathbf{k} \cdot \mathbf{R_{i}}} H_{\mathbf{R_{i}}}~,
   \end{equation}
    
where :math:`H_{0}` corresponds to the Hamiltonian in unit cell, which contains the on-site energies 
and hopping parameters inside the cell. :math:`H_{\mathbf{R_{i}}}` corresponds to the hopping matrices, 
representing the interaction between unit cell and neighbors cells, while the matrix elements 
of :math:`H_{0}` and :math:`H_{\mathbf{R_{i}}}` are the output from the Wannier90 package [Wannier90] and 
the number of neighbors cell proportional to the :math:`\textbf{k}-mesh` used for Wannier interpolation. In our 
code the values of :math:`H_{0}` and :math:`H_{\mathbf{R_{i}}}` are declared in the :math:`\texttt{PARAMS\_FILE}`.

The electronic energy levels are obtained as the following:

.. math::
   :label: eq:eigenvalues

   \begin{equation}
       H(\mathbf{k}) |n,\mathbf{k} \rangle = E_{n,\mathbf{k}} |n,\mathbf{k} \rangle
   \end{equation}

where :math:`E_{n,\mathbf{k}}` and :math:`|n,\mathbf{k} \rangle` are the eigenvalues and eigenvectors respectively, :math:`n` 
corresponds to the band index, that could be addressed as :math:`v` for the valence (occupied) states and :math:`c` 
for the conduction (unoccupied) states, :math:`\mathbf{k}` are the :math:`\textbf{k}-point` in Brillouin zone.

==================
Optical properties
==================

To obtain the optical properties, we calculated the real and imaginary parts of the frequency dependent 
dielectric tensor, :math:`\epsilon_{1,\alpha,\beta}(\omega)` and  :math:`\epsilon_{2,\alpha,\beta}(\omega)`, 
respectively, through the following expressions:

.. math::
   :label: eq:dielectric_tensor

   \begin{align}
        \epsilon_{1,\alpha,\beta}(\omega) =  \delta_{\alpha,\beta} +  \frac{e^{2} S_{p}}{\epsilon_{0}\Omega N_{\mathbf{k}}} \sum_{\mathbf{k},c,v} F_{\alpha,\beta}^{c,v,\mathbf{k}} \frac{(E_{c,\mathbf{k}}-E_{v,\mathbf{k}})-\hbar \omega}{\left(\hbar \omega - (E_{c,\mathbf{k}}-E_{v,\mathbf{k}})\right)^{2}+\eta^{2}}~,
   \end{align}

.. math::
    :label: eq:dielectric_tensor2

    \begin{align}
       \epsilon_{2,\alpha,\beta}(\omega)=  \frac{ e^{2} S_{p}}{\epsilon_{0}\Omega N_{\mathbf{k}}} \sum_{\mathbf{k},c,v}  F_{\alpha,\beta}^{c,v,\mathbf{k}}   \frac{\eta}{\left(\hbar \omega - (E_{c,\mathbf{k}}-E_{v,\mathbf{k}})\right)^{2}+\eta^{2}}~,
    \end{align}

where :math:`\delta_{\alpha,\beta}` is a delta kroenecker, :math:`S_{p}` is the spin factor, being :math:`1` for 
SOC and spin polarized calculations and :math:`2` for non-polarized calculations, :math:`F_{\alpha,\beta}^{c,v,\mathbf{k}}`, 
in the scope of independent particle approximation (IPA), corresponds to the oscillator force, defined by:

.. math::
    :label: eq:oscillator_force

    \begin{equation}
        F_{\alpha,\beta}^{c,v,\mathbf{k}} =  \frac{\langle c,\mathbf{k} |P_{\alpha}|v,\mathbf{k} \rangle \langle v,\mathbf{k} |P_{\beta}|c,\mathbf{k} \rangle}{\left(E_{c,\mathbf{k}}-E_{v,\mathbf{k}}-i\eta_{1}\right) \left(E_{c,\mathbf{k}}-E_{v,\mathbf{k}}+i\eta_{1}\right)}~,
    \end{equation}

where :math:`\Omega` is the volume of unit cell, :math:`\epsilon_{0}` is the vacuum permittivity constant, :math:`N_{\mathbf{k}}` 
is the number of :math:`\textbf{k}-points` employed for the BZ integration, :math:`\omega` is the incident photon frequency, 
:math:`c(v)` corresponds to the conduction(valence) states. :math:`\eta` is a parameter to smooth the dielectric function, 
where :math:`\eta= \eta_{1}+\eta_{2}`, being :math:`\eta_{1}` defined by the input flag :math:`\texttt{CSHIFT}` and :math:`\eta_{2}` 
automatically defined by the code through the separation energy between the transition states. :math:`\alpha` and :math:`\beta` 
corresponds to the components :math:`x, y` and :math:`z` in the dielectric tensor. :math:`P_{\alpha}` corresponds to the 
light-matter interaction operator, which is given by,

.. math::
    :label: eq:light_matter

    \begin{equation}
        P_{\alpha} = \frac{\partial H(\mathbf{k})}{\partial k_{\alpha}}~,
    \end{equation}

where :math:`H(\mathbf{k})` corresponds to the electronic Hamiltonian, and  :math:`\alpha=`{:math:`x,y,z`}. For circularly 
polarized light, selected by the flag :math:`\texttt{CPOL= T}`, the light-matter interaction operator for :math:`\sigma_{\pm}` 
are written by the following expression:

.. math::
    :label: eq:light_matter_cpol

    \begin{equation}
        P_{\sigma_{\pm}} = \frac{1}{\sqrt{2}} \left( \frac{\partial H(\mathbf{k})}{\partial k_{x}}\pm i\frac{\partial H(\mathbf{k})}{\partial k_{y}}\right)~.    
    \end{equation}

It's well known the relation between the complex dielectric constant :math:`\epsilon(\omega)` and the complex refractive 
index :math:`\tilde{n}(\omega)=n(\omega)+i\kappa(\omega)`, where :math:`n(\omega)` is the refractive index and 
:math:`\kappa(\omega)` the extinction coefficient. They are related by:

.. math:: 
    :label: eq:refractive_index

    \begin{equation}
        \epsilon(\omega) =\tilde{n}^{2}(\omega)~,
    \end{equation}

separating :math:`\epsilon(\omega)` in real and imaginary part, :math:`\tilde{n}(\omega)` in refractive index and extinction 
coefficient we have:

.. math::
    :label: eq:refractive_index2

    \begin{equation}
        \epsilon_{1,\alpha,\beta}(\omega)+i\epsilon_{2,\alpha,\beta}(\omega) = n_{\alpha,\beta}^{2}(\omega) + 2 in_{\alpha,\beta}(\omega)\kappa(\omega)-\kappa_{\alpha,\beta}^{2}(\omega)~.
    \end{equation}
    
Then, we obtain the real and imaginary part of dielectric function, i.e.,

.. math::
    :label: eq:refractive_index3
    
    \begin{equation}
        \epsilon_{1,\alpha,\beta}(\omega)= n_{\alpha,\beta}^{2}(\omega) - \kappa_{\alpha,\beta}^{2}(\omega)~,
    \end{equation}

.. math::
    :label: eq:refractive_index4

    \begin{equation}
        \epsilon_{2,\alpha,\beta}(\omega)= 2 n_{\alpha,\beta}(\omega)\kappa_{\alpha,\beta}(\omega)~.
    \end{equation}

From these two equations we derive the expressions of the extinction coefficient and of the refractive index, as follows,

.. math::
    :label: eq:extinction_coefficient

    \begin{equation}
        \kappa_{\alpha,\beta}(\omega)= \left[\frac{\sqrt{\epsilon_{1,\alpha,\beta}^{2}(\omega)+\epsilon_{2,\alpha,\beta}^{2}(\omega)}-\epsilon_{1,\alpha,\beta}(\omega)}{2}\right]^{\frac{1}{2}}
    \end{equation}

.. math::
    :label: eq:refractive_index5

    \begin{equation}
        n_{\alpha,\beta}(\omega) = \left[\frac{\sqrt{\epsilon_{1,\alpha,\beta}^{2}(\omega)+\epsilon_{2,\alpha,\beta}^{2}(\omega)}+\epsilon_{1,\alpha,\beta}(\omega)}{2}\right]^{\frac{1}{2}}~.
    \end{equation}

The absorption coefficient :math:`A_{\alpha,\beta}(\omega)` is defined as:

.. math::
    :label: eq:absorption_coefficient
    \begin{equation}
        A_{\alpha,\beta}(\omega)=\frac{2\kappa_{\alpha,\beta}(\omega) \omega}{c} =\frac{\sqrt{2}\omega}{c} \left[\sqrt{\epsilon_{1,\alpha,\beta}^{2}(\omega)+\epsilon_{2,\alpha,\beta}^{2}(\omega)}-\epsilon_{1,\alpha,\beta}(\omega)\right]^{\frac{1}{2}}~.
    \end{equation}

where :math:`c` is the light speed. The reflectivity :math:`R_{\alpha,\beta}(\omega)` is defined by the refractive index and 
extinction coefficient by the following expression:

.. math::
    :label: eq:reflectivity

    \begin{equation}
        R_{\alpha,\beta}(\omega) = \frac{(n_{\alpha,\beta}(\omega)-1)^{2}+\kappa_{\alpha,\beta}^{2}(\omega)}{(n_{\alpha,\beta}(\omega)+1)^{2}+\kappa_{\alpha,\beta}^{2}(\omega)}~.
    \end{equation}

The energy loss function :math:`L_{\alpha,\beta}(\omega)` is defined as:

.. math::
    :label: eq:energy_loss_function

    \begin{equation}
        L_{\alpha,\beta}(\omega)=\frac{\epsilon_{2,\alpha,\beta}}{\epsilon_{1,\alpha,\beta}^{2}+\epsilon_{2,\alpha,\beta}^{2}}~. 
    \end{equation}

================
Berry Curvature
================

In solid state physics, the crystal symmetry rules the electronic band structure, as well as the nature  of  Bloch  
states. For the crystal with inversion symmetry, the Berry curvatures of the Bloch states are zero [Xiao2010]_. Nevertheless, 
in crystals with inversion asymmetry such as the :math:`\ce{MoS2}` monolayer and the :math:`\ce{WS2}/\ce{MoS2}` vdWs 
heterostructure, they are nonzero [Zhang2011]_, [Kormanyos2018]_ . Moreover, time reversal symmetry requires all 
Berry-phase related physical quantities to be valley-contrasting. To gain further insight into the electronic band 
structure and optical properties of the condensed-matter systems,  let us explore the Berry curvature 
:math:`\Omega_{n}(\textbf{k})`, dictated by, [Cai2013]_.

.. math::
    :label: eq:Berry_curvature 
  
    \begin{equation}
        \begin{split}
        & \Omega_{\rm n}(\bf k)= i \langle \nabla_{k} u_{n}\vert \times \vert \nabla_{k} u_{n}\rangle~, \\
        \label{Berry-1}
        \end{split}
    \end{equation}

where :math:`\vert u_{n} \rangle`is the :math:`n`-th Bloch state.

In this code, one can obtain the total Berry curvature (semiconductors only) either along certain 
:math:`\textbf{k}`-path :math:`(\texttt{KPATH\_FILE})`, using the flag :math:`\texttt{BERRY= T}`, or the 
whole BZ, using the flag :math:`\texttt{BERRY\_BZ= T}`. Total Berry curvature :math:`\Omega_{\alpha,\beta}(\mathbf{k})` 
are written by the following expression:

.. math::
    :label: eq:Berry_curvature2

    \begin{equation}
        \Omega_{\alpha,\beta} (\mathbf{k}) = -2 \text{Im} \sum_{v,c} \frac{\langle c,\mathbf{k} |P_{\alpha}|v,\mathbf{k} \rangle \langle v,\mathbf{k} |P_{\beta}|c,\mathbf{k} \rangle}{\left(E_{c,\mathbf{k}}-E_{v,\mathbf{k}}\right)^{2}}~.
    \end{equation}

The code only outputs the non-zero :math:`\Omega_{\alpha,\beta}(\mathbf{k})` components: :math:`\Omega_{x,y}(\mathbf{k})`, 
:math:`\Omega_{x,z}(\mathbf{k})` and :math:`\Omega_{y,z}(\mathbf{k})`. More details of Berry curvature calculation in 
the scope of MLWF, can be found in Wang's work [Wang2006]_.

==========================
Bethe--Salpeter Formalism
==========================

The Bethe--Salpeter equation (BSE) is a many-body equation that describes the interaction between an electron and a hole. The 
excitonic states are obtained through the solution of the two-particle problem via BSE [Dias2020]_, [Dias2021]_.
The excitonic Hamiltonian, :math:`H_{exc}`, is composed by the electron, :math:`H_{e}`, and hole, :math:`H_{h}`, 
single particle Hamiltonians plus Coulomb interaction potential, :math:`V_{eh}`, which binds the electron-hole pairs, i.e.,

.. math::
    :label: eq:excitonic_hamiltonian

    \begin{equation}
    H_{exc} = H_{e} + H_{h}+V_{eh}~.
    \end{equation}

The excitonic states with momentum center of mass :math:`\mathbf{Q}` can be expanded in terms of the product of 
electron and hole pairs wave functions, as follows,

.. math::
    :label: eq:Exc_Basis

    \begin{equation}
    \Psi_{ex}^{n}(\mathbf{Q}) = \sum_{c,v,\mathbf{k}} A_{c,v,\mathbf{k},\mathbf{Q}}^{n} \ \left( |c,\mathbf{k}+\mathbf{Q} \rangle \otimes |v,\mathbf{k} \rangle \right)~, \label{eq:Exc_Basis}
    \end{equation}

where the index :math:`c` and :math:`v` corresponds to the conduction and valence bands states, with momentum 
:math:`\mathbf{k}+\mathbf{Q}` and :math:`\mathbf{k}`, respectively. The problem of excitons eigenvalues, can be 
transformed into BSE, [Salpeter1951]_ using the expansion of Equation :eq:`eq:Exc_Basis`, it reads,

.. math::
    :label: eq:bse

    \begin{eqnarray}
        \left( E_{c,\mathbf{k}+\mathbf{Q}}-E_{v,\mathbf{k}}\right) A_{c,v,\mathbf{k},\mathbf{Q}}^{n}  +  \frac{1}{N_{k}}  \sum_{\mathbf{k'},v',c'} W_{(\mathbf{k},v,c),(\mathbf{k'},v',c'),\mathbf{Q}} \ A_{c',v',\mathbf{k'},\mathbf{Q}}^{n}  = E^{n}_{\mathbf{Q}} A_{c,v,\mathbf{k},\mathbf{Q}}^{n} \label{bse}~,
    \end{eqnarray}

where :math:`E^{n}_{\mathbf{Q}}` are the energy of n-th excitonic state with momentum :math:`\mathbf{Q}`, 
:math:`A_{c,v,\mathbf{k},\mathbf{Q}}^{n}` are the exciton wave function (eigenvector), which are obtained 
by solving Equation :eq:`eq:bse`. :math:`E_{c,\mathbf{k} + \mathbf{Q}} - E_{v,\mathbf{k}}` are the single-particle 
energy difference between a conduction band state :math:`c` with momentum :math:`\mathbf{k}+\mathbf{Q}` and 
a valence band state :math:`v` with momentum :math:`\mathbf{k}`, and :math:`W_{(\mathbf{k},v,c),(\mathbf{k'},v',c'),\mathbf{Q}}` 
are the many-body Coulomb interaction matrix element, which can be divided into two parts, direct interaction, :math:`W^d`, 
and exchange interaction, :math:`W^x`, respectively, i.e.,

.. math::
    :label: eq:W
    
    \begin{equation}
        W_{(\mathbf{k},v,c),(\mathbf{k'},v',c'),\mathbf{Q}}=W^d_{(\mathbf{k},v,c),(\mathbf{k'},v',c'),\mathbf{Q}}+W^x_{(\mathbf{k},v,c),(\mathbf{k'},v',c'),\mathbf{Q}}~.
    \end{equation}

Since the Coulomb potential varies slightly inside unit cell in comparison with Bloch functions, we can approximate the 
orbital character of Coulomb term in the following way:

.. math::
    :label: eq:Wd
    
    \begin{equation}
        W^{d}_{(\mathbf{k},v,c),(\mathbf{k'},v',c'),\mathbf{Q}}=V(\mathbf{k}-\mathbf{k'}) \ \langle c,\mathbf{k}+\mathbf{Q}|c',\mathbf{k'}+\mathbf{Q} \rangle \ \langle v',\mathbf{k'}|v,\mathbf{k} \rangle
    \end{equation}

and

.. math::
    :label: eq:Wx
    \begin{equation}
        W^{x}_{(\mathbf{k},v,c),(\mathbf{k'},v',c'),\mathbf{Q}}=-V(\mathbf{Q}) \ \langle c,\mathbf{k}+\mathbf{Q}|v,\mathbf{k} \rangle \ \langle v',\mathbf{k'}|c',\mathbf{k'}+\mathbf{Q} \rangle,
    \end{equation}

where, :math:`N_{k}` is the number of :math:`\textbf{k}-points` in the BZ. 

In BSE formalism, the real and imaginary parts of the frequency dependent dielectric tensor 
:math:`\epsilon^{BSE}_{1,\alpha,\beta}(\omega)` and  :math:`\epsilon^{BSE}_{2,\alpha,\beta}(\omega)` 
are obtained from the following expressions:

.. math::
    :label: eq:eps1

    \begin{align}
    \epsilon^{BSE}_{1,\alpha,\beta}(\omega) =  \delta_{\alpha,\beta} +  \frac{e^{2} S_{p}}{\epsilon_{0}\Omega N_{\mathbf{k}}} \sum_{n} F_{\alpha,\beta}^{n,BSE}  
    &\frac{E_{0}^{n}-\hbar \omega}{\left(\hbar \omega - E_{0}^{n}\right)^{2}+\eta^{2}}~,
    \end{align}

.. math::
    :label: eq:eps2

    \begin{align}
    \epsilon^{BSE}_{2,\alpha,\beta}(\omega)=  \frac{e^{2} S_{p}}{\epsilon_{0}\Omega N_{\mathbf{k}}}  \sum_{n}  F_{\alpha,\beta}^{n,BSE}   \frac{\eta}{\left(\hbar \omega - E_{0}^{n}\right)^{2}+\eta^{2}}~,
    \end{align}

where :math:`E_{0}^{n}` is the n-th direct :math:`(\mathbf{Q}=0)` excitonic state energy, :math:`F_{\alpha,\beta}^{n,BSE}` is 
the excitonic modulated oscillator force, given by, 

.. math::
    :label: eq:fosc

    \begin{align}
    F_{\alpha,\beta}^{n,BSE} = \left( \sum_{c,v,\mathbf{k}} \frac{A^{n}_{c,v,\mathbf{k},0}\langle c,\mathbf{k} |P_{\alpha}|v,\mathbf{k} \rangle}{\left(E_{c,\mathbf{k}}-E_{v,\mathbf{k}}+i\eta_{1}\right)} \right) \left(\sum_{c',v',\mathbf{k'}} \frac{A^{n*}_{c',v',\mathbf{k'},0}\langle v',\mathbf{k'} |P_{\beta}|c',\mathbf{k'} \rangle}{\left(E_{c',\mathbf{k'}}-E_{v',\mathbf{k'}}-i\eta_{1}\right)} \right)\label{eq:bse-fosc} ~. 
    \end{align}

===============================
Finite temperature BSE approach
===============================

The code also calculate the exciton energy levels, dielectric functions and other optical 
properties at a finite temperature for the excitons with :math:`\mathbf{Q}=0` by the flags :math:`\texttt{BSET= T}`,  
and :math:`\texttt{BSET\_BND= T}` to calculate exciton band structure. 
:red:`These flags cannot be combined with their counterparts without thermal effects` 
:math:`\texttt{BSE= T}` :red:`and` :math:`\texttt{BSE\_BND= T}`, :red:`respectively`. 
To incoporate the temperature effects, we have to modify BSE as follows [Albrecht1998]_, [Marini2008]_, and [MolinaSanchez2016]_.

.. math::
    :label: eq:bse-temp
    \begin{eqnarray}
    \left( \Xi_{c,\mathbf{k}+\mathbf{Q}}-E_{v,\mathbf{k}}\right) A_{c,v,\mathbf{k},\mathbf{Q}}^{n}  +  \frac{\left(f(E_{v,\mathbf{k}})-f(\Xi_{c,\mathbf{k}+\mathbf{Q}})\right)}{N_{k}}  \sum_{\mathbf{k'},v',c'} W_{(\mathbf{k},v,c),(\mathbf{k'},v',c'),\mathbf{Q}} \ A_{c',v',\mathbf{k'},\mathbf{Q}}^{n}  = E^{n}_{\mathbf{Q}} A_{c,v,\mathbf{k},\mathbf{Q}}^{n} \label{bse-temp}~,
    \end{eqnarray}

where :math:`f(E)` is the Fermi-Dirac distribution, and :math:`\Xi_{c,\mathbf{k}+\mathbf{Q}}` is the conduction 
band energy with a correction of temperature effects, defined as :

.. math::
    :label: eq:xi
    \begin{equation}
    \Xi_{c,\mathbf{k}+\mathbf{Q}} = E_{c,\mathbf{k}+\mathbf{Q}} - \Delta(\alpha_{B},\Theta,T)~,  
    \end{equation}

where :math:`T` is the temperature in :math:`K`, given by the flag :math:`\texttt{TEMP}`, :math:`\alpha_{B}` 
and :math:`\Theta` are empirical parameters to be fitted to experimental data, given by the flags :math:`\texttt{ST}` 
and :math:`\texttt{PHAVG}`, respectively, and the analytical expression of the correction :math:`\Delta(\alpha_{B},\Theta,T)` 
depends on the the approximations made in the calculation. Usually, the following three formulations have 
been widely used in the literature. The first one is the frozen atom approximation in which we assume 
:math:`\Delta(\alpha_{B},\Theta,T)=0`, given by the flag :math:`\texttt{TA= FA}`. The second one is  
Bose-Einstein approximation [Liu2020]_ given by the flag :math:`\texttt{TA= BE}`, where

.. math::
    :label: eq:be
    \begin{equation}
        \Delta(a_{B},\Theta,T) =  \frac{2 a_{B}}{e^{\Theta/T}-1}~,
    \end{equation}

where :math:`\alpha_B` represents the strength of electron-phonon interactions in \si{\electronvolt} 
and :math:`\Theta` is the average phonon temperature in :math:`K`. The third one is given by the 
flag :math:`\texttt{TA= VE}`, in which the correction term is described by [ODonnell1991]_.

.. math::
    :label: eq:ve
    \begin{equation}
        \Delta(\alpha_{B},\Theta,T) = \alpha_{B} \Theta \left[coth\left(\frac{\alpha_{B}}{2 k_{b} T}\right)-1\right]~,
    \end{equation}

where :math:`\Theta` is a dimensionless coupling constant and :math:`\alpha_B` is an average of phonon energy in :math:`eV`.

These temperature effects also correct the expressions for the oscillator force :math:`F_{\alpha,\beta}^{c,v,\mathbf{k}}` 
and  excitonic modulated oscillator force :math:`F_{\alpha,\beta}^{n,BSE}` by

.. math::
    :label: eq:force-temp
    \begin{equation}
        F_{\alpha,\beta}^{c,v,\mathbf{k}} =  \frac{\langle c,\mathbf{k} |P_{\alpha}|v,\mathbf{k} \rangle \langle v,\mathbf{k} |P_{\beta}|c,\mathbf{k} \rangle}{\left(\Xi_{c,\mathbf{k}}-E_{v,\mathbf{k}}-i\eta_{1}\right) \left(\Xi_{c,\mathbf{k}}-E_{v,\mathbf{k}}+i\eta_{1}\right)} \left(f(E_{v,\mathbf{k}})-f(\Xi_{c,\mathbf{k}})\right)~,
    \end{equation}    

.. math::
    :label: eq:force-bse-temp   
    \begin{align}
    F_{\alpha,\beta}^{n,BSE} = \left( \sum_{c,v,\mathbf{k}} \frac{A^{n}_{c,v,\mathbf{k},0}\langle c,\mathbf{k} |P_{\alpha}|v,\mathbf{k} \rangle}{\left(\Xi_{c,\mathbf{k}}-E_{v,\mathbf{k}}+i\eta_{1}\right)} \right) \left(\sum_{c',v',\mathbf{k'}} \frac{A^{n*}_{c',v',\mathbf{k'},0}\langle v',\mathbf{k'} |P_{\beta}|c',\mathbf{k'} \rangle}{\left(\Xi_{c',\mathbf{k'}}-E_{v',\mathbf{k'}}-i\eta_{1}\right)} \right) \left(f(E_{v',\mathbf{k'}})-f(\Xi_{c',\mathbf{k'}})\right) \label{eq:bse-t-fosc} ~. 
    \end{align}

==================
Coulomb Potentials
==================

Our code posses several options for the Coulomb interaction :math:`V_eh` (reciprocal space) in the BSE formalism. In 
this section we'll briefly discuss each of them. To avoid divergence in these potentials, a tolerance parameter 
:math:`\mathbf{Q}_{tol}` was introduced in our implementation, its value given by the flag :math:`\texttt{KTOL}`.

Bare Coulomb Potential (V3D)
----------------------------

This is the traditional Coulomb Potential in reciprocal space, being identified by the input flag
:math:`\texttt{COULOMB\_POT= V3D}`, and described by the following expression

.. math::
    :label: eq:v3d

    \begin{equation}
        V_{e h}(\mathbf{Q}) = \frac{4 \pi e^{2}}{\epsilon_{0} \mathbf{Q}^{2}}~,
    \end{equation}

where :math:`\epsilon_{0}` is the vacuum permittivity.

.. math::
    :label: eq:v3d

    \begin{equation}
    V(\mathbf{Q}) = -\frac{e^{2}}{2 V_{uc} \epsilon_{0}  \mathbf{Q}^2}~,  
    \end{equation}

where :math:`V_{uc}` is the unit cell volume. To avoid the divergence at :math:`\mathbf{Q} \rightarrow 0`, we define 

.. math::
    :label: eq:v3d

    \begin{equation}
        V(\mathbf{|Q|<Q_{tol}}) = 0. 
    \end{equation}

2D Keldysh Potential(V2DK)
--------------------------

A Keldysh type Coulomb potential normally be used to properly describe the 2D Coulomb 
interaction [Ridolfi2018]_. It's  selected by the flag 
:math:`\texttt{COULOMB\_POT= V2DK}` in main input file, with the following equation

.. math::
    :label: eq:v2dk

    \begin{equation}
        V(\mathbf{Q})=-\frac{e^{2}}{2 A_{uc} \epsilon_{0} \epsilon_{d} |\mathbf{Q}| (1+r_{0} |\mathbf{Q}|)}~. \label{keldysh-k}
    \end{equation}

with the objective to avoid Coulomb potential singularity, we make the following approximation 
for :math:`|\mathbf{Q}| \le \mathbf{Q}_{tol}`, 

.. math::
    :label: eq:v2dk

    \begin{equation}
        V(|\mathbf{Q}|  \le \mathbf{Q}_{tol} ) = \frac{-e^{2} a N_{k}}{4 \pi A_{uc} \epsilon_{0} \epsilon_{d}} \left[\alpha_{1}+\alpha_{2} \Delta+\alpha_{3} \Delta^{2} \right],
    \end{equation}

where :math:`\Delta=2 \pi r_{0} /a N_{k}`, and :math:`\alpha_{1}=1.76`, :math:`\alpha_{2}=1`, 
and :math:`\alpha_{3}=0` [Dias2020]_. :math:`N_{k}` is the number of :math:`\textbf{k}`-points used 
in :math:`\textbf{k}`-mesh, :math:`A_{uc}` is the unit cell area and :math:`a` is the average of 
the first and second lattice vectors size. The Coulomb potential screening length :math:`r_0` is given by the expression:

.. math:: 
    :label: eq:v2dk

    \begin{equation}
    r_0 = l_c \frac{(\epsilon_{2}-1)}{(\epsilon_{1}+\epsilon_{3})} ~,
    \end{equation}

and the effective dielectric constant :math:`\epsilon_{d}` is given by:

.. math::
    :label: eq:v2dk

    \begin{equation}
        \epsilon_{d} = \frac{\epsilon_{1}+\epsilon_{3}}{2} 
    \end{equation}

where :math:`l_{c}` is a free parameter, given by the flag :math:`\texttt{LC}`, 
that corresponds to the third lattice vector size or the distance between two neighbor 
layers of the 2D systems, :math:`\epsilon_{2}` are in plane macroscopic effective 
dielectric constant, given in the main input file by the flag :math:`\texttt{EDIEL}`, :math:`\epsilon_{1}` and 
:math:`\epsilon_{3}` corresponds to the dielectric constants of the substrate above and bellow, given by 
the flags :math:`\texttt{EDIEL\_T}` and  :math:`\texttt{EDIEL\_B}` respectively.

2D Rytova--Keldysh Potential (V2DRK)
------------------------------------

2D Rytova--Keldysh Potential is another version of a Keldysh type Coulomb potential used 
for 2D systems [VanTuan2018]_. It's selected by the flag :math:`\texttt{COULOMB\_POT= V2DRK}` 
in main input file, being described,

.. math::
    :label: eq:v2drk
    
    \begin{equation}
        V(\mathbf{Q}) =  -\frac{e^{2}}{2 A_{uc} \epsilon_{0} |\mathbf{Q}| F(\mathbf{Q})} e^{-w_{0} |\mathbf{Q}|}  ~,
    \end{equation}

where

.. math::
    :label: eq:v2drk

    \begin{equation}
        F(\mathbf{Q}) = \frac{\left[1-\left(p_{b} \ p_{t} \ e^{-2 |\mathbf{Q}| \eta l_{c} }\right)\right] \kappa}{\left[1-\left(p_{t} e^{-\eta |\mathbf{Q}| l_{c}}\right)\right] \left[1-\left(p_{b} e^{-\eta |\mathbf{Q}| l_{c}}\right)\right]} + r_{0} |\mathbf{Q}| e^{-w_{0} |\mathbf{Q}|} 
    \end{equation}

and

.. math::
    :label: eq:v2drk
    \begin{eqnarray}
    p_{b} = \frac{\epsilon_{b}-\kappa}{\epsilon_{b}+\kappa}~, \nonumber \\
    p_{t} = \frac{\epsilon_{t}-\kappa}{\epsilon_{t}+\kappa}~, \nonumber \\
    \kappa = \sqrt{\epsilon_{2} \epsilon_{z}}~, \nonumber \\
    \eta = \sqrt{\frac{\epsilon_{2}}{\epsilon_{z}}} ~,
    \end{eqnarray}

where :math:`A_{uc}` is the area of crystal unit cell, :math:`w_{0}` and :math:`r_{0}` are free 
parameters given by the flags :math:`\texttt{W\_COUL}` and :math:`\texttt{R\_0}` respectively. 
:math:`\epsilon_{2}` is the in plane effective dielectric constant of the crystal, given in the 
main input file by the flag :math:`\texttt{EDIEL}`, :math:`\epsilon_{z}` is the out of plane 
effective dielectric constant of the crystal, given by the flag :math:`\texttt{EDIEL\_Z}`, :math:`\epsilon_{b}` 
is the dielectric constant of the environment bellow the 2D system, given by the flag :math:`\texttt{EDIEL\_B}`,  
:math:`\epsilon_{t}` is the dielectric constant of the environment above the 2D system, given by the 
flag :math:`\texttt{EDIEL\_T}`. :math:`l_{c}` refers to the crystal thickness (in :math:`\mathrm{\mathring{A}}`), 
given by the flag :math:`\texttt{LC}`.

To avoid the divergence at :math:`\mathbf{Q} \rightarrow 0`, we consider the following 

.. math::
    :label: eq:v2drk

    \begin{equation}
        V(\mathbf{|Q|<Q_{tol}}) = 0~. 
    \end{equation}

2D truncated Coulomb Potential (V2DT)
-------------------------------------

A Coulomb potential truncated for 2D systems, proposed by Rozzi \textit{et. al.} [Rozzi2006]_ being 
selected by the flag \texttt{COULOMB\_POT= V2DT} in main input file. This potential has the following expression:

.. math::
    :label: eq:v2dt

    \begin{equation}
        V(\mathbf{Q}) =  -\frac{e^{2}}{2 V_{uc} \epsilon_{0}  \mathbf{Q}^2} \left[ 1 - e^{-C_{2}} \left( C_{1} \sin(C_3) - \cos(C_3) \right) \right]~,
    \end{equation}

where :math:`V_{uc}` is volume of the unit cell and :math:`\mathbf{r}_{3}` is the size of the third 
lattice vector (real space). C:math:`_1`, C:math:`_2` and C:math:`_3` are defined as,

.. math::
    :label: eq:v2dt

    \begin{eqnarray}
        C_{1} = \frac{|Q_{z}|}{\sqrt{Q_{x}^{2}+Q_{y}^{2}}}~,\nonumber \\
        C_{2} = \frac{\mathbf{r}_{3}}{2} \sqrt{Q_{x}^{2}+Q_{y}^{2}}~, \nonumber \\
        C_{3} = \frac{\mathbf{r}_{3}}{2} |Q_{z}|~.
    \end{eqnarray}

If :math:`\sqrt{Q_{x}^{2}+Q_{y}^{2}} < |\mathbf{Q}_{tol}|` and :math:`|Q_{z}| \ge |\mathbf{Q}_{tol}|`, then 
the Coulomb potential is described by,

.. math::
    :label: eq:vq

    \begin{equation}
        V(\mathbf{Q}) =  -\frac{e^{2} }{2 V_{uc} \epsilon_{0} \mathbf{Q}^2} \left[ 1 - \cos(0.5 |Q_{z}| 
        \mathbf{r}_{3}) - (0.5 |Q_{z}| \mathbf{r}_{3}) \sin(0.5 |Q_{z}| \mathbf{r}_{3})  \right] .
    \end{equation}


Else if :math:`\sqrt{Q_{x}^{2}+Q_{y}^{2}} < |\mathbf{Q}_{tol}|` and :math:`|Q_{z}| < |\mathbf{Q}_{tol}|`, 
then Coulomb potential becomes,

.. math::
    :label: eq:vq

    \begin{equation}
        V(\mathbf{Q}) = -\frac{e^{2} }{2 V_{uc} \epsilon_{0}} \left(\frac{\mathbf{r}_{3}^{2}}{8} \right)~,
    \end{equation}


2D truncated simplified Coulomb Potential (V2DT2)
-------------------------------------------------

A variation for the truncated Coulomb potential for 2D systems proposed by 
IsmailBeigi \textit{et. al.} [IsmailBeigi2006]_ being selected by the flag :math:`\texttt{COULOMB\_POT= V2DT2}` 
in main input file. It has the following expression:

.. math::
    :label: eq:v2dt2

    \begin{align}
        &V(\mathbf{Q}) =  -\frac{e^{2}}{2 V_{uc} \epsilon_{0}  \mathbf{Q}^2}  \left[1-\text{e}^{-Q_{xy}Z_{c}}\cos(Q_{z}Z_{c})\right] ~,
    \end{align}

where :math:`Q_{xy}=\sqrt{(Q_{x}^{2}+Q_{y}^{2})}`, :math:`V_{uc}` is the unit cell volume and :math:`Z_c` is half 
of the lattice vector in :math:`\hat{z}` direction, given by the flag :math:`\texttt{LC}`.

To avoid the divergence at :math:`\mathbf{Q} \rightarrow 0`, we suppose

.. math::
    :label: eq:v2dt2

    \begin{equation}
        V(\mathbf{|Q|<Q_{tol}}) = 0~. 
    \end{equation}

2D Ohno Potential (V2DOH)
-------------------------

Ohno Coulomb potential for 2D systems [Trolle2014]_ being selected by the 
flag :math:`\texttt{COULOMB\_POT= V2DOH}` in main input file. It is given by the following expression:

.. math::
    :label: eq:v2doh

    \begin{equation}
    V(\mathbf{Q}) =  -\frac{e^{2}}{2 A_{uc} \epsilon_{0} \epsilon_{d}  |\mathbf{Q}|}  e^{-w_{0} |\mathbf{Q}|}~,
    \end{equation}

where :math:`A_{uc}` is the unit cell area, :math:`\epsilon_{d}` is an effective dielectric constant parameter, 
given by the flag :math:`\texttt{EDIEL}`, :math:`w_{0}` is a free parameter given by the flag :math:`\texttt{W\_COUL}`.

To avoid the divergence at :math:`\mathbf{Q} \rightarrow 0`, we define

.. math::
    :label: eq:v2doh

    \begin{equation}
        V(\mathbf{|Q|<Q_{tol}}) = 0~. 
    \end{equation}

0D Potential (V0DT)
-------------------

An adaption of the Coulomb potential for 0D systems, proposed by Rozzi :math:`\textit{et. al.}` [Rozzi2006]_, 
being selected by the flag :math:`\texttt{COULOMB\_POT= V0DT}` in main input file. It is described 
by the following expression:

.. math:: 
    :label: eq:v0dt

    \begin{equation}
    V(\mathbf{Q}) =  -\frac{e^{2}}{2 V_{uc} \epsilon_{0}  \mathbf{Q}^{2}} \left[1- \cos(0.5 \mathbf{r}_{min} |\mathbf{Q}|) \right] 
    \end{equation}

To avoid the divergence at :math:`\mathbf{Q} \rightarrow 0`, we consider the following condition

.. math::
    :label: eq:v0dt
    \begin{equation}
        V(\mathbf{|Q|<Q_{tol}}) =  -\frac{e^{2} }{2 V_{uc} \epsilon_{0}} \left(\frac{\mathbf{r}_{min}^{2}}{8} \right) ~. 
    \end{equation}

where :math:`V_{uc}` is the unit cell volume and :math:`\mathbf{r}_{min}` is the size of the smallest lattice vector (real space).

==========================
Exciton radiative lifetime
==========================

In this code the exciton radiative lifetime is calculated directly from the excitonic state oscillator 
force (:math:`F_{\alpha,\beta}^{n,BSE}`), described in equation :eq:`eq:fosc`. Being calculated using 
the flag :math:`\texttt{BSE= T}` combined with :math:`\texttt{SPEC= T}`, where the lifetime is obtained 
in seconds. This quantity is only calculated for direct excitons.

For 3D systems (:math:`\texttt{SYSDIM= 3D}`), the lifetime, for the n-th excitonic states, is 
obtained by,

.. math:: 
    :label: eq:tau3d

    \begin{equation}
        \tau_{3D,\alpha,\beta}^{n} = \frac{3 c^{2}  \hbar^{3} N_{\mathbf{k}} }{4 \chi  \left(E_{0}^{n}\right)^{3}  F_{\alpha,\beta}^{n,BSE}} ~.
    \end{equation}

While for 2D systems (:math:`\texttt{SYSDIM= 2D}`), a similar expression is given by [Palummo2015]_

.. math::
    :label: eq:tau2d

    \begin{equation}
        \tau_{2D,\alpha,\beta}^{n} = \frac{\hbar A_{uc} N_{\mathbf{k}} }{8 \pi \chi E_{0}^{n}  F_{\alpha,\beta}^{n,BSE}}~.
    \end{equation}

Finally for 1D systems (:math:`\texttt{SYSDIM= 1D}`), it is described by [Spataru2005]_

.. math::
    :label: eq:tau1d

    \begin{equation}
        \tau_{1D,\alpha,\beta}^{n} = \frac{c \hbar^{2} \mathbf{r}_{1} N_{\mathbf{k}} }{2 \pi \chi  \left(E_{0}^{n}\right)^{2} F_{\alpha,\beta}^{n,BSE}} ~,
    \end{equation}

where :math:`c` is the light speed, :math:`E_{0}^{n}` is the n-th excitonic state energy, :math:`A_{uc}` is 
the 2D crystal unit cell area, :math:`\mathbf{r}_{1}` is the 1D unit cell size and :math:`\chi` is the fine 
structure constant, given by:

.. math::
    :label: eq:chi
 
    \begin{equation}
        \chi = \frac{e^{2}}{4 \pi \epsilon_{0} \hbar c} \approx \frac{1}{137}~.
    \end{equation}


================
k-mesh generator
================

The :math:`\textbf{k}`-meshes are generated using the Monkhorst--Pack scheme [Monkhorst1976]_, 
where the :math:`\textbf{k}`-points are defined by the following expression 
:math:`\texttt{NGY}` and :math:`\texttt{NGZ}` in the input file, it's possible to define it 
through the flags :math:`\texttt{MESH\_TYPE= RK3D}` or :math:`\texttt{MESH\_TYPE= RK2D}`, 
choosing a density of :math:`\textbf{k}`-points defined by the flag :math:`\texttt{RK}`. The 
values of :math:`\texttt{NGX}`, :math:`\texttt{NGY}` and :math:`\texttt{NGZ}`, are obtained 
for the option :math:`\texttt{MESH\_TYPE= RK3D}` by the following expression:

.. math::
    :label: eq:ngxyz

    \begin{eqnarray}
        NGX = int \left(max\left(1,\texttt{RK} \frac{|\mathbf{b}_{1}|}{2 \pi}+0.5\right)\right)\nonumber \\
        NGY = int \left(max\left(1,\texttt{RK} \frac{|\mathbf{b}_{2}|}{2 \pi}+0.5\right)\right) \nonumber \\
        NGZ = int \left(max\left(1,\texttt{RK} \frac{|\mathbf{b}_{3}|}{2 \pi}+0.5\right)\right)
    \end{eqnarray}

for the option :math:`\texttt{MESH\_TYPE= RK2D}` the only difference is that :math:`\texttt{NGZ=1}` 
independent of :math:`\texttt{RK}`.

======================================
Solar Cell Power Conversion Efficiency
======================================

To estimate the power conversion efficiency (PCE), of the studied system, in the scope of 
Shockley-Queisser Limit (SQ-limit), [Shockley1961]_ and spectroscopy limited maximum efficiency (SLME) 
scheme [Yu2012]_. This simulation is available by the input flag :math:`\texttt{PCE= T}`.

Both approximations are based on the principle of detailed balance between absorbed photons and emitted 
photons. Below, we will summarize the mathematical formalism [Bercx2018]_ and the SQ-limit and SLME approximations.

The PCE is defined as the maximum output power density (:math:`P_{\text{PV}}`) from the photovoltaic device 
divided by the total incoming power density from the solar spectrum, :math:`P_{solar}`, as follows,

.. math::
    :label: eq:pce

    \begin{equation}
        \text{PCE} = \frac{P_{\text{PV}}}{P_{solar}}~,
    \end{equation}

where

.. math::
    :label: eq:psolar
    
    \begin{equation}
        P_{solar} = \int_{0}^{\infty}P(E)dE~,
    \end{equation}

and :math:`P(E)` is the solar energy flux, which is selected by the flag :math:`\texttt{SES}`, and has 
the options: :math:`\texttt{AM15G}`, :math:`\texttt{AM15D}` and :math:`\texttt{AM0G}`, which corresponds 
to the standard solar spectrum for non-concentrated photovoltaic conversion, taking light absorption 
and scattering in the atmosphere into account [Astm2012]_. The output power density is 
described by the product :math:`J(V)V`, as the maximum output power density (:math:`P_{\text{PV}}`) is 
obtained maximizing the :math:`J-V` characteristic of an illuminated solar cell : 

.. math::
    :label: eq:pv

    \begin{equation}
        P_{\text{PV}} = J(V_{max}) V_{max}~,
    \end{equation}

where :math:`V_{max}` is the voltage that results in the maximum output power density. The open circuit voltage 
:math:`V_{oc}` is the voltage that minimizes :math:`J(V)`. In this method, the current density, :math:`J(V)`, 
are described by the following expression:

.. math::
    :label: eq:jv

    \begin{equation}
    J(V) = J_{sc}-\frac{J_{0}}{fr}\left(exp\left(\frac{e V}{k_{\text{B}}T}\right)-1\right)~,
    \end{equation}

where :math:`k_{\text{B}}` is Boltzmann's constant, :math:`e` is the elementary charge, :math:`fr` is the 
radiative electron-hole recombination fraction and :math:`T` is the temperature of the solar cell, 
defined by the flag :math:`\texttt{CTEMP}`. :math:`J_{sc}` is the short-circuit current density, also 
known as the illuminated current or photogenerated current, calculated from the following expression,

.. math::
\begin{equation}
J_{sc} = e\int_{0}^{\infty}a(E)\frac{P(E)}{E}dE~.
\end{equation}
:math:`a(E)` is the absorbance, which is defined as the ratio of power absorbed by the solar device over the 
power of incident sunlight.

:math:`J_{0}` is the reverse saturation current density, calculated considering the detailed balance principle 
when in equilibrium conditions, the photon emission rate from radiative recombination is equal to the photon 
absorption from the surrounding environment. This was done considering our solar cell attached to an ideal 
heat sink, expecting the cell temperature to be the ambient temperature.  Hence, the spectrum of the 
surrounding environment is that of a black body at cell temperature :math:`T`,

.. math::
    :label: eq:phi

    \begin{equation}
    J_{0} = e \pi \int_{0}^{\infty} a(E) \Phi_{bb}(E) dE~,
    \end{equation}

where,

.. math::
    :label: eq:phibb

    \begin{equation}
    \Phi_{bb}(E) = \frac{2E^{2}}{h^{3}v_{c}^{2}} \left(e^{\frac{E}{k_{\text{B}}T}}-1\right)^{-1}~, 
    \end{equation}

and :math:`h` is Planck's constant and :math:`v_{c}` is the speed of light. Complementary we can 
also calculate the Fill-Factor (:math:`FF`) of our solar device, by the expression:

.. math::
    :label: eq:ff

    \begin{equation}
        FF = \frac{V_{max} J(V_{max})}{V_{oc} J_{sc}}~.
    \end{equation}

Shockley--Queisser Limit
------------------------

In the SQ-limit approximation, we consider the absorbance, :math:`a(E)`, as a Heaviside step function, 
where all photons with energy higher or equal to the energy bandgap, :math:`E_g`, are absorbed, i.e., 
:math:`a(E) = 1` for :math:`E{~}\ge{~}E_{g}`, and :math:`a(E) = 0` for :math:`E{~}<{~}E_{g}`. Furthermore, 
this approximation assumes :math:`fr = 1`, i.e., the radiative recombination process is the only 
recombination process for all systems, neglecting the non-radiative recombinations (e.g., Auger recombination) 
due to indirect bandgap [Huldt1971]_, [Green_671_1984]_.

Spectroscopy Limited Maximum Efficiency
---------------------------------------

In contrast with the SQ-limit approach, the SLME approximation requires the total absorption coefficient,

.. math::
    :label: eq:alpha

    \begin{equation}
        \alpha(E) = \frac{4\pi}{\lambda}k(E)~,
    \end{equation}

where :math:`k(E)` is the imaginary part of the dielectric function, :math:`\epsilon(E)`, and :math:`\lambda`

.. math::
    :label: eq:lambda

    \begin{equation}
        A(\omega)=A_{x,x}(\omega)+A_{y,y}(\omega)+A_{z,z}(\omega)~,
    \end{equation}

material thickness, :math:`\Delta`, and the bandgaps. Its also considers the non-radiative 
recombination in the solar cell by modeling the fraction of radiative recombination, :math:`fr`, using a 
Boltzmann factor [Yu2012]_,

.. math::
    :label: eq:fr

    \begin{equation}
    fr = e^{-\frac{\delta}{k_{B}T}} 
    \end{equation}

for calculations in the scope of IPA (without excitons), we can define :math:`\delta = E_{op}-E_{g}`, where :math:`E_{op}` 
is the optical bandgap, given by the flag :math:`\texttt{EGD}` and :math:`E_{g}` is the fundamental energy 
bandgap, given by the flag :math:`\texttt{EG}`. In the scope of BSE (with excitonic effects), we can define 
:math:`\delta = Ex_{br}-Ex_{gs}`, where :math:`Ex_{br}` is the exciton bright ground state (optical bandgap 
considering excitonic effects), given by the flag :math:`\texttt{EBGS}`, while :math:`Ex_{gs}` is the exciton 
ground state, given by the flag \texttt{EGS}. The absorbance, :math:`a(E)`, is obtained considering the solar cell 
with the same conditions of SQ-Limit described previously, given by the following expression [Yu2012]_, [Duan2019]_.

.. math::
    :label: eq:a

    \begin{equation}
    a(E) = 1 - e^{-2 \ A(\omega) \ \Delta}~,  
    \end{equation}

where :math:`E = \hbar\omega`, and :math:`\Delta` is the material thickness, in this code we calculate 
the PCE, in the scope of SLME method from :math:`\Delta=0` until :math:`\Delta= \Delta_{max}`, being 
:math:`\Delta_{max}` defined by the flag :math:`\texttt{THMAX}`. 


==========
References
==========

    .. [Wannier90] https://doi.org/10.1016/j.cpc.2007.11.016 
    .. [Xiao2010] https://doi.org/10.1103/RevModPhys.82.1959
    .. [Zhang2011] https://doi.org/10.1103/PhysRevLett.106.156801
    .. [Cai2013] https://doi.org/10.1103/PhysRevB.88.115140
    .. [Kormanyos2018] https://doi.org/10.1103/PhysRevB.98.035408
    .. [Wang2006] https://doi.org/10.1103/PhysRevB.74.195118
    .. [Dias2020] https://doi.org/10.1103/PhysRevB.101.085406
    .. [Dias2021] https://pubs.acs.org/doi/10.1021/acsaem.0c03039
    .. [Salpeter1951] https://doi.org/10.1103/PhysRev.84.1232
    .. [Albrecht1998] https://doi.org/10.1103/PhysRevLett.80.4510
    .. [Marini2008] https://doi.org/10.1103/PhysRevLett.101.106405
    .. [MolinaSnchez2016] https://doi.org/10.1103/PhysRevB.93.155435 
    .. [Liu2020] https://doi.org/10.1038/s41598-020-71808-y
    .. [ODonnell1991] https://doi.org/10.1063/1.104723
    .. [Ridolfi2018] https://doi.org/10.1103/PhysRevB.97.205409
    .. [VanTuan2018] https://doi.org/10.1103/PhysRevB.98.125308
    .. [Rozzi2006] https://doi.org/10.1103/PhysRevB.73.205119
    .. [IsmailBeigi2006] https://doi.org/10.1103/PhysRevB.74.233103
    .. [Trolle2014] https://doi.org/10.1103/PhysRevB.89.235410
    .. [Spataru2005] https://doi.org/10.1103/PhysRevLett.95.247402
    .. [Palummo2015] https://doi.org/10.1021/nl503799t
    .. [Monkhorst1976] https://doi.org/10.1103/PhysRevB.13.5188
    .. [Yu2012] https://doi.org/10.1103/PhysRevLett.108.068701
    .. [Bercx2018] https://doi.org/10.1007/978-3-319-72374-7_15
    .. [Astm2012] https://doi.org/10.1520/g0173-03r20
    .. [Shockley1961] https://doi.org/10.1063/1.1736034
    .. [Huldt1971] https://doi.org/10.1002/pssa.2210080118
    .. [Green1984] https://10.1109/T-ED.1984.21588
    .. [Duan2019] https://doi.org/10.1039/C9TA06674H