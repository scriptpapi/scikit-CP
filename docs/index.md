# About scikit-CP
scikit-CP is a Python scientific code library for simulations and numerical solutions in the field of computational
physics. It is intended to be used by students, researchers, or teachers seeking to use computational physics solutions
in their projects.

Computational physics solutions are applied when a mathematical model describing exactly how a system behaves
does not yet exist. This is the case when the solution for a system does not have a closed-form expression, or is just 
too complicated.

We aim with scikit-CP to make use of Python scientific computing, with packages such as Numpy and SciPy, and make a one 
library for all of computational physics solutions. Long-term we aim to make scikit-CP able to solve any system 
computationally, and we aim to make that happen by making it easier for any physicist to contribute by adding a new
simulation script or new computational method for solving a physical system. 


# About the Documentation
This documentation lists all of the systems (of different physics fields) of which scikit-CP has a computational
solution available. It also documents the mathematics behind each computational solution.


# Organization of the Package Code
The package is divided into multiple directories, each directory categorizes scripts according to the phyical field.
For example, Projectile Trajectory script is under the Classical Mechanics directory. The random walker problem 
is under Random Systems. And the Electric Field Potential is under EM (Electricity and Magnetism) directory.

Within each physical field directory, the scripts will be either to simulate a physical object or a system (e.g.: 
oscillator, planet), or a simulation script of a physical phenomena that may or may not require the import of another 
physical object or a system modules (e.g.: oscillator.py, planet.py) within scikit-CP.


# Organization of the Documentation
Documentation is organized the following way:

Physics Field #1:
   + System 1: Description, Math/Derivation, Example.
   + Object 2: Description, Math/Derivation, Example.
   + System 2: Description, Math/Derivation, Example.
   
Physics Field #2:
   + Simulation script 1: Description, Math/Derivation, Example.
   + Simulation script 2: Description, Math/Derivation, Example.
   + Object 1: Description, Math/Derivation, Example.