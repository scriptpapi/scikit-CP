[![PyPI version](https://badge.fury.io/py/scikit-CP.svg)](https://badge.fury.io/py/scikit-CP)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![](https://img.shields.io/appveyor/ci/MentalN/scikit-CP.svg)

# scikit-CP
scikit-CP is a computational physics simulation and modeling python scientific library. It is intended
for students or scientists seeking to integrate physics computational solutions into their python 
projects. It is written in and only compatible with Python 3. 

# Installation
The easiest way to use scikit-CP in your project is by adding it using your IDE's package manager:

In *PyCharm*, this would be by going to File > Settings > Project: <yourprojectname> > Project Interpreter > Install, and then searching for sciki-CP and clicking on Install Package.

In *Atom*, this would be by going to Settings > Install tab > and then searching for the package.

You can also just install the package to your environment using pip:
```
$pip3 install scikit-CP
```

# Available modules
Below is the currently available stable classes and simulation scripts, more are on the way.
Contributions are welcomed, but they mus follow the format of the project and be coded either as a 
simulation script or a class file for a physical object. A contribution tutorial is coming soon.

### Classical Mechanics
Classes:
 + Oscillator
 + Planet
 + Projectile
 
Simulation scripts:
 + Projectiles Collision Detector
 + Solar System

### Electricity and Magnetism
Simulation scripts:
 + Electric Field

### Random Systems
Classes:
 + Fluid (Percolation)
 + Substance (Diffusion)
 + Cluster (Growth)
 + Random Walker
 
Simulation scripts:
 + Random Walker Population
