# -*- coding: utf-8 -*-

"""Compares STD and Mean for: OF, SMF and DMF"""

import os.path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['xtick.labelsize'] = 22
plt.rcParams['ytick.labelsize'] = 22

DIR_PATH = os.path.dirname(__file__)
BASE_PATH = DIR_PATH + '/../../results/simulated/pileup_data/error_bar'

if __name__ == '__main__':
    num_runs = 10
    num_events = 200
    # In %
    probs = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]

    of_means_mean = []
    of_means_std = []
    of_stds_mean = []
    of_stds_std = []

    smf_means_mean = []
    smf_means_std = []
    smf_stds_mean = []
    smf_stds_std = []

    dmf_means_mean = []
    dmf_means_std = []
    dmf_stds_mean = []
    dmf_stds_std = []

    for prob in probs:
        of_mean_file_name = BASE_PATH + f'/{num_events}_events/{num_runs}_runs_of_mean_prob_{prob}.txt'
        of_std_file_name = BASE_PATH + f'/{num_events}_events/{num_runs}_runs_of_std_prob_{prob}.txt'
        smf_mean_file_name = BASE_PATH + f'/{num_events}_events/{num_runs}_runs_smf_mean_prob_{prob}.txt'
        smf_std_file_name = BASE_PATH + f'/{num_events}_events/{num_runs}_runs_smf_std_prob_{prob}.txt'
        dmf_mean_file_name = BASE_PATH + f'/{num_events}_events/{num_runs}_runs_dmf_mean_prob_{prob}.txt'
        dmf_std_file_name = BASE_PATH + f'/{num_events}_events/{num_runs}_runs_dmf_std_prob_{prob}.txt'

        of_means = np.loadtxt(of_mean_file_name)
        of_stds = np.loadtxt(of_std_file_name)
        smf_means = np.loadtxt(smf_mean_file_name)
        smf_stds = np.loadtxt(smf_std_file_name)
        dmf_means = np.loadtxt(dmf_mean_file_name)
        dmf_stds = np.loadtxt(dmf_std_file_name)

        of_means_mean.append(np.mean(of_means))
        of_means_std.append(np.std(of_means))
        of_stds_mean.append(np.mean(of_stds))
        of_stds_std.append(np.std(of_stds))

        smf_means_mean.append(np.mean(smf_means))
        smf_means_std.append(np.std(smf_means))
        smf_stds_mean.append(np.mean(smf_stds))
        smf_stds_std.append(np.std(smf_stds))

        dmf_means_mean.append(np.mean(dmf_means))
        dmf_means_std.append(np.std(dmf_means))
        dmf_stds_mean.append(np.mean(dmf_stds))
        dmf_stds_std.append(np.std(dmf_stds))

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)
    font = {
            'family': 'Times New Roman',
            'size': 22
            }

    fig.suptitle(f'High SNR: OF X DMF X SMF \n {num_events} eventos & {num_runs} runs')

    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_xlabel('Ocupação (%)', **font)
    ax0.set_ylabel('Média', **font)
    ax0.errorbar(probs, of_means_mean, c='r', marker='o', yerr=of_means_std, label='OF',ls='None')
    ax0.errorbar(probs, dmf_means_mean, c='g', marker='+', yerr=dmf_means_std, label='DMF',ls='None')
    ax0.errorbar(probs, smf_means_mean, c='b', marker='s', yerr=smf_means_std, label='SMF',ls='None')
    ax0.legend(loc='upper left', fontsize=21)

    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_xlabel('Ocupação (%)', **font)
    ax1.set_ylabel('RMS', **font)
    ax1.errorbar(probs, of_stds_mean, c='r', marker='o', yerr=of_stds_std, label='OF', ls='None')
    ax1.errorbar(probs, dmf_stds_mean, c='g', marker='+', yerr=dmf_stds_std, label='DMF', ls='None')
    ax1.errorbar(probs, smf_stds_mean, c='b', marker='s', yerr=smf_stds_std, label='SMF', ls='None')
    ax1.legend(loc='upper left', fontsize=21)

    plt.show()
