"""Plots covariance matrix in grayscale"""

import os.path
import numpy as np
import matplotlib.pyplot as plt
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    np.set_printoptions(suppress=True, precision=3)
    prob = 100.0
    dataset = 'simulated'
    num_events = 20000

    # Pile data
    BASE_PATH = DIR_PATH + f'/../../results/{dataset}/pileup_data/prob_{prob}/{num_events}_events'
    noise_file_name = BASE_PATH + '/base_data/noise.txt'

    noises = np.loadtxt(noise_file_name)

    print('Noises')
    print(np.mean(noises))
    print(np.std(noises))

    cov = np.cov(np.transpose(noises))
    plt.matshow(cov)
    print(cov)
    plt.gray()
    plt.colorbar()
    plt.show()
