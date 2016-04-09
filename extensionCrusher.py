#!/usr/bin/python

import sys
import os
import re

def main(filename):

    exts = filename.split('.')
    ext = exts[len(exts)-1]
    print '\nFile extension: ' + ext
    print 'Running file command...\n'
    command = 'file ' + filename 
    os.system(command)

    if "xor" in str(ext):
        xor(filename,ext)
    elif "b64" in str(ext):
        b64(filename,ext)
    elif "gz" in str(ext):
        gz(filename,ext)
    elif "bz2" in str(ext):
        bz2(filename,ext)
    elif "zip" in str(ext):
        zipz(filename,ext)
    else:
        print '\nNot able to crush that extenstion' 

def xor(filename,ext):
    newfilename = filename[:-len(ext)-1]
    xorwith = ext.split('xor')[1]
    xorwith = int(xorwith,16)

    b = bytearray(open(filename, 'rb').read())
    for i in range(len(b)):
        b[i] ^= xorwith
    open(newfilename, 'wb').write(b)
    main(newfilename)

def b64(filename,ext):
    newfilename = filename[:-len(ext)-1]
    command = "cat " + filename + " | base64 -d > " + newfilename
    os.system(command)
    main(newfilename)

def gz(filename,ext):
    newfilename = filename[:-len(ext)-1]
    command = "gunzip -c " + filename + " > " + newfilename
    os.system(command)
    main(newfilename)

def bz2(filename,ext):
    newfilename = filename[:-len(ext)-1]
    command = "bzip2 -f -d " + filename
    os.system(command)
    main(newfilename)

def zipz(filename,ext):
    command = "unzip -o " + filename
    out = os.popen(command).read()
    try:
        m = re.search('  inflating: (.*)', out)
        newfilename = m.group(1)
    except:
        m = re.search(' extracting: (.*)', out)
        newfilename = m.group(1)
    main(newfilename.strip())

filename = str(sys.argv[1])
main(filename)