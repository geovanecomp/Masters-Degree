"""Compares Pileups from all PU Signals components"""

import os.path
import numpy as np
import matplotlib.pyplot as plt

DIR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    prob = 0.0
    num_events = 10000

    # Pile data
    pu_data_file_name = DIR_PATH + '/../results/pileup_data/prob_{}/{}_events/tile_signal_prob_{}.txt'.format(prob, num_events, prob)

    pu_data = np.loadtxt(pu_data_file_name)

    fig, ((ax0, ax1, ax2, ax3), (ax4, ax5, ax6, ax7)) = plt.subplots(nrows=2, ncols=4)

    # fig.suptitle('Comparação da Amplitude: Verdadeira X Numerica \n' '{} eventos'
    #              .format(num_events))
    fig.suptitle('Comparação dos 7 canais de sinal \n' '{} eventos e Empilhamento de {}%'
                 .format(num_events, prob))
    ax0.hist(pu_data[0], bins="auto")
    ax0.legend(prop={'size': 10})
    ax0.grid(axis='y', alpha=0.75)
    ax0.set_title('PU: Comp0 ' r'$\mu={:.5f}$, $\sigma={:.5f}$'
                  .format(pu_data[0].mean(), pu_data[0].std()))
    ax0.set_xlabel('Valor')
    ax0.set_ylabel('Frequência')

    ax1.hist(pu_data[1], bins="auto")
    ax1.legend(prop={'size': 10})
    ax1.grid(axis='y', alpha=0.75)
    ax1.set_title('PU: Comp1 ' r'$\mu={:.5f}$, $\sigma={:.5f}$'
                  .format(pu_data[1].mean(), pu_data[1].std()))
    ax1.set_xlabel('Valor')
    ax1.set_ylabel('Frequência')

    ax2.hist(pu_data[2], bins="auto")
    ax2.legend(prop={'size': 10})
    ax2.grid(axis='y', alpha=0.75)
    ax2.set_title('PU: Comp2 ' r'$\mu={:.5f}$, $\sigma={:.5f}$'
                  .format(pu_data[2].mean(), pu_data[2].std()))
    ax2.set_xlabel('Valor')
    ax2.set_ylabel('Frequência')

    ax3.hist(pu_data[3], bins="auto")
    ax3.legend(prop={'size': 10})
    ax3.grid(axis='y', alpha=0.75)
    ax3.set_title('PU: Comp3 ' r'$\mu={:.5f}$, $\sigma={:.5f}$'
                  .format(pu_data[3].mean(), pu_data[3].std()))
    ax3.set_xlabel('Valor')
    ax3.set_ylabel('Frequência')

    ax4.hist(pu_data[4], bins="auto")
    ax4.legend(prop={'size': 10})
    ax4.grid(axis='y', alpha=0.75)
    ax4.set_title('PU: Comp4 ' r'$\mu={:.5f}$, $\sigma={:.5f}$'
                  .format(pu_data[4].mean(), pu_data[4].std()))
    ax4.set_xlabel('Valor')
    ax4.set_ylabel('Frequência')

    ax5.hist(pu_data[5], bins="auto")
    ax5.legend(prop={'size': 10})
    ax5.grid(axis='y', alpha=0.75)
    ax5.set_title('PU: Comp5 ' r'$\mu={:.5f}$, $\sigma={:.5f}$'
                  .format(pu_data[5].mean(), pu_data[5].std()))
    ax5.set_xlabel('Valor')
    ax5.set_ylabel('Frequência')

    ax6.hist(pu_data[6], bins="auto")
    ax6.legend(prop={'size': 10})
    ax6.grid(axis='y', alpha=0.75)
    ax6.set_title('PU: Comp6 ' r'$\mu={:.5f}$, $\sigma={:.5f}$'
                  .format(pu_data[6].mean(), pu_data[6].std()))
    ax6.set_xlabel('Valor')
    ax6.set_ylabel('Frequência')

    ax7.hist([0], bins="auto")
    ax7.legend(prop={'size': 10})
    ax7.grid(axis='y', alpha=0.75)
    ax7.set_title('Empty'
                  .format(pu_data[6].mean(), pu_data[6].std()))
    ax7.set_xlabel('Valor')
    ax7.set_ylabel('Frequência')

    plt.show()
