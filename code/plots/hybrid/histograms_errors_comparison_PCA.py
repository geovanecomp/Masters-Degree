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
    channel = 36
    noise_mean = 30

    sufix = f'_ch{channel}'
    base_folder = DIR_PATH + f'/../../results/hybrid/amplitude_mean{amplitude_mean}'
    pca1_smf_error_file_name = f'{base_folder}/S_MF_PCA1/mu{noise_mean}/smf_amp_error{sufix}.txt'
    pca3_smf_error_file_name = f'{base_folder}/S_MF_PCA3/mu{noise_mean}/smf_amp_error{sufix}.txt'
    pca5_smf_error_file_name = f'{base_folder}/S_MF_PCA5/mu{noise_mean}/smf_amp_error{sufix}.txt'
    pca7_smf_error_file_name = f'{base_folder}/S_MF/mu{noise_mean}/smf_amp_error{sufix}.txt'

    pca1_smf_amp_error = np.loadtxt(pca1_smf_error_file_name)
    pca3_smf_amp_error = np.loadtxt(pca3_smf_error_file_name)
    pca5_smf_amp_error = np.loadtxt(pca5_smf_error_file_name)
    pca7_smf_amp_error = np.loadtxt(pca7_smf_error_file_name)

    fig, ((ax0)) = plt.subplots(nrows=1, ncols=1)
    rangeR = 200
    rangeL = -rangeR
    bins = 100

    print('\nS-MF-PCA1 ' r'$\mu= {}$, $\sigma= {}$'
        '\nS-MF-PCA3 ' r'$\mu= {}$, $\sigma= {}$'
        '\nS-MF-PCA5 ' r'$\mu= {}$, $\sigma= {}$'
        '\nS-MF-PCA7 ' r'$\mu= {}$, $\sigma= {}$'
          .format(pca1_smf_amp_error.mean(), pca1_smf_amp_error.std(),
                  pca3_smf_amp_error.mean(), pca3_smf_amp_error.std(),
                  pca5_smf_amp_error.mean(), pca5_smf_amp_error.std(),
                  pca7_smf_amp_error.mean(), pca7_smf_amp_error.std()))

    ax0.hist(pca1_smf_amp_error, bins=bins, range=(rangeL, rangeR), color='red', histtype=u'step', label='PCA-1')
    ax0.hist(pca3_smf_amp_error, bins=bins, range=(rangeL, rangeR), color='green', histtype=u'step', label='PCA-3')
    ax0.hist(pca5_smf_amp_error, bins=bins, range=(rangeL, rangeR), color='blue', histtype=u'step', label='PCA-5')
    ax0.hist(pca7_smf_amp_error, bins=bins, range=(rangeL, rangeR), color='black', histtype=u'step', label='PCA-7')
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_xlabel('Erro', **Legend.font)
    ax0.set_ylabel('Eventos', **Legend.font)
    plt.xticks(**Tick.font)
    plt.yticks(**Tick.font)

    plt.show()
