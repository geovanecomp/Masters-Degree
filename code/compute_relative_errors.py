"""Generates Partition data without Pedestal"""

# -*- coding: UTF-8 -*-
import numpy as np

from utils import file_helper


def _relative_error(exact_value, approx_value):
    return (approx_value - exact_value) / exact_value


if __name__ == '__main__':
    # Real data
    amplitude_means = [10, 100, 300]
    noise_means = [30, 50, 90]
    channels = [1, 10, 36]

    method_folder = 'D_MF'
    method_name = 'dmf'

    for amplitude_mean in amplitude_means:
        for noise_mean in noise_means:
            for channel in channels:
                sufix = f'_ch{channel}'
                print(f'Processing {method_folder} for Amplitude {amplitude_mean} and {noise_mean}{sufix}')
                base_folder = f'results/hybrid/amplitude_mean{amplitude_mean}'

                method_amp_file_name = f'{base_folder}/{method_folder}/mu{noise_mean}/{method_name}_amp_signal{sufix}.txt'
                reference_data_file_name = f'{base_folder}/base_data/mu{noise_mean}/tile_A{sufix}.txt'

                method_data = np.loadtxt(method_amp_file_name)
                reference_data = np.loadtxt(reference_data_file_name)[:len(method_data)]

                method_relative_error = _relative_error(reference_data, method_data)

                folder_name = f'{base_folder}/{method_folder}/mu{noise_mean}'
                file_helper.save_file_in(f'{method_name}_relative_error{sufix}', folder_name, method_relative_error)
