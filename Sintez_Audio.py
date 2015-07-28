import urllib.request
import urllib.parse
import urllib.error
from urllib.parse import urlparse


def gen(string_input):
   url = 'https://tts.voicetech.yandex.net/generate?text={}&format=wav&lang=ru-RU&speaker=omazh&key=2ddb24a0-130a-4334-90c1-67c669b525d3'
   text = string_input
   urlEncoded = urllib.parse.quote(text)
   url = url.format(urlEncoded)


   urllib.request.urlretrieve(url, 'Audio.mp3')