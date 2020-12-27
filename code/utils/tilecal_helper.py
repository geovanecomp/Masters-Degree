"""Helper that provides quick and easy access to the Tilecal data"""

import numpy as np

# Considering 3 intial columns for partition, channel and module
TILE_DIMENSION = 10
FULL_PEDESTAL_DIRECTORY_FILE = 'data/ped_tile.txt'


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
