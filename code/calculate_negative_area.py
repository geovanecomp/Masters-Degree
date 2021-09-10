"""Calculates negative area of OF in its numeric amplitude"""

import os.path
import numpy as np

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    dataset = 'simulated_snr3'
    prob = 100.0
    num_events = 200000

    # Pile data
    BASE_PATH = DIR_PATH + f'/results/{dataset}/pileup_data/prob_{prob}/{num_events}_events'
    of_amplitude_file_name = BASE_PATH + '/OF/of_amp_signal.txt'

    of_amplitude = np.loadtxt(of_amplitude_file_name)

    neg_count = len(list(filter(lambda x: (x < 0), of_amplitude)))

    print(f'% of negative numbers in the amps list: {(neg_count/len(of_amplitude)) * 100}%')
