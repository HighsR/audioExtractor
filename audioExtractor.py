import moviepy

import os

path=input("Enter the path of your audio file: ")

videoclip=moviepy.VideoFileClip(path)
audioclip=videoclip.audio
audioclip.write_audiofile('audio.mp3')