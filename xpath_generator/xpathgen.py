#!/usr/bin/python2.7
import sys
import xml.etree.ElementTree as ET

def printpath(node, path):
    path += '/' + node.tag
    nexts = list(node)
    if len(nexts) == 0:
        print path
    else:
        for n in nexts:
            printpath(n, path)

f = open(sys.argv[1], 'r')
s = f.read()
root = ET.fromstring(s)
printpath(root, '')


