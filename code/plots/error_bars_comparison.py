# -*- coding: utf-8 -*-

"""Compares OF and MF STD and mean."""

import os.path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['xtick.labelsize'] = 22
plt.rcParams['ytick.labelsize'] = 22

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    num_runs = 10
    num_events = 10000
    # In %
    probs = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]

    of_means_mean = []
    of_means_std = []
    of_stds_mean = []
    of_stds_std = []

    mf_means_mean = []
    mf_means_std = []
    mf_stds_mean = []
    mf_stds_std = []

    for prob in probs:
        of_mean_file_name = DIR_PATH + '/../results/error_bar/{}_events/{}_runs_of_mean_prob_{}.txt'.format(num_events, num_runs, prob)
        of_std_file_name = DIR_PATH + '/../results/error_bar/{}_events/{}_runs_of_std_prob_{}.txt'.format(num_events, num_runs, prob)
        mf_mean_file_name = DIR_PATH + '/../results/error_bar/{}_events/{}_runs_mf_mean_prob_{}.txt'.format(num_events, num_runs, prob)
        mf_std_file_name = DIR_PATH + '/../results/error_bar/{}_events/{}_runs_mf_std_prob_{}.txt'.format(num_events, num_runs, prob)

        of_means = np.loadtxt(of_mean_file_name)
        of_stds = np.loadtxt(of_std_file_name)

        mf_means = np.loadtxt(mf_mean_file_name)
        mf_stds = np.loadtxt(mf_std_file_name)

        of_means_mean.append(np.mean(of_means))
        of_means_std.append(np.std(of_means))

        of_stds_mean.append(np.mean(of_stds))
        of_stds_std.append(np.std(of_stds))

        mf_means_mean.append(np.mean(mf_means))
        mf_means_std.append(np.std(mf_means))

        mf_stds_mean.append(np.mean(mf_stds))
        mf_stds_std.append(np.std(mf_stds))

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)
    font = {
            'family': 'Times New Roman',
            'size': 22
            }

    # fig.suptitle('OF X MF' ' {} eventos\n A=300, PU=100'
    #              .format(num_events))

    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_xlabel('Ocupação (%)', **font)
    ax0.set_ylabel('Média', **font)
    ax0.errorbar(probs, of_means_mean, c='k', marker='o', yerr=of_means_std, label='DP-OF',ls='None')
    ax0.errorbar(probs, mf_means_mean, c='k', marker='s', yerr=mf_means_std, label='DP-MF',ls='None')
    ax0.legend(loc='upper left', fontsize=21)

    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_xlabel('Ocupação (%)', **font)
    ax1.set_ylabel('RMS', **font)
    ax1.errorbar(probs, of_stds_mean, c='k', marker='o', yerr=of_stds_std, label='DP-OF', ls='None')
    ax1.errorbar(probs, mf_stds_mean, c='k', marker='s', yerr=mf_stds_std, label='DP-MF', ls='None')
    ax1.legend(loc='upper left', fontsize=21)

    plt.show()
