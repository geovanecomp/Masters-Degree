"""Generates signals and noises considering pileup scenario"""

import numpy as np
from utils import file_helper, pulse_helper

TILECAL_NUMBER_OF_CHANNELS = 7


# Generates a base data that will be randomized to simulate the real signal
def _base_data(number_of_data, pedestal):
    mu, sigma = pedestal, 1.5  # Mean and standard deviation
    return np.random.normal(mu, sigma, number_of_data)  # Base data


def _pileup_indexes(signal_probability, number_of_data):
    pu_indexes = np.random.permutation(number_of_data)
    # What about when "signal_probability" is float?
    pu_indexes = pu_indexes[0:int(signal_probability * number_of_data)]
    return pu_indexes


def _pileup():
    pileup_mean = 100  # Exponential pileup mean
    return np.random.exponential(pileup_mean)


# pileup should be added in the position "i" and then in its corners.
# for exemple, for n=100, i=97, and a 7th dimension signal we will have pileup
# added at positions 94, 95, 96, 97, 98, 99, 100
# TODO: Improve these magic numbers.
def _apply_pileup_indexes_when_tilecal(i, pu_indexes, x):
    pu = np.multiply(_pileup(), pulse_helper.get_jitter_pulse())
    number_of_data = len(x)

    if pu_indexes[i] < 4:
        for j in range(pu_indexes[i] - 2, 3):
            x[pu_indexes[i] + j] = x[pu_indexes[i] + j] + pu[j + 4]

    elif pu_indexes[i] > (number_of_data - 3):
        for j in range(-4, number_of_data - pu_indexes[i]):
            x[pu_indexes[i] + j] = x[pu_indexes[i] + j] + pu[j + 4]
    else:
        for j in range(-4, 3):
            x[pu_indexes[i] + j] = x[pu_indexes[i] + j] + pu[j + 4]
    return x


def _apply_pileup_indexes(i, pu_indexes, x):
    pu = np.multiply(_pileup(), pulse_helper.get_pulse_paper_COF())
    number_of_data = len(x)

    if pu_indexes[i] < 3:
        for j in range(pu_indexes[i]-2, 7):
            x[pu_indexes[i] + j] = x[pu_indexes[i] + j] + pu[j + 3]
    elif pu_indexes[i] > 999993:
        for j in range(-3, number_of_data - pu_indexes[i]):
            x[pu_indexes[i] + j] = x[pu_indexes[i] + j] + pu[j + 3]
    else:
        for j in range(-3, 7):
            x[pu_indexes[i] + j] = x[pu_indexes[i] + j] + pu[j + 3]
    return x


def pu_generator(number_of_events, signal_probabilities, pedestal, is_noise=False):
    number_of_data = TILECAL_NUMBER_OF_CHANNELS * number_of_events
    base_folder = 'results/simulated/pileup_data'

    for level in range(0, len(signal_probabilities)):
        signal_probability = signal_probabilities[level]  # Signal_probability
        signal_probability_percentage = signal_probability * 100
        signal_mean = 300  # Exponential signal mean

        print(f'PU Generator - Processing signal probability:  {signal_probability_percentage}%\n')

        x = _base_data(number_of_data, pedestal)
        pu_indexes = _pileup_indexes(signal_probability, number_of_data)

        if signal_probability > 0:
            for i in range(0, int(signal_probability * number_of_data)):
                x = _apply_pileup_indexes_when_tilecal(i, pu_indexes, x)

        # Formatting data
        data = np.reshape(x, (TILECAL_NUMBER_OF_CHANNELS, number_of_events))
        data = np.transpose(data)

        # Stores Noise Data
        folder_name = f'{base_folder}/prob_{signal_probability_percentage}'
        base_file_name = f'noise_prob_{signal_probability_percentage}'
        file_helper.save_file('tile_' + base_file_name, folder_name, data)

        # Stores mixed signal and amplitude
        folder_name = f'{base_folder}/prob_{signal_probability_percentage}'
        base_file_name = f'signal_prob_{signal_probability_percentage}'
        A = np.zeros(number_of_events)  # Amplitude
        for i in range(0, number_of_events):
            A[i] = np.random.exponential(signal_mean)  # Simulating true Amplitude
            data[i, :] = data[i, :] + np.multiply(A[i], pulse_helper.get_jitter_pulse())

        file_helper.save_file('tile_' + base_file_name, folder_name, data)
        file_helper.save_file('tile_A_' + base_file_name, folder_name, A)
        level += 1


if __name__ == '__main__':
    # Represents all possible probabilities of the cell receive signals
    # Example: 0.5 equals 50% of chance of receiving a signal in a collision.
    # We can use an array to generate signas for several probabilities.
    # signal_probabilities = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    signal_probabilities = [0.0, 0.5, 1.0]
    number_of_events = 10000
    pedestal = 0

    pu_generator(number_of_events, signal_probabilities, pedestal, is_noise=False)
