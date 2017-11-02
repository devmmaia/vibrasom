from pydub import AudioSegment
from pydub import silence

def get_padrao_vibracao(wav_path):
    ''' retorna um padrao de vibracao em decimais,
        O primeiro valor de cada item indica o tempo em
        decimos de segundo. O segundo valor indica se durante
        esse tempo, deve ou nao vibrar. \n
    Exemplo de retorno, onde o padrao seria: \n
    1. Vibrar 10 decimos.
    2. Aguardar 5 decimos
    3. vibrar 3 decimos:    \n
    [                   
        [10, 1],   \n
        [5, 0],    \n
        [3, 1],    \n
    ]


      '''
      
    musica = AudioSegment.from_wav(wav_path)

    tamanho = len(musica)

    nonsilence = silence.detect_nonsilent(musica, min_silence_len=100)
    silent = silence.detect_silence(musica, min_silence_len=100)
    retorno = []

    primeiro_intervalo = nonsilence[0]

    anterior = 0  
    
    for intervalo in nonsilence:
        silencio = (intervalo[0]) - anterior 
        retorno.append([silencio, 0])
        
        vibracao = (intervalo[1]) - intervalo[0]
        retorno.append([vibracao, 1])

        anterior = intervalo[1]     

    if retorno[0][0] <= 0:
        retorno = retorno[1:]



    return retorno
