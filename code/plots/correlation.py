import os.path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datashader as ds
import datashader.transfer_functions as tf

from datashader.mpl_ext import dsshow
from functools import partial

DIR_PATH = os.path.dirname(__file__)


def correlation_plot(x, y, ax, method):
    ax.legend()
    ax.grid(True)

    ax.set_ylabel(f'Amplitude Aproximada {method}')
    ax.set_xlabel('Amplitude de Referencia')
    df = pd.DataFrame(dict(x=x, y=y))

    da1 = dsshow(df, ds.Point('x', 'y'), norm='log', aspect='auto', ax=ax, x_range=(-100, 400), y_range=(-100, 400), shade_hook=partial(tf.dynspread, threshold=0.8))

    fig.colorbar(da1, ax=ax).set_label('Densidade')
    return ax


if "__main__" == __name__:

    # Real data
    noise_mean = 30
    channel = 36
    amplitude_mean = 30

    sufix = f'_ch{channel}'
    base_folder = DIR_PATH + f'/../results/hybrid/amplitude_mean{amplitude_mean}'

    of_amp_file_name = f'{base_folder}/OF/mu{noise_mean}/of_amp_signal{sufix}.txt'
    dmf_amp_file_name = f'{base_folder}/D_MF/mu{noise_mean}/dmf_amp_signal{sufix}.txt'
    emf_amp_file_name = f'{base_folder}/E_MF/mu{noise_mean}/mf_amp_signal{sufix}.txt'
    reference_data_file_name = f'{base_folder}/base_data/mu{noise_mean}/tile_A{sufix}.txt'

    of_data = np.loadtxt(of_amp_file_name)
    dmf_data = np.loadtxt(dmf_amp_file_name)
    emf_data = np.loadtxt(emf_amp_file_name)
    reference_data = np.loadtxt(reference_data_file_name)[:len(of_data)]
    fig, (ax0, ax1, ax2) = plt.subplots(3)
    fig.suptitle(f'Correlação entre Amplitudes \n Ruido: {noise_mean} Canal: {channel} Amplitude: {amplitude_mean}')
    ax0 = correlation_plot(reference_data, of_data, ax0, method='OF')
    ax1 = correlation_plot(reference_data, dmf_data, ax1, method='D-MF')
    ax2 = correlation_plot(reference_data, emf_data, ax2, method='E-MF')
    plt.show()
