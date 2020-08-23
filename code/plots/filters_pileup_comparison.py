"""Compares OF Amplitude against OF Error (OF Amplitude - Amplitude)."""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    num_events = 10000
    probs = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]

    of_stds = []
    of_means = []

    mf_stds = []
    mf_means = []
    for prob in probs:
        of_error_file_name = DIR_PATH + '/../results/optimal_filter/{}_events/pileup_prob_{}_of_amp_error.txt'.format(num_events, prob)
        mf_error_file_name = DIR_PATH + '/../results/matched_filter/{}_events/pileup_prob_{}_amp_signal.txt'.format(num_events, prob)
        of_error = np.loadtxt(of_error_file_name)
        mf_error = np.loadtxt(mf_error_file_name)

        of_means.append(np.mean(of_error))
        of_stds.append(np.std(of_error))

        mf_means.append(np.mean(mf_error))
        mf_stds.append(np.std(mf_error))

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)

    fig.suptitle('OF X MF' ' {} eventos'
                 .format(num_events))

    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('Média')
    ax0.set_xlabel('Empilhamento (%)')
    ax0.set_ylabel('Média')
    ax0.plot(probs, of_means, 'ro', label='OF')
    ax0.plot(probs, mf_means, 'bo', label='MF')
    ax0.legend()

    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('Desvio Padrão')
    ax1.set_xlabel('Empilhamento (%)')
    ax1.set_ylabel('Desvio Padrão')
    ax1.plot(probs, of_stds, 'ro', label='OF')
    ax1.plot(probs, mf_stds, 'bo', label='MF')
    ax1.legend()

    plt.show()
