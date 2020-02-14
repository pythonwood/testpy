#! /usr/bin/env python3

import os
import sys
from map_dig2str import main, mainprint, _err_input, log

# from . import map_dig2str
# map_dig2str.log = True

# $python3 /tmp/map_dig2str_plus.py 23
# ad bd cd ae be ce af bf cf
if __name__ == '__main__':
    if log: print('args', sys.argv)
    if not (len(sys.argv)==2 and len(sys.argv[1])<=2 and 
            all(i.isdigit() for i in sys.argv[1:])):
        print(_err_input)
        sys.exit(2)
    arr = [int(i) for i in sys.argv[1]]
    mainprint(arr)


