"""Generates signals and noises considering real noises"""

import numpy as np
import pandas as pd
from utils import file_helper, pulse_helper


def real_signals_generator(real_noises, noise_mean, sufix=''):
    dimension = 7
    amplitude_mean = 30  # Exponential signal mean
    number_of_events = len(real_noises)
    print(f'Real Signal Generator using mean: {noise_mean}{sufix}')

    folder_name = f'results/real_data/mu{noise_mean}'

    A = np.zeros(number_of_events)  # Amplitude
    data = np.zeros((number_of_events, dimension))
    for i in range(0, number_of_events):
        A[i] = np.random.exponential(amplitude_mean)  # Simulating true Amplitude
        data[i, :] = real_noises.values[i][:] + \
            np.multiply(A[i], pulse_helper.get_jitter_pulse())

    file_helper.save_file_in(f'tile_signal{sufix}', folder_name, data)
    file_helper.save_file_in(f'tile_A{sufix}', folder_name, A)


if __name__ == '__main__':
    noise_mean = 90
    sufix = '_small'
    tile_partition = 'LBA'
    real_noise_file_name = f'data/{tile_partition}/{tile_partition}mu{noise_mean}{sufix}_no_ped.txt'
    real_noises = pd.read_csv(real_noise_file_name, sep=" ", usecols=(3, 4, 5, 6, 7, 8, 9), header=None)
    real_signals_generator(real_noises, noise_mean, sufix)
