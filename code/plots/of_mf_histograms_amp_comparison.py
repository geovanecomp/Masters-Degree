"""Compares all amplitudes"""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':

    # num_events = 10000
    # prob = 0.0
    # Normal data
    # amp_file_name = DIR_PATH + '/../results/base_data/{}_events/amplitude.txt'.format(num_events)
    # of_amp_file_name = DIR_PATH + '/../results/optimal_filter/{}_events/of_amplitude.txt'.format(num_events)

    # Pile data
    # amp_file_name = DIR_PATH + '/../results/pileup_data/prob_{}/{}_events/tile_A_signal_prob_{}.txt'.format(prob, num_events, prob)
    # of_amp_file_name = DIR_PATH + '/../results/optimal_filter/{}_events/pileup_prob_{}_of_amplitude.txt'.format(num_events, prob)
    # mf_amp_file_name = DIR_PATH + '/../results/matched_filter/{}_events/pileup_prob_{}_amp_signal.txt'.format(num_events, prob)

    # Real data
    noise_mean = 30
    amp_file_name = DIR_PATH + '/../results/real_data/mu{}/tile_A.txt'.format(noise_mean)
    of_amp_file_name = DIR_PATH + '/../results/real_data/mu{}/optimal_filter/of_amp_signal.txt'.format(noise_mean)
    mf_amp_file_name = DIR_PATH + '/../results/real_data/mu{}/matched_filter/mf_amp_signal.txt'.format(noise_mean)

    amplitude = np.loadtxt(amp_file_name)
    of_amplitude = np.loadtxt(of_amp_file_name)
    mf_amplitude = np.loadtxt(mf_amp_file_name)

    fig, ((ax0, ax1, ax2)) = plt.subplots(nrows=1, ncols=3)

    # fig.suptitle('Comparação da Amplitude: Verdadeira X Numerica \n' '{} eventos'
    #              .format(num_events))
    # fig.suptitle('Comparação da Amplitude Verdadeira X Numérica \n' '{} eventos e Empilhamento de {}%'
    #              .format(num_events, prob))
    fig.suptitle('Comparação da Amplitude Verdadeira X Numérica considerando ruídos reais')
    ax0.hist(amplitude, bins="auto", color='dimgrey')
    ax0.legend(prop={'size': 10})
    ax0.grid(alpha=0.75)
    ax0.set_title('Verdadeira \n' r'$\mu={}$, $\sigma={}$'
                  .format(amplitude.mean(), amplitude.std()))
    ax0.set_xlabel('Valor')
    ax0.set_ylabel('Frequência')

    ax1.hist(of_amplitude, bins="auto", color='dimgrey')
    ax1.legend(prop={'size': 10})
    ax1.grid(alpha=0.75)
    ax1.set_title('OF: Numerica \n' r'$\mu={}$, $\sigma={}$'
                  .format(of_amplitude.mean(), of_amplitude.std()))
    ax1.set_xlabel('Valor')
    ax1.set_ylabel('Frequência')

    ax2.hist(mf_amplitude, bins="auto", color='dimgrey')
    ax2.legend(prop={'size': 10})
    ax2.grid(alpha=0.75)
    ax2.set_title('MF: Numerica \n' r'$\mu={}$, $\sigma={}$'
                  .format(mf_amplitude.mean(), mf_amplitude.std()))
    ax2.set_xlabel('Valor')
    ax2.set_ylabel('Frequência')

    plt.show()
