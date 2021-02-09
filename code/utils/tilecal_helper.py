"""Helper that provides quick and easy access to the Tilecal data"""

import numpy as np
import collections

TILE_DIMENSION = 10  # Considering 3 intial columns for partition, channel and module
DATA_DIMENSION = 7  # Ignoring columns for partition, channel and module
FULL_PEDESTAL_DIRECTORY_FILE = 'data/ped_tile.txt'
DEFAULT_PARTITION_NAME = 'LBA'


# Tilecal has 4 Partitions called: LBA, EBA, LBC, EBC
# Each one has its own number which is respectively 0, 1, 2, 3.
def _partition_mapper(tile_partition):
    if isinstance(tile_partition, float) or isinstance(tile_partition, int):
        if tile_partition == 0:
            return 'LBA'
        elif tile_partition == 1:
            return 'EBA'
        elif tile_partition == 2:
            return 'LBC'
        elif tile_partition == 3:
            return 'EBC'
    elif isinstance(tile_partition, str):
        if tile_partition == 'LBA':
            return 0
        elif tile_partition == 'EBA':
            return 1
        elif tile_partition == 'LBC':
            return 2
        elif tile_partition == 'EBC':
            return 3
    return 'Error, unsupported partition value'


def generate_ped_file_per_partition(tile_partition):
    new_ped_file = open(f'data/{tile_partition}/pedestal.txt', 'w')
    for line in open(FULL_PEDESTAL_DIRECTORY_FILE):
        if tile_partition in line:
            # To ignore the first three letters of the partition
            new_ped_file.writelines(line[3:])
    new_ped_file.close()


def read_tile_data(tile_partition, noise_mean):
    real_noise = np.loadtxt(
        'data/{}/{}mu{}.txt'
        .format(tile_partition, tile_partition, noise_mean)
        )

    return real_noise


# The noise file contains the 3 first columns to identify: Partition, Module
# and Channel. The remaining 7 columns are their respectives signals. The goal
# here is to identify which pedestal should we use and apply a pre-processing
# of removing the pedestal for each module and channel.
def generate_partition_data_without_ped(noises, high_gain=1):
    module_pos = 1
    channel_pos = 2
    invalid_value = -1  # Represents outliers in that channel

    ped_list = np.loadtxt(f'data/{DEFAULT_PARTITION_NAME}/pedestal.txt')
    invalid_rows = []

    for i in range(len(noises)):

        module = int(noises[i][module_pos])
        channel = int(noises[i][channel_pos])
        noise_row = noises[i][channel_pos+1:TILE_DIMENSION]

        row_with_outliers = collections.Counter(noise_row)[invalid_value] == DATA_DIMENSION

        if row_with_outliers:
            invalid_rows.append(i)
            continue

        pedestal = _get_ped_value_for_partition_cleanup(ped_list, DEFAULT_PARTITION_NAME, module, channel, high_gain)
        noises[i][channel_pos+1:TILE_DIMENSION] = noise_row - pedestal

    # Deleting everything at the end for performance.
    noises = np.delete(noises, invalid_rows, 0)
    return noises


def _get_ped_value_for_partition_cleanup(ped_list, tile_partition, module, channel, high_gain=1):
    module_pos = 0
    channel_pos = 1
    gain_pos = 2
    ped_pos = 3

    for i in range(len(ped_list)):
        if ped_list[i][module_pos] == module:
            for j in range(len(ped_list[channel_pos])):
                if ped_list[i][channel_pos] == channel and ped_list[i][gain_pos] == high_gain:
                    pedestal = float(ped_list[i][ped_pos])
                    return pedestal

    print('Pedestal Not Found')
    return None


# Each partition has 64 modules and each module has 48 channels.
# Finally each cell has two values, one for high_gain and other for low_gain
# High Gain is commonly used to get more expresive values, however for
# scenarios where we have saturated values, we can use Low Gain.
def get_ped_value(tile_partition, module, channel, high_gain=1):
    ped_list = np.loadtxt(f'data/{tile_partition}/pedestal.txt')
    module_pos = 0
    channel_pos = 1
    gain_pos = 2
    ped_pos = 3

    for i in range(len(ped_list)):
        if ped_list[i][module_pos] == module:
            for j in range(len(ped_list[channel_pos])):
                if ped_list[i][channel_pos] == channel and ped_list[i][gain_pos] == high_gain:
                    return float(ped_list[i][ped_pos])

    print('Pedestal Not Found')
    return None


# Real noise module starts from 0 to 63, but Pedestal files starts at 1 to 64.
# It is easy to fix this value difference than always need to fix it during
# execution time.
def fix_ped_value(tile_partition):
    ped_list = np.loadtxt(f'data/{tile_partition}/pedestal.txt')
    module_pos = 0
    for i in range(len(ped_list)):
        ped_list[i][module_pos] -= 1

    file_directory = f'data/{tile_partition}/pedestal.txt'
    np.savetxt(file_directory, ped_list, fmt='%i %i %i %6f')
