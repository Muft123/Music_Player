import os
import pygame
import time
import eyed3
import random

def playmusic(filename,filedir):
    pygame.mixer.init()
    print(filename)
    print("开始播放")
    track = pygame.mixer.music.load(filedir + '\\' + filename)

    voice_file=eyed3.load(filedir + '\\' + filename)
    pygame.mixer.music.play()
    time.sleep(int(voice_file.info.time_secs))
    pygame.mixer.music.stop()

class playmould ():
    def __init__(self,sourcedirtory):
        self.dirtory = sourcedirtory
    def listloop (self,*args,**kwargs):
        file = os.listdir(self.dirtory)
        self.i = 0
        lenth = len(file)
        while self.i < lenth:
            self.nowplaying = file[self.i]
            music = file[self.i]
            print(f'正在播放的列表是{self.dirtory}')
            playmusic(music, self.dirtory)
            i = i + 1


    def singleloop(self,*args,**kwargs):
        file = os.listdir(self.dirtory)
        nowplaying = file[0]
        while True:
            print(f"正在单曲循环{file[0]}")
            playmusic(file[0], self.dirtory)


    def randomplay(self,*args,**kwargs):
        file = os.listdir(self.dirtory)
        temp = 0
        while True:
            num = random.randint(0, len(file) - 1)
            self.nowplaying = file[num]
            if num != temp:
                playmusic(file[num], self.dirtory)
            else:
                continue
            temp = num
    def returnnowplaying(self):
        return self.nowplaying

    def play(self):
        pygame.mixer.music.unpause()
    def pause(self):
        pygame.mixer.music.pause()

    def nextmusic(self):
        self.i = self.i + 1

    def lyrics(self):
        file = open('lyrics/问-陈淑桦.lrc', 'r', encoding='utf-8')
        lrc_list = file.read()

        return lrc_list