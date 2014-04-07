#!/usr/bin/env python2
# coding:utf-8

from __future__ import print_function
from textwrap import dedent
import PIL.Image as img
import numpy as np
import sys
import os
from rgbtoansi import colorize_bg
from rgbtoansi import grayscale_bg

def get_termsize():
    try:
        import fcntl, termios, struct
        h, w, _, _ = struct.unpack(
            'HHHH',
            fcntl.ioctl(
                sys.stdout.fileno(),
                termios.TIOCGWINSZ,
                struct.pack('HHHH', 0, 0, 0, 0)))
    except IOError:
        import os
        h, w = map(int,os.popen('stty size', 'r').read().split())
    return w, h

def show_img(imgfile, widthratio=2.0/3, fontratio=2.5, method="upperleft"):
    '''
    imgfile : image file readable by PIL.Image.open
    widthratio : how much of terminal width the image uses
    fontratio : the ratio height/width of your font
    about 2 for monaco, 2.5 for ubuntu mono.
    returns list of lines.
    '''
    if os.path.splitext(imgfile)[1] == '.gif':  # gif animation not supported yet
        pass
        #return ''
    w, _ = get_termsize()
    w = int(w*widthratio)
    imgary = np.array(img.open(imgfile))
    try:
        imgheight, imgwidth = len(imgary), len(imgary[0])
    except TypeError as e:
        '''
        ./imgs/1_81580523345.png
        '''
        # FIXME : can't handle transparent (not rgba?)
        return ''
    mode = ''
    if len(imgary.shape) == 2:
        mode = 'grayscale'
    elif len(imgary.shape) == 3:
        if imgary.shape[2] == 3:
            mode = 'rgb'
        elif imgary.shape[2] == 4:
            mode = 'rgba'
    if mode == '':
        raise IOError("Unknown filetype?")
    marks = [int(float(i)*imgwidth/w) for i in range(w+1)]
    rowpixels = (imgwidth/w)*fontratio  # 2 for monaco, 2.5 for ubuntu mono
    yreadingstart = 0
    img_str = []
    while yreadingstart < imgheight-1:
        line = []
        for (i,m) in enumerate(marks[1:]):
            m_b = marks[i]
            if method == "upperleft":
                pixel = imgary[yreadingstart,m_b]
            elif method == "mean":
                grid = imgary[yreadingstart:yreadingstart+rowpixels,
                              m_b:m]
                if mode == 'grayscale':
                    pixel = sum(grid.flatten())/float(
                        grid.shape[0]*grid.shape[1])
                else:
                    if mode == 'rgb':
                        pixel = np.array((0,0,0))
                    elif mode == 'rgba':
                        pixel = np.array((0,0,0,0))
                    for y_ in range(len(grid)):
                        for x_ in range(len(grid[0])):
                            pixel += grid[y_,x_]
                    pixel = pixel//(len(grid)*len(grid[0]))
            
            if mode == 'rgb':
                line.append(colorize_bg(' ', list(pixel)))
            elif mode == 'rgba':
                line.append(colorize_bg(' ', list(pixel)[:3]))
            elif mode == 'grayscale':
                line.append(grayscale_bg(' ', pixel))
        yreadingstart += rowpixels
        img_str.append(''.join(line))
    return img_str

def main():
    filenames = sys.argv[1:]
    if not filenames:
        print("specify filename(s).")
        return
    
    for filename in filenames:
        try:
            imgstr = show_img(filename) #, method='mean')
            print('\n'.join(imgstr))
        except IOError:
            print("No file found. Or something like that.")
            continue


if __name__ == "__main__":
    main()
