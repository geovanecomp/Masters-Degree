# -*- coding: utf-8 -*-

"""Compares OF, D-MF, E-MF STD and mean for real data."""
# results_low_snr_adc_5
import os.path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['xtick.labelsize'] = 22
plt.rcParams['ytick.labelsize'] = 22

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    noise_mean = 90
    amplitude_means = [10, 100, 300]
    channels = [1, 10, 36]

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

    mf_means = []
    mf_stds = []
    mf_means_mean = []
    mf_means_std = []
    mf_stds_mean = []
    mf_stds_std = []

    for channel in channels:
        sufix = f'_ch{channel}'
        for amplitude_mean in amplitude_means:
            base_folder = DIR_PATH + f'/../results/hybrid/amplitude_mean{amplitude_mean}'
            of_file_name = base_folder + f'/OF/mu{noise_mean}/of_amp_error{sufix}.txt'
            dmf_file_name = base_folder + f'/D_MF/mu{noise_mean}/dmf_amp_error{sufix}.txt'
            mf_file_name = base_folder + f'/E_MF/mu{noise_mean}/mf_amp_error{sufix}.txt'

            of_error = np.loadtxt(of_file_name)
            dmf_error = np.loadtxt(dmf_file_name)
            mf_error = np.loadtxt(mf_file_name)

            of_means.append(np.mean(of_error))
            of_stds.append(np.std(of_error))

            dmf_means.append(np.mean(dmf_error))
            dmf_stds.append(np.std(dmf_error))

            mf_means.append(np.mean(mf_error))
            mf_stds.append(np.std(mf_error))

        of_means_mean.append(np.mean(of_means))
        of_means_std.append(np.std(of_means))
        of_stds_mean.append(np.mean(of_stds))
        of_stds_std.append(np.std(of_stds))

        dmf_means_mean.append(np.mean(mf_means))
        dmf_means_std.append(np.std(mf_means))
        dmf_stds_mean.append(np.mean(mf_stds))
        dmf_stds_std.append(np.std(mf_stds))

        mf_means_mean.append(np.mean(mf_means))
        mf_means_std.append(np.std(mf_means))
        mf_stds_mean.append(np.mean(mf_stds))
        mf_stds_std.append(np.std(mf_stds))

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

    print('EMF: \n')
    print(mf_means_mean)
    print(mf_stds_mean)
    # fig.suptitle('OF X MF' ' {} eventos\n A=300, PU=100'
    #              .format(num_events))
    fig.suptitle(f'Errorbar para channels: {channels} Amps: {amplitude_means} Media: {noise_mean}')
    x_ticks = [1, 10, 36]
    # plt.xticks(x_ticks)
    # x_ticks = np.arange(-26, 26, 2)
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_xlabel('Channel', **font)
    ax0.set_ylabel('Média', **font)
    ax0.errorbar(channels, of_means_mean, c='r', marker='o', yerr=of_means_std, label='DP-OF',ls='None')
    ax0.errorbar(channels, dmf_means_mean, c='b', marker='s', yerr=dmf_means_std, label='DP-MF',ls='None')
    ax0.errorbar(channels, mf_means_mean, c='g', marker='_', yerr=mf_means_std, label='DP-MF',ls='None')
    ax0.legend(loc='upper left', fontsize=21)
    ax0.set_xticks(x_ticks)

    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_xlabel('Channel', **font)
    ax1.set_ylabel('RMS', **font)
    ax1.errorbar(channels, of_stds_mean, c='r', marker='o', yerr=of_stds_std, label='DP-OF', ls='None')
    ax1.errorbar(channels, dmf_stds_mean, c='b', marker='s', yerr=dmf_stds_std, label='DP-MF', ls='None')
    ax1.errorbar(channels, mf_stds_mean, c='g', marker='_', yerr=mf_stds_std, label='DP-MF', ls='None')
    ax1.legend(loc='upper left', fontsize=21)
    ax1.set_xticks(x_ticks)

    plt.show()