
# <p align="center"> CoVid-19 distribution<p>

This is a simple Python code evaluating the distribution of CoVid-19 for two different models, one based on probability theory and the other one based on the spreading factor of the virus. It also models the confinement effects on the spreading power of the virus.

## How to execute
It has a main point of entrance where you pass the data and can give a config. To execute it, the command is:

python coronavirus19.py <path to data file> [--config <path to config file>]

Where:
  - <path to data file> is a mandatory argument. It is the path to your data.
  - --config <path to config file> is optional. If given, the config file is a JSON file that defines all configuration options. If not given, it will use the default configuration.

You can also run:

python coronavirus19.py --help

## Structure of the code
The code is organised in 3 directories:
- **src** - This is where the source code is.
- **config** - This is where the boundary conditions are.
- **real_data** - This directory contains a file with real Spanish data for total CoVid-19 cases.
## What does it compute?

- **Infected** - Computes the number of infected population.
- **Non-infected** - Computes the number of non-infected population.
- **Immune** - Computes the number of immune population.
- **Deaths** - Computes the number of deaths.

## Comparison with real data
It is possible to compare with real data from worldometer.

Authors: dani.gallart@gmail.com and jeanbaptiste.favre@hotmail.fr

