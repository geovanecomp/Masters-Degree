"""Compares OF and MF amplitudes"""

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
    amplitude_mean = 10
    channel = 1
    noise_mean = 90

    sufix = f'_ch{channel}'
    base_folder = DIR_PATH + f'/../../results/hybrid/amplitude_mean{amplitude_mean}'
    of_amp_file_name = f'{base_folder}/OF/mu{noise_mean}/of_amp_signal{sufix}.txt'
    dmf_amp_file_name = f'{base_folder}/D_MF/mu{noise_mean}/dmf_amp_signal{sufix}.txt'
    smf_amp_file_name = f'{base_folder}/S_MF/mu{noise_mean}/smf_amp_signal{sufix}.txt'
    true_amplitude_file_name = base_folder + f'/base_data/mu{noise_mean}/tile_A{sufix}.txt'

    of_amp = np.loadtxt(of_amp_file_name)
    dmf_amp = np.loadtxt(dmf_amp_file_name)
    smf_amp = np.loadtxt(smf_amp_file_name)
    true_amplitude = np.loadtxt(true_amplitude_file_name)[:len(of_amp)]

    fig, ((ax0)) = plt.subplots(nrows=1, ncols=1)
    rangeR = 200
    rangeL = -100
    bins = 100

    fig.suptitle(f'Comparação das amplitudes. ruido_medio = {noise_mean} Canal: {channel} Amplitude: {amplitude_mean} Eventos: {len(of_amp)}')

    ax0.hist(of_amp, bins=bins, range=(rangeL, rangeR), color='red', histtype=u'step', label='OF')
    ax0.hist(dmf_amp, bins=bins, range=(rangeL, rangeR), color='green', histtype=u'step', label='D-MF')
    ax0.hist(smf_amp, bins=bins, range=(rangeL, rangeR), color='blue', histtype=u'step', label='S-MF')
    ax0.hist(true_amplitude, bins=bins, range=(rangeL, rangeR), color='black', histtype=u'step', label='Amp-Verdadeira')
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('\nOF ' r'$\mu={}$, $\sigma={}$'
                  '\nD-MF ' r'$\mu={}$, $\sigma={}$'
                  '\nS-MF ' r'$\mu={}$, $\sigma={}$'
                  .format(of_amp.mean(), of_amp.std(),
                          dmf_amp.mean(), dmf_amp.std(),
                          smf_amp.mean(), smf_amp.std()))
    ax0.set_xlabel('Energia (MeV)', **Legend.font)
    ax0.set_ylabel('Eventos', **Legend.font)
    plt.xticks(**Tick.font)
    plt.yticks(**Tick.font)

    plt.show()
