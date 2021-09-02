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


def of_calculation(number_of_events, probs, dataset):
    base_folder = f'results/{dataset}/pileup_data'
    number_of_data = number_of_events * 2  # Due to the 50% training of E-MF.

    # For printing and files, probability must be in %.
    probs = np.array(probs) * 100

    for prob in probs:
        print(f'Simulated OF - Processing {number_of_events} events for signal for probability {prob}\n')

        # Pileup data
        base_data = f'{base_folder}/prob_{prob}/{number_of_data}_events'
        amplitude_file_name = f'{base_data}/base_data/tile_A.txt'
        signal_file_name = f'{base_data}/base_data/tile_signal.txt'

        amplitude = pd.read_csv(amplitude_file_name, sep=" ", header=None)[:number_of_events]
        signal = pd.read_csv(signal_file_name, sep=" ", header=None)[:number_of_events][:]

        weights = pd.DataFrame([-0.37873481, -0.35634348, 0.17828771, 0.81313877, 0.27867064, -0.20540129, -0.32961754])

        of_amplitude = signal.dot(weights)
        amp_error = of_amplitude - amplitude

        folder_name = f'{base_data}/OF'
        file_helper.save_file_in('of_amp_signal', folder_name, of_amplitude)
        file_helper.save_file_in('of_amp_error', folder_name, amp_error)


if __name__ == '__main__':
    dataset = 'simulated_snr01'
    number_of_events = 100
    probs = [0.0, 0.1, 0.5, 1.0]

    of_calculation(number_of_events, probs, dataset)
