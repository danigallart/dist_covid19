# INITIAL CONDITIONS

# N = total country's population
# infected = number of people infected
# healthy = people still not infected
# immune = immune people



f = 1.65/7.                  # contagious factor (number of people infected by one person infected/day) 
k = 14                       # days to immunity
first_ill = 10               # number of people ill at time = 0
days_2 = 400                 # days of the simulation
population = 45000000.       # total Spain's population
days = range(0,days_2)       # days array
alpha = 45                   # people met every day
beta = 0.0098                # factor taking into account the probability of becoming infected
death_rate = 0.03            # percentage of death in infected population
confinement_factor = 1.      # factor dividing f after confinement restrictions
confinement_alpha = 1.85     # factor dividing alpha after confinement restrictions

