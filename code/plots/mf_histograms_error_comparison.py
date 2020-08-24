"""Compares MF Amplitude against its Amplitude error"""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    prob = 0.0
    num_events = 10000

    # Normal data
    # amplitude_file_name = DIR_PATH + '/../results/base_data/{}_events/amplitude.txt'.format(num_events)
    # mf_amplitude_file_name = DIR_PATH + '/../results/matched_filter/{}_events/amp_signal.txt'.format(num_events)

    # Pile data
    amplitude_file_name = DIR_PATH + '/../results/pileup_data/prob_{}/{}_events/tile_A_signal_prob_{}.txt'.format(prob, num_events, prob)
    mf_amplitude_file_name = DIR_PATH + '/../results/matched_filter/{}_events/pileup_prob_{}_amp_signal.txt'.format(num_events, prob)

    amplitude = np.loadtxt(amplitude_file_name)
    mf_amplitude = np.loadtxt(mf_amplitude_file_name)

    mf_error = mf_amplitude - amplitude

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)

    # fig.suptitle('Comparação da Amplitude: Verdadeira X Numerica \n' '{} eventos'
    #              .format(num_events))
    fig.suptitle('MF: Comparação da Amplitude X Erro \n' '{} eventos e Empilhamento de {}%'
                 .format(num_events, prob))
    ax0.hist(mf_amplitude, bins="auto")
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('Amplitude \n' r'$\mu={}$, $\sigma={}$'
                  .format(mf_amplitude.mean(), mf_amplitude.std()))
    ax0.set_xlabel('Valor')
    ax0.set_ylabel('Frequência')

    ax1.hist(mf_error, bins="auto")
    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('Erro \n' r'$\mu={}$, $\sigma={}$'
                  .format(mf_error.mean(), mf_error.std()))
    ax1.set_xlabel('Valor')
    ax1.set_ylabel('Frequência')

    plt.show()
