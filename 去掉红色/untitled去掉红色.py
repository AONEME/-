# -*- coding: utf-8 -*-
"""
Created on Sat May 12 14:07:35 2018

@author: 郭汕
"""
from PIL import Image
im = Image.open('D:\自然.jpg')
r, g, b = im.split()
newr = r.point(lambda i:i*0)
om = Image.merge(im.mode,(newr,g,b))
om.save('D:\新自然.jpg')