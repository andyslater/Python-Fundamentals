#
# File and Resource Manaement
#
# file modes https://stackoverflow.com/questions/16208206/confused-by-python-file-mode-w

# binary and text mode -- sys.getdefaultencoding -- returns the defulat encoding. neet to get this right





#
# read a file from googledrive
#   doc: https://developers.google.com/drive/v3/web/manage-downloads
#
# this is a shareable link. go to google drive.rtclik on file then click on shareable link
# https://drive.google.com/open?id=0BzBVcktvddLkRGREVG5OMEc3d1k
# https://drive.google.com/open?id=0BzBVcktvddLkZ3pVWXpFVmJnZEk
# <googkeldrive> FBX/data.csv https://drive.google.com/open?id=0BzBVcktvddLkaXJTWEpDMno2bTQ


import urllib.request
#x = urllib.request.urlretrieve("https://drive.google.com/open?id=0BzBVcktvddLkaXJTWEpDMno2bTQ/export?format=txt")
x = urllib.request.urlretrieve("https://drive.google.com/open?id=0BzBVcktvddLkaXJTWEpDMno2bTQ")
print(x)

import urllib.request
with urllib.request.urlopen('https://drive.google.com/open?id=0BzBVcktvddLkaXJTWEpDMno2bTQ') as response:
   html = response.read()



from itertools import count, islice

def sequence():
    """Generate Recman's sequence"""
    seen = set()
    a = 0
    for n in count(1):  # starts counting from 1 and keeps going for ever
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


def write_sequence(filename, num):
    """write recaman's sequence to a text ifile."""
    ## with opens the file with context so that it is automatically closed after use
    with open(filename, mode='wt', encoding='utf-8') as f:
        f.writelines("{0}\n".format(r) for r in islice(sequence(), num +1))  # islice will get only the first 1000 in th esequence


def read_series(filename):
    """ the below is identical to whte 'with open' 
    try:
        f = open(filename, mode='rt', encoding='utf-8')
        return [ int(line.strip()) for line in f ] # keep reading f and append to the list until f is null
    finally:
        f.close()  # finnaly is always executed even if there is an error
    return series
    """

    # with creates a context which auto closes the file after the block or on error
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [ int(line.strip()) for line in f ] # keep reading f and append to the list until f is null
    ### dont need to close f, since 'with' will do it even if there is an error


     
from files import *
write_sequence('recaman.dat', 1000)
read_series('recaman.dat')

"""

f = open('wasteland.txt', mode='wt', encoding='utf-8')

#help(f)

f.write("what are the roots that clutch, ")
f.write("what branches grow\n")
f.write("Out of this stony subbish? ")
f.close()

g = open('wasteland.txt', mode='rt', encoding='utf-8')
g.read(32) # read 32 characters, may be different than reading 32 bytes ?
g.read() # read till end of file

g.seek(0) # go to the 0th location in the file
g.readline() # get the next line
g.readline() # get the next line

g.seek(0) # go to the 0th location in the file
g.readlines() # get all the lines into a list

f.close()

h = open('wasteland.txt', mode='at', encoding='utf-8') # append, text
h.writelines(['\n1 2', ' 3 4', '\n5 6 7 8'])  # write everything in a list
h.close()

import sys

def read_file(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        sys.stdout.write(line) # like print but does not add its own \n so the \n read in will do the next line
    f.close()

read_file('wasteland.txt')


"""

