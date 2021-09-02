import numpy as np

from simulated_pileup_signals_generator import pu_generator
from simulated_signals_stochastic_matched_filter import smf_calculation
from simulated_signals_deterministic_matched_filter import dmf_calculation
from simulated_signals_optimal_filter import of_calculation

np.set_printoptions(suppress=True)

DATA_SET = 'simulated_snr1'
BASE_FOLER = f'results/{DATA_SET}/pileup_data'


def _save_file(file_name, file_folder, num_events, data):
    fileText = f'{BASE_FOLER}/{file_folder}/{num_events}_events/{file_name}.txt'

    np.savetxt(
        fileText,
        data,
        fmt='%.13f',
        delimiter=' ')


if __name__ == '__main__':
    num_runs = 10
    num_data = 200000
    training_percentage = 50
    num_events = int(num_data / (100 / training_percentage))

    probs = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

    of_stds = dict.fromkeys(probs, 0)
    of_means = dict.fromkeys(probs, 0)

    smf_stds = dict.fromkeys(probs, 0)
    smf_means = dict.fromkeys(probs, 0)

    dmf_stds = dict.fromkeys(probs, 0)
    dmf_means = dict.fromkeys(probs, 0)

    _of_stds = []
    _of_means = []

    _smf_stds = []
    _smf_means = []

    _dmf_stds = []
    _dmf_means = []

    for prob in probs:
        print('Processing signal probability:  {}%\n\n\n'.format(prob))
        for i in range(0, num_runs):
            print('--------------------Execution number: {}\n'.format(i))

            # Generates a new data set for MF graph error
            pu_generator(num_data, [prob], DATA_SET)

            of_calculation(num_events, [prob], DATA_SET)
            dmf_calculation(num_events, [prob], DATA_SET)
            smf_calculation(num_data, [prob], DATA_SET)

            of_error_file_name = f'{BASE_FOLER}/prob_{prob * 100}/{num_data}_events/OF/of_amp_error.txt'
            smf_error_file_name = f'{BASE_FOLER}/prob_{prob * 100}/{num_data}_events/S_MF/smf_amp_error.txt'
            dmf_error_file_name = f'{BASE_FOLER}/prob_{prob * 100}/{num_data}_events/D_MF/dmf_amp_error.txt'

            of_error = np.loadtxt(of_error_file_name)
            smf_error = np.loadtxt(smf_error_file_name)
            dmf_error = np.loadtxt(dmf_error_file_name)

            _of_means.append(np.mean(of_error))
            _of_stds.append(np.std(of_error))

            _smf_means.append(np.mean(smf_error))
            _smf_stds.append(np.std(smf_error))

            _dmf_means.append(np.mean(dmf_error))
            _dmf_stds.append(np.std(dmf_error))

        of_means[prob] = _of_means
        of_stds[prob] = _of_stds

        smf_means[prob] = _smf_means
        smf_stds[prob] = _smf_stds

        dmf_means[prob] = _dmf_means
        dmf_stds[prob] = _dmf_stds

        _of_stds = []
        _of_means = []
        _smf_stds = []
        _smf_means = []
        _dmf_stds = []
        _dmf_means = []

    folder_name = 'error_bar'
    prefix = '{}_runs_'.format(num_runs)
    of_prefix = prefix + 'of_'
    smf_prefix = prefix + 'smf_'
    dmf_prefix = prefix + 'dmf_'

    for prob in probs:
        sufix = '_prob_{}'.format(prob * 100)
        _save_file(of_prefix + 'std' + sufix, folder_name, num_data, of_stds[prob])
        _save_file(of_prefix + 'mean' + sufix, folder_name, num_data, of_means[prob])

        _save_file(smf_prefix + 'std' + sufix, folder_name, num_data, smf_stds[prob])
        _save_file(smf_prefix + 'mean' + sufix, folder_name, num_data, smf_means[prob])

        _save_file(dmf_prefix + 'std' + sufix, folder_name, num_data, dmf_stds[prob])
        _save_file(dmf_prefix + 'mean' + sufix, folder_name, num_data, dmf_means[prob])
