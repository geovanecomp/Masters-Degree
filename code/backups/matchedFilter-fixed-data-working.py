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
    number_of_data = 20
    qtd_for_training = 10
    qtd_for_testing = number_of_data - qtd_for_training

    noise = pedestal + np.random.randn(number_of_data, dimension)
    # Getting data from boundaries
    noise_training = noise[:qtd_for_training, :]
    noise_testing = noise[qtd_for_testing:, :]
    noise_training = np.matrix([
        [-0.8756796,  -0.9904594,   0.0763564,   0.2866689,  -0.8491597,  -2.6331943,  0.4875299],
        [0.5691059,   1.0500695,   0.2050344,   0.5682747,   0.9148819,   0.9840557,  0.0631626],
        [-0.8314480,  -1.2014296,   0.0640685,   1.0649667,   0.3001502,   0.7921802,  0.0182123],
        [-1.6749044,   0.9083217,   0.4855328,  -0.8777319,  -0.4533996,   0.4545650,  0.4935619],
        [-2.0737103,  -0.3444838,   2.6205070,  -2.3721530,   0.3851043,   0.2318063,  0.6319781],
        [-0.1389740,  -0.7860030,  -0.0916941,   2.4410314,   1.6296622,  -0.3318915,  0.1720283],
        [1.5643478,  -0.4838364,  -1.3568845,  -0.0097646,   0.3173777,   1.0363776,  1.1373946],
        [1.2958982,  -0.4076244,   0.0509913,  -0.3809160,  -0.0055843,  -0.5429556,  -1.2209100],
        [-0.4553984,   0.2447099,  -0.0911029,   1.5816856,  -0.1473872,  -0.2368131,  0.7251548],
        [0.8811581,   0.2740093,   0.2105274,   0.0017615,  -0.1050384,   0.5999477,  -0.4440812]
    ])

    noise_testing = np.matrix([
        [0.9431525,   0.4929578,   0.8702650,  -0.2384978,   1.1779368,   0.9613488, 0.7198087],
        [-0.1507800,  -0.8556539,  -0.3505294,   0.4385733,   0.2599012,   0.6289688, 1.1821911],
        [-1.1579471,  -0.7761330,   0.5048862,  -0.7994381,   0.5862172,  -1.0139671, 0.0973860],
        [-0.8073489,   0.6542282,   0.2723901,  -0.5065714,   1.4904722,   0.4038073, -0.9281103],
        [0.7330344,  -0.5733226,   0.2751025,   2.3656258,  -0.1680237,  -0.6095974, -0.9048640],
        [-1.0540677,   0.2591932,   0.5585528,   0.5630835,   0.3494722,   0.3133169, 0.1195288],
        [1.0160440,   1.0072891,   0.2649281,   0.0984453,   0.8794560,   0.7006237, -0.4429727],
        [-0.9385259,   1.1363805,   0.3755675,  -0.3434197,  -0.2836825,   0.3928002, -0.5461819],
        [-0.0046605,   1.2195139,   0.0973187,   1.4662556,  -1.0468390,   0.7239156, 0.5695964],
        [0.7419353,  -0.1169670,   0.8664425,   0.4642078,   0.2907896,  -1.3489066, 0.3598890]
    ])

    amplitude = np.zeros(qtd_for_testing)
    signal_testing = np.zeros((qtd_for_testing, dimension))

    for i in range(0, qtd_for_testing):
        amplitude[i] = TEN_BITS_ADC_VALUE * np.random.random(1)
        signal_testing[i, :] = pedestal + np.random.randn(1, dimension) + \
            np.multiply(amplitude[i], pulse_helper.get_jitter_pulse())

    amplitude = [775.902, 10.351, 771.456, 1019.714, 512.243, 396.846, 65.751, 68.398, 439.107, 913.696]

    signal_testing = np.matrix([
        [0.236776,     11.798491,    352.442790,    777.724908,    436.837438,   115.284537,     31.993758],
        [-0.868811,     -0.044646,      3.415924,      9.414231,      6.257210,   2.728463,     -0.782330],
        [0.047594,     14.065240,    348.083577,    772.605168,    432.601323,   114.304198,     33.564886],
        [0.696711,     19.768088,    461.249975,   1019.274032,    575.525264,   152.047669,     44.799316],
        [-0.508484,      7.670365,    233.040694,    512.310657,    288.821356,   74.425243,     21.451117],
        [-0.970319,      5.826021,    181.056663,    398.103175,    223.515092,   59.347880,     18.228919],
        [0.413107,      1.553945,     29.551838,     64.758933,     35.236955,   10.107259,      3.132132],
        [0.444259,      2.005030,     30.434815,     68.274549,     37.801127,   10.440632,      2.696392],
        [-0.177446,      8.735986,    197.462098,    437.059435,    247.049569,   63.410463,     17.028772],
        [-1.036739,     15.283146,    413.917933,    912.159329,    513.726378,   135.862961,     38.262066]
    ])

    # Branqueamento
    # noise_train_cov = np.cov(noise_training)
    noise_train_cov = np.matrix([
            [1.5238484,   0.0343165,  -0.8543985,   0.4900083,   0.1731590,   0.2918901,   -0.3036230],
            [0.0343165,   0.5913561,   0.0801816,  -0.2130887,  -0.0283764,   0.3523750,   0.0020615],
            [-0.8543985,   0.0801816,   0.9541332,  -0.8122446,  -0.0099779,  -0.0503286,  -0.0313772],
            [0.4900083,  -0.2130887,  -0.8122446,   1.7790657,   0.3740738,  -0.1521554,   -0.0214180],
            [0.1731590,  -0.0283764,  -0.0099779,   0.3740738,   0.4885224,   0.3277632,   -0.0170296],
            [0.2918901,   0.3523750,  -0.0503286,  -0.1521554,   0.3277632,   1.1858336,   0.0485573],
            [-0.3036230,   0.0020615,  -0.0313772,  -0.0214180,  -0.0170296,   0.0485573,  0.4439914]
        ])

    [D, V] = LA.eig(noise_train_cov)

    # TODO Discover why I cant do it after np.diag for whitening filter.
    # If I do it, I am getting a diag matrix with other elements as inf.
    D = D**(-.5)

    # eig returns D as an array, we need to transform it into a diagonal matrix
    D = np.diag(D)

    W = D * np.transpose(V)

    W_t = np.transpose(W)

    # PCA Part
    pure_signal = np.zeros((qtd_for_testing, dimension))
    for i in range(0, qtd_for_testing):
        pure_signal[i, :] = np.multiply(
                                TEN_BITS_ADC_VALUE * np.random.random(1),
                                pulse_helper.get_jitter_pulse()
                            )

    pure_signal = np.matrix([
            [0.00089477,     0.66899891,    17.57100806,    38.83567740,    21.87640893, 5.79952588,     1.64507153],
            [0.00463039,     3.46201728,    90.92859833,   200.97160612,   113.20871253, 30.01209480,     8.51311704],
            [0.00371731,    2.77933154,   72.99811097,   161.34140276,   90.88474157, 24.09391838,     6.83438955],
            [0.01695149,    12.67418518,   332.88276802,   735.74195320,   414.44859243, 109.87202458,    31.16588199],
            [0.00950488,     7.10654984,   186.65089286,   412.53830380,   232.38571430, 61.60640760,    17.47504004],
            [0.01038399,     7.76383156,   203.91415341,   450.69379353,   253.87896875, 67.30435766,    19.09129896],
            [0.00079089,     0.59132464,    15.53092201,    34.32665187,    19.33644329, 5.12617056,     1.45407011],
            [0.02063659,    15.42943668,   405.24842555,   895.68549890,   504.54591133, 133.75719398,    37.94105860],
            [0.00129928,     0.97144042,    25.51452205,    56.39253843,    31.76631165, 8.42137973,     2.38877665],
            [0.01686500,    12.60951796,   331.18430740,   731.98799279,   412.33396025, 109.31142690,    31.00686498]
        ])

    n_pca_components = dimension
    pca = PCA(n_components=n_pca_components)
    coeff = pca.fit(pure_signal * W_t).components_
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
    print('==================== estimated_signal')
    print(estimated_signal)
    print('====================')
    print('==================== estimated_noise')
    print(estimated_noise)
    print('====================')
    print('==================== amp_signal')
    print(amp_signal)
    print('====================')
    print('==================== amp_noise')
    print(amp_noise)
    print('====================')
