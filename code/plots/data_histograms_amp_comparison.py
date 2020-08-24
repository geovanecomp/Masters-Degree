"""Compares all Amplitudes"""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    prob = 0.0
    num_events = 10000

    # Pile data
    pu_amplitude_file_name = DIR_PATH + '/../results/pileup_data/prob_{}/{}_events/tile_A_signal_prob_{}.txt'.format(prob, num_events, prob)
    of_amplitude_file_name = DIR_PATH + '/../results/optimal_filter/{}_events/pileup_prob_{}_of_amplitude.txt'.format(num_events, prob)
    mf_amplitude_file_name = DIR_PATH + '/../results/matched_filter/{}_events/pileup_prob_{}_amp_signal.txt'.format(num_events, prob)

    pu_amplitude = np.loadtxt(pu_amplitude_file_name)
    of_amplitude = np.loadtxt(of_amplitude_file_name)
    mf_amplitude = np.loadtxt(mf_amplitude_file_name)

    fig, ((ax0, ax1, ax2)) = plt.subplots(nrows=1, ncols=3)

    fig.suptitle('Comparação da Amplitude Verdadeira X Numérica \n' '{} eventos e Empilhamento de {}%'
                 .format(num_events, prob))
    ax0.hist(pu_amplitude, bins="auto")
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('PU: Verdadeira \n' r'$\mu={}$, $\sigma={}$'
                  .format(pu_amplitude.mean(), pu_amplitude.std()))
    ax0.set_xlabel('Valor')
    ax0.set_ylabel('Frequência')

    ax1.hist(of_amplitude, bins="auto")
    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('OF: Numerica \n' r'$\mu={}$, $\sigma={}$'
                  .format(of_amplitude.mean(), of_amplitude.std()))
    ax1.set_xlabel('Valor')
    ax1.set_ylabel('Frequência')

    ax2.hist(mf_amplitude, bins="auto")
    ax2.legend(prop={'size': 10})
    ax2.grid(axis='y', alpha=0.75)
    ax2.set_title('MF: Numerica \n' r'$\mu={}$, $\sigma={}$'
                  .format(mf_amplitude.mean(), mf_amplitude.std()))
    ax2.set_xlabel('Valor')
    ax2.set_ylabel('Frequência')

    plt.show()
