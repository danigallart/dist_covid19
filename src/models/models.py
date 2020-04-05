import numpy as np


class CombinationAndProbabilityModel:
    def __init__(self, config, data):
        self.config = config
        self.data = data

        self.healthy = np.zeros(config.days) # Total number of healthy people at t = t_i
        self.infected = np.zeros(config.days) # Total number of infected people at t = t_i
        self.immune = np.zeros(config.days) # Total number of immune people at t = t_i
        self.deaths = np.zeros(config.days) # Total number of deaths up to t = t_i
        self.total_cases = np.zeros(self.config.days) # Total number of cases of CoVid-19 up to t = t_i

        self.healthy[0]  = self.config.population - self.infected[0] - self.immune[0]
        self.infected[0] = self.config.first_ill

        self.experimental = np.loadtxt(data)
        for _ in range(1, self.config.days - (len(self.experimental) - 1)):
            if len(self.experimental) <= self.config.days:
                self.experimental = np.append(self.experimental, 0.)

    # Model based on probability and combination theory
    def combination(self, a, b, c, d):
        """
        Model that takes into account a combination of
        all possible people that you can meet every day
        """
        combination = 1.0
        for i in range(0,d):
            combination = (float((round(a + b) - i)) / float((round(a + b + c) - i))) * combination
        return combination

    def run_model(self):
        # CALCULATIONS FOR COVID-19 DISTRIBUTION
        alpha2 = self.config.alpha
        for i in range(1, self.config.days):
            if i > self.config.k:
                alpha2 = int(self.config.alpha / self.config.confinement_alpha)
            self.healthy[i] = (1 - self.config.beta *
                (1 - self.combination(self.immune[i-1], self.healthy[i-1], self.infected[i-1], alpha2))) * self.healthy[i-1] # Second model based on probabilistic theory
            self.total_cases[i] = self.healthy[i-1] - self.healthy[i] + self.total_cases[i-1]
            if self.healthy[i] > 0:
                if i == self.config.k:
                    self.immune[i] = self.config.first_ill
                elif i > self.config.k:
                    self.deaths[i] = -(self.healthy[i - self.config.k] - self.healthy[i-(self.config.k + 1)]) * (self.config.death_rate) + self.deaths[i - 1]
                    self.immune[i] = -(self.healthy[i - self.config.k] - self.healthy[i - (self.config.k + 1)]) * (1. - self.config.death_rate) + self.immune[i - 1]

                self.infected[i] = -(self.healthy[i] - self.healthy[i - 1]) - (self.immune[i] + self.deaths[i] - (self.immune[i - 1] + self.deaths[i - 1])) + self.infected[i - 1]
