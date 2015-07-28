def voice():
    import speech_recognition as sr
    r = sr.Recognizer(language = "ru")
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        return(r.recognize(audio))
    except LookupError:
        return("Could not understand audio")