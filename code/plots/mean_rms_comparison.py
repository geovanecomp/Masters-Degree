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
    noise_means = [30, 50, 90]
    sufix = '_small'
    base_folder = DIR_PATH + '/../results/hybrid'

    of_means = []
    of_stds = []

    dmf_means = []
    dmf_stds = []

    mf_means = []
    mf_stds = []

    for noise_mean in noise_means:
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

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)
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

    print('EMF: \n')
    print(mf_means)
    print(mf_stds)
    # fig.suptitle('OF X MF' ' {} eventos\n A=300, PU=100'
    #              .format(num_events))

    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_xlabel('Ruído', **font)
    ax0.set_ylabel('Média', **font)
    ax0.plot(noise_means, of_means, '-ro', label='Média-OF')
    ax0.plot(noise_means, dmf_means, '-bo', label='Média-DMF')
    ax0.plot(noise_means, mf_means, '-go', label='Média-EMF')
    ax0.legend(loc='best', fontsize=19)

    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_xlabel('Ruído', **font)
    ax1.set_ylabel('RMS', **font)
    ax1.plot(noise_means, of_stds, '-ro', label='RMS-OF')
    ax1.plot(noise_means, dmf_stds, '-bo', label='RMS-DMF')
    ax1.plot(noise_means, mf_stds, '-go', label='RMS-EMF')
    ax1.legend(loc='best', fontsize=19)

    plt.show()
