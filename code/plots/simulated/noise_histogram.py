"""Plots all noise histograms at once"""

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
    prob = 0.0
    dataset = 'simulated_snr01'
    num_events = 200000

    # Pile data
    BASE_PATH = DIR_PATH + f'/../../results/{dataset}/pileup_data/prob_{prob}/{num_events}_events'
    noise_file_name = BASE_PATH + '/base_data/noise.txt'

    noises = np.loadtxt(noise_file_name)[:, 0]

    fig, ((ax1)) = plt.subplots(nrows=1, ncols=1)


    fig.suptitle('Comparação do Sinal gerado X Ruído \n' '{} eventos e Empilhamento de {}%'
                 .format(num_events, prob))

    plt.hist(noises, bins=100, color='k', histtype=u'step')
    plt.legend(prop={'size': 10})
    plt.grid(axis='y', alpha=0.75)
    plt.set_title('Eventos: ' r'$\mu={}$, $\sigma={}$'.format(noises.mean(), noises.std()))
    plt.xlabel('Energia (MeV)', **Legend.font)
    plt.ylabel('Eventos', **Legend.font)
    plt.xticks(**Tick.font)
    plt.yticks(**Tick.font)

    plt.show()
