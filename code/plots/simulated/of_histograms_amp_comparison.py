"""Compares OF Amplitude against True Amplitude"""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    prob = 0.0
    num_events = 10000

    # Normal data
    # amplitude_file_name = DIR_PATH + '/../results/base_data/{}_events/amplitude.txt'.format(num_events)
    # of_amplitude_file_name = DIR_PATH + '/../results/optimal_filter/{}_events/of_amplitude.txt'.format(num_events)

    # Pile data
    amplitude_file_name = DIR_PATH + '/../results/pileup_data/prob_{}/{}_events/tile_A_signal_prob_{}.txt'.format(prob, num_events, prob)
    of_amplitude_file_name = DIR_PATH + '/../results/optimal_filter/{}_events/pileup_prob_{}_of_amplitude.txt'.format(num_events, prob)

    amplitude = np.loadtxt(amplitude_file_name)
    of_amplitude = np.loadtxt(of_amplitude_file_name)

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)

    # fig.suptitle('Comparação da Amplitude: Verdadeira X Numerica \n' '{} eventos'
    #              .format(num_events))
    fig.suptitle('OF: Comparação da Amplitude Verdadeira X Numérica \n' '{} eventos e Empilhamento de {}%'
                 .format(num_events, prob))
    ax0.hist(amplitude, bins="auto")
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('Verdadeira \n' r'$\mu={}$, $\sigma={}$'
                  .format(amplitude.mean(), amplitude.std()))
    ax0.set_xlabel('Valor')
    ax0.set_ylabel('Frequência')

    ax1.hist(of_amplitude, bins="auto")
    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('Numerica \n' r'$\mu={}$, $\sigma={}$'
                  .format(of_amplitude.mean(), of_amplitude.std()))
    ax1.set_xlabel('Valor')
    ax1.set_ylabel('Frequência')

    plt.show()
