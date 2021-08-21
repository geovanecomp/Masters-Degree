# -*- coding: utf-8 -*-

"""Compares OF, D-MF, S-MF STD and mean for real data."""

import os.path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['xtick.labelsize'] = 22
plt.rcParams['ytick.labelsize'] = 22

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    amplitude_mean = 10
    channels = [1, 10, 36]
    noise_means = [30, 50, 90]

    of_means = []
    of_stds = []
    of_means_mean = []
    of_means_std = []
    of_stds_mean = []
    of_stds_std = []

    dmf_means = []
    dmf_stds = []
    dmf_means_mean = []
    dmf_means_std = []
    dmf_stds_mean = []
    dmf_stds_std = []

    smf_means = []
    smf_stds = []
    smf_means_mean = []
    smf_means_std = []
    smf_stds_mean = []
    smf_stds_std = []

    for noise_mean in noise_means:
        base_folder = DIR_PATH + f'/../../results/hybrid/amplitude_mean{amplitude_mean}'
        for channel in channels:
            sufix = f'_ch{channel}'
            of_file_name = base_folder + f'/OF/mu{noise_mean}/of_amp_error{sufix}.txt'
            dmf_file_name = base_folder + f'/D_MF/mu{noise_mean}/dmf_amp_error{sufix}.txt'
            smf_file_name = base_folder + f'/S_MF/mu{noise_mean}/smf_amp_error{sufix}.txt'

            of_error = np.loadtxt(of_file_name)
            dmf_error = np.loadtxt(dmf_file_name)
            smf_error = np.loadtxt(smf_file_name)

            of_means.append(np.mean(of_error))
            of_stds.append(np.std(of_error))

            dmf_means.append(np.mean(dmf_error))
            dmf_stds.append(np.std(dmf_error))

            smf_means.append(np.mean(smf_error))
            smf_stds.append(np.std(smf_error))

        of_means_mean.append(np.mean(of_means))
        of_means_std.append(np.std(of_means))
        of_stds_mean.append(np.mean(of_stds))
        of_stds_std.append(np.std(of_stds))

        dmf_means_mean.append(np.mean(dmf_means))
        dmf_means_std.append(np.std(dmf_means))
        dmf_stds_mean.append(np.mean(dmf_stds))
        dmf_stds_std.append(np.std(dmf_stds))

        smf_means_mean.append(np.mean(smf_means))
        smf_means_std.append(np.std(smf_means))
        smf_stds_mean.append(np.mean(smf_stds))
        smf_stds_std.append(np.std(smf_stds))

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)
    font = {
            'family': 'Times New Roman',
            'size': 22
            }
    print('Means and RMSs')
    print('OF: \n')
    print(of_means_mean)
    print(of_stds_mean)

    print('DMF: \n')
    print(dmf_means_mean)
    print(dmf_stds_mean)

    print('SMF: \n')
    print(smf_means_mean)
    print(smf_stds_mean)

    fig.suptitle(f'Errorbar para channels: {channels} Amp: {amplitude_mean}')
    x_ticks = [30, 50, 90]
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_xlabel('noiseMean', **font)
    ax0.set_ylabel('Média', **font)
    ax0.errorbar(noise_means, of_means_mean, c='r', marker='o', yerr=of_means_std, label='DP-OF',ls='None')
    ax0.errorbar(noise_means, dmf_means_mean, c='b', marker='s', yerr=dmf_means_std, label='DP-MF',ls='None')
    ax0.errorbar(noise_means, smf_means_mean, c='g', marker='_', yerr=smf_means_std, label='DP-MF',ls='None')
    ax0.legend(loc='upper left', fontsize=21)
    ax0.set_xticks(x_ticks)

    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_xlabel('noiseMean', **font)
    ax1.set_ylabel('RMS', **font)
    ax1.errorbar(noise_means, of_stds_mean, c='r', marker='o', yerr=of_stds_std, label='DP-OF', ls='None')
    ax1.errorbar(noise_means, dmf_stds_mean, c='b', marker='s', yerr=dmf_stds_std, label='DP-MF', ls='None')
    ax1.errorbar(noise_means, smf_stds_mean, c='g', marker='_', yerr=smf_stds_std, label='DP-MF', ls='None')
    ax1.legend(loc='upper left', fontsize=21)
    ax1.set_xticks(x_ticks)

    plt.show()
