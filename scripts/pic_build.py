
import random
from PIL import Image,ImageDraw,ImageFont
import datetime
import sys
import math
import os

postgraduateExamsDay = datetime.datetime(2022,12,24,0,0,0)
picDir = '/home/janey/Pictures/eva-wallpaper'


fileList = os.listdir(picDir)
fileList.sort()
#for file in fileList:
#    print(file)
today = datetime.datetime.now()
imgStatus=True
#print(picDir+'/'+fileList[random.randint(0,len(fileList))-1])
try:
    img = Image.open(picDir+'/'+fileList[random.randint(1,len(fileList)-1)])
except IOError:
    print('fail to load image')
    imgStatus=False

if imgStatus != False :
    with img.convert("RGBA") as base:
        txt = Image.new("RGBA",base.size,(255,255,255,0))
        try:
            #fnt = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSerif-BoldItalic.ttf",80)

            fnt = ImageFont.truetype("/usr/share/fonts/TTF/ukai.ttc",80)
        except OSError:
            print('fail to open ttf file.')
        d = ImageDraw.Draw(txt)
        day = (postgraduateExamsDay-today).days
        # d.text((10,10),str(day)+'days',font=fnt,fill=(255,255,255,200))
        # d.text((10,60),"#",font=fnt,fill=(255,255,255,255))
        d.multiline_text((10,10),'#距离->\n考研还有 -| \n'+str(day)+'days '+' -|',font=fnt,fill=(255,255,255,200))
        out = Image.alpha_composite(base,txt)
        out.save(picDir+'/'+'pic2.png')
        
