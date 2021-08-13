from pydub import AudioSegment, silence


def get_padrao_vibracao(wav_path):
    ''' retorna um padrao de vibracao em decimais,
        O primeiro valor de cada item indica o tempo em
        decimos de segundo. O segundo valor indica se durante
        esse tempo, deve ou nao vibrar.
    Exemplo de result, onde o padrao seria:
    1. Vibrar 10 decimos.
    2. Aguardar 5 decimos
    3. vibrar 3 decimos:
    [                   
        [10, 1],
        [5, 0],
        [3, 1],
    ]


      '''
    music = AudioSegment.from_wav(wav_path)

    nonsilence = silence.detect_nonsilent(music, min_silence_len=100)
    
    result = []

    previous = 0
    
    for interruption in nonsilence:
        silencio = interruption[0] - previous
        result.append([silencio, 0])
        
        vibration = interruption[1] - interruption[0]
        result.append([vibration, 1])

        previous = interruption[1]

    # ignore if it starts in silence
    if result[0][0] <= 0:
        result = result[1:]

    return result
