#!/usr/bin/env python

"""
Problem:
    Implement a dynamic equivalent of tail -f when reading a file
"""
import os
import sys

def tailf(filepath):
    """
    Unix tail(1) -f like behaviour.
    """
    try:
        fd = open(filepath, 'r')
        file_size = os.stat(filepath).st_size
        offset = 0
        while True:
            fd.seek(offset, os.SEEK_SET)
            new_size = os.stat(filepath).st_size
            if new_size >= file_size:
                data = fd.read(new_size)
                if not data:
                    continue
                else:
                    print(data.strip())
                offset = fd.tell()
                fd.seek(offset, os.SEEK_CUR)
            else:
                fd.seek(offset, os.SEEK_END)
    except KeyboardInterrupt:
        fd.close()

if __name__ == '__main__':
   tailf(sys.argv[1])
