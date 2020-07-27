# not sure why it is commented
# ocup = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] # why? can it be a matrix?
import numpy as np
import datetime

ocup = [1.0]
tilecal = 1 # O QUE EH ISSO? - ACHO QUE OUVI BASTANTE SOBRE NA APRESENTACAO
NUMBER_OF_SIGNALS = 1


# To be implemented
def pegaPulsePaperCOF():
    pass


def pegaPulseJitter():
    pulso = np.loadtxt('pulsehi_physics.txt')
    pulso = np.concatenate((np.zeros((150, 2)), pulso, np.zeros((150, 2))))

    # jitter = np.random.randint(-6, 6, 1)
    # jitter = 0 # desvio de fase USAR ESTE
    jitter = 5 # desvio de fase

    # deformacao no pulso
    # deformacao = 0.02.*randn(1,7); #why was it commented?
    # deformacao = 0.05.*randn(1,7);
    deformacao = [-0.021571, -0.017683,  0.036657,  0.027222,  0.040167, -0.016309,  0.023051]
    # deformacao = [0, 0, 0, 0, 0, 0, 0] # sim. o envelhecimento dos componentes eletronicos / incerteza geral
    # python version
    # mu, sigma = 0, 0.05 # mean and standard deviation
    # deformacao = np.random.normal(mu, sigma, n)

    zero_index = np.where(pulso[:, 0] < 0)  # why not == 0?
    zero_index = zero_index[0][-1] + 1

    pulsehi = [
                pulso[zero_index - 150 + jitter, 1] + deformacao[0],
                pulso[zero_index - 100 + jitter, 1] + deformacao[1],
                pulso[zero_index - 50 + jitter, 1] + deformacao[2],
                pulso[zero_index + jitter, 1] + deformacao[3],
                pulso[zero_index + 50 + jitter, 1] + deformacao[4],
                pulso[zero_index + 100 + jitter, 1] + deformacao[5],
                pulso[zero_index + 150 + jitter, 1] + deformacao[6]
              ]

    print('================== pulsehi')
    print(pulsehi)
    print('==================')

    return pulsehi


if __name__ == '__main__':
    print('PYTHON CODE')

    # for gS in range(0, max_time1, step1):
    for gS in range(0, NUMBER_OF_SIGNALS):  # PQ ZERO NO CODIGO MATHLAB

        geraSinal = gS

        for level in range(0, len(ocup)):
            print('Processando: {0:d} / {0:2.6f}\n'.format(gS, ocup[level]))
            # cria conjunto de dados
            nEvt = 1  # 100000
            if tilecal:
                am = 7 # QUAL A DIFERENCA DE AMOSTRA PARA NUM DE EVENTOS?
            else:
                am = 10

            n = am * nEvt  # numero de amostras e eventos
            oc = ocup[level]  # ocupancia
            mPU = 100  # media da exponencial do pileup CHECAR DEFINICAO
            #The term “pileup” refers to the number of proton collisions per bunch crossing (roughly how many interactions we can expect to see when we record an event.)
            mSig = 300  # media exponencial sinal

            # dados
            x = [30.110, 31.290, 28.717, 28.479, 28.744, 29.141, 28.238]
            # x = 30 + 1.5.*randn(1,n) # mean 30 e standard deviation of 5?
            # python version
            # mu, sigma = 30, 1.5 # mean and standard deviation
            # x = np.random.normal(mu, sigma, n)

            # inclui pileup
            # python version
            # indPU = np.random.permutation(n)
            indPU = [2, 2, 6, 3, 4, 7, 1]
            # What about when "oc" is float?
            indPU = indPU[0:int(oc*n)]  # it is weird just get the same data again...

            if oc != 0:
                for i in range(0, int(oc*n)):
                    if tilecal:
                        # pu = exprnd(mPU).*pegaPulseTile();
                        # pu = np.multiply(np.random.exponential(mPU), pegaPulseJitter())
                        pu = np.multiply(111.79, pegaPulseJitter())

                        if indPU[i] < 4:
                            for j in range(indPU[i]-2, 3):
                                x[indPU[i] + j] = x[indPU[i] + j] + pu[j + 4]

                        elif indPU[i] > n-3:
                            for j in range(-4, n - indPU[i]):
                                x[indPU[i] + j] = x[indPU[i] + j] + pu[j + 4]
                        else:
                            for j in range(-4, 3):
                                x[indPU[i] + j] = x[indPU[i] + j] + pu[j + 4]

                    else:
                        # NOT TESTED!!!
                        print('NOT TESTED!!!')
                        pu = np.random.exponential(mPU) * pegaPulsePaperCOF()

                        if indPU[i] < 3:
                            for j in range(indPU[i]-2, 7):
                                x[indPU[i] + j] = x[indPU[i] + j] + pu[j + 3]

                        elif indPU[i] > 999993:
                            for j in range(-3, n - indPU[i]):
                                x[indPU[i] + j] = x[indPU[i] + j] + pu[j + 3]
                        else:
                            for j in range(-3, 7):
                                x[indPU[i] + j] = x[indPU[i] + j] + pu[j + 3]

            dados = np.reshape(x, (am, nEvt))
            dados = np.transpose(dados)
            geraSinal=1
            if geraSinal == 1:
                A = np.zeros(nEvt)
                for i in range(0, nEvt):
                    # A[i] = np.random.exponential(mSig)
                    A[i] = 60.426

                    if tilecal:
                        dados[i, :] = dados[i, :] + np.multiply(A[i], pegaPulseJitter())
                        print('===================')
                        print(dados)
                        print('===================')
                    else:
                        # NOT TESTED!!!
                        print('NOT TESTED!!!')
                        dados[i, :] = dados[i, :] + np.multiply(A[i], pegaPulsePaperCOF())

                dadosMean = np.mean(dados, axis=0)
                dadosStd = np.std(dados, axis=0)

                if tilecal:
                    fileText = 'GEGEdadosTileOcup{}.txt'.format(int(oc * 100))
                    header = 'Arquivo gerado em: {} \n' \
                             'Amplitude (A): {} \n' \
                             'Dados: \n\n'.format(datetime.datetime.now(), A)
                    footer = '\n\nMedia: {}, Desvio Padrão: {}' \
                             .format(dadosMean, dadosStd)
                    np.savetxt(
                        fileText,
                        dados,
                        fmt='%.13f',
                        delimiter=' ',
                        header=header,
                        footer=footer)
                else:
                    fileText = 'GEGEdadosOcup{}.txt'.format(int(oc * 100))
                    header = 'Arquivo gerado em: {} \n' \
                             'Amplitude (A): {} \n' \
                             'Dados: \n\n'.format(datetime.datetime.now(), A)
                    footer = '\n\nMedia: {}, Desvio Padrão: {}' \
                             .format(dadosMean, dadosStd)
                    np.savetxt(
                        fileText,
                        dados,
                        fmt='%.13f',
                        delimiter=' ',
                        header=header,
                        footer=footer)
            else:
                dadosMean = np.mean(dados, axis=0)
                dadosStd = np.std(dados, axis=0)
                if tilecal:
                    fileText = 'GEGEruidoTileOcup{}.txt'.format(int(oc * 100))
                    header = 'Arquivo gerado em: {} \n' \
                             'Dados: \n\n'.format(datetime.datetime.now())
                    footer = '\n\nMedia: {}, Desvio Padrão: {}' \
                             .format(dadosMean, dadosStd)
                    np.savetxt(
                        fileText,
                        dados,
                        fmt='%.13f',
                        delimiter=' ',
                        header=header,
                        footer=footer)
                else:
                    fileText = 'GEGEruidoOcup{}.txt'.format(int(oc * 100))
                    header = 'Arquivo gerado em: {} \n' \
                             'Dados: \n\n'.format(datetime.datetime.now())
                    footer = '\n\nMedia: {}, Desvio Padrão: {}' \
                             .format(dadosMean, dadosStd)
                    np.savetxt(
                        fileText,
                        dados,
                        fmt='%.13f',
                        delimiter=' ',
                        header=header,
                        footer=footer)

    # from pudb import set_trace; set_trace()
