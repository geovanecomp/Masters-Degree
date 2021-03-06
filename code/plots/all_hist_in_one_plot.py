"""Compares data generated by Matlab, Python python and the real data."""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    num_events = 100000
    prob = 0.0
    noise_mean = 30

    # Signals
    # matlab_data = np.loadtxt(DIR_PATH + '/../matlab_code/results/matlabSignals/ped0/{}dadosTileOcup{}.txt'.format(num_events, int(prob)))
    # python_data = np.loadtxt(DIR_PATH + '/../results/pileup_data/prob_{}/{}_events/tile_signal_prob_{}.txt'.format(prob, num_events, prob))
    # real_data = np.loadtxt(DIR_PATH + '/../results/real_data/mu{}/tile_signal.txt'.format(noise_mean))

    # Noises
    # matlab_data = np.loadtxt(DIR_PATH + '/../matlab_code/results/matlabNoises/ped0/{}ruidoTileOcup{}.txt'.format(num_events, int(prob)))
    # python_data = np.loadtxt(DIR_PATH + '/../results/pileup_data/prob_{}/{}_events/tile_noise_prob_{}.txt'.format(prob, num_events, prob))
    # real_data = np.loadtxt(DIR_PATH + '/../results/real_data/mu{}/tile_signal.txt'.format(noise_mean))

    # Amplitude
    matlab_data = np.loadtxt(DIR_PATH + '/../matlab_code/results/matlabSignals/ped0/{}dadosTileOcup{}-A.txt'.format(num_events, int(prob)))
    python_data = np.loadtxt(DIR_PATH + '/../results/pileup_data/prob_{}/{}_events/tile_A_signal_prob_{}.txt'.format(prob, num_events, prob))
    real_data = np.loadtxt(DIR_PATH + '/../results/no_ped_real_data/mu{}/tile_A.txt'.format(noise_mean))

    matlab_data_mean = np.mean(matlab_data)
    matlab_data_std = np.std(matlab_data)

    python_data_mean = np.mean(python_data)
    python_data_std = np.std(python_data)

    real_data = real_data[0:num_events]
    real_data_mean = np.mean(real_data)
    real_data_std = np.std(real_data)

    # plt.suptitle('{} events | Ocup: {}% | Noise Mean: {}'.format(num_events, prob, noise_mean), fontsize=14)
    plt.hist(matlab_data, bins=20, alpha=0.4, facecolor='dimgrey', label='Matlab')
    plt.hist(python_data, bins=20, alpha=0.4, facecolor='darkblue', label='Python')
    plt.hist(real_data, bins=20, alpha=0.4, facecolor='green', label='Real')
    plt.legend(prop={'size': 10})
    plt.grid(axis='y', alpha=0.75)
    plt.suptitle('{} events | Ocup: {}% | Noise Mean: {}'
                 '\n Matlab ' r'$\mu={}$, $\sigma={}$'
                 '\n Python ' r'$\mu={}$, $\sigma={}$'
                 '\n Real ' r'$\mu={}$, $\sigma={}$'
                 .format(
                        num_events, prob, noise_mean,
                        matlab_data_mean, matlab_data_std,
                        python_data_mean, python_data_std,
                        real_data_mean, real_data_std
                      )
                 )
    plt.show()
