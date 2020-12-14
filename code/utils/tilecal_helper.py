"""Helper that provides quick and easy access to the Tilecal data"""

import numpy as np

FULL_PEDESTAL_DIRECTORY_FILE = 'data/ped_tile.txt'


# Tilecal has 4 Partitions called: LBA, EBA, LBC, EBC
# Each one has its own number which is respectively 0, 1, 2, 3.
def _partition_mapper(tilecal_partition):
    if tilecal_partition == 'LBA':
        return 0
    elif tilecal_partition == 'EBA':
        return 1
    elif tilecal_partition == 'LBC':
        return 2
    elif tilecal_partition == 'EBC':
        return 3
    return 'Error, unsupported partition value'


def generate_ped_file_per_partition(tilecal_partition):
    new_ped_file = open(f'data/{tilecal_partition}/pedestal.txt', 'w')
    for line in open(FULL_PEDESTAL_DIRECTORY_FILE):
        if tilecal_partition in line:
            # To ignore the first three letters of the partition
            new_ped_file.writelines(line[3:])
    new_ped_file.close()


def read_tile_data(tilecal_partition, noise_mean):
    real_noise = np.loadtxt(
        'data/{}/{}mu{}.txt'
        .format(tilecal_partition, tilecal_partition, noise_mean)
        )

    return real_noise


# Each partition has 64 modules and each module has 48 channels.
# Finally each cell has two values, one for high_gain and other for low_gain
# High Gain is commonly used to get more expresive values, however for
# scenarios where we have saturated values, we can use Low Gain.
def get_ped_value(tilecal_partition, module, channel, high_gain='1'):
    partition_number = _partition_mapper(tilecal_partition)
    ped_list = np.loadtxt(f'data/{tilecal_partition}/pedestal.txt', dtype='str')
    desired_peds = []
    module_pos = 0
    channel_pos = 1
    gain_pos = 2
    ped_pos = 3

    for i in range(len(ped_list)):
        if ped_list[i][module_pos] == module:
            for j in range(len(ped_list[channel_pos])):
                if ped_list[i][j] == channel and ped_list[i][gain_pos] == high_gain:
                    return float(ped_list[i][ped_pos])

    print('Pedestal Not Found')
    return 0
