"""Correlation plot between two datasets"""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)


def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # Lables
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # The scatter plot:
    ax.scatter(x, y)

    # Now determine nice limits by hand:
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(0, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins)
    ax_histy.hist(y, bins=bins, orientation='horizontal')


if __name__ == '__main__':
    num_events = 100000

    analitic_amplitude = np.loadtxt(DIR_PATH + '/../results/base_data/{}-events/amplitude.txt'.format(num_events))
    numeric_amplitude = np.loadtxt(DIR_PATH + '/../results/matched_filter/{}-events/amp_signal.txt'.format(num_events))

    fig, ax = plt.subplots()
    ax.set_title('Amplitudes')
    i = 0
    labels = ['Analítica', 'Numérica']
    for color in ['blue', 'red']:
        ax.scatter(analitic_amplitude, numeric_amplitude, c=color, label=labels[i],
                   alpha=0.3, edgecolors='none')
        i += 1

    ax.legend()
    ax.grid(True)

    plt.show()
