"""Compares simulated signals and its noises"""

import os.path
import numpy as np
import matplotlib.pyplot as plt
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from config import Legend, Tick

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    # prob = 100.0
    num_events = 200000

    # Pile data
    BASE_PATH0 = DIR_PATH + f'/../../results/simulated_low_snr/pileup_data/prob_0.0/{num_events}_events'
    BASE_PATH50 = DIR_PATH + f'/../../results/simulated_low_snr/pileup_data/prob_50.0/{num_events}_events'
    BASE_PATH100 = DIR_PATH + f'/../../results/simulated_low_snr/pileup_data/prob_100.0/{num_events}_events'

    signal_file_name0 = BASE_PATH0 + '/base_data/tile_signal.txt'
    noise_file_name0 = BASE_PATH0 + '/base_data/noise.txt'

    signal_file_name50 = BASE_PATH50 + '/base_data/tile_signal.txt'
    noise_file_name50 = BASE_PATH50 + '/base_data/noise.txt'

    signal_file_name100 = BASE_PATH100 + '/base_data/tile_signal.txt'
    noise_file_name100 = BASE_PATH100 + '/base_data/noise.txt'

    signals0 = np.loadtxt(signal_file_name0)
    noises0 = np.loadtxt(noise_file_name0)

    signals50 = np.loadtxt(signal_file_name50)
    noises50 = np.loadtxt(noise_file_name50)

    signals100 = np.loadtxt(signal_file_name100)
    noises100 = np.loadtxt(noise_file_name100)

    fig, ((ax0, ax1), (ax2, ax3), (ax4, ax5)) = plt.subplots(nrows=3, ncols=2)

    fig.suptitle('Comparação do Sinal gerado X Ruído \n' '{} eventos e Empilhamentos de 0, 50 e 100%'
                 .format(num_events))
    # fig.suptitle('Comparação do Sinal gerado X Ruído \n' '{} eventos e Empilhamento de {}%'
    #              .format(num_events, prob))
    ax0.hist(signals0, bins="auto")
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('Sinais: ' r'$\mu={}$, $\sigma={}$'
                  .format(signals0.mean(), signals0.std()))
    ax0.set_xlabel('Valor', **Legend.font)
    ax0.set_ylabel('Frequência', **Legend.font)
    ax0.set_ylim(0, 8000)

    ax1.hist(noises0, bins="auto")
    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('Ruídos: ' r'$\mu={}$, $\sigma={}$'
                  .format(noises0.mean(), noises0.std()))
    ax1.set_xlabel('Valor', **Legend.font)
    ax1.set_ylabel('Frequência', **Legend.font)

    ax2.hist(signals50, bins="auto")
    ax2.legend(prop={'size': 10})
    ax2.grid(axis='y', alpha=0.75)
    ax2.set_title('Sinais: ' r'$\mu={}$, $\sigma={}$'
                  .format(signals50.mean(), signals50.std()))
    ax2.set_xlabel('Valor', **Legend.font)
    ax2.set_ylabel('Frequência', **Legend.font)

    ax3.hist(noises50, bins="auto")
    ax3.legend(prop={'size': 10})
    ax3.grid(axis='y', alpha=0.75)
    ax3.set_title('Ruídos: ' r'$\mu={}$, $\sigma={}$'
                  .format(noises50.mean(), noises50.std()))
    ax3.set_xlabel('Valor', **Legend.font)
    ax3.set_ylabel('Frequência', **Legend.font)

    ax4.hist(signals100, bins="auto")
    ax4.legend(prop={'size': 10})
    ax4.grid(axis='y', alpha=0.75)
    ax4.set_title('Sinais: ' r'$\mu={}$, $\sigma={}$'
                  .format(signals100.mean(), signals100.std()))
    ax4.set_xlabel('Valor', **Legend.font)
    ax4.set_ylabel('Frequência', **Legend.font)

    ax5.hist(noises100, bins="auto")
    ax5.legend(prop={'size': 10})
    ax5.grid(axis='y', alpha=0.75)
    ax5.set_title('Ruídos: ' r'$\mu={}$, $\sigma={}$'
                  .format(noises100.mean(), noises100.std()))
    ax5.set_xlabel('Valor', **Legend.font)
    ax5.set_ylabel('Frequência', **Legend.font)

    plt.show()
