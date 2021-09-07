"""Plots covariance matrix in grayscale"""

import os.path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from config import Legend, Tick

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    np.set_printoptions(suppress=True, precision=3)
    prob = 0.0
    dataset = 'simulated_snr3'
    num_events = 200000

    # Pile data
    BASE_PATH = DIR_PATH + f'/../../results/{dataset}/pileup_data/prob_{prob}/{num_events}_events'
    noise_file_name = BASE_PATH + '/base_data/noise.txt'

    noises = np.loadtxt(noise_file_name)

    cov = np.cov(np.transpose(noises))
    plt.matshow(cov, cmap='gray_r')
    plt.gca().xaxis.tick_bottom()

    print('Noises')
    print(np.mean(noises))
    print(np.std(noises))
    print(cov)

    cbar = plt.colorbar()
    tick_font_size = 14
    cbar.ax.tick_params(labelsize=tick_font_size)
    plt.xlabel('Amostra Temporal', **Legend.font)
    plt.ylabel('Amostra Temporal', **Legend.font)
    plt.xticks(**Tick.font)
    plt.yticks(**Tick.font)
    plt.show()
