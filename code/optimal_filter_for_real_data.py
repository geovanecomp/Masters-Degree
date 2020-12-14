import numpy as np
import pandas as pd

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


def of_calculation(noise_mean):
    print('OF - Processing signal\n')

    amplitude_file_name = 'results/real_data/mu{}/tile_A.txt'.format(noise_mean)
    signal_file_name = 'results/real_data/mu{}/tile_signal.txt'.format(noise_mean)

    amplitude = pd.read_csv(amplitude_file_name, sep=" ", header=None)
    signal = pd.read_csv(signal_file_name, sep=" ", header=None)

    weights = pd.DataFrame([-0.37873481, -0.35634348, 0.17828771, 0.81313877, 0.27867064, -0.20540129, -0.32961754])

    of_amplitude = signal.dot(weights)
    amp_error = amplitude - of_amplitude

    folder_name = 'real_data/mu{}/optimal_filter'.format(noise_mean)
    file_helper.save_file_in('of_amp_signal', folder_name, of_amplitude)
    file_helper.save_file_in('of_amp_error', folder_name, amp_error)


if __name__ == '__main__':
    noise_mean = 50

    of_calculation(noise_mean)
