#!/usr/bin/env python2

SEQ = '\033[{}m{{}}\033[0m'

fgcodes = {
    None            : 39, 'black'         : 30, 'red'           : 31,
    'green'         : 32, 'yellow'        : 33, 'blue'          : 34,
    'magenta'       : 35, 'cyan'          : 36, 'light gray'    : 37,
    'dark gray'     : 90, 'light red'     : 91, 'light green'   : 92,
    'light yellow'  : 93, 'light blue'    : 94, 'light magenda' : 95,
    'light cyan'    : 96, 'white'         : 97
}

bgcodes = {
    None            : 49, 'black'         : 40, 'red'           : 41,
    'green'         : 42, 'yellow'        : 43, 'blue'          : 44,
    'magenta'       : 45, 'cyan'          : 46, 'light gray'    : 47,
    'dark gray'     : 100, 'light red'     : 101, 'light green'   : 102,
    'light yellow'  : 103, 'light blue'    : 104, 'light magenda' : 105,
    'light cyan'    : 106, 'white'         : 107
}

stylecodes = {
    'bold'       : 1, 'dim'        : 2, 'underlined' : 4, 'blink'      : 5,
    'reverse'    : 7, 'hidden'     : 8,
}

def prettify(string,fg=None,bg=None,*styles):
    try:
        if styles:
            code = '{};{};{}'.format(
                ';'.join(map(lambda x:str(stylecodes[x]), styles)),
                fgcodes[fg],bgcodes[bg])
        else:
            code = "{};{}".format(fgcodes[fg],bgcodes[bg])
    except KeyError as e:
        raise ValueError("style or color not supported: \n{}".format(e))
    return SEQ.format(code).format(string)

def bold(string):
    return SEQ.format(stylecodes['bold']).format(string)

def underlined(string):
    return SEQ.format(stylecodes['underlined']).format(string)

if __name__ == "__main__":
    print(prettify("I'm blue!", 'blue',None,'bold','underlined'))
    print(prettify("reversed!",None,None,'reverse','blink'))
