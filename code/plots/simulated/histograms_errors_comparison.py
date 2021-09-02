"""Compares all amplitude errors"""

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
    prob = 50.0
    num_events = 200000
    dataset = 'simulated_snr01'

    # Pile data
    BASE_PATH = DIR_PATH + f'/../../results/{dataset}/pileup_data/prob_{prob}/{num_events}_events'
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
    ax1.set_xlabel('Valor', **Legend.font)
    ax1.set_ylabel('Frequência', **Legend.font)

    ax2.hist(dmf_amp_error, bins="auto")
    ax2.legend(prop={'size': 10})
    ax2.grid(axis='y', alpha=0.75)
    ax2.set_title('DMF: Numerica \n' r'$\mu={}$, $\sigma={}$'
                  .format(dmf_amp_error.mean(), dmf_amp_error.std()))
    ax2.set_xlabel('Valor', **Legend.font)
    ax2.set_ylabel('Frequência', **Legend.font)

    ax3.hist(smf_amp_error, bins="auto")
    ax3.legend(prop={'size': 10})
    ax3.grid(axis='y', alpha=0.75)
    ax3.set_title('SMF: Numerica \n' r'$\mu={}$, $\sigma={}$'
                  .format(smf_amp_error.mean(), smf_amp_error.std()))
    ax3.set_xlabel('Valor', **Legend.font)
    ax3.set_ylabel('Frequência', **Legend.font)

    plt.show()
