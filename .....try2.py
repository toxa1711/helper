import voice_rec
import Play_audio
import Sintez_Audio
x = voice_rec.voice()
Sintez_Audio.gen(x)
Play_audio.play()