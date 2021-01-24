# -*- coding: utf-8 -*-

"""Compares OF and MF STD and mean for real data."""

import os.path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['xtick.labelsize'] = 22
plt.rcParams['ytick.labelsize'] = 22

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    noise_means = [30, 50, 90]

    of_means = []
    of_stds = []

    mf_means = []
    mf_stds = []

    for noise_mean in noise_means:
        of_error_file_name = DIR_PATH + '/../results/real_data/mu{}/optimal_filter/of_amp_error.txt'.format(noise_mean)
        mf_error_file_name = DIR_PATH + '/../results/real_data/mu{}/matched_filter/mf_amp_error.txt'.format(noise_mean)

        of_error = np.loadtxt(of_error_file_name)
        mf_error = np.loadtxt(mf_error_file_name)

        of_means.append(np.mean(of_error))
        of_stds.append(np.std(of_error))

        mf_means.append(np.mean(mf_error))
        mf_stds.append(np.std(mf_error))

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)
    font = {
            'family': 'Times New Roman',
            'size': 22
            }

    # fig.suptitle('OF X MF' ' {} eventos\n A=300, PU=100'
    #              .format(num_events))

    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_xlabel('Ruído', **font)
    ax0.set_ylabel('Média', **font)
    ax0.plot(noise_means, of_means, 'ro', label='Média-OF')
    ax0.plot(noise_means, mf_means, 'bo', label='Média-MF')
    ax0.legend(loc='upper left', fontsize=21)

    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_xlabel('Ruído', **font)
    ax1.set_ylabel('RMS', **font)
    ax1.plot(noise_means, of_stds, 'ro', label='RMS-OF')
    ax1.plot(noise_means, mf_stds, 'bo', label='RMS-MF')
    ax1.legend(loc='upper left', fontsize=21)

    plt.show()
