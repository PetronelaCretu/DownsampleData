# -*- coding: utf-8 -*-
# Python version: 3
'''
Created on Thu May 2 12:51:00 2017
@author: p.cretu

Make a video from jpgs

'''
import os

class Video():
    
    def __init__(self):
        pass

    def makeVideo(self):
        path = 'ffmpeg-20170601-bd1179e-win64-static\\bin\\ffmpeg'
        os.system(path + " -f image2 -r 1/1 -i %d.jpg -vcodec mpeg4 -y movie.mp4")
