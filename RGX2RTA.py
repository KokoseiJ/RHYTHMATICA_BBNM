import os
import shutil
from pydub import AudioSegment

mv = [False, False]

keynote = open("keynote.txt", 'r').readlines()
timenote = open("timenote.txt", 'r').readlines()

notes = [[], [], [], [], [], []]

for key, time in zip(keynote, timenote):
    key = key.replace("\n", "")
    time = time.replace("\n", "")
    if key == '1':
        notes[0].append(time)
    elif key == '2':
        if mv[0]:
            mv[0] = False
            notes[4].append(time)
        else:
            mv[0] = True
            notes[2].append(time)
    elif key == '3':
        if mv[1]:
            mv[1] = False
            notes[5].append(time)
        else:
            mv[1] = True
            notes[3].append(time)
    elif key == '4':
        notes[1].append(time)

os.mkdir("meow")
note = open("meow/note.txt", "w")
note.write("ver:A3\n")
for x in range(6):
    note.write("/\n")
    for y in notes[x]:
        note.write(y + "\n")
note.write('/')
info = open("meow/info.txt", "w")
originfo = open("info.txt", "r").readlines()

info.write(originfo[0] + originfo[1])
info.write(input("bpm: ") + "\n")
info.write(str(sum(map(lambda x:  len(x), notes))))

shutil.copyfile("select.png", "meow/img.png")

song = AudioSegment.from_mp3("song.mp3")
pre = AudioSegment.from_mp3("select.mp3")
song.export("meow/song.wav", format="wav")
pre.export("meow/pre.wav", format="wav")

print('done')