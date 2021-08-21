# -*- coding: utf-8 -*-

"""Compares OF, D-MF, S-MF STD and mean for real data."""
# results_low_snr_adc_5
import os.path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['xtick.labelsize'] = 22
plt.rcParams['ytick.labelsize'] = 22

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    amplitude_mean = 10
    channel = 1
    noise_means = [30, 50, 90]

    sufix = f'_ch{channel}'
    base_folder = DIR_PATH + f'/../../results/hybrid/amplitude_mean{amplitude_mean}'

    of_means = []
    of_stds = []

    dmf_means = []
    dmf_stds = []

    smf_means = []
    smf_stds = []

    for noise_mean in noise_means:
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

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2, figsize=(19,10))
    font = {
            'family': 'Times New Roman',
            'size': 22
            }
    print('Means and RMSs')
    print('OF: \n')
    print(of_means)
    print(of_stds)

    print('DMF: \n')
    print(dmf_means)
    print(dmf_stds)

    print('SMF: \n')
    print(smf_means)
    print(smf_stds)

    fig.suptitle(f'Comparação das Médias e RMS \n Canal: {channel} Amplitude: {amplitude_mean}')
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_xlabel('Ruído', **font)
    ax0.set_ylabel('Média', **font)
    ax0.plot(noise_means, of_means, '-ro', label='Média-OF')
    ax0.plot(noise_means, dmf_means, '-bo', label='Média-DMF')
    ax0.plot(noise_means, smf_means, '-go', label='Média-SMF')
    ax0.legend(loc='best', fontsize=19)

    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_xlabel('Ruído', **font)
    ax1.set_ylabel('RMS', **font)
    ax1.plot(noise_means, of_stds, '-ro', label='RMS-OF')
    ax1.plot(noise_means, dmf_stds, '-bo', label='RMS-DMF')
    ax1.plot(noise_means, smf_stds, '-go', label='RMS-SMF')
    ax1.legend(loc='best', fontsize=19)

    plt.show()
