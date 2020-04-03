################################################################################
#                        COVID-19 DISTRIBUTION MODEL
#                    By Jean-Baptiste Favre & Dani Gallart 
#                                 24/03/2020
################################################################################

import sys
sys.path.append('..\\bc')

import numpy as np
import matplotlib.pyplot as plt
import initialconditions as ic

#IMPORTING CONSTANTS FROM initialconditions module
#Refer to the module for a description of each value

f          = ic.f
k          = ic.k      
first_ill  = ic.first_ill
days_2     = ic.days_2
days       = ic.days 
alpha      = ic.alpha 
alpha2     = alpha
beta       = ic.beta
death_rate = ic.death_rate
population = ic.population

# Confinement factors for the two models
confinement_factor = ic.confinement_factor
confinement_alpha = ic.confinement_alpha

# Load experimental data for comparison with the model
experimental = np.loadtxt('..\\real_data\\Spain_Corona.txt')

for i in range(1,days_2 - (len(experimental) - 1)):
    if len(experimental) <= days_2:
        experimental = np.append(experimental,0.)

# First model based on a speading factor of CoVid-19
def factor(i): 
    """Model that takes into account a linear decrease
       of the spreading factor of Covid-19."""
    if i < k + 1:
        factor = f/population * (healthy[i] - population) + f
    elif i >= k + 1:
        factor = (f / confinement_factor) / population * (healthy[i] - population) + f / confinement_factor
    return factor

# Second model based on probability and combination theory
def combination(a,b,c,d):
    """Model that takes into account a combination of 
       all possible people that you can meet every day"""
    combination = 1.0
    for i in range(0,d):
        combination = (float((round(a + b) - i)) / float((round(a + b + c) - i))) * combination
    return combination

# Initialisation of arrays 
healthy     = np.zeros(days_2) # Total number of healthy people at t = t_i
infected    = np.zeros(days_2) # Total number of infected people at t = t_i
immune      = np.zeros(days_2) # Total number of immune people at t = t_i
deaths      = np.zeros(days_2) # Total number of deaths up to t = t_i
total_cases = np.zeros(days_2) # Total number of cases of CoVid-19 up to t = t_i

infected[0] = first_ill
healthy[0]  = population - infected[0] - immune[0]

#CALCULATIONS FOR COVID-19 DISTRIBUTION
for i in range(1,days_2):

#    healthy[i] = -infected[i-1]*factor(i-1) + healthy[i-1] # First model based on CoVid-19 spreading factor
    if i > k:
        alpha2 = int(alpha/confinement_alpha)
    healthy[i] = (1 -beta * (1 - combination(immune[i-1], healthy[i-1], infected[i-1], alpha2))) * healthy[i-1] # Second model based on probabilistic theory
#    healthy[i] = -alpha*population/2.0*beta/population**2*healthy[i-1]*infected[i-1]+healthy[i-1] # This model is certainly wrong ...
    total_cases[i] = healthy[i-1] - healthy[i] + total_cases[i-1]
    if healthy[i] > 0:
        if i == k:
            immune[i] = first_ill
        elif i > k:
            deaths[i] = -(healthy[i-k] - healthy[i-(k+1)]) * (death_rate) + deaths[i-1]
            immune[i] = -(healthy[i-k] - healthy[i-(k+1)]) * (1.-death_rate) + immune[i-1]
        infected[i] = -(healthy[i]-healthy[i-1]) - (immune[i] + deaths[i] - (immune[i-1]+deaths[i-1])) + infected[i-1] 

for i in range(1, days_2):
    if experimental[i-1] != 0.:
        plt.ylim(0, experimental[i-1])
        plt.xlim(0,i-1)

#plt.plot(days,r, label = 'infected')
#plt.plot(days,b, label = 'immune')
#plt.plot(days,n, label = 'healthy')
#plt.plot(days,deaths, label = 'Deaths')
plt.plot(days,total_cases, label = 'Total cases')
plt.plot(days,experimental, label = 'Total cases_experimental')
plt.legend()
plt.show()


#for i in range(0,399):
#    print(immune[i])





