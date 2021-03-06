import numpy as np
import pandas as pd

from scipy import linalg as LA
from sklearn.decomposition import PCA

from utils import pulse_helper, file_helper

np.set_printoptions(suppress=True)


def mf_calculation(number_of_data, pedestal, probs, training_percentage=50):
    TEN_BITS_ADC_VALUE = 1023
    # base_folder = 'results/simulated/pileup_data'  # Normal data
    base_folder = 'results/simulated/base_data'  # Pileup data
    dimension = 7
    qtd_for_training = int(number_of_data / ((100 / training_percentage)))
    qtd_for_testing = number_of_data - qtd_for_training

    # For printing and files, probability must be in %.
    probs = np.array(probs) * 100
    for prob in probs:
        prob = prob
        print(f'MF - Processing signal probability:  {prob}%\n')
        # Normal data
        # amplitude_file_name = f'{base_folder}/{qtd_for_training}_events/amplitude.txt'
        # signal_testing_file_name = f'{base_folder}/{qtd_for_training}_events/signal_testing.txt'

        # Pileup data
        amplitude_file_name = f'{base_folder}/prob_{prob}/{qtd_for_training}_events/tile_A_signal_prob_{prob}.txt'
        signal_testing_file_name = f'{base_folder}/prob_{prob}/{qtd_for_training}_events/tile_signal_prob_{prob}.txt'
        result_prefix = f'pileup_prob_{prob}_'

        amplitude = pd.read_csv(amplitude_file_name, sep=" ", header=None)
        signal_testing = pd.read_csv(signal_testing_file_name, sep=" ", header=None)

        noise = pd.DataFrame(pedestal + np.random.randn(number_of_data, dimension))
        # Getting data from boundaries
        noise_training = noise[:qtd_for_training][:]
        noise_testing = noise[qtd_for_testing:][:]

        # Branqueamento
        noise_train_cov = noise_training.cov()

        [D, V] = LA.eigh(noise_train_cov)

        # Apply before diag to avoid inf value due to the 0 negative exponentiation
        D = D**(-.5)

        # eig returns D as an array, we need to transform it into a diagonal matrix
        D = pd.DataFrame(np.diag(D))
        V = pd.DataFrame(V)

        W = pd.DataFrame(D.dot(V.transpose()))

        W_t = W.transpose()

        # PCA Part
        pure_signal = np.zeros((qtd_for_testing, dimension))
        for i in range(0, qtd_for_testing):
            pure_signal[i, :] = TEN_BITS_ADC_VALUE * np.random.randn(1) * pulse_helper.get_jitter_pulse()

        pure_signal = pd.DataFrame(pure_signal)

        n_pca_components = dimension
        pca = PCA(n_components=n_pca_components)
        coeff = pd.DataFrame(pca.fit(pure_signal.dot(W_t)).components_)
        coeff_t = coeff.transpose()
        Y = pca.explained_variance_.T

        # stochastic filter params
        # ddof=1 to use Sampled data variance -> N-1
        variance = noise_training[:][3].var()
        reference_pulse = pd.DataFrame([0.0000, 0.0172, 0.4524, 1.0000, 0.5633, 0.1493, 0.0424])
        bleached_reference_pulse = reference_pulse.T.dot(W_t)

        optimal_reference_pulse = bleached_reference_pulse.dot(coeff_t[:][:n_pca_components])

        optimal_noise = ((noise_testing - pedestal).dot(W_t)).dot(coeff_t[:][:n_pca_components])
        optimal_signal = ((signal_testing - pedestal).dot(W_t)).dot(coeff_t[:][:n_pca_components])

        No = variance * 2
        h1 = np.zeros((dimension, dimension))
        h2 = np.zeros((dimension, dimension))

        for i in range(0, n_pca_components):
            h1 = h1 + (Y[i] / (Y[i] + variance)) * (coeff_t[:][i].values.reshape(1, dimension) * coeff_t[:][i].values.reshape(dimension, 1))
            h2 = h2 + (1.0 / (Y[i] + variance)) * (coeff_t[:][i].values.reshape(1, dimension) * coeff_t[:][i].values.reshape(dimension, 1))

        IR_noise = np.zeros((len(noise_testing), 1))
        IR_signal = np.zeros((len(signal_testing), 1))

        for ev in range(0, len(noise_testing)):
            IR_noise[ev] = (1.0 / No) * ((
                        (optimal_noise.values[ev][:].dot((coeff[:][:n_pca_components])))
                        .dot(h1).dot(
                            (optimal_noise.values[ev][:].dot(coeff[:][:n_pca_components]))
                        ).transpose()
                    ).transpose())

        for ev in range(0, len(signal_testing)):
            IR_signal[ev] = (1.0 / No) * ((
                        (optimal_signal.values[ev][:].dot((coeff[:][:n_pca_components])))
                        .dot(h1).dot(
                            (optimal_signal.values[ev][:].dot(coeff[:][:n_pca_components]))
                        ).transpose()
                    ).transpose())

        ID_noise = np.zeros((len(noise_testing), 1))
        ID_signal = np.zeros((len(signal_testing), 1))
        for ev in range(0, len(noise_testing)):
            ID_noise[ev] = ((optimal_reference_pulse.dot(coeff[:][:n_pca_components]))
                            .dot(h2).dot(
                                (optimal_noise.values[ev][:].dot(coeff[:][:n_pca_components]))
                                .transpose()
                                )
                            )

        for ev in range(0, len(signal_testing)):
            ID_signal[ev] = ((optimal_reference_pulse.dot(coeff[:][:n_pca_components]))
                             .dot(h2).dot(
                                (optimal_signal.values[ev][:].dot(coeff[:][:n_pca_components]))
                                .transpose()
                                )
                             )
        # Matched Filter estimatives
        estimated_noise = ID_noise + IR_noise
        estimated_signal = ID_signal + IR_signal
        print('Almost...\n')

        # Amplitude estimative
        b1 = coeff[:][:n_pca_components].transpose().dot(coeff_t[:][:n_pca_components])
        # DAQUI PARA BAIXO B2 E B3 NAO BATEM DEVIDO A ALGUMAS LINHAS DE COEFF
        b2 = (1.0 / No) * (
            coeff_t[:][:n_pca_components].transpose().dot(h1)
            .dot(coeff[:][:n_pca_components])
        )
        b3 = (optimal_reference_pulse.dot(coeff[:][:n_pca_components])).dot(h2).dot(coeff[:][:n_pca_components])

        amp_noise = np.zeros((len(noise_testing), 1))
        amp_signal = np.zeros((len(signal_testing), 1))

        a = (1.0 / No) * (
                    (optimal_reference_pulse.dot(coeff[:][:n_pca_components])).dot(h1)
                    .dot((optimal_reference_pulse.dot(coeff[:][:n_pca_components])).transpose())
                )
        b = (optimal_reference_pulse.dot(coeff[:][:n_pca_components])).dot(h2).dot((optimal_reference_pulse.dot(coeff[:][:n_pca_components])).transpose())

        cs = 0
        cr = 0
        for i in range(0, len(signal_testing)):
            ra = b * b + 4 * a * estimated_signal[i]
            if ra.values < 0:
                ra = 0
                cs = cs + 1
            # signal amplitute using MF filter output
            amp_signal[i] = (-b + np.sqrt(ra)) / (2 * a)

        for i in range(0, len(noise_testing)):
            ra = b * b + 4 * a * estimated_noise[i]
            if ra.values < 0:
                ra = 0
                cr = cr + 1
            amp_noise[i] = (-b + np.sqrt(ra)) / (2 * a)

        amp_signal = pd.DataFrame(amp_signal)
        amp_error = amp_signal.values - amplitude.values

        file_helper.save_file(result_prefix + 'amp_signal', 'matched_filter', amp_signal)
        file_helper.save_file(result_prefix + 'amp_noise', 'matched_filter', amp_noise)
        file_helper.save_file(result_prefix + 'amp_error', 'matched_filter', amp_error)

        print('Finished!')


if __name__ == '__main__':
    number_of_data = 20000
    pedestal = 30
    # probs = [0.0]
    probs = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    mf_calculation(number_of_data, pedestal, probs, training_percentage=50)
