"""Gets a sample of jitter pulse and plot it."""

import os.path
import numpy as np
import matplotlib.pyplot as plt
from config import Legend, Tick

np.set_printoptions(suppress=True)
DIR_PATH = os.path.dirname(__file__)


if __name__ == '__main__':
    prob = 0.0
    num_events = 200000
    reading_interval = np.arange(-25, 150, 25)

    BASE_PATH = DIR_PATH + f'/../results/simulated/pileup_data/prob_{prob}/{num_events}_events'
    jitter_filename = BASE_PATH + '/base_data/jitter.txt'

    jitters = np.loadtxt(jitter_filename)[0]

    single_jitter_pulse = jitters[1:]

    plt.plot(reading_interval, single_jitter_pulse, '-ko')
    plt.xticks(reading_interval, **Tick.font)
    plt.yticks(np.arange(0, 1.2, 0.2), **Tick.font)
    plt.xlabel('Tempo (ns)', **Legend.font)
    plt.ylabel('Amplitude', **Legend.font)

    plt.show()
