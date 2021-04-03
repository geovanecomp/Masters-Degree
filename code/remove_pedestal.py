"""Generates Partition data without Pedestal"""

# -*- coding: UTF-8 -*-
import numpy as np

from utils import tilecal_helper


if __name__ == '__main__':
    tile_partition = 'EBA'
    noise_mean = 30
    sufix = '_real'

    print(f'Processing for mean: {tile_partition}_{noise_mean}{sufix}')

    noise_file_name = f'data/{tile_partition}/{tile_partition}mu{noise_mean}{sufix}.txt'
    noises = np.loadtxt(noise_file_name)
    new_noises = tilecal_helper.generate_partition_data_without_ped(noises)
    file_path = f'data/{tile_partition}/{tile_partition}mu{noise_mean}{sufix}_no_ped.txt'

    # 3 int digits for localization and others for the data
    fmt = '%d', '%d', '%d', '%.6f', '%.6f', '%.6f', '%.6f', '%.6f', '%.6f', '%.6f', '%.4f'
    np.savetxt(file_path, new_noises, fmt=fmt, delimiter=' ')
