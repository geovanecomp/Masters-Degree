"""Compares OF and MF STD and mean."""

import os.path
import numpy as np
import matplotlib.pyplot as plt

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

    print(len(probs))
    print(len(of_means_mean))
    print(len(of_means_std))

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)

    fig.suptitle('OF X MF' ' {} eventos'
                 .format(num_events))

    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('Média')
    ax0.set_xlabel('Empilhamento (%)')
    ax0.set_ylabel('Média')
    ax0.errorbar(probs, of_means_mean, c='r', yerr=of_means_std, label='DP-OF',ls='None')
    ax0.plot(probs, of_means_mean, 'ro', label='OF')
    ax0.errorbar(probs, mf_means_mean, c='b', yerr=mf_means_std, label='DP-MF',ls='None')
    ax0.plot(probs, mf_means_mean, 'bo', label='MF')
    ax0.legend(loc='upper left',)

    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('Desvio Padrão')
    ax1.set_xlabel('Empilhamento (%)')
    ax1.set_ylabel('Desvio Padrão')
    ax1.errorbar(probs, of_stds_mean, c='r', yerr=of_stds_std, label='DP-OF', ls='None')
    ax1.plot(probs, of_stds_mean, 'ro', label='OF')
    ax1.errorbar(probs, mf_stds_mean, c='b', yerr=mf_stds_std, label='DP-MF', ls='None')
    ax1.plot(probs, mf_stds_mean, 'bo', label='MF')
    ax1.legend(loc='upper left',)

    plt.show()

    # fig = plt.figure()
    # x = np.arange(10)
    # y = 2.5 * np.sin(x / 20 * np.pi)
    # yerr = np.linspace(0.05, 0.2, 10)
    #
    # plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
    #
    # plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
    #
    # plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True,
    #              label='uplims=True, lolims=True')
    #
    # upperlimits = [True, False] * 5
    # lowerlimits = [False, True] * 5
    # plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits,
    #              label='subsets of uplims and lolims')
    #
    # plt.legend(loc='lower right')
    #
    # plt.show()
