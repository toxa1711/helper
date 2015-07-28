import urllib.request
import urllib.parse
import urllib.error
from urllib.parse import urlparse
import pyaudio
import wave



def gen(string_input):
   url = 'https://tts.voicetech.yandex.net/generate?text={}&format=wav&lang=ru-RU&speaker=omazh&key=2ddb24a0-130a-4334-90c1-67c669b525d3'
   text = string_input
   urlEncoded = urllib.parse.quote(text)
   url = url.format(urlEncoded)


   urllib.request.urlretrieve(url, 'test.mp3')


def play():
    chunk = 1024
    wf = wave.open('test.mp3', 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(
        format = p.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True)
    data = wf.readframes(chunk)

    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)

    stream.close()
    p.terminate()