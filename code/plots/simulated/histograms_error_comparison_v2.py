"""Compares simulated data to all Amplitudes between OF, SMF and DMF in one figure"""

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
    dataset = 'simulated'
    prob = 0.0
    num_events = 200000

    # Pile data
    BASE_PATH = DIR_PATH + f'/../../results/{dataset}/pileup_data/prob_{prob}/{num_events}_events'
    of_amp_error_file_name = BASE_PATH + '/OF/of_amp_error.txt'
    dmf_amp_error_file_name = BASE_PATH + '/D_MF/dmf_amp_error.txt'
    smf_amplitude_file_name = BASE_PATH + '/S_MF/smf_amp_error.txt'

    of_amp_error = np.loadtxt(of_amp_error_file_name)
    dmf_amp_error = np.loadtxt(dmf_amp_error_file_name)
    smf_amp_error = np.loadtxt(smf_amplitude_file_name)

    print(f'OF Mean: {of_amp_error.mean()} | OF STD: {of_amp_error.std()} \n' \
          f'DMF Mean: {dmf_amp_error.mean()} | DMF STD: {dmf_amp_error.std()} \n' \
          f'SMF Mean: {smf_amp_error.mean()} | SMF STD: {smf_amp_error.std()} \n')


    # fig.suptitle('Comparação da Amplitude Verdadeira X Numérica \n' '{} eventos e Empilhamento de {}%'
                 # .format(num_events, prob))
    bins = 100
    plt.hist(of_amp_error, bins=bins, color='red', histtype=u'step', label='OF')
    plt.hist(dmf_amp_error, bins=bins, color='green', histtype=u'step', label='D-MF')
    plt.hist(smf_amp_error, bins=bins, color='blue', histtype=u'step', label='S-MF')
    plt.legend(prop={'size': 10})
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Erro', **Legend.font)
    plt.ylabel('Eventos', **Legend.font)
    plt.xlim(-500, 500)

    plt.show()
