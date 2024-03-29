"""Process Histogram comparing data generated by Matlab and Python script."""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    num_events = 200000
    prob = 100.0

    # Signals
    matlab_data = np.loadtxt(DIR_PATH + f'/../../matlab_code/results/matlabSignals/{int(num_events/2)}dadosTileOcup{int(prob)}.txt')
    script_data = np.loadtxt(DIR_PATH + f'/../../results/simulated/pileup_data/prob_{prob}/{num_events}_events/base_data/tile_signal.txt')

    # Noises
    # matlab_data = np.loadtxt(DIR_PATH + f'/../../matlab_code/results/matlabNoises/{int(num_events/2)}ruidoTileOcup{int(prob)}.txt')
    # script_data = np.loadtxt(DIR_PATH + f'/../../results/simulated/pileup_data/prob_{prob}/{num_events}_events/base_data/noise.txt')

    # Amplitude
    # matlab_data = np.loadtxt(DIR_PATH + f'/../../matlab_code/results/matlabSignals/{int(num_events/2)}dadosTileOcup{int(prob)}-A.txt')
    # script_data = np.loadtxt(DIR_PATH + f'/../../results/simulated/pileup_data/prob_{prob}/{num_events}_events/base_data/tile_A.txt')

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
