import speech_recognition as sr

rec = sr.Recognizer()

def choose_microphone() -> int|None:
    mics = sr.Microphone().list_microphone_names()
    # mics = []
    print(f'Mics: {mics}')
    if len(mics) > 1:
        for index, mic in enumerate(mics):
            print(f'{index} - {mic}')
        option = int(input('Escolha um microfone: '))
        return option
    else:
        return None


def listen(mic: int):

    with sr.Microphone(device_index=mic) as microphone:
        rec.adjust_for_ambient_noise(microphone)
        try:
            while True:
                print('Ouvindo...')
                audio = rec.listen(microphone)
                text = rec.recognize_google(audio, language='pt-BR')
                print(text)

        except KeyboardInterrupt:
            pass
    


if __name__ == "__main__":
    mic = choose_microphone()
    if mic:
        listen(mic)
    else:
        print('Nenhum microfone encontrado...')
