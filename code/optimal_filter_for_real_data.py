import numpy as np
import pandas as pd
import time

from utils import file_helper

np.set_printoptions(suppress=True)

DIMENSION = 7


# Function adpted from from @ingoncalves
# This function is responsible to generate the used OF weights. There is no
# need to execute it always.
def of_weights():
    vec_g = np.array(
        [0.0000, 0.0172, 0.4524, 1.0000, 0.5633, 0.1493, 0.0424])
    vec_dg = np.array(
        [0.00004019, 0.00333578, 0.03108120, 0.00000000, -0.02434490, -0.00800683, -0.00243344])

    # unitary covariance matrix
    mat_c = np.identity(DIMENSION)

    # defines solution vector
    vec_b = np.zeros(DIMENSION + 3)
    vec_b[DIMENSION] = 1.0

    # defines matrix A, where Aw=b
    mat_a = np.zeros((DIMENSION + 3, DIMENSION + 3))

    for i in range(DIMENSION):
        # copies C to A
        for j in range(DIMENSION):
            mat_a[i][j] = mat_c[i][j]

        # copies g to A
        mat_a[DIMENSION][i] = vec_g[i]
        mat_a[i][DIMENSION] = -vec_g[i]

        # copies dg to A
        mat_a[DIMENSION + 1][i] = vec_dg[i]
        mat_a[i][DIMENSION + 1] = -vec_dg[i]

        # sets the unitary column
        mat_a[DIMENSION + 2][i] = 1.0
        mat_a[i][DIMENSION + 2] = -1.0

    vec_w = np.linalg.solve(mat_a, vec_b)

    weights = np.zeros(DIMENSION)
    for i in range(DIMENSION):
        weights[i] = vec_w[i]

    return weights


def of_calculation(amplitude_mean, oise_mean, number_of_data, sufix=''):
    print(f'OF - Processing signal for amp{amplitude_mean} and mu {noise_mean}{sufix}\n')

    base_folder = f'results/hybrid/amplitude_mean{amplitude_mean}'
    data_folder = f'{base_folder}/base_data/mu{noise_mean}'
    amplitude_file_name = f'{data_folder}/tile_A{sufix}.txt'
    signal_file_name = f'{data_folder}/tile_signal{sufix}.txt'

    amplitude = pd.read_csv(amplitude_file_name, sep=" ", header=None)[:number_of_data]
    signal = pd.read_csv(signal_file_name, sep=" ", header=None)[:number_of_data][:]

    print(f'Length of amplitudes {len(amplitude)}')
    print(f'Length of signals {len(signal)}\n')

    weights = pd.DataFrame([-0.37873481, -0.35634348, 0.17828771, 0.81313877, 0.27867064, -0.20540129, -0.32961754])

    of_amplitude = signal.dot(weights)
    amp_error = amplitude - of_amplitude

    folder_name = f'{base_folder}/OF/mu{noise_mean}'
    file_helper.save_file_in(f'of_amp_signal{sufix}', folder_name, of_amplitude)
    file_helper.save_file_in(f'of_amp_error{sufix}', folder_name, amp_error)


if __name__ == '__main__':
    tile_partition = 'EBA'
    amplitude_mean = 30
    noise_mean = 30
    channel = 10
    sufix = f'_ch{channel}'
    t0 = time.time()

    noise_file_name = f'data/{tile_partition}/{tile_partition}mu{noise_mean}_no_ped{sufix}.txt'

    # Getting data from boundaries
    all_noises = pd.read_csv(noise_file_name, sep=" ", usecols=(3, 4, 5, 6, 7, 8, 9), header=None)
    number_of_data = int(len(all_noises) / 2)  # Only half part is needed due to the E-MF 50% training

    of_calculation(amplitude_mean, noise_mean, number_of_data, sufix=sufix)
    print('OF Script finished!')
    print(time.time() - t0, "seconds wall time")
