"""Helper to provide common structure for file generations"""

import numpy as np


def save_file(file_name, file_folder, data):
    fileText = 'results/{}/{}_events/{}.txt' \
               .format(file_folder, len(data), file_name)

    np.savetxt(
        fileText,
        data,
        fmt='%.13f',
        delimiter=' ')


def save_file_in(file_name, file_folder, data):
    fileText = 'results/{}/{}.txt' \
               .format(file_folder, file_name)

    np.savetxt(
        fileText,
        data,
        fmt='%.13f',
        delimiter=' ')
