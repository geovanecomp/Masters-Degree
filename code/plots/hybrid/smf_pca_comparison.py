"""Compares means and stds for SMF PCA Components: 1, 3, 5, 7."""

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

if __name__ == '__main__':
    channel = 1
    noise_mean = 90
    sufix = f'_ch{channel}'

    amps = [10, 100, 300]

    pca1_smf_stds = []
    pca1_smf_means = []

    pca3_smf_stds = []
    pca3_smf_means = []

    pca5_smf_stds = []
    pca5_smf_means = []

    pca7_smf_stds = []
    pca7_smf_means = []
    for amp in amps:
        base_folder = DIR_PATH + f'/../../results/hybrid/amplitude_mean{amp}'

        pca1_smf_error_file_name = f'{base_folder}/S_MF_PCA1/mu{noise_mean}/smf_amp_error{sufix}.txt'
        pca3_smf_error_file_name = f'{base_folder}/S_MF_PCA3/mu{noise_mean}/smf_amp_error{sufix}.txt'
        pca5_smf_error_file_name = f'{base_folder}/S_MF_PCA5/mu{noise_mean}/smf_amp_error{sufix}.txt'
        pca7_smf_error_file_name = f'{base_folder}/S_MF/mu{noise_mean}/smf_amp_error{sufix}.txt'

        pca1_smf_error = np.loadtxt(pca1_smf_error_file_name)
        pca3_smf_error = np.loadtxt(pca3_smf_error_file_name)
        pca5_smf_error = np.loadtxt(pca5_smf_error_file_name)
        pca7_smf_error = np.loadtxt(pca7_smf_error_file_name)

        pca1_smf_means.append(np.mean(pca1_smf_error))
        pca1_smf_stds.append(np.std(pca1_smf_error))

        pca3_smf_means.append(np.mean(pca3_smf_error))
        pca3_smf_stds.append(np.std(pca3_smf_error))

        pca5_smf_means.append(np.mean(pca5_smf_error))
        pca5_smf_stds.append(np.std(pca5_smf_error))

        pca7_smf_means.append(np.mean(pca7_smf_error))
        pca7_smf_stds.append(np.std(pca7_smf_error))

    print(f'1 && {pca1_smf_means[0]} & {pca1_smf_stds[0]}')
    print(f'3 && {pca3_smf_means[0]} & {pca3_smf_stds[0]}')
    print(f'5 && {pca5_smf_means[0]} & {pca5_smf_stds[0]}')
    print(f'7 && {pca7_smf_means[0]} & {pca7_smf_stds[0]}')

    print(f'1 && {pca1_smf_means[1]} & {pca1_smf_stds[1]}')
    print(f'3 && {pca3_smf_means[1]} & {pca3_smf_stds[1]}')
    print(f'5 && {pca5_smf_means[1]} & {pca5_smf_stds[1]}')
    print(f'7 && {pca7_smf_means[1]} & {pca7_smf_stds[1]}')

    print(f'1 && {pca1_smf_means[2]} & {pca1_smf_stds[2]}')
    print(f'3 && {pca3_smf_means[2]} & {pca3_smf_stds[2]}')
    print(f'5 && {pca5_smf_means[2]} & {pca5_smf_stds[2]}')
    print(f'7 && {pca7_smf_means[2]} & {pca7_smf_stds[2]}')


    fig, ((ax0)) = plt.subplots(nrows=1, ncols=1)

    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    # ax0.set_title('Média')
    ax0.set_xlabel('Amplitude', **Legend.font)
    ax0.set_ylabel('Média', **Legend.font)
    ax0.errorbar(amps, pca1_smf_means, c='r', ls='--', marker='o', yerr=pca1_smf_stds, label='PCA-1')
    ax0.errorbar(amps, pca3_smf_means, c='g', ls='--', marker='s', yerr=pca3_smf_stds, label='PCA-3')
    ax0.errorbar(amps, pca5_smf_means, c='b', ls='--', marker='+', yerr=pca5_smf_stds, label='PCA-5')
    ax0.errorbar(amps, pca7_smf_means, c='k', ls='--', marker='v', yerr=pca7_smf_stds, label='PCA-7')
    ax0.legend()
    ax0.set_xticks(amps)
    ax0.tick_params(axis='both', which='major', labelsize=11)

    plt.show()
