from speech_recognition import Microphone, Recognizer, AudioFile, __version__ as version


def gettingWordsFromMic():
    mic = Microphone()
    recognizer = Recognizer()
    print("Say something...")
    print(Microphone.list_microphone_names())
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    input("Press a key to process")
    print(recognizer.recognize_google(audio))

def gettingWordsFromAudio():
    print(version)

    r = Recognizer()

    print("captures any speech")
    harvard = AudioFile('harvard.wav')

    with harvard as source:
        audio = r.record(source)

    print(type(audio))
    print(r.recognize_google(audio))

    print("")
    print("")
    print("captures any speech in the first four seconds of the file")
    with harvard as source:
        audio = r.record(source, duration=4)

    print(r.recognize_google(audio))

    print("")
    print("")
    print("The record() method, when used inside a with block, always moves ahead in the file stream.")
    with harvard as source:
        audio1 = r.record(source, duration=4)
        audio2 = r.record(source, duration=4)

    print(r.recognize_google(audio1))
    print(r.recognize_google(audio2))

    print("")
    print("")
    print("To capture only the second phrase in the file, you could start with an offset of four seconds and record for, say, three seconds.")
    with harvard as source:
        audio = r.record(source, offset=4, duration=3)

    print(r.recognize_google(audio))

    print("")
    print("")
    print("****************")
    print("noisy audio")
    jackhammer = AudioFile('jackhammer.wav')
    with jackhammer as source:
        audio = r.record(source)

    print(r.recognize_google(audio))

    print("")
    print("")
    print("The adjust_for_ambient_noise() method reads the first second of the file stream and calibrates the recognizer to the noise level of the audio.")
    with jackhammer as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.record(source)

    print(r.recognize_google(audio))

    print("")
    print("")
    print("Prints all json alternatives")
    print(r.recognize_google(audio, show_all=True))



if __name__ == "__main__":
    print("******** Speech to words *********\n")
    print("(1) Getting words from audio file\n")
    print("(2) Getting words from mic input\n")
    option = input("Select one option: ")
    if option == "1":
        gettingWordsFromAudio()
    else:
        gettingWordsFromMic()

