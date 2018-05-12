# -*- coding: utf-8 -*-
"""
Created on Sat May 12 14:58:36 2018

@author: 郭汕
"""
from PIL import Image
im = Image.open('D:\龙文峻.jpg')
r, g, b = im.split()
newr = r.point(lambda i:i*0.8)
newb = b.point(lambda i:i*0.5)
newg = g.point(lambda i:i<120)
om = Image.merge(im.mode,(newr,newb,newg))
om.save('D:\新龙文峻.jpg')
