from scipy.io import wavfile


def get_dados_musica(caminho):
    samp_freq, dados = wavfile.read(caminho)
    print(f'samp_freq: {samp_freq}')
    #print(dados)
    return dados

caminho = 'media/musicas/Happy.wav'

