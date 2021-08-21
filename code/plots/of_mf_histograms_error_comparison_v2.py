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
    channel = 1
    amplitude_mean = 10

    sufix = f'_ch{channel}'
    base_folder = DIR_PATH + f'/../results/hybrid/amplitude_mean{amplitude_mean}'
    of_amp_error_file_name = f'{base_folder}/OF/mu{noise_mean}/of_amp_error{sufix}.txt'
    dmf_amp_error_file_name = f'{base_folder}/D_MF/mu{noise_mean}/dmf_amp_error{sufix}.txt'
    smf_amp_error_file_name = f'{base_folder}/E_MF/mu{noise_mean}/mf_amp_error{sufix}.txt'

    of_amp_error = np.loadtxt(of_amp_error_file_name)
    dmf_amp_error = np.loadtxt(dmf_amp_error_file_name)
    smf_amp_error = np.loadtxt(smf_amp_error_file_name)

    if len(of_amp_error) != len(smf_amp_error) or len(smf_amp_error) != len(dmf_amp_error):
        print('DIFFERENT DIMENSIONS!!!')
        print(f'OF Amp len: {len(of_amp_error)}')
        print(f'D-MF Amp len: {len(dmf_amp_error)}')
        print(f'S-MF Amp len: {len(smf_amp_error)}')

    bins = 200

    fig, ((ax0)) = plt.subplots(nrows=1, ncols=1, figsize=(19,10))
    font = {
            'family': 'Times New Roman',
            'size': 16
            }

    fig.suptitle(f'Comparação do erro com Ruído Médio = {noise_mean} Canal: {channel} Amplitude: {amplitude_mean} Eventos: {len(of_amp_error)}')

    ax0.hist(of_amp_error, bins=bins, range=(-100, 100), color='red', histtype=u'step', label='OF')
    ax0.hist(dmf_amp_error, bins=bins, range=(-100, 100), facecolor='dimgrey', histtype=u'step', label='D-MF')
    ax0.hist(smf_amp_error, bins=bins, range=(-100, 100), facecolor='blue', histtype=u'step', label='S-MF')
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('\nOF ' r'$\mu={}$, $\sigma={}$'
                  '\nD-MF ' r'$\mu={}$, $\sigma={}$'
                  '\nE-MF ' r'$\mu={}$, $\sigma={}$'
                  .format(of_amp_error.mean(), of_amp_error.std(),
                          dmf_amp_error.mean(), dmf_amp_error.std(),
                          smf_amp_error.mean(), smf_amp_error.std()))
    ax0.set_xlabel('Erro de Estimação', **font)
    ax0.set_ylabel('Eventos', **font)

    plt.show()
