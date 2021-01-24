# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

from utils import file_helper


def deterministic_A(noise_mean, number_of_data, sufix=''):
    tile_partition = 'LBA'

    print(f'Deterministic MF - Processing signal for mean {noise_mean}{sufix}\n')

    # Real data
    base_folder = f'results/real_data/mu{noise_mean}'
    amplitude_file_name = f'{base_folder}/tile_A{sufix}.txt'
    signal_file_name = f'{base_folder}/tile_signal{sufix}.txt'
    real_noise_file_name = f'data/{tile_partition}/{tile_partition}mu{noise_mean}{sufix}_no_ped.txt'

    # Getting data from boundaries
    amplitude = pd.read_csv(amplitude_file_name, sep=" ", header=None)[:number_of_data]
    signal_testing = pd.read_csv(signal_file_name, sep=" ", header=None)[:number_of_data][:]
    real_noises = pd.read_csv(real_noise_file_name, sep=" ", usecols=(3, 4, 5, 6, 7, 8, 9), header=None)

    S = pd.DataFrame([0, 0.0172, 0.4524, 1.0000, 0.5633, 0.1493, 0.0424])

    C = real_noises.cov()
    C_i = np.linalg.inv(C)

    R = signal_testing

    S_t = S.T

    dmf_amplitude = ((R.dot(C_i)).dot(S)) / ((S_t.dot(C_i)).dot(S))[0]
    amp_error = amplitude - dmf_amplitude

    folder_name = f'{base_folder}/deterministic_matched_filter'
    file_helper.save_file_in(f'dmf_amp_signal{sufix}', folder_name, dmf_amplitude)
    file_helper.save_file_in(f'dmf_amp_error{sufix}', folder_name, amp_error)


if __name__ == '__main__':
    noise_mean = 30
    number_of_data = 200000
    deterministic_A(noise_mean, number_of_data, sufix='_small')
