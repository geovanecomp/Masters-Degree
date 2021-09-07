"""Compares OF and MF error"""

import os.path
import sys
import inspect
import numpy as np
import matplotlib.pyplot as plt

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from config import Legend, Tick

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    # Real data
    amplitude_mean = 300
    channel = 1
    noise_mean = 30

    sufix = f'_ch{channel}'
    base_folder = DIR_PATH + f'/../../results/hybrid/amplitude_mean{amplitude_mean}'
    of_amp_error_file_name = f'{base_folder}/OF/mu{noise_mean}/of_amp_error{sufix}.txt'
    dmf_amp_error_file_name = f'{base_folder}/D_MF/mu{noise_mean}/dmf_amp_error{sufix}.txt'
    smf_amp_error_file_name = f'{base_folder}/S_MF/mu{noise_mean}/smf_amp_error{sufix}.txt'

    of_amp_error = np.loadtxt(of_amp_error_file_name)
    dmf_amp_error = np.loadtxt(dmf_amp_error_file_name)
    smf_amp_error = np.loadtxt(smf_amp_error_file_name)

    if len(of_amp_error) != len(smf_amp_error) or len(smf_amp_error) != len(dmf_amp_error):
        print('DIFFERENT DIMENSIONS!!!')
        print(f'OF Amp len: {len(of_amp_error)}')
        print(f'D-MF Amp len: {len(dmf_amp_error)}')
        print(f'S-MF Amp len: {len(smf_amp_error)}')

    fig, ((ax0)) = plt.subplots(nrows=1, ncols=1)
    rangeR = 600
    rangeL = -rangeR
    bins = 100

    print('\nOF ' r'$\mu= {}$, $\sigma= {}$'
          '\nD-MF ' r'$\mu= {}$, $\sigma= {}$'
          '\nS-MF ' r'$\mu= {}$, $\sigma= {}$'
          .format(of_amp_error.mean(), of_amp_error.std(),
                  dmf_amp_error.mean(), dmf_amp_error.std(),
                  smf_amp_error.mean(), smf_amp_error.std()))

    fig.suptitle(f'Comparação do erro com Ruído Médio = {noise_mean} Canal: {channel} Amplitude: {amplitude_mean} Eventos: {len(of_amp_error)}')

    ax0.hist(of_amp_error, bins=bins, range=(rangeL, rangeR), color='red', histtype=u'step', label='OF')
    ax0.hist(dmf_amp_error, bins=bins, range=(rangeL, rangeR), color='green', histtype=u'step', label='D-MF')
    ax0.hist(smf_amp_error, bins=bins, range=(rangeL, rangeR), color='blue', histtype=u'step', label='S-MF')
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('\nOF ' r'$\mu={}$, $\sigma={}$'
                  '\nD-MF ' r'$\mu={}$, $\sigma={}$'
                  '\nS-MF ' r'$\mu={}$, $\sigma={}$'
                  .format(of_amp_error.mean(), of_amp_error.std(),
                          dmf_amp_error.mean(), dmf_amp_error.std(),
                          smf_amp_error.mean(), smf_amp_error.std()))
    ax0.set_xlabel('Erro de Estimação', **Legend.font)
    ax0.set_ylabel('Eventos', **Legend.font)
    plt.xticks(**Tick.font)
    plt.yticks(**Tick.font)

    plt.show()
