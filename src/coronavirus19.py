################################################################################
#                        COVID-19 DISTRIBUTION MODEL
#                    By Jean-Baptiste Favre & Dani Gallart
#                                 24/03/2020
################################################################################

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

from initialconditions import Config
from models import CombinationAndProbabilityModel

# IMPORTING CONSTANTS FROM initialconditions module
# Refer to the module for a description of each value
config = Config()

# Creating the model
model = CombinationAndProbabilityModel(config, os.path.join('..', 'real_data', 'Spain_Corona.txt'))

model.run_model()

plt.ylim(0, config.plot_y_lim)
plt.xlim(0, config.plot_x_lim)

if config.plot_infected:
    plt.plot(range(0, config.days), model.infected, label='infected')

if config.plot_immune:
    plt.plot(range(0, config.days), model.immune, label='immune')

if config.plot_healthy:
    plt.plot(range(0, config.days), model.healthy, label='healthy')

if config.plot_deaths:
    plt.plot(range(0, config.days), model.deaths, label='Deaths')

if config.plot_total_cases:
    plt.plot(range(0, config.days), model.total_cases, label='Total cases')

if config.plot_total_cases_experimental:
    plt.plot(range(0, config.days), model.experimental, label='Total cases_experimental')

plt.legend()
plt.show()
