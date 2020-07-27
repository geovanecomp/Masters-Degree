import numpy as np
import matplotlib.pyplot as plt

from numpy import linalg as LA
from sklearn.decomposition import PCA

from utils import pulse_helper

np.set_printoptions(suppress=True)

if __name__ == '__main__':
    TEN_BITS_ADC_VALUE = 1023
    pedestal = 0
    dimension = 7
    number_of_data = 10000
    qtd_for_training = 5000
    qtd_for_testing = number_of_data - qtd_for_training

    noise = pedestal + np.random.randn(number_of_data, dimension)
    # Getting data from boundaries
    noise_training = noise[:qtd_for_training, :]
    noise_testing = noise[qtd_for_testing:, :]

    amplitude = np.zeros(qtd_for_testing)
    signal_testing = np.zeros((qtd_for_testing, dimension))

    for i in range(0, qtd_for_testing):
        amplitude[i] = TEN_BITS_ADC_VALUE * np.random.random(1)
        signal_testing[i, :] = pedestal + np.random.randn(1, dimension) + \
            np.multiply(amplitude[i], pulse_helper.get_jitter_pulse())

    # Branqueamento
    noise_train_cov = np.asmatrix(np.cov(noise_training, rowvar=False))

    [D, V] = LA.eig(noise_train_cov)
    from pudb import set_trace; set_trace()
    # TODO Discover why I cant do it after np.diag for whitening filter.
    # If I do it, I am getting a diag matrix with other elements as inf.
    D = D**(-.5)

    # eig returns D as an array, we need to transform it into a diagonal matrix
    D = np.diag(D)

    W = D * V.T

    # W = np.matrix([
    #     [-1.6748373,   0.5175131,  -2.9246219,  -1.3834463,   2.2066308,  -0.6199292,    -1.4226427],
    #     [0.6572618,   0.6355380,   0.3928698,  -0.2736311,   1.1956474,  -0.9112701,    1.1674937],
    #     [-0.0684082,   1.2086504,   0.2564293,   0.3959205,  -0.2316473,  -0.3087873,    -0.6167130],
    #     [0.2274185,  -0.4449974,   0.6545361,   0.0488708,   0.6400391,  -0.0656841,    -0.8013342],
    #     [-0.4987594,   0.0996750,   0.1633758,   0.4668367,   0.3917242,   0.4615647,    0.2400612],
    #     [0.3093050,   0.2629946,   0.0019590,  -0.3352125,   0.0916674,   0.5640587,    -0.0501276],
    #     [0.3268204,  -0.0336678,  -0.2916859,   0.3680302,   0.0858922,   0.0387934,    -0.0389346]
    # ])

    W_t = np.transpose(W)

    # PCA Part
    pure_signal = np.zeros((qtd_for_testing, dimension))
    for i in range(0, qtd_for_testing):
        pure_signal[i, :] = np.multiply(
                                TEN_BITS_ADC_VALUE * np.random.random(1),
                                pulse_helper.get_jitter_pulse()
                            )

    # print (noise_train_cov)

    n_pca_components = dimension
    pca = PCA(n_components=n_pca_components)
    coeff = pca.fit(pure_signal.dot(W_t)).components_
    Y = pca.explained_variance_

    # stochastic filter params
    # ddof=1 to use Sampled data variance -> N-1
    variance = np.var(noise_training[:, 3], ddof=1)
    reference_pulse = [0.0000, 0.0172, 0.4524, 1.0000, 0.5633, 0.1493, 0.0424]
    bleached_reference_pulse = reference_pulse * W_t

    optimal_reference_pulse = bleached_reference_pulse * (coeff[:, :n_pca_components].T)

    optimal_noise = ((noise_testing - pedestal) * W_t) * coeff[:, :n_pca_components].T
    optimal_signal = ((signal_testing - pedestal) * W_t) * coeff[:, :n_pca_components].T

    No = variance * 2
    h1 = np.zeros((dimension, dimension))
    h2 = np.zeros((dimension, dimension))

    for i in range(0, n_pca_components):
        h1 = h1 + (Y[i] / (Y[i] + variance)) * (np.asmatrix(coeff[i, :]).T * coeff[i, :])
        h2 = h2 + (1.0 / (Y[i] + variance)) * (np.asmatrix(coeff[i, :]).T * coeff[i, :])

    IR_noise = np.zeros((len(noise_testing), 1))
    IR_signal = np.zeros((len(signal_testing), 1))

    for ev in range(0, len(noise_testing)):
        IR_noise[ev] = (1.0 / No) * (
                    (optimal_noise[ev, :] * coeff[:, :n_pca_components]) * h1 *
                    (optimal_noise[ev, :] * coeff[:, :n_pca_components]).T
                )

    for ev in range(0, len(signal_testing)):
        IR_signal[ev] = (1.0 / No) * (
                    (optimal_signal[ev, :] * coeff[:, :n_pca_components]) * h1 *
                    (optimal_signal[ev, :] * coeff[:, :n_pca_components]).T
                )

    ID_noise = np.zeros((len(noise_testing), 1))
    ID_signal = np.zeros((len(signal_testing), 1))
    for ev in range(0, len(noise_testing)):
        ID_noise[ev] = (
                (optimal_reference_pulse * coeff[:, :n_pca_components]) * h2 *
                (optimal_noise[ev, :] * coeff[:, :n_pca_components]).T
            )

    for ev in range(0, len(signal_testing)):
        ID_signal[ev] = (
                (optimal_reference_pulse * coeff[:, :n_pca_components]) * h2 *
                (optimal_signal[ev, :] * coeff[:, :n_pca_components]).T
            )

    # Matched Filter estimatives
    estimated_noise = ID_noise + IR_noise
    estimated_signal = ID_signal + IR_signal

    # Amplitue estimative
    b1 = coeff[:, :n_pca_components].T.dot(coeff[:, :n_pca_components])
    # DAQUI PARA BAIXO B2 E B3 NAO BATEM DEVIDO A ALGUMAS LINHAS DE COEFF
    b2 = (1.0 / No) * (
        coeff[:, :n_pca_components].T * h1 *
        coeff[:, :n_pca_components]
    )
    b3 = (optimal_reference_pulse * coeff[:, :n_pca_components]) * h2 * \
        coeff[:, :n_pca_components]

    amp_noise = np.zeros((len(noise_testing), 1))
    amp_signal = np.zeros((len(signal_testing), 1))

    a = (1.0 / No) * (
                (optimal_reference_pulse * coeff[:, :n_pca_components]) * h1 *
                (optimal_reference_pulse * coeff[:, :n_pca_components]).T
            )
    b = (optimal_reference_pulse * coeff[:, :n_pca_components]) * h2 * \
        (optimal_reference_pulse * coeff[:, :n_pca_components]).T

    cs = 0
    cr = 0
    for i in range(0, len(signal_testing)):
        ra = b * b + 4 * a * estimated_signal[i]
        if ra < 0:
            ra = 0
            cs = cs + 1
        # signal amplitute using MF filter output
        amp_signal[i] = (-b + np.sqrt(ra)) / (2 * a)

    for i in range(0, len(noise_testing)):
        ra = b * b + 4 * a * estimated_noise[i]
        if ra < 0:
            ra = 0
            cr = cr + 1
        amp_noise[i] = (-b + np.sqrt(ra)) / (2 * a)

    fig, ((ax0, ax1, ax2)) = plt.subplots(nrows=1, ncols=3)

    # colors = ['red', 'tan', 'lime']
    # fig.suptitle('{} events'.format(num_events), fontsize=14)
    ax0.hist((amp_signal - amplitude), bins="auto", density=True, histtype='bar')
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('amp_signal - amplitude')

    ax1.hist(amplitude, bins="auto", density=True, histtype='bar')
    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('Amplitude Verdadeira')

    ax2.hist(amp_signal, bins="auto", density=True, histtype='bar')
    ax2.legend(prop={'size': 10})
    ax2.grid(axis='y', alpha=0.75)
    ax2.set_title('Amplitude Estimada')

    plt.show()

    # from pudb import set_trace; set_trace()
    # print('==================== estimated_signal')
    # print(estimated_signal)
    # print('====================')
    # print('==================== estimated_noise')
    # print(estimated_noise)
    # print('====================')
    # print('==================== amp_signal')
    # print(amp_signal)
    # print('====================')
    # print('==================== amp_noise')
    # print(amp_noise)
    # print('====================')
