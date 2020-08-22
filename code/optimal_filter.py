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


if __name__ == '__main__':
    num_events = 10000

    amplitude = pd.read_csv('results/base_data/{}-events/amplitude.txt'.format(num_events), sep=" ", header=None)
    signal_testing = pd.read_csv('results/base_data/{}-events/signal_testing.txt'.format(num_events), sep=" ", header=None)

    weights = pd.DataFrame([-0.37873481, -0.35634348, 0.17828771, 0.81313877, 0.27867064, -0.20540129, -0.32961754])

    if num_events != len(amplitude):
        print('Dimension error!')

    of_amplitude = signal_testing.dot(weights)
    amp_error = amplitude - of_amplitude

    file_helper.save_file('of_amplitude', 'optimal_filter', of_amplitude)
    file_helper.save_file('amp_error', 'optimal_filter', amp_error)
