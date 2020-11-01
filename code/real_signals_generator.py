"""Generates signals and noises considering real noises"""

import numpy as np
import pandas as pd
from utils import file_helper, pulse_helper


def real_signals_generator(real_noises, noise_mean):
    dimension = 7
    amplitude_mean = 300  # Exponential signal mean
    number_of_events = len(real_noises)
    print('Real Signal Generator')

    folder_name = 'real_data/mu{}'.format(noise_mean)

    A = np.zeros(number_of_events)  # Amplitude
    data = np.zeros((number_of_events, dimension))
    for i in range(0, number_of_events):
        A[i] = np.random.exponential(amplitude_mean)  # Simulating true Amplitude
        data[i, :] = real_noises.values[i][:] + \
            np.multiply(A[i], pulse_helper.get_jitter_pulse())

    file_helper.save_file_in('tile_signal', folder_name, data)
    file_helper.save_file_in('tile_A', folder_name, A)


if __name__ == '__main__':
    noise_mean = 50
    real_noise_file_name = 'data/ruidoMu{}par2modALLch1_semped.txt'.format(noise_mean)
    real_noises = pd.read_csv(real_noise_file_name, sep=" ", header=None)
    real_signals_generator(real_noises, noise_mean)
