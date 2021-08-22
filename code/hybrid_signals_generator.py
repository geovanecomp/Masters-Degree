"""Generates signals and noises considering real noises"""

import numpy as np
import pandas as pd
from utils import file_helper, pulse_helper


def _save_jitter_file(file_name, folder_name, data):
    jitter_file_fmt = '%d', '%.7f', '%.7f', '%.7f', '%.7f', '%.7f', '%.7f', '%.7f'
    np.savetxt(
        f'{folder_name}/{file_name}.txt',
        data,
        fmt=jitter_file_fmt,
        delimiter=' ')


def signals_generator(amp_mean, noises, noise_mean, sufix=''):
    dimension = 7
    number_of_events = len(noises)
    number_of_jitter_info = dimension + 1
    print(f'Hybrid Signal Generator amp{amplitude_mean} using mean: {noise_mean}{sufix}')

    folder_name = f'results/hybrid/amplitude_mean{amplitude_mean}/base_data/mu{noise_mean}'

    A = np.zeros(number_of_events)  # Amplitude
    jitters = np.zeros((number_of_events, number_of_jitter_info))
    data = np.zeros((number_of_events, dimension))
    for i in range(0, number_of_events):
        A[i] = np.random.exponential(amplitude_mean)  # Simulating true Amplitude
        jitter_pulse, jitter = pulse_helper.get_jitter_pulse()
        data[i, :] = noises.values[i][:] + np.multiply(A[i], jitter_pulse)

        jitters[i][0] = int(jitter)
        jitters[i][1:number_of_jitter_info] = jitter_pulse

    file_helper.save_file_in(f'tile_signal{sufix}', folder_name, data)
    file_helper.save_file_in(f'tile_A{sufix}', folder_name, A)
    _save_jitter_file(f'jitter{sufix}', folder_name, jitters)


if __name__ == '__main__':
    # 10 ADC when converted to MeV it is equal to 100MeV = 0.1GeV
    # In this case we are considering 1ADC=10MeV (instead of 12MeV)
    amplitude_mean = 10  # Exponential signal mean
    channel = 1
    noise_mean = 30

    sufix = f'_ch{channel}'
    tile_partition = 'EBA'
    noise_file_name = f'data/{tile_partition}/{tile_partition}mu{noise_mean}_no_ped{sufix}.txt'
    noises = pd.read_csv(noise_file_name, sep=" ", usecols=(3, 4, 5, 6, 7, 8, 9), header=None)
    signals_generator(amp_mean, noises, noise_mean, sufix)
