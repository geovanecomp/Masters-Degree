"""Compares simulated data to all Amplitudes between OF, SMF and DMF in one figure"""

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
    dataset = 'simulated_snr1'
    prob = 100.0
    num_events = 200000

    # Pile data
    BASE_PATH = DIR_PATH + f'/../../results/{dataset}/pileup_data/prob_{prob}/{num_events}_events'
    pca1_smf_amplitude_file_name = BASE_PATH + '/S_MF_PCA1/smf_amp_error.txt'
    pca3_smf_amplitude_file_name = BASE_PATH + '/S_MF_PCA3/smf_amp_error.txt'
    pca5_smf_amplitude_file_name = BASE_PATH + '/S_MF_PCA5/smf_amp_error.txt'
    pca7_smf_amplitude_file_name = BASE_PATH + '/S_MF/smf_amp_error.txt'

    pca1_smf_amp_error = np.loadtxt(pca1_smf_amplitude_file_name)
    pca3_smf_amp_error = np.loadtxt(pca3_smf_amplitude_file_name)
    pca5_smf_amp_error = np.loadtxt(pca5_smf_amplitude_file_name)
    pca7_smf_amp_error = np.loadtxt(pca7_smf_amplitude_file_name)

    print(
          f'SMF-PCA1 Mean: {pca1_smf_amp_error.mean()} | SMF-PCA STD: {pca1_smf_amp_error.std()} \n' \
          f'SMF-PCA3 Mean: {pca3_smf_amp_error.mean()} | SMF-PCA STD: {pca3_smf_amp_error.std()} \n' \
          f'SMF-PCA5 Mean: {pca5_smf_amp_error.mean()} | SMF-PCA STD: {pca5_smf_amp_error.std()} \n' \
          f'SMF-PCA7 Mean: {pca7_smf_amp_error.mean()} | SMF-PCA STD: {pca7_smf_amp_error.std()} \n'
          )

    bins = 100
    rangeR = 600
    rangeL = -rangeR
    plt.hist(pca1_smf_amp_error, bins=bins, range=(rangeL, rangeR), color='red', histtype=u'step', label='PCA-1')
    plt.hist(pca3_smf_amp_error, bins=bins, range=(rangeL, rangeR), color='green', histtype=u'step', label='PCA-3')
    plt.hist(pca5_smf_amp_error, bins=bins, range=(rangeL, rangeR), color='blue', histtype=u'step', label='PCA-5')
    plt.hist(pca7_smf_amp_error, bins=bins, range=(rangeL, rangeR), color='black', histtype=u'step', label='PCA-7')
    plt.legend(prop={'size': 10})
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Erro', **Legend.font)
    plt.ylabel('Eventos', **Legend.font)

    plt.show()
