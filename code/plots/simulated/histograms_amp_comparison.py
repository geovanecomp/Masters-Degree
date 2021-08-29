"""Compares simulated data to all Amplitudes between OF, SMF and DMF"""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    prob = 0.0
    num_events = 200

    # Pile data
    BASE_PATH = DIR_PATH + f'/../../results/simulated/pileup_data/prob_{prob}/{num_events}_events'
    true_amplitude_file_name = BASE_PATH + '/base_data/tile_A.txt'
    of_amplitude_file_name = BASE_PATH + '/OF/of_amp_signal.txt'
    dmf_amplitude_file_name = BASE_PATH + '/D_MF/dmf_amp_signal.txt'
    smf_amplitude_file_name = BASE_PATH + '/S_MF/smf_amp_signal.txt'

    true_amplitude = np.loadtxt(true_amplitude_file_name)[:int(num_events/2)]
    of_amplitude = np.loadtxt(of_amplitude_file_name)
    dmf_amplitude = np.loadtxt(dmf_amplitude_file_name)
    smf_amplitude = np.loadtxt(smf_amplitude_file_name)

    fig, ((ax0, ax1, ax2, ax3)) = plt.subplots(nrows=1, ncols=4)

    fig.suptitle('Comparação da Amplitude Verdadeira X Numérica \n' '{} eventos e Empilhamento de {}%'
                 .format(num_events, prob))
    ax0.hist(true_amplitude, bins="auto")
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('PU: Verdadeira \n' r'$\mu={}$, $\sigma={}$'
                  .format(true_amplitude.mean(), true_amplitude.std()))
    ax0.set_xlabel('Valor')
    ax0.set_ylabel('Frequência')

    ax1.hist(of_amplitude, bins="auto")
    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('OF: Numerica \n' r'$\mu={}$, $\sigma={}$'
                  .format(of_amplitude.mean(), of_amplitude.std()))
    ax1.set_xlabel('Valor')
    ax1.set_ylabel('Frequência')

    ax2.hist(dmf_amplitude, bins="auto")
    ax2.legend(prop={'size': 10})
    ax2.grid(axis='y', alpha=0.75)
    ax2.set_title('DMF: Numerica \n' r'$\mu={}$, $\sigma={}$'
                  .format(dmf_amplitude.mean(), dmf_amplitude.std()))
    ax2.set_xlabel('Valor')
    ax2.set_ylabel('Frequência')

    ax3.hist(smf_amplitude, bins="auto")
    ax3.legend(prop={'size': 10})
    ax3.grid(axis='y', alpha=0.75)
    ax3.set_title('SMF: Numerica \n' r'$\mu={}$, $\sigma={}$'
                  .format(smf_amplitude.mean(), smf_amplitude.std()))
    ax3.set_xlabel('Valor')
    ax3.set_ylabel('Frequência')

    plt.show()
