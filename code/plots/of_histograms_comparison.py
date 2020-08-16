"""Process Linear plot comparing two datasets."""

import os.path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    num_events = 1000

    amp_error = pd.read_csv(DIR_PATH + '/../results/optimal_filter/{}-events/amp_error.txt'.format(num_events), sep=" ", header=None).T
    of_amplitude = pd.read_csv(DIR_PATH + '/../results/optimal_filter/{}-events/of_amplitude.txt'.format(num_events), sep=" ", header=None).T

    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)

    fig.suptitle('Comparação do OF Data X Error \n' '{} eventos'
                 .format(num_events))
    ax0.hist(of_amplitude, bins="auto")
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('OF Data \n' r'$\mu={}$, $\sigma={}$'
                  .format(of_amplitude.mean(axis=1)[0], of_amplitude.std(axis=1)[0]))
    ax0.set_xlabel('Valor')
    ax0.set_ylabel('Frequência')

    ax1.hist(amp_error, bins="auto")
    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('OF Error \n' r'$\mu={}$, $\sigma={}$'
                  .format(amp_error.mean(axis=1)[0], amp_error.std(axis=1)[0]))
    ax1.set_xlabel('Valor')
    ax1.set_ylabel('Frequência')

    plt.show()
