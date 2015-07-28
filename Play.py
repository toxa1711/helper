__author__ = 'student'
import subprocess


def play():
    sound_program = "mpg123"
    sound_file = "Audio.mp3"
    subprocess.call([sound_program, sound_file])






