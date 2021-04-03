"""Generates data from a specific channel"""

# -*- coding: UTF-8 -*-
import numpy as np

from utils import tilecal_helper


if __name__ == '__main__':
    tile_partition = 'EBA'
    noise_mean = 30
    channel = 10
    sufix = '_real_no_ped'

    print(f'Processing for mean: {noise_mean}')
    print(f'Channel: {channel}')

    noise_file_name = f'data/{tile_partition}/{tile_partition}mu{noise_mean}{sufix}.txt'
    noises = np.loadtxt(noise_file_name)
    new_noises = tilecal_helper.generate_data_by_channel(noises, channel)
    file_path = f'data/{tile_partition}/{tile_partition}mu{noise_mean}{sufix}_ch{channel}.txt'

    # 3 int digits for localization and others for the data
    fmt = '%d', '%d', '%d', '%.6f', '%.6f', '%.6f', '%.6f', '%.6f', '%.6f', '%.6f', '%.4f'
    np.savetxt(file_path, new_noises, fmt=fmt, delimiter=' ')
