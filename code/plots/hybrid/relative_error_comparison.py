import os.path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datashader as ds
import datashader.transfer_functions as tf

from datashader.mpl_ext import dsshow
from functools import partial

import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from config import Legend, Tick

DIR_PATH = os.path.dirname(__file__)


def _relative_error(exact_value, approx_value):
    # In a few cases where the len is even and due to the 50% of training,
    # we may have one last and extra value that can be ignored.
    if len(exact_value) > len(approx_value):
        exact_value = np.delete(exact_value, -1)
    elif len(approx_value) > len(exact_value):
        approx_value = np.delete(approx_value, -1)

    return (approx_value - exact_value) / exact_value


def correlation_plot(x, y, ax, method):
    ax.legend()
    ax.grid(True)

    ax.set_ylabel(f'{method}', **Legend.font)
    if method == 'S-MF':
        ax.set_xlabel('Amplitude de Referência', **Legend.font)

    df = pd.DataFrame(dict(x=x, y=y))

    da1 = dsshow(df, ds.Point('x', 'y'), norm='log', aspect='auto', ax=ax, x_range=(-0.1, 100), y_range=(-50, 50), shade_hook=partial(tf.dynspread, threshold=0.8))

    fig.colorbar(da1, ax=ax).set_label('Densidade')
    return ax


if "__main__" == __name__:

    # Real data
    amplitude_mean = 10
    noise_mean = 90
    channel = 1

    sufix = f'_ch{channel}'
    base_folder = DIR_PATH + f'/../../results/hybrid/amplitude_mean{amplitude_mean}'

    of_amp_file_name = f'{base_folder}/OF/mu{noise_mean}/of_amp_signal{sufix}.txt'
    dmf_amp_file_name = f'{base_folder}/D_MF/mu{noise_mean}/dmf_amp_signal{sufix}.txt'
    smf_amp_file_name = f'{base_folder}/S_MF/mu{noise_mean}/smf_amp_signal{sufix}.txt'
    reference_data_file_name = f'{base_folder}/base_data/mu{noise_mean}/tile_A{sufix}.txt'

    of_data = np.loadtxt(of_amp_file_name)
    dmf_data = np.loadtxt(dmf_amp_file_name)
    smf_data = np.loadtxt(smf_amp_file_name)
    reference_data = np.loadtxt(reference_data_file_name)[:len(of_data)]

    of_relative_error = _relative_error(reference_data, of_data)
    dmf_relative_error = _relative_error(reference_data, dmf_data)
    smf_relative_error = _relative_error(reference_data, smf_data)

    fig, (ax0, ax1, ax2) = plt.subplots(3)

    fig.suptitle(f'Correlação entre Amplitudes \n Ruido: {noise_mean} Canal: {channel} Amplitude: {amplitude_mean}')
    ax0 = correlation_plot(reference_data, of_relative_error, ax0, method='OF')
    ax1 = correlation_plot(reference_data, dmf_relative_error, ax1, method='D-MF')
    ax2 = correlation_plot(reference_data, smf_relative_error, ax2, method='S-MF')

    ax0.tick_params(axis='both', which='major', labelsize=16)
    ax1.tick_params(axis='both', which='major', labelsize=16)
    ax2.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
