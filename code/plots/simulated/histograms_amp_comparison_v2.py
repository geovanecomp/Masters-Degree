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
    dataset = 'simulated_snr01'
    prob = 100.0
    num_events = 200000

    # Pile data
    BASE_PATH = DIR_PATH + f'/../../results/{dataset}/pileup_data/prob_{prob}/{num_events}_events'
    true_amplitude_file_name = BASE_PATH + '/base_data/tile_A.txt'
    of_amplitude_file_name = BASE_PATH + '/OF/of_amp_signal.txt'
    dmf_amplitude_file_name = BASE_PATH + '/D_MF/dmf_amp_signal.txt'
    smf_amplitude_file_name = BASE_PATH + '/S_MF/smf_amp_signal.txt'

    true_amplitude = np.loadtxt(true_amplitude_file_name)[:int(num_events/2)]
    of_amplitude = np.loadtxt(of_amplitude_file_name)
    dmf_amplitude = np.loadtxt(dmf_amplitude_file_name)
    smf_amplitude = np.loadtxt(smf_amplitude_file_name)

    print(f'True Amp Mean: {true_amplitude.mean()} | True Amp STD: {true_amplitude.std()} \n' \
          f'OF Mean: {of_amplitude.mean()} | OF STD: {of_amplitude.std()} \n' \
          f'DMF Mean: {dmf_amplitude.mean()} | DMF STD: {dmf_amplitude.std()} \n' \
          f'SMF Mean: {smf_amplitude.mean()} | SMF STD: {smf_amplitude.std()} \n')


    # fig.suptitle('Comparação da Amplitude Verdadeira X Numérica \n' '{} eventos e Empilhamento de {}%'
                 # .format(num_events, prob))
    bins = 100
    plt.hist(true_amplitude, bins=bins, color='black', histtype=u'step', label='Amp-Verdadeira')
    plt.hist(of_amplitude, bins=bins, color='red', histtype=u'step', label='OF')
    plt.hist(dmf_amplitude, bins=bins, color='green', histtype=u'step', label='D-MF')
    plt.hist(smf_amplitude, bins=bins, color='blue', histtype=u'step', label='S-MF')
    plt.legend(prop={'size': 10})
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Energia (MeV)', **Legend.font)
    plt.ylabel('Eventos', **Legend.font)

    plt.show()
