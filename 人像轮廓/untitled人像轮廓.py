# -*- coding: utf-8 -*-
"""
Created on Sat May 12 14:37:24 2018

@author: 郭汕
"""
from PIL import Image
from PIL import ImageFilter
im = Image.open('D:\我.jpg')
om = im.filter(ImageFilter.CONTOUR)
om.save('D:\新我.jpg')