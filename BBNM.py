from os import system as execute
from platform import system as osname
from pydub import AudioSegment as audio
from pydub.playback import play
import pygame
from pygame.locals import *
def clear():
    if osname() == "Windows":
        execute("cls")
    else:
        execute("clear")
if input("기존의 note.txt의 내용은 전부 삭제됩니다. 계속하시겠습니까?(Y/N): ") == 'N':
  exit()
listfile = open("note.txt", "w")
songfile = input("파일을 드래그 앤 드롭 해주십시오.")
type = input("파일의 확장자를 입력하여 주십시오.")
song = audio.from_file(songfile[1:-1], type)
bpm = float(input("곡의 BPM을 입력하여 주십시오."))
div = int(input("div 값을 입력하여 주십시오."))
tmp = float(input("시작하는 초를 입력하여 주십시오."))
nexttmp = 0
prevtmp = 0
playmod = 0
note = ["ver:A4", "b"+str(bpm), "d"+str(div), "w"+str(tmp)]
while True:
    nexttmp = tmp + (60/bpm)/div
    prevtmp = tmp - (60/bpm)/div
    if playmod == 1:
        playmod = 0
        play(song[tmp*1000:nexttmp*1000])
    else:
        play(song[prevtmp*1000:tmp*1000])
    res = input()
    if res == '':
        tmp = nexttmp
        note.append("/")
        clear()
        print("nothing appended")
    elif res[0] == 'v':#bpm
        bpm = int(res[1:])
        note.append(res)
        clear()
        print("BPM changed to", res[1:])
    elif res[0] == 'd':#div
        div = int(res[1:])
        note.append(res)
        clear()
        print("div changed to", res[1:])
    elif res[0] == 'w':#wait
        tmp = int(res[1:])
        note.append(res)
        clear()
        print("position moved to", res[1:])
    elif res[0] == 'r':#delete
        del(note[-1])
        clear()
        print("Removed")
    elif res[0] == 'e':#edit
        tmp -= (60/bpm)/div
        del(note[-1])
        clear()
        print("Removed, position rolled back")
    elif res[0] == 'c':#Current List
        clear()
        print(note)
    elif res[0] == 'q':#redo
        clear()
        print("I will play it again for you")
    elif res[0] == 'm':
        clear()
        playmod = 1
        print("play mode changed to", playmod)
    elif res[0] == 's':#stop
        clear()
        print("iT's tIme tO sTop")
        break
    else:
        tmp = nexttmp
        tempnote = ""
        for x in res:
            if x == 't':
                tempnote += "1"
            elif x == 'y':
                tempnote += "2"
            elif x == 'g':
                tempnote += "3"
            elif x == 'h':
                tempnote += "4"
            elif x == 'b':
                tempnote += "5"
            elif x == 'n':
                tempnote += "6"
        note.append(tempnote)
        clear()
        print(tempnote, "appended")
input("processing to .txt file. press Enter to proceed...")
for x in note:
    print(x)
    listfile.write(x+"\n")
input("done. press Enter to get outta here...")