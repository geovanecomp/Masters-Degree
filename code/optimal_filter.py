import numpy as np
import pandas as pd

from utils import file_helper

np.set_printoptions(suppress=True)


if __name__ == '__main__':
    num_events = 100

    amplitude = pd.read_csv('results/base_data/{}-events/amplitude.txt'.format(num_events), sep=" ", header=None)
    signal_testing = pd.read_csv('results/base_data/{}-events/signal_testing.txt'.format(num_events), sep=" ", header=None)

    weights = pd.DataFrame([-0.37873481, -0.35634348, 0.17828771, 0.81313877, 0.27867064, -0.20540129, -0.32961754])

    if num_events != len(amplitude):
        print('Dimension error!')

    of_amplitude = signal_testing.dot(weights)
    amp_error = amplitude - of_amplitude

    file_helper.save_file('of_amplitude', 'optimal_filter', of_amplitude)
    file_helper.save_file('amp_error', 'optimal_filter', amp_error)
