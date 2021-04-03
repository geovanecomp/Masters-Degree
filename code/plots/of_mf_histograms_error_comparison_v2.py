"""Compares OF and MF error"""

import os.path
import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams['xtick.labelsize'] = 22
# plt.rcParams['ytick.labelsize'] = 22

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    # Real data
    noise_mean = 90
    channel = 36
    amplitude_mean = 100

    sufix = f'_ch{channel}'
    base_folder = DIR_PATH + f'/../results/hybrid/amplitude_mean{amplitude_mean}'
    of_amp_error_file_name = f'{base_folder}/OF/mu{noise_mean}/of_amp_error{sufix}.txt'
    dmf_amp_error_file_name = f'{base_folder}/D_MF/mu{noise_mean}/dmf_amp_error{sufix}.txt'
    emf_amp_error_file_name = f'{base_folder}/E_MF/mu{noise_mean}/mf_amp_error{sufix}.txt'

    of_amp_error = np.loadtxt(of_amp_error_file_name)
    dmf_amp_error = np.loadtxt(dmf_amp_error_file_name)
    emf_amp_error = np.loadtxt(emf_amp_error_file_name)

    if len(of_amp_error) != len(emf_amp_error) or len(emf_amp_error) != len(dmf_amp_error):
        print('DIFFERENT DIMENSIONS!!!')
        print(f'OF Amp len: {len(of_amp_error)}')
        print(f'D-MF Amp len: {len(dmf_amp_error)}')
        print(f'E-MF Amp len: {len(emf_amp_error)}')

    bins = 200

    fig, ((ax0)) = plt.subplots(nrows=1, ncols=1, figsize=(19,10))
    font = {
            'family': 'Times New Roman',
            'size': 16
            }

    # fig.suptitle('Comparação do erro \n' '{} eventos e Empilhamento de {}%'
    #              .format(num_events, prob))
    fig.suptitle(f'Comparação do erro com Ruído Médio = {noise_mean} Canal: {channel} Eventos: {len(of_amp_error)}')

    # ax0.hist(of_amp_error, bins=bins, range=(-75, 75), color='red', histtype=u'step', label='OF')
    ax0.hist(of_amp_error, bins=bins, range=(-75, 75), color='red', histtype=u'step', label='OF')
    ax0.hist(dmf_amp_error, bins=bins, range=(-75, 75), facecolor='dimgrey', histtype=u'step', label='D-MF')
    ax0.hist(emf_amp_error, bins=bins, range=(-75, 75), facecolor='blue', histtype=u'step', label='E-MF')
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('\nOF ' r'$\mu={}$, $\sigma={}$'
                  '\nD-MF ' r'$\mu={}$, $\sigma={}$'
                  '\nE-MF ' r'$\mu={}$, $\sigma={}$'
                  .format(of_amp_error.mean(), of_amp_error.std(),
                          dmf_amp_error.mean(), dmf_amp_error.std(),
                          emf_amp_error.mean(), emf_amp_error.std()))
    ax0.set_xlabel('Erro de Estimação', **font)
    ax0.set_ylabel('Eventos', **font)

    plt.show()
