"""Compares means and stds for: OF, DMF and SMF."""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    num_events = 200000
    probs = [0.0, 10.0, 50.0, 100.0]

    of_stds = []
    of_means = []

    dmf_stds = []
    dmf_means = []

    smf_stds = []
    smf_means = []
    for prob in probs:
        common_path = DIR_PATH + f'/../../results/simulated/pileup_data/prob_{prob}/{num_events}_events'

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

    fig.suptitle('OF X DMF X SMF' ' {} eventos'
                 .format(num_events))

    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('Média')
    ax0.set_xlabel('Empilhamento (%)')
    ax0.set_ylabel('Média')
    ax0.plot(probs, of_means, '-ro', label='OF')
    ax0.plot(probs, dmf_means, '-bo', label='DMF')
    ax0.plot(probs, smf_means, '-go', label='SMF')
    ax0.legend()

    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('Desvio Padrão')
    ax1.set_xlabel('Empilhamento (%)')
    ax1.set_ylabel('Desvio Padrão')
    ax1.plot(probs, of_stds, '-ro', label='OF')
    ax1.plot(probs, dmf_stds, '-bo', label='DMF')
    ax1.plot(probs, smf_stds, '-go', label='SMF')
    ax1.legend()

    plt.show()
