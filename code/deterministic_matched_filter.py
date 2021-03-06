# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

from utils import file_helper


def deterministic_matched_filter(noise_mean, tile_partition, sufix=''):
    print(f'Deterministic MF - Processing signal for mean {noise_mean}{sufix}\n')

    # Real data
    base_folder = 'results/hybrid'
    amplitude_file_name = f'{base_folder}/base_data/mu{noise_mean}/tile_A{sufix}.txt'
    signal_file_name = f'{base_folder}/base_data/mu{noise_mean}/tile_signal{sufix}.txt'
    noise_file_name = f'data/{tile_partition}/{tile_partition}mu{noise_mean}_no_ped{sufix}.txt'

    # Getting data from boundaries
    all_noises = pd.read_csv(noise_file_name, sep=" ", usecols=(3, 4, 5, 6, 7, 8, 9), header=None)
    number_of_data = int(len(all_noises) / 2)  # Only half part is needed due to the E-MF 50% training

    amplitude = pd.read_csv(amplitude_file_name, sep=" ", header=None)[:number_of_data]
    signal_testing = pd.read_csv(signal_file_name, sep=" ", header=None)[:number_of_data][:]
    noises = all_noises[:number_of_data][:]

    S = pd.DataFrame([0, 0.0172, 0.4524, 1.0000, 0.5633, 0.1493, 0.0424])

    C = noises.cov()

    C_i = np.linalg.inv(C)

    R = signal_testing

    S_t = S.T

    dmf_amplitude = ((R.dot(C_i)).dot(S)) / ((S_t.dot(C_i)).dot(S))[0]
    amp_error = amplitude - dmf_amplitude

    folder_name = f'{base_folder}/D_MF/mu{noise_mean}'
    file_helper.save_file_in(f'dmf_amp_signal{sufix}', folder_name, dmf_amplitude)
    file_helper.save_file_in(f'dmf_amp_error{sufix}', folder_name, amp_error)


if __name__ == '__main__':
    tile_partition = 'EBA'
    noise_mean = 30
    channel = 10
    deterministic_matched_filter(noise_mean, tile_partition, sufix=f'_ch{channel}')
