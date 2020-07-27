"""Histogram comparing numeric and analitic Amplitudes."""

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    mathlab_data = np.loadtxt('results/mathlab/1000ruidoTileOcup100.txt')
    script_data = np.loadtxt('results/noises/1000-events/TileNoiseProbability100.txt')

    fig, ((ax0), (ax1)) = plt.subplots(nrows=2, ncols=1)

    # colors = ['red', 'tan', 'lime']
    fig.suptitle('1000 events', fontsize=14)

    ax0.plot(mathlab_data[:, 0])
    ax1.plot(script_data[:, 0])
    # plt.ylabel('some numbers')
    plt.show()
