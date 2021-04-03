from os import walk
from moviepy.editor import *

directory = input("Directory: ")

for subdir, dirs, files in os.walk(directory):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".mp4"):
            mp4_file = filepath
            videoclip = VideoFileClip(mp4_file)
            audioclip = videoclip.audio
            audioclip.write_audiofile(mp3_file)

            audioclip.close()
            videoclip.close()

