"""Compares OF and MF error"""

import os.path
import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams['xtick.labelsize'] = 22
# plt.rcParams['ytick.labelsize'] = 22

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    # Real data
    noise_mean = 30
    sufix = '_small'
    base_folder = DIR_PATH + f'/../results/real_data/mu{noise_mean}'
    amplitude_file_name = f'{base_folder}/tile_A{sufix}.txt'
    of_amp_error_file_name = f'{base_folder}/optimal_filter/of_amp_error{sufix}.txt'
    mf_amp_error_file_name = f'{base_folder}/matched_filter/mf_amp_error{sufix}.txt'
    dmf_amp_error_file_name = f'{base_folder}/deterministic_matched_filter/dmf_amp_error{sufix}.txt'

    amplitude = np.loadtxt(amplitude_file_name)
    of_amp_error = np.loadtxt(of_amp_error_file_name)
    mf_amp_error = np.loadtxt(mf_amp_error_file_name)
    dmf_amp_error = np.loadtxt(dmf_amp_error_file_name)

    if len(of_amp_error) != len(mf_amp_error) or len(mf_amp_error) != len(dmf_amp_error):
        print('DIFFERENT DIMENSIONS!!!')

    # of_amp_error = of_amp_error[0:10000]
    # mf_amp_error = mf_amp_error[0:10000]
    bins = 500

    fig, ((ax0)) = plt.subplots(nrows=1, ncols=1)
    font = {
            'family': 'Times New Roman',
            'size': 16
            }

    # fig.suptitle('Comparação do erro \n' '{} eventos e Empilhamento de {}%'
    #              .format(num_events, prob))
    fig.suptitle('Comparação do erro com Ruído Médio = {}\n {} eventos'.format(noise_mean, len(amplitude)))
    ax0.hist(of_amp_error, bins=bins, color='dimgrey', histtype=u'step', label='OF')
    ax0.hist(dmf_amp_error, bins=bins, facecolor='dimgrey', histtype=u'step', label='D-MF')
    ax0.hist(mf_amp_error, bins=bins, facecolor='dimgrey', histtype=u'step', label='E-MF')
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('\nOF ' r'$\mu={}$, $\sigma={}$'
                  '\nD-MF ' r'$\mu={}$, $\sigma={}$'
                  '\nE-MF ' r'$\mu={}$, $\sigma={}$'
                  .format(of_amp_error.mean(), of_amp_error.std(),
                          dmf_amp_error.mean(), dmf_amp_error.std(),
                          mf_amp_error.mean(), mf_amp_error.std()))
    ax0.set_xlabel('Erro de Estimação', **font)
    ax0.set_ylabel('Eventos', **font)
    ax0.set_xlim(-100, 100)
    # ax0.set_ylim(0, 5000000)

    plt.show()
