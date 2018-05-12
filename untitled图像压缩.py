# -*- coding: utf-8 -*-
"""
Created on Sat May 12 13:44:59 2018

@author: 郭汕
"""
from PIL import Image 
im = Image.open('C:\Users\郭汕\Pictures\截图\汇雅书世界.png')
im.size
im_resize = im.resize((256,256)) 
im_resize0 = im.resize((256,256), Image.BILINEAR)
im_resize0.size
im_resize1 = im.resize((256,256), Image.BICUBIC)
im_resize2 = im.resize((256,256), Image.ANTIALIAS)
