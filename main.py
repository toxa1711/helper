import os
import time
from importlib.machinery import SourceFileLoader
import voice_rec
import Sintez_Audio as sau
import Play_audio as pau

spis = os.listdir('/home/anton/PycharmProjects/untitled1/lib')
modules = []

for i in spis:
    modules.append(i)

while True:
    sau.gen('ожидаю запрос')
    pau.play()
    x = voice_rec.voice()
    if x != 'окей':
        while x != 'окей':
            x = voice_rec.voice()
            time.sleep(0.3)

    sau.gen('слушаю')
    pau.play()

    x = voice_rec.voice()
    for i in range(len(spis)-1):
        f = SourceFileLoader(modules[i], "lib/"+modules[i]).load_module()
        if f.KEYS == x:
           sau.gen(f.func())
           pau.play()