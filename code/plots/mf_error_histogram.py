"""Process Absolute Error between numeric and analitic Amplitudes."""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    num_events = 10000

    script_data = np.loadtxt(DIR_PATH + '/../results/matched_filter/{}-events/amp_error.txt'.format(num_events))

    mu = np.mean(script_data)
    sigma = np.std(script_data)

    fig, ax = plt.subplots()

    # the histogram of the data
    n, bins, patches = ax.hist(script_data, bins="auto")

    # Hist plot
    ax.set_xlabel('Erro de estimação (GeV)')
    ax.set_ylabel('Entradas')
    ax.set_title('Matlab Numeric Amplitude: {} events \n' r'$\mu={}$, $\sigma={}$'
                 .format(num_events, mu, sigma))
    ax.grid()

    # Tweak spacing to prevent clipping of ylabel
    fig.tight_layout()
    plt.show()
