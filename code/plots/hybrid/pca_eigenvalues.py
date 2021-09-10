"""Plost the PCA eigen values from the SMF"""

import os.path
import numpy as np
import matplotlib.pyplot as plt

import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from config import Legend, Tick

np.set_printoptions(suppress=True)
DIR_PATH = os.path.dirname(__file__)


if __name__ == '__main__':
    number_of_components = 7
    x = np.arange(1, number_of_components + 1)
    mu_30_pca_eigen_values = [0.48618934, 0.3848968, 0.09967202, 0.01884712, 0.00912632, 0.00078607, 0.00048231]
    mu_50_pca_eigen_values = [0.49203833, 0.37803991, 0.10215386, 0.01775441, 0.00879264, 0.00073698, 0.00048386]
    mu_90_pca_eigen_values = [0.50298509, 0.37427696, 0.09274505, 0.01987774, 0.0094876,  0.00036911, 0.00025845]

    pca_eigen_values = mu_30_pca_eigen_values

    for i in range(1, len(pca_eigen_values)):
        pca_eigen_values[i] = pca_eigen_values[i] + pca_eigen_values[i-1]

    plt.plot(x, pca_eigen_values, '-ko')
    plt.xticks(**Tick.font)
    plt.yticks(**Tick.font)
    plt.xlabel('Componentes', **Legend.font)
    plt.ylabel('Energia (%)', **Legend.font)

    plt.show()
