"""This helper provides different deformation pulses"""

import numpy as np


# To be implemented
def get_pulse_paper_COF():
    pass


# Generates a deformation pulse. It can represents for example hardware aging.
def get_jitter_pulse():
    base_pulse = np.loadtxt('data/pulsehi_physics.txt')
    pulsehi = []  # Stores the deformation pulse
    pulse_dim = 2
    pulse_idx = 1
    pulse_bandwidth = 150  # In nanoseconds
    reading_interval = 25  # In nanoseconds
    number_of_pulses = int(pulse_bandwidth / reading_interval) + 1  # WHY?

    # Sum of each side of the Normal Distribution
    step = reading_interval + reading_interval
    reading_position = pulse_bandwidth * (-1)

    pulse = np.concatenate(
                (
                    np.zeros((pulse_bandwidth, pulse_dim)),
                    base_pulse,
                    np.zeros((pulse_bandwidth, pulse_dim))
                )
            )

    jitter = int(np.random.normal(0, 25, 1))  # Gaussian Phase deviation
    # jitter = int(np.random.randint(-25, 25, 1))  # Phase deviation

    mu, sigma = 0, 0.02  # mean and standard deviation
    # Represents hardware agin or general uncertainty
    deformation = np.random.normal(mu, sigma, number_of_pulses)
    # deformation = np.zeros(number_of_pulses)  # It is set as 0 for now...

    zero_idx = np.where(pulse[:, 0] < 0)
    zero_idx = zero_idx[0][-1] + 1

    for i in range(0, number_of_pulses):
        pulsehi.append(pulse[zero_idx + reading_position + jitter, pulse_idx] + deformation[i])
        reading_position = reading_position + step

    return pulsehi, jitter
