import numpy as np

from utils import pulse_helper, file_helper

np.set_printoptions(suppress=True)

if __name__ == '__main__':
    TEN_BITS_ADC_VALUE = 1023
    pedestal = 0
    dimension = 7
    number_of_data = 1000000

    print('Generating Data for {} signals'.format(number_of_data))

    amplitude = np.zeros(number_of_data)
    signal_testing = np.zeros((number_of_data, dimension))

    for i in range(0, number_of_data):
        amplitude[i] = TEN_BITS_ADC_VALUE * np.random.random(1)
        signal_testing[i, :] = pedestal + np.random.randn(1, dimension) + \
            np.multiply(amplitude[i], pulse_helper.get_jitter_pulse())

    file_helper.save_file('signal_testing', 'base_data', signal_testing)
    file_helper.save_file('amplitude', 'base_data', amplitude)

    print('Finished!')
