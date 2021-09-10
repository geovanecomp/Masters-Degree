"""Plots covariance matrix in grayscale"""

import os.path
import pandas as pd
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
    partition = 'EBA'
    amplitude_mean = 300
    channel = 1
    noise_mean = 30

    base_folder = DIR_PATH + '/../../data'
    noise_file_name = base_folder + f'/{partition}/{partition}mu{noise_mean}_no_ped_ch{channel}.txt'

    noises = pd.read_csv(noise_file_name, sep=" ", usecols=(3, 4, 5, 6, 7, 8, 9), header=None)
    # noises = np.loadtxt(noise_file_name)

    # cov = np.cov(noises)
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
