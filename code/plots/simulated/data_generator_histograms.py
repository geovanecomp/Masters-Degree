"""Process Histogram comparing data generated by Matlab and Python script."""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    num_events = 10000

    # Signals
    matlab_data = np.loadtxt(DIR_PATH + '/../matlab_code/results/matlabSignals/{}dadosTileOcup50.txt'.format(num_events))
    script_data = np.loadtxt(DIR_PATH + '/../results/pileup_data/prob_50.0/{}_events/tile_signal_prob_50.0.txt'.format(num_events))

    # Noises
    # matlab_data = np.loadtxt(DIR_PATH + '/../matlab_code/results/matlabNoises/{}ruidoTileOcup0.txt'.format(num_events))
    # script_data = np.loadtxt(DIR_PATH + '/../results/pileup_data/prob_0.0/{}_events/tile_noise_prob_0.0.txt'.format(num_events))

    # Amplitude
    # matlab_data = np.loadtxt(DIR_PATH + '/../matlab_code/results/matlabSignals/{}dadosTileOcup0-A.txt'.format(num_events))
    # script_data = np.loadtxt(DIR_PATH + '/../results/pileup_data/prob_0.0/{}_events/tile_A_signal_prob_0.0.txt'.format(num_events))

    script_data_mean = np.mean(script_data)
    script_data_std = np.std(script_data)

    matlab_data_mean = np.mean(matlab_data)
    matlab_data_std = np.std(matlab_data)

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)

    fig.suptitle('{} events'.format(num_events), fontsize=14)
    ax0.hist(matlab_data, bins="auto", density=True, histtype='bar')
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('Matlab: Sinal \n' r'$\mu={}$, $\sigma={}$'
                  .format(matlab_data_mean, matlab_data_std))

    ax0.set_xlim(0, 1100)
    ax0.set_ylim(0, 0.005)

    ax1.hist(script_data, bins="auto", density=True, histtype='bar')
    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('Python: Sinal \n' r'$\mu={}$, $\sigma={}$'
                  .format(script_data_mean, script_data_std))
    ax1.set_xlim(0, 1100)
    ax1.set_ylim(0, 0.005)

    plt.show()