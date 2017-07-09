#!/usr/bin/python2.7
import sys


def read_chunk(file, size):
    # use generator to read file by [size] bytes each time
    while True:
        data = file.read(size)
        if not data:
            break
        yield data


def write_chunk(fname, seq, content):
    fname += '_' + str(seq)
    out_f = open(fname, 'w')
    out_f.write(content)
    out_f.close()


# file name
fname = sys.argv[1]
# chunk size
csize = int(sys.argv[2])


f = open(fname, 'r')
k = 0
for chunk in read_chunk(f, csize):
    k += 1
    write_chunk(fname, k, chunk)