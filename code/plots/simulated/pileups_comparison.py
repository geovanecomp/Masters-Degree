"""Compares means and stds for: OF, DMF and SMF."""

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
    dataset = 'simulated_snr01'
    num_events = 200000
    probs = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]

    of_stds = []
    of_means = []

    dmf_stds = []
    dmf_means = []

    smf_stds = []
    smf_means = []
    for prob in probs:
        common_path = DIR_PATH + f'/../../results/{dataset}/pileup_data/prob_{prob}/{num_events}_events'

        of_error_file_name = common_path + '/OF/of_amp_error.txt'
        dmf_error_file_name = common_path + '/D_MF/dmf_amp_error.txt'
        smf_error_file_name = common_path + '/S_MF/smf_amp_error.txt'

        of_error = np.loadtxt(of_error_file_name)
        dmf_error = np.loadtxt(dmf_error_file_name)
        smf_error = np.loadtxt(smf_error_file_name)

        of_means.append(np.mean(of_error))
        of_stds.append(np.std(of_error))

        dmf_means.append(np.mean(dmf_error))
        dmf_stds.append(np.std(dmf_error))

        smf_means.append(np.mean(smf_error))
        smf_stds.append(np.std(smf_error))

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)

    fig.suptitle('OF X DMF X SMF' ' {} eventos SNR = 0,1'
                 .format(num_events))

    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('Média')
    ax0.set_xlabel('Empilhamento (%)', **Legend.font)
    ax0.set_ylabel('Média', **Legend.font)
    ax0.plot(probs, of_means, '-ro', label='OF')
    ax0.plot(probs, dmf_means, '-bo', label='DMF')
    ax0.plot(probs, smf_means, '-go', label='SMF')
    ax0.legend()
    ax0.set_xticks(probs)

    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('Desvio Padrão')
    ax1.set_xlabel('Empilhamento (%)', **Legend.font)
    ax1.set_ylabel('Desvio Padrão', **Legend.font)
    ax1.plot(probs, of_stds, '-ro', label='OF')
    ax1.plot(probs, dmf_stds, '-bo', label='DMF')
    ax1.plot(probs, smf_stds, '-go', label='SMF')
    ax1.legend()
    ax1.set_xticks(probs)

    plt.show()
