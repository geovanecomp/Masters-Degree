"""Compares OF and MF error"""

import os.path
import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams['xtick.labelsize'] = 22
# plt.rcParams['ytick.labelsize'] = 22

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':

    # Pile data
    prob = 50.0
    amplitude_file_name = DIR_PATH + '/../results/pileup_data/prob_{}/{}_events/tile_A_signal_prob_{}.txt'.format(prob, num_events, prob)
    of_amp_error_file_name = DIR_PATH + '/../results/optimal_filter/{}_events/pileup_prob_{}_of_amp_error.txt'.format(num_events, prob)
    mf_amp_error_file_name = DIR_PATH + '/../results/matched_filter/{}_events/pileup_prob_{}_amp_error.txt'.format(num_events, prob)

    amplitude = np.loadtxt(amplitude_file_name)
    of_amp_error = np.loadtxt(of_amp_error_file_name)
    mf_amp_error = np.loadtxt(mf_amp_error_file_name)

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)
    font = {
            'family': 'Times New Roman',
            'size': 16
            }

    # fig.suptitle('Comparação do erro \n' '{} eventos e Empilhamento de {}%'
    #              .format(num_events, prob))
    fig.suptitle('Comparação do erro')
    ax0.hist(of_amp_error, bins="auto", color='dimgrey')
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('OF \n' r'$\mu={}$, $\sigma={}$'
                  .format(of_amp_error.mean(), of_amp_error.std()))
    ax0.set_xlabel('Erro de Estimação', **font)
    ax0.set_ylabel('Eventos', **font)

    ax1.hist(mf_amp_error, bins="auto", facecolor='dimgrey')
    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('MF \n' r'$\mu={}$, $\sigma={}$'
                  .format(mf_amp_error.mean(), mf_amp_error.std()))
    ax1.set_xlabel('Erro de Estimação', **font)
    ax1.set_ylabel('Eventos', **font)

    plt.show()
