# -*- coding: utf-8 -*-

"""For the same ocupation, compare OF and MF Mean/STD for all amplitudes."""

import os.path
import numpy as np
import matplotlib.pyplot as plt
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from config import Legend, Tick


DIR_PATH = os.path.dirname(__file__)
BASE_PATH = DIR_PATH + '/../../results'
np.set_printoptions(suppress=True, precision=3)
if __name__ == '__main__':
    np.set_printoptions(suppress=True, precision=4)
    num_runs = 10
    num_events = 200000

    probs = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
    # simulated_amp = 300 ADC and simulated_low_snr_amp = 10 ADC
    amplitudes = [300, 100, 10]
    datasets = ['simulated_snr3', 'simulated_snr1', 'simulated_snr01']

    of_stds = dict.fromkeys(probs, 0)
    of_means = dict.fromkeys(probs, 0)

    smf_stds = dict.fromkeys(probs, 0)
    smf_means = dict.fromkeys(probs, 0)

    dmf_stds = dict.fromkeys(probs, 0)
    dmf_means = dict.fromkeys(probs, 0)

    of_means_mean = []
    of_means_std = []
    of_stds_mean = []
    of_stds_std = []

    dmf_means_mean = []
    dmf_means_std = []
    dmf_stds_mean = []
    dmf_stds_std = []

    smf_means_mean = []
    smf_means_std = []
    smf_stds_mean = []
    smf_stds_std = []

    for dataset in datasets:
        for prob in probs:
            common_path = BASE_PATH + f'/{dataset}/pileup_data/error_bar/{num_events}_events'
            of_errorbar_mean_file_name = common_path + f'/{num_runs}_runs_of_mean_prob_{prob}.txt'
            of_errorbar_std_file_name = common_path + f'/{num_runs}_runs_of_std_prob_{prob}.txt'
            dmf_errorbar_mean_file_name = common_path + f'/{num_runs}_runs_dmf_mean_prob_{prob}.txt'
            dmf_errorbar_std_file_name = common_path + f'/{num_runs}_runs_dmf_std_prob_{prob}.txt'
            smf_errorbar_mean_file_name = common_path + f'/{num_runs}_runs_smf_mean_prob_{prob}.txt'
            smf_errorbar_std_file_name = common_path + f'/{num_runs}_runs_smf_std_prob_{prob}.txt'

            of_errorbar_means = np.loadtxt(of_errorbar_mean_file_name)
            of_errorbar_stds = np.loadtxt(of_errorbar_std_file_name)
            dmf_errorbar_means = np.loadtxt(dmf_errorbar_mean_file_name)
            dmf_errorbar_stds = np.loadtxt(dmf_errorbar_std_file_name)
            smf_errorbar_means = np.loadtxt(smf_errorbar_mean_file_name)
            smf_errorbar_stds = np.loadtxt(smf_errorbar_std_file_name)

            of_means_mean.append(np.mean(of_errorbar_means))
            of_means_std.append(np.std(of_errorbar_means))
            of_stds_mean.append(np.mean(of_errorbar_stds))
            of_stds_std.append(np.std(of_errorbar_stds))

            dmf_means_mean.append(np.mean(dmf_errorbar_means))
            dmf_means_std.append(np.std(dmf_errorbar_means))
            dmf_stds_mean.append(np.mean(dmf_errorbar_stds))
            dmf_stds_std.append(np.std(dmf_errorbar_stds))

            smf_means_mean.append(np.mean(smf_errorbar_means))
            smf_means_std.append(np.std(smf_errorbar_means))
            smf_stds_mean.append(np.mean(smf_errorbar_stds))
            smf_stds_std.append(np.std(smf_errorbar_stds))

    part1 = len(probs)
    part2 = part1 + len(probs)

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_xlabel('Ocupação (%)', **Legend.font)
    ax0.set_ylabel('Média', **Legend.font)
    ax0.errorbar(probs, of_means_mean[:part1], c='r', marker='o', yerr=of_means_std[:part1], label='OF-SNR3',ls='None')
    ax0.errorbar(probs, of_means_mean[part1:part2], c='#FA6E6E', marker='o', yerr=of_means_std[part1:part2], label='OF-SNR1',ls='None')
    ax0.errorbar(probs, of_means_mean[part2:], c='#FEC1B4', marker='o', yerr=of_means_std[part2:], label='OF-SNR0.1',ls='None')
    ax0.errorbar(probs, dmf_means_mean[:part1], c='g', marker='s', yerr=dmf_means_std[:part1], label='DMF-SNR3',ls='None')
    ax0.errorbar(probs, dmf_means_mean[part1:part2], c='#6FFB56', marker='s', yerr=dmf_means_std[part1:part2], label='DMF-SNR1',ls='None')
    ax0.errorbar(probs, dmf_means_mean[part2:], c='#C3FFB9', marker='s', yerr=dmf_means_std[part2:], label='DMF-SNR0.1',ls='None')
    ax0.errorbar(probs, smf_means_mean[:part1], c='b', marker='+', yerr=smf_means_std[:part1], label='SMF-SNR3',ls='None')
    ax0.errorbar(probs, smf_means_mean[part1:part2], c='#77A0FF', marker='+', yerr=smf_means_std[part1:part2], label='SMF-SNR1',ls='None')
    ax0.errorbar(probs, smf_means_mean[part2:], c='#AFC7FF', marker='+', yerr=smf_means_std[part2:], label='SMF-SNR0.1',ls='None')
    ax0.legend(loc='best', fontsize=21)
    ax0.set_xticks(probs)
    ax0.tick_params(axis='both', which='major', labelsize=16)

    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_xlabel('Ocupação (%)', **Legend.font)
    ax1.set_ylabel('RMS', **Legend.font)
    ax1.errorbar(probs, of_stds_mean[:part1], c='r', marker='o', yerr=of_stds_std[:part1], label='OF-SNR3',ls='None')
    ax1.errorbar(probs, of_stds_mean[part1:part2], c='#FA6E6E', marker='o', yerr=of_stds_std[part1:part2], label='OF-SNR1',ls='None')
    ax1.errorbar(probs, of_stds_mean[part2:], c='#FEC1B4', marker='o', yerr=of_stds_std[part2:], label='OF-SNR0.1',ls='None')
    ax1.errorbar(probs, dmf_stds_mean[:part1], c='g', marker='s', yerr=dmf_stds_std[:part1], label='DMF-SNR3',ls='None')
    ax1.errorbar(probs, dmf_stds_mean[part1:part2], c='#6FFB56', marker='s', yerr=dmf_stds_std[part1:part2], label='DMF-SNR1',ls='None')
    ax1.errorbar(probs, dmf_stds_mean[part2:], c='#C3FFB9', marker='s', yerr=dmf_stds_std[part2:], label='DMF-SNR0.1',ls='None')
    ax1.errorbar(probs, smf_stds_mean[:part1], c='b', marker='+', yerr=smf_stds_std[:part1], label='SMF-SNR3',ls='None')
    ax1.errorbar(probs, smf_stds_mean[part1:part2], c='#77A0FF', marker='+', yerr=smf_stds_std[part1:part2], label='SMF-SNR1',ls='None')
    ax1.errorbar(probs, smf_stds_mean[part2:], c='#AFC7FF', marker='+', yerr=smf_stds_std[part2:], label='SMF-SNR0.1',ls='None')
    ax1.legend(loc='best', fontsize=21)
    ax1.set_xticks(probs)
    ax1.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
