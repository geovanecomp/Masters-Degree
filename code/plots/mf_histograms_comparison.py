"""Process Linear plot comparing two datasets."""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    num_events = 100

    amplitude = np.loadtxt(DIR_PATH + '/../results/base_data/{}-events/amplitude.txt'.format(num_events))
    amp_signal = np.loadtxt(DIR_PATH + '/../results/matched_filter/{}-events/amp_signal.txt'.format(num_events))

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)

    fig.suptitle('Comparação da Amplitude: Verdadeira X Numerica \n' '{} eventos'
                 .format(num_events))
    ax0.hist(amplitude, bins="auto")
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('Verdadeira \n' r'$\mu={}$, $\sigma={}$'
                  .format(amplitude.mean(), amplitude.std()))
    ax0.set_xlabel('Valor')
    ax0.set_ylabel('Frequência')

    ax1.hist(amp_signal, bins="auto")
    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('Numerica \n' r'$\mu={}$, $\sigma={}$'
                  .format(amp_signal.mean(), amp_signal.std()))
    ax1.set_xlabel('Valor')
    ax1.set_ylabel('Frequência')

    plt.show()
