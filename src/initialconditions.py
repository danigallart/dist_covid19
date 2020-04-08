import json

# INITIAL CONDITIONS

# N = total country's population
# infected = number of people infected
# healthy = people still not infected
# immune = immune people

class Config:
    def __init__(self, *args, **kwargs):
        """
        By default this is the config for Spain
        """
        self.f = 1.65/7.               # contagious factor (number of people infected by one person infected/day)
        self.k = 14                    # days to immunity
        self.first_ill = 10            # number of people ill at time = 0
        self.days = 400                # days of the simulation
        self.population = 45000000.    # total Spain's population
        self.alpha = 45                # people met every day
        self.beta = 0.0098             # factor taking into account the probability of becoming infected
        self.death_rate = 0.03         # percentage of death in infected population
        self.confinement_factor = 1.   # factor dividing f after confinement restrictions
        self.confinement_alpha = 1.85  # factor dividing alpha after confinement restrictions
        self.plot_infected = False
        self.plot_immune = False
        self.plot_healthy = False
        self.plot_deaths = False
        self.plot_total_cases = True
        self.plot_total_cases_experimental = True
        self.plot_y_lim = 86000
        self.plot_x_lim = 33

    def load(self, config_file):
        """
        Loads a specific configuration from `config_file`
        """
        data = json.load(config_file)
        self.f = data["f"]
        self.k = data["k"]
        self.first_ill = data["first_ill"]
        self.population = data["population"]
        self.days = data["days"]
        self.alpha = data["alpha"]
        self.beta = data["beta"]
        self.death_rate = data["death_rate"]
        self.confinement_factor = data["confinement_factor"]
        self.confinement_alpha = data["confinement_alpha"]
        self.plot_infected = data["plot_infected"]
        self.plot_immune = data["plot_immune"]
        self.plot_healthy = data["plot_healthy"]
        self.plot_deaths = data["plot_deaths"]
        self.plot_total_cases = data["plot_total_cases"]
        self.plot_total_cases_experimental = data["plot_total_cases_experimental"]
        self.plot_y_lim = data["plot_y_lim"]
        self.plot_x_lim = data["plot_x_lim"]
