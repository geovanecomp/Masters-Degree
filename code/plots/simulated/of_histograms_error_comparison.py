"""Compares MF Amplitude against its Amplitude error"""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    prob = 100.0
    num_events = 10000

    # Normal data
    # amp_error_file_name = DIR_PATH + '/../results/optimal_filter/{}_events/of_amp_error.txt'.format(num_events)
    # of_amplitude_file_name = DIR_PATH + '/../results/optimal_filter/{}_events/of_amplitude.txt'.format(num_events)

    # Pile data
    amp_error_file_name = DIR_PATH + '/../results/optimal_filter/{}_events/pileup_prob_{}_of_amp_error.txt'.format(num_events, prob)
    of_amplitude_file_name = DIR_PATH + '/../results/optimal_filter/{}_events/pileup_prob_{}_of_amplitude.txt'.format(num_events, prob)

    amp_error = np.loadtxt(amp_error_file_name).T
    of_amplitude = np.loadtxt(of_amplitude_file_name).T

    amp_error_mean = np.mean(amp_error)
    amp_error_std = np.std(amp_error)

    of_amplitude_mean = np.mean(of_amplitude)
    of_amplitude_std = np.std(of_amplitude)

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)

    fig.suptitle('OF: Comparação da Amplitude X Erro \n' '{} eventos e Empilhamento de {}%'
                 .format(num_events, prob))
    ax0.hist(of_amplitude, bins="auto")
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('Amplitude \n' r'$\mu={}$, $\sigma={}$'
                  .format(of_amplitude_mean, of_amplitude_std))
    ax0.set_xlabel('Valor')
    ax0.set_ylabel('Frequência')

    ax1.hist(amp_error, bins="auto")
    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('Erro \n' r'$\mu={}$, $\sigma={}$'
                  .format(amp_error_mean, amp_error_std))
    ax1.set_xlabel('Valor')
    ax1.set_ylabel('Frequência')

    plt.show()
