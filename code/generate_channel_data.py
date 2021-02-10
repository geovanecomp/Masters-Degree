"""Generates data from a specific channel"""

# -*- coding: UTF-8 -*-
import numpy as np

from utils import tilecal_helper


if __name__ == '__main__':
    noise_mean = 30
    print(f'Processing for mean: {noise_mean}')
    tile_partition = 'LBA'
    channel = 36
    noise_file_name = f'data/{tile_partition}/{tile_partition}mu{noise_mean}_no_ped.txt'
    noises = np.loadtxt(noise_file_name)
    new_noises = tilecal_helper.generate_data_by_channel(noises, channel)
    file_path = f'data/LBA/LBAmu{noise_mean}_no_ped_ch{channel}.txt'

    # 3 int digits for localization and others for the data
    fmt = '%d', '%d', '%d', '%.6f', '%.6f', '%.6f', '%.6f', '%.6f', '%.6f', '%.6f'
    np.savetxt(file_path, new_noises, fmt=fmt, delimiter=' ')
