#!/usr/bin/env python3
# coding:utf-8

from __future__ import print_function  # for compatibility
from textwrap import dedent

def rgb_to_code(rgb):
    '''\
    r,g,b should be given in 0-255 integer.
    '''
    if not all(map(lambda x: 0<=x<=255, rgb)):
        raise ValueError(dedent(
            """\
            rgb should be given as a list of 0-255 integers.
            you gave : {}
            """.format(rgb)))
    rlevel, glevel, blevel = map(lambda x:x*6//256, rgb)
    return 16 + rlevel*36 + glevel*6 + blevel

def grayscale_to_code(gray):
    """ gray : 0<=gray<=255"""
    if not 0 <= gray <= 255:
        raise ValueError(" 0<=gray<=255 required.")
    graylevel = int(gray*24/256)
    return 232+graylevel

def colorize_fg(string, rgb):
    return "\033[38;5;{}m{}\033[0m".format(
        rgb_to_code(rgb),string)

def colorize_bg(string, rgb):
    return "\033[48;5;{}m{}\033[0m".format(
        rgb_to_code(rgb),string)

def grayscale_fg(string, gray):
    return "\033[38;5;{}m{}\033[0m".format(
        grayscale_to_code(gray),string)

def grayscale_bg(string, gray):
    return "\033[48;5;{}m{}\033[0m".format(
        grayscale_to_code(gray),string)

def fgbegin(rgb):
    return "\033[38;5;{}m".format(
        rgb_to_code(rgb))

def bgbegin(rgb):
    return "\033[48;5;{}m".format(
        rgb_to_code(rgb))
    
def set_color(fg, bg):
    colorcodes = [
        '{};5;{}'.format(fb, rgb_to_code(col))
            for (fb, col) in ((38,fg), (48,bg)) if col]
    return '\033[{}m'.format(';'.join(colorcodes))

    if fg:
        print("\033[38;5;{}m".format(fg), end='')
    if bg:
        print("\033[48;5;{}m".format(bg), end='')

def clear_style():
    return "\033[0m"


if __name__ == "__main__":
    print(colorize_fg("there",(25,0,0)))
    print(colorize_bg("there",(100,100,100)))
    print(set_color((250,0,0),(0,255,0)),end='')
    print("FOOOOOO    ",end='')
    print(clear_style())
    for i in range(0,255,10):
        print(grayscale_fg('gray :{}'.format(i),i))

