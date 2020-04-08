################################################################################
#                        COVID-19 DISTRIBUTION MODEL
#                    By Jean-Baptiste Favre & Dani Gallart
#                                 24/03/2020
################################################################################

import argparse

import matplotlib.pyplot as plt

from initialconditions import Config
from models import CombinationAndProbabilityModel


def plot(config, model):
    for i in range(1, config.days):
        if model.experimental[i - 1] != 0.:
            plt.ylim(0, model.experimental[i - 1])
            plt.xlim(0, i - 1)

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


def run(data, configuration):
    # IMPORTING CONSTANTS FROM initialconditions module
    # Refer to the module for a description of each value
    config = Config()
    if configuration:
        with open(configuration) as f:
            config.load(f)

    # Creating the model
    model = CombinationAndProbabilityModel(config, data)

    model.run_model()

    plot(config, model)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run some COVID-19 simulations")
    parser.add_argument("data", help="Data to process")
    parser.add_argument("--config", help="path to the configuration file")

    args = parser.parse_args()

    run(args.data, args.config)
