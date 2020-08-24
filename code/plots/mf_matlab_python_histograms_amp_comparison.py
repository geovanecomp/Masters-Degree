"""Compares MF's Amplitude against True Amplitude and Matlab"""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    prob = 100.0
    num_events = 10000

    # Pile data
    amplitude_file_name = DIR_PATH + '/../results/pileup_data/prob_{}/{}_events/tile_A_signal_prob_{}.txt'.format(prob, num_events, prob)
    matlab_amplitude_file_name = DIR_PATH + '/../matlab_code/results/pileupMf/{}_events/ampsinalTileOcup{}.txt'.format(num_events, prob)
    mf_amplitude_file_name = DIR_PATH + '/../results/matched_filter/{}_events/pileup_prob_{}_amp_signal.txt'.format(num_events, prob)

    amplitude = np.loadtxt(amplitude_file_name)
    matlab_amplitude = np.loadtxt(matlab_amplitude_file_name)
    mf_amplitude = np.loadtxt(mf_amplitude_file_name)

    fig, ((ax0, ax1, ax2)) = plt.subplots(nrows=1, ncols=3)

    fig.suptitle('Comparação da Amplitude Verdadeira X Numérica \n' '{} eventos e Empilhamento de {}%'
                 .format(num_events, prob))
    ax0.hist(amplitude, bins="auto")
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('Verdadeira \n' r'$\mu={}$, $\sigma={}$'
                  .format(amplitude.mean(), amplitude.std()))
    ax0.set_xlabel('Valor')
    ax0.set_ylabel('Frequência')

    ax1.hist(matlab_amplitude, bins="auto")
    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('Matlab: MF Numerica \n' r'$\mu={}$, $\sigma={}$'
                  .format(matlab_amplitude.mean(), matlab_amplitude.std()))
    ax1.set_xlabel('Valor')
    ax1.set_ylabel('Frequência')

    ax2.hist(mf_amplitude, bins="auto")
    ax2.legend(prop={'size': 10})
    ax2.grid(axis='y', alpha=0.75)
    ax2.set_title('Python: MF Numerica \n' r'$\mu={}$, $\sigma={}$'
                  .format(mf_amplitude.mean(), mf_amplitude.std()))
    ax2.set_xlabel('Valor')
    ax2.set_ylabel('Frequência')

    plt.show()
