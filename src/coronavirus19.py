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

# IMPORTING CONSTANTS FROM initialconditions module
# Refer to the module for a description of each value
config = Config()


# Load experimental data for comparison with the model
experimental = np.loadtxt(os.path.join('..', 'real_data', 'Spain_Corona.txt'))

for i in range(1, config.days - (len(experimental) - 1)):
    if len(experimental) <= config.days:
        experimental = np.append(experimental, 0.)

# Second model based on probability and combination theory
def combination(a,b,c,d):
    """Model that takes into account a combination of
       all possible people that you can meet every day"""
    combination = 1.0
    for i in range(0,d):
        combination = (float((round(a + b) - i)) / float((round(a + b + c) - i))) * combination
    return combination

# Initialisation of arrays
healthy     = np.zeros(config.days) # Total number of healthy people at t = t_i
infected    = np.zeros(config.days) # Total number of infected people at t = t_i
immune      = np.zeros(config.days) # Total number of immune people at t = t_i
deaths      = np.zeros(config.days) # Total number of deaths up to t = t_i
total_cases = np.zeros(config.days) # Total number of cases of CoVid-19 up to t = t_i

infected[0] = config.first_ill
healthy[0]  = config.population - infected[0] - immune[0]

# CALCULATIONS FOR COVID-19 DISTRIBUTION
alpha2 = config.alpha
for i in range(1, config.days):
    if i > config.k:
        alpha2 = int(config.alpha / config.confinement_alpha)
    healthy[i] = (1 - config.beta * (1 - combination(immune[i-1], healthy[i-1], infected[i-1], alpha2))) * healthy[i-1] # Second model based on probabilistic theory
    total_cases[i] = healthy[i-1] - healthy[i] + total_cases[i-1]
    if healthy[i] > 0:
        if i == config.k:
            immune[i] = config.first_ill
        elif i > config.k:
            deaths[i] = -(healthy[i - config.k] - healthy[i-(config.k + 1)]) * (config.death_rate) + deaths[i - 1]
            immune[i] = -(healthy[i - config.k] - healthy[i - (config.k + 1)]) * (1. - config.death_rate) + immune[i - 1]

        infected[i] = -(healthy[i]-healthy[i - 1]) - (immune[i] + deaths[i] - (immune[i - 1]+deaths[i - 1])) + infected[i - 1]

plt.ylim(0, config.plot_y_lim)
plt.xlim(0, config.plot_x_lim)

if config.plot_infected:
    plt.plot(range(0, config.days), infected, label='infected')

if config.plot_immune:
    plt.plot(range(0, config.days), immune, label='immune')

if config.plot_healthy:
    plt.plot(range(0, config.days), healthy, label='healthy')

if config.plot_deaths:
    plt.plot(range(0, config.days), deaths, label='Deaths')

if config.plot_total_cases:
    plt.plot(range(0, config.days), total_cases, label='Total cases')

if config.plot_total_cases_experimental:
    plt.plot(range(0, config.days), experimental, label='Total cases_experimental')

plt.legend()
plt.show()
