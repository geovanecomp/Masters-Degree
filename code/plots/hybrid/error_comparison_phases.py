import os.path
import time
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)


def _get_distinct_jitters(jitters):
    return list(set(jitters))


def _compute_phase_mean(jitter_value, jitters, errors):
    jitter_errors = []
    jitter_std_errors = []
    for i in range(len(jitters)):
        if jitter_value == jitters[i]:
            jitter_errors.append(errors[i])
            jitter_std_errors.append(errors[i]/20)

    jitter_mean = np.mean(jitter_errors)
    jitter_std = np.std(jitter_errors)
    jitter_std_error_bar = np.std(jitter_std_errors)

    return jitter_mean, jitter_std, jitter_std_error_bar


def _compute_relative_mean_per_phase(jitters, errors):
    if len(jitters) != len(errors):
        print('Different length for jitters and amplitudes')
        print(len(jitters))
        print(len(errors))

    jitter_values = _get_distinct_jitters(jitters)

    phase_means = {}
    phase_stds = {}
    jitter_std_error_bar = {}
    for jitter_value in set(jitter_values):
        phase_means[jitter_value], phase_stds[jitter_value], jitter_std_error_bar[jitter_value] = _compute_phase_mean(jitter_value, jitters, errors)

    return phase_means, phase_stds, jitter_std_error_bar


if "__main__" == __name__:
    amplitude_mean = 10
    channel = 1
    noise_mean = 30

    sufix = f'_ch{channel}'
    base_folder = DIR_PATH + f'/../../results/hybrid/amplitude_mean{amplitude_mean}'

    of_amp_file_name = f'{base_folder}/OF/mu{noise_mean}/of_amp_error{sufix}.txt'
    dmf_amp_file_name = f'{base_folder}/D_MF/mu{noise_mean}/dmf_amp_error{sufix}.txt'
    smf_amp_file_name = f'{base_folder}/S_MF/mu{noise_mean}/smf_amp_error{sufix}.txt'
    of_error = np.loadtxt(of_amp_file_name)
    dmf_error = np.loadtxt(dmf_amp_file_name)
    smf_error = np.loadtxt(smf_amp_file_name)

    reference_jitter = f'{base_folder}/base_data/mu{noise_mean}/jitter{sufix}.txt'

    jitter_data = np.loadtxt(reference_jitter)[:len(of_error)][:, 0]

    t0 = time.time()

    phase_means_of, phase_stds_of, std_error_bar_of = _compute_relative_mean_per_phase(jitter_data, of_error)
    phase_means_dmf, phase_stds_dmf, std_error_bar_dmf = _compute_relative_mean_per_phase(jitter_data, dmf_error)
    phase_means_smf, phase_stds_smf, std_error_bar_smf = _compute_relative_mean_per_phase(jitter_data, smf_error)
    print(time.time() - t0, "seconds wall time")

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)
    fig.suptitle(f'Erro X Fase \n Ruido: {noise_mean} Canal: {channel} Amplitude: {amplitude_mean}')

    ax0.set_title('Média')
    ax0.errorbar(phase_means_of.keys(), phase_means_of.values(), c='r', marker='.', yerr=std_error_bar_of.values(), label='OF', ls='None')
    ax0.errorbar(phase_means_dmf.keys(), phase_means_dmf.values(), c='g', marker='x', yerr=std_error_bar_dmf.values(), label='D-MF', ls='None')
    ax0.errorbar(phase_means_smf.keys(), phase_means_smf.values(), c='b', marker='+', yerr=std_error_bar_smf.values(), label='S-MF', ls='None')

    ax0.grid(alpha=0.75)
    ax0.set_xlabel('Fase')
    ax0.set_ylabel('Contagens de ADC')
    ax0.legend()
    ax0.set_ylim(-400, 10)

    ax1.set_title('RMS')
    ax1.plot(phase_stds_of.keys(), phase_stds_of.values(), 'r.', label='OF')
    ax1.plot(phase_stds_dmf.keys(), phase_stds_dmf.values(), 'gx', label='D-MF')
    ax1.plot(phase_stds_smf.keys(), phase_stds_smf.values(), 'b+', label='S-MF')
    ax1.grid(alpha=0.75)
    ax1.set_xlabel('Fase')
    ax1.set_ylabel('Contagens de ADC')
    ax1.legend()
    ax1.set_ylim(-1, 400)

    plt.show()
