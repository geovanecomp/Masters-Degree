"""Helper to provide common structure for file generations"""

import numpy as np
import datetime


def save_tile_noise(sig_prob, data, dataMean, dataStd):
    fileText = 'results/noises/{}-events/TileNoiseProbability{}.txt' \
               .format(len(data), int(sig_prob * 100))
    header = 'Arquivo gerado em: {} \n' \
             'Dados: \n\n'.format(datetime.datetime.now())
    footer = '\n\nMedia: {}, Desvio Padrão: {}' \
             .format(dataMean, dataStd)
    np.savetxt(
        fileText,
        data,
        fmt='%.13f',
        delimiter=' ',
        header=header,
        footer=footer)


def save_noise(sig_prob, data, dataMean, dataStd):
    fileText = 'results/noises/{}-events/NoiseProbability{}.txt' \
               .format(len(data), int(sig_prob * 100))
    header = 'Arquivo gerado em: {} \n' \
             'Dados: \n\n'.format(datetime.datetime.now())
    footer = '\n\nMedia: {}, Desvio Padrão: {}' \
             .format(dataMean, dataStd)
    np.savetxt(
        fileText,
        data,
        fmt='%.13f',
        delimiter=' ',
        header=header,
        footer=footer)


def save_tile_data(sig_prob, data, dataMean, dataStd, A):
    time = datetime.datetime.now()
    fileText = 'results/signals/{}-events/TileDataProbability{}.txt' \
               .format(len(data), int(sig_prob * 100))

    header = 'Arquivo gerado em: {}'.format(time)
    np.savetxt(
        fileText,
        data,
        fmt='%.13f',
        delimiter=' ',
        header=header)

    fileText = 'results/signals/{}-events/TileDataProbability{}-Amplitude.txt'\
               .format(len(data), int(sig_prob * 100))
    header = 'Arquivo gerado em: {} \n' \
             'Amplitude (A): '.format(time)
    footer = 'Media: {}, Desvio Padrão: {}' \
             .format(dataMean, dataStd)
    np.savetxt(
        fileText,
        A,
        fmt='%.13f',
        delimiter=' ',
        header=header,
        footer=footer)


def save_data(sig_prob, data, dataMean, dataStd, A):
    time = datetime.datetime.now()
    fileText = 'results/signals/{}-events/DataProbability{}.txt' \
               .format(len(data), int(sig_prob * 100))
    header = 'Arquivo gerado em: {} \n'.format(time)
    np.savetxt(
        fileText,
        data,
        fmt='%.13f',
        delimiter=' ',
        header=header)

    fileText = 'results/signals/{}-events/DataProbability{}-Amplitude.txt' \
               .format(len(data), int(sig_prob * 100))
    header = 'Arquivo gerado em: {} \n' \
             'Amplitude (A): \n'.format(time)
    footer = '\n\nMedia: {}, Desvio Padrão: {}' \
             .format(dataMean, dataStd)
    np.savetxt(
        fileText,
        A,
        fmt='%.13f',
        delimiter=' ',
        header=header,
        footer=footer)


def save_file(fileName, fileFolder, data):
    fileText = 'results/{}/{}-events/{}.txt' \
               .format(fileFolder, len(data), fileName)

    np.savetxt(
        fileText,
        data,
        fmt='%.13f',
        delimiter=' ')
