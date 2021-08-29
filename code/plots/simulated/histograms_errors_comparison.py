"""Compares all amplitude errors"""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    prob = 0.0
    num_events = 200

    # Pile data
    BASE_PATH = DIR_PATH + f'/../../results/simulated/pileup_data/prob_{prob}/{num_events}_events'
    of_amplitude_file_name = BASE_PATH + '/OF/of_amp_error.txt'
    dmf_amplitude_file_name = BASE_PATH + '/D_MF/dmf_amp_error.txt'
    smf_amplitude_file_name = BASE_PATH + '/S_MF/smf_amp_error.txt'

    of_amp_error = np.loadtxt(of_amplitude_file_name)
    dmf_amp_error = np.loadtxt(dmf_amplitude_file_name)
    smf_amp_error = np.loadtxt(smf_amplitude_file_name)

    fig, ((ax1, ax2, ax3)) = plt.subplots(nrows=1, ncols=3)

    fig.suptitle(f'Comparação dos erros\n {num_events} eventos e Empilhamento de {prob}%')
    ax1.hist(of_amp_error, bins="auto")
    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('OF: Numerica \n' r'$\mu={}$, $\sigma={}$'
                  .format(of_amp_error.mean(), of_amp_error.std()))
    ax1.set_xlabel('Valor')
    ax1.set_ylabel('Frequência')

    ax2.hist(dmf_amp_error, bins="auto")
    ax2.legend(prop={'size': 10})
    ax2.grid(axis='y', alpha=0.75)
    ax2.set_title('DMF: Numerica \n' r'$\mu={}$, $\sigma={}$'
                  .format(dmf_amp_error.mean(), dmf_amp_error.std()))
    ax2.set_xlabel('Valor')
    ax2.set_ylabel('Frequência')

    ax3.hist(smf_amp_error, bins="auto")
    ax3.legend(prop={'size': 10})
    ax3.grid(axis='y', alpha=0.75)
    ax3.set_title('SMF: Numerica \n' r'$\mu={}$, $\sigma={}$'
                  .format(smf_amp_error.mean(), smf_amp_error.std()))
    ax3.set_xlabel('Valor')
    ax3.set_ylabel('Frequência')

    plt.show()
