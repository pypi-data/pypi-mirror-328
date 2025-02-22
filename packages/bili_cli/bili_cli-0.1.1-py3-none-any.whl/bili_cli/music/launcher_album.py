#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import pygame
import os
import sys

import cv2

from bili_cli.music.AudioAnalyzer import AudioAnalyzer, RotatedAverageAudioBar, np
from bili_cli.music.music_player import MusicPlayer
from bili_cli.music.models import Music
from bili_cli.music.manage import build_music, build_album_musics


filename = "/Volumes/Getea/影片/音乐/爱情公寓/靠近"
args = sys.argv[1:]
if args:
    filename = args[0]

is_album_dir = False
album_image = os.path.join(filename, 'album.png')
if os.path.exists(album_image):
    is_album_dir = True

musics = []
if is_album_dir:
    musics = build_album_musics(filename)
else:
    m = build_music(filename)
    musics.append(m)

for mu in musics:
    print(mu.path)

infoObject = pygame.display.Info()

screen_w = int(infoObject.current_w/2.2)
screen_h = int(infoObject.current_w/2.2)

screen_w = 1920
screen_h = 1080

player = MusicPlayer.build([screen_w, screen_h], musics)
pygame.mixer.init()
#  player.start_time = 205

# 视频参数
#  fourcc = cv2.VideoWriter_fourcc(*"XVID")
#  video_out = cv2.VideoWriter(
    #  "/Users/wxnacy/Downloads/test1.mp4", fourcc, 60.0, (screen_w, screen_h))

clock = pygame.time.Clock()
t = pygame.time.get_ticks()
getTicksLastFrame = t


player.load_cur_music()
player.draw_album()
player.play(play_type='album')

running = True
count = 0
while running:
    clock.tick(24)

    avg_bass = 0
    poly = []

    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    player.draw_album()

    if player.is_play_finish():
        player.cut()

    for event in pygame.event.get():
        #  if event.type == pygame.QUIT or not pygame.mixer.music.get_busy():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    player.save_play_album_frame()
    count += 1

pygame.quit()
