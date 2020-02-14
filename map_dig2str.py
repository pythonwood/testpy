#! /usr/bin/env python3

import os
import sys

_map = {
    0: ''    ,
    1: ''    ,
    2: 'ABC' ,
    3: 'DEF' ,
    4: 'GHI' ,
    5: 'JKL' ,
    6: 'MNO' ,
    7: 'PQRS',
    8: 'TUV' ,
    9: 'WXYZ',
}

_err_input = 'input data need to be number arry'

log = False # True

def main(arr):
    global _map
    result = ['']
    if log: print('main() arr', arr)
    if not all(isinstance(i, int) and 0<= i <= 9 for i in arr):
        print(_err_input)
        return result
    for i in arr:
        if i in [0,1]: continue
        _result = []
        for c in _map[i].lower():
            for now in result:
                _result.append(now+c)
        result = _result
        if log: print('main() forloop', i, result)
    return result

def mainprint(arr):
    result = main(arr)
    print(' '.join(result))

# $python3 /tmp/map_dig2str.py 2 3
# ad bd cd ae be ce af bf cf
if __name__ == '__main__':
    if log: print('args', sys.argv)
    if not (sys.argv[1:] and all(i.isdigit() for i in sys.argv[1:])):
        print(_err_input)
        sys.exit(2)
    arr = [int(i) for i in sys.argv[1:]]
    mainprint(arr)
