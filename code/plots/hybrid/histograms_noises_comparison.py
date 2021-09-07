"""Compares a specific noise againt multiple channels"""

import os.path
import sys
import inspect
import pandas as pd
import matplotlib.pyplot as plt

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from config import Legend, Tick

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    # Real data
    noise_mean = 90

    base_folder = DIR_PATH + '/../../data'
    noise_ch1_file_name = base_folder + f'/EBA/EBAmu{noise_mean}_no_ped_ch1.txt'
    noise_ch10_file_name = base_folder + f'/EBA/EBAmu{noise_mean}_no_ped_ch10.txt'
    noise_ch36_file_name = base_folder + f'/LBA/LBAmu{noise_mean}_no_ped_ch36.txt'

    noise_ch1 = pd.read_csv(noise_ch1_file_name, sep=" ", usecols=(3, 4, 5, 6, 7, 8, 9), header=None).to_numpy().flatten()
    noise_ch10 = pd.read_csv(noise_ch10_file_name, sep=" ", usecols=(3, 4, 5, 6, 7, 8, 9), header=None).to_numpy().flatten()
    noise_ch36 = pd.read_csv(noise_ch36_file_name, sep=" ", usecols=(3, 4, 5, 6, 7, 8, 9), header=None).to_numpy().flatten()

    bins = 100

    fig, ((ax0)) = plt.subplots(nrows=1, ncols=1)
    fig.suptitle(f'Comparação do erro com Ruído Médio = {noise_mean} Canal: {channel} Amplitude: {amplitude_mean} Eventos: {len(of_amp_error)}')

    ax0.hist(noise_ch1, bins=bins, color='red', histtype=u'step', label='A1')
    ax0.hist(noise_ch10, bins=bins, color='green', histtype=u'step', label='A3')
    ax0.hist(noise_ch36, bins=bins, color='blue', histtype=u'step', label='A9')
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('\nA1 ' r'$\mu={}$, $\sigma={}$'
                  '\nA3 ' r'$\mu={}$, $\sigma={}$'
                  '\nA9 ' r'$\mu={}$, $\sigma={}$'
                  .format(noise_ch1.mean(), noise_ch1.std(),
                          noise_ch10.mean(), noise_ch10.std(),
                          noise_ch36.mean(), noise_ch36.std()))
    ax0.set_xlabel('Ruído', **Legend.font)
    ax0.set_ylabel('Eventos', **Legend.font)
    ax0.set_xlim(-150, 150)
    plt.xticks(**Tick.font)
    plt.yticks(**Tick.font)

    plt.show()
