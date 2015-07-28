import speech_recognition as sr


def input_audio():
    r = sr.Recognizer(language="ru")

    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

    try:
        return r.recognize(audio)                # recognize speech using Google Speech Recognition
    except LookupError:                            # speech is unintelligible
        return " "
