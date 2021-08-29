# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

from utils import file_helper


def deterministic_matched_filter(number_of_events, probs):
    base_folder = 'results/simulated/pileup_data'
    number_of_data = number_of_events * 2  # Due to the 50% training of S-MF.

    # For printing and files, probability must be in %.
    probs = np.array(probs) * 100

    for prob in probs:
        print(f'Simulated D-MF - Processing {number_of_data} events for signal for probability {prob}\n')

        # Pileup data
        base_data = f'{base_folder}/prob_{prob}/{number_of_data}_events'
        amplitude_file_name = f'{base_data}/base_data/tile_A.txt'
        signal_file_name = f'{base_data}/base_data/tile_signal.txt'
        noise_file_name = f'{base_data}/base_data/noise.txt'

        # Getting data from boundaries
        all_noises = pd.read_csv(noise_file_name, sep=" ", header=None)

        amplitude = pd.read_csv(amplitude_file_name, sep=" ", header=None)[:number_of_events]
        signal_testing = pd.read_csv(signal_file_name, sep=" ", header=None)[:number_of_events][:]
        noises = all_noises[:number_of_events][:]

        S = pd.DataFrame([0, 0.0172, 0.4524, 1.0000, 0.5633, 0.1493, 0.0424])

        C = noises.cov()

        C_i = np.linalg.inv(C)

        R = signal_testing

        S_t = S.T

        dmf_amplitude = ((R.dot(C_i)).dot(S)) / ((S_t.dot(C_i)).dot(S))[0]
        amp_error = dmf_amplitude - amplitude

        folder_name = f'{base_data}/D_MF'
        file_helper.save_file_in('dmf_amp_signal', folder_name, dmf_amplitude)
        file_helper.save_file_in('dmf_amp_error', folder_name, amp_error)


if __name__ == '__main__':
    number_of_events = 100
    probs = [0.0, 0.1, 0.5, 1.0]
    deterministic_matched_filter(number_of_events, probs)
