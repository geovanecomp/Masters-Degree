"""Generates signals and noises considering pileup scenario"""

import numpy as np
from utils import file_helper, pulse_helper

TILECAL_NUMBER_OF_CHANNELS = 7


def _save_jitter_file(file_name, folder_name, data):
    jitter_file_fmt = '%d', '%.7f', '%.7f', '%.7f', '%.7f', '%.7f', '%.7f', '%.7f'
    np.savetxt(
        f'{folder_name}/{file_name}.txt',
        data,
        fmt=jitter_file_fmt,
        delimiter=' ')


# Generates a base data that will be randomized to simulate the real signal
def _base_data(number_of_data, pedestal):
    mu, sigma = pedestal, 1.5  # Mean and standard deviation
    return np.random.normal(mu, sigma, number_of_data)  # Base data


def _pileup_indexes(signal_probability, number_of_data):
    pu_indexes = np.random.permutation(number_of_data)
    pu_indexes = pu_indexes[0:int(signal_probability * number_of_data)]
    return pu_indexes


def _pileup():
    pileup_mean = 100  # Exponential pileup mean
    return np.random.exponential(pileup_mean)


# Pileup should be added in the position "i" and then in its corners.
# for exemple, for n=100, i=97, and a 7th dimension signal we will have pileup
# added at positions 94, 95, 96, 97, 98, 99, 100
def _apply_pileup_indexes(i, pu_indexes, x):
    jitter_pulse, _ = pulse_helper.get_jitter_pulse()
    pu = np.multiply(_pileup(), jitter_pulse)
    number_of_data = len(x)

    first_pu_index = -3
    last_pu_index = 4
    index_in_left_corner = pu_indexes[i] <= 3
    index_in_right_corner = pu_indexes[i] >= (number_of_data - 3)
    off_set = 3

    # Start checking the corners 1st. then all intermediary values
    # Besides that, for cases when i=0 being the central value, j can be
    # -3, -2 or -1 sometimes, that is why we have "j+off_set", to fix this.
    if index_in_left_corner:
        for j in range(pu_indexes[i] - 1, last_pu_index):
            x[pu_indexes[i] + j -1] = x[pu_indexes[i] + j-1] + pu[j + off_set]
    elif index_in_right_corner:
        for j in range(first_pu_index, (number_of_data - pu_indexes[i])+1):
            x[pu_indexes[i] + j-1] = x[pu_indexes[i] + j-1] + pu[j + off_set]
    else:
        for j in range(first_pu_index, last_pu_index):
            x[pu_indexes[i] + j-1] = x[pu_indexes[i] + j-1] + pu[j + off_set]
    return x


def pu_generator(signal_mean, number_of_events, signal_probabilities, dataset, pedestal=0):
    number_of_data = TILECAL_NUMBER_OF_CHANNELS * number_of_events
    base_folder = f'results/{dataset}/pileup_data'
    number_of_jitter_info = TILECAL_NUMBER_OF_CHANNELS + 1
    jitters = np.zeros((number_of_events, number_of_jitter_info))

    for level in range(0, len(signal_probabilities)):
        signal_probability = signal_probabilities[level]  # Signal_probability
        signal_probability_percentage = signal_probability * 100

        print(f'PU {number_of_events} events Generator {signal_mean} ADCs - Processing signal probability:  {signal_probability_percentage}%\n')

        x = _base_data(number_of_data, pedestal)
        if signal_probability > 0:
            pu_indexes = _pileup_indexes(signal_probability, number_of_data)
            for i in range(0, int(signal_probability * number_of_data)):
                x = _apply_pileup_indexes(i, pu_indexes, x)
        # Formatting data to the tilecal shape (nx7)
        pu_data = np.reshape(x, (number_of_events, TILECAL_NUMBER_OF_CHANNELS))
        pu_signals = np.empty_like(pu_data)

        # Stores Noise Data
        folder_name = f'{base_folder}/prob_{signal_probability_percentage}/{number_of_events}_events/base_data'
        file_helper.save_file_in('noise', folder_name, pu_data)

        A = np.zeros(number_of_events)  # Amplitude
        for i in range(0, number_of_events):
            A[i] = np.random.exponential(signal_mean)  # Simulating true Amplitude
            jitter_pulse, jitter = pulse_helper.get_jitter_pulse()
            pu_signals[i, :] = pu_data[i, :] + np.multiply(A[i], jitter_pulse)
            jitters[i][0] = int(jitter)
            jitters[i][1:number_of_jitter_info] = jitter_pulse

        # Stores mixed signal and amplitude
        file_helper.save_file_in('tile_signal', folder_name, pu_signals)
        file_helper.save_file_in('tile_A', folder_name, A)

        # Its important to store jitter and use the same values across methods
        _save_jitter_file('jitter', folder_name, jitters)
        level += 1


if __name__ == '__main__':
    dataset = 'simulated'
    # Represents all possible probabilities of the cell receive signals
    # Example: 0.5 equals 50% of chance of receiving a signal in a collision.
    # We can use an array to generate signas for several probabilities.
    # signal_probabilities = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    signal_probabilities = [0.0, 0.1, 0.5, 1.0]
    # 300 ADC when converted to MeV it is equal to 3000MeV = 3GeV
    # In this case we are considering 1ADC=10MeV (instead of 12MeV)
    signal_mean = 300  # Exponential signal mean
    number_of_events = 200
    pedestal = 0

    pu_generator(signal_mean, number_of_events, signal_probabilities, dataset, pedestal)
