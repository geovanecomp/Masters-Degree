import numpy as np

from pileup_signals_generator import pu_generator
from matched_filter import mf_calculation
from optimal_filter import of_calculation

np.set_printoptions(suppress=True)

BASE_FOLER = 'results/simulated'


def _save_file(file_name, file_folder, num_events, data):
    fileText = f'BASE_FOLER/{file_folder}/{num_events}_events/{file_name}.txt'

    np.savetxt(
        fileText,
        data,
        fmt='%.13f',
        delimiter=' ')


if __name__ == '__main__':
    num_runs = 10
    num_data = 20000
    training_percentage = 50
    num_events = int(num_data / (100 / training_percentage))
    pedestal = 30
    # probs = [0.0, 1.0]
    probs = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    probs_percentage = np.array(probs) * 100

    of_stds = dict.fromkeys(probs, 0)
    of_means = dict.fromkeys(probs, 0)

    mf_stds = dict.fromkeys(probs, 0)
    mf_means = dict.fromkeys(probs, 0)

    _of_stds = []
    _of_means = []

    _mf_stds = []
    _mf_means = []

    for prob in probs:
        # print('Processing signal probability:  {}%\n'.format(prob))
        for i in range(0, num_runs):
            # print('Execution number: {}\n'.format(i))

            # Generates a new data set for MF graph error
            pu_generator(num_events, [prob])

            of_calculation(num_events, [prob])
            mf_calculation(num_data, pedestal, [prob], training_percentage)

            of_error_file_name = f'{BASE_FOLER}/optimal_filter/{num_events}_events/pileup_prob_{prob * 100}_of_amp_error.txt'
            mf_error_file_name = f'{BASE_FOLER}/matched_filter/{num_events}_events/pileup_prob_{prob * 100}_amp_error.txt'
            of_error = np.loadtxt(of_error_file_name)
            mf_error = np.loadtxt(mf_error_file_name)

            _of_means.append(np.mean(of_error))
            _of_stds.append(np.std(of_error))

            _mf_means.append(np.mean(mf_error))
            _mf_stds.append(np.std(mf_error))

        of_means[prob] = _of_means
        of_stds[prob] = _of_stds

        mf_means[prob] = _mf_means
        mf_stds[prob] = _mf_stds

        _of_stds = []
        _of_means = []
        _mf_stds = []
        _mf_means = []

    folder_name = 'error_bar'
    prefix = '{}_runs_'.format(num_runs)
    of_prefix = prefix + 'of_'
    mf_prefix = prefix + 'mf_'

    for prob in probs:
        sufix = '_prob_{}'.format(prob * 100)
        _save_file(of_prefix + 'std' + sufix, folder_name, num_events, of_stds[prob])
        _save_file(of_prefix + 'mean' + sufix, folder_name, num_events, of_means[prob])

        _save_file(mf_prefix + 'std' + sufix, folder_name, num_events, mf_stds[prob])
        _save_file(mf_prefix + 'mean' + sufix, folder_name, num_events, mf_means[prob])
