#!/usr/bin/python
from __future__ import division
import struct
import sys
print sys.argv
import fileinput
import binascii
from optparse import OptionParser
from StringIO import StringIO
import struct
import pdb;

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE" )

parser.add_option("-i", "--internal", action="store_true", dest="SHOW_INTERNAL", default="False", help="show Internal block")

parser.add_option("-F", "--feature", action="store_true", dest="SHOW_FEATURE", default="False", help="show feature block")

parser.add_option("-p", "--programing", action="store_true", dest="SHOW_PROGRAMING", default="False", help="show programing block")

(options, args) = parser.parse_args()

#print options


def chunks(f):
    skip = 0
    offset = 0
    while True:
        byte = f.read(1)
        if byte == "":
            break
        if ord(byte) != 0x00:
            print ""
            print "field found"
            print "skipped:", skip
            skip = 0
            size = ord(byte)
            type = ord(f.read(1))
            chunk = f.read(size-1)
            checksum = ord(f.read(1))
            yield size, type, chunk, checksum, offset
            offset = (offset + 2 + size)
        else:
            skip += 1
            offset +=1

def hexprint(data, addrfmt=None):
    """Return a hexdump-like encoding of @data"""
    if addrfmt is None:
        addrfmt = '%(addr)03i'
    
    block_size = 8
    
    lines = int(( len(data) / block_size) )
    print lines
    
    if (len(data) % block_size) != 0:
        lines += 1
        data += "\x00" * ((lines * block_size) - len(data))

    out = ""
    
    for block in range(0, lines):
        addr = block * block_size
        try:
            out += addrfmt % locals()
        except (OverflowError, ValueError, TypeError, KeyError):
            out += "%03i" % addr
        out += ': '
        
        left = len(data) - (block * block_size)
        if left < block_size:
            limit = left
        else:
            limit = block_size
        
        for j in range(0, limit):
            out += "%02x " % ord(data[(block * block_size) + j])
        
        out += "  "
        
        for j in range(0, limit):
            char = data[(block * block_size) + j]
            
            if ord(char) > 0x20 and ord(char) < 0x7E:
                out += "%s" % char
            else:
                out += "."
        out += "\n"
    return out


class BinaryReaderEOFException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return 'Not enough bytes in file to satisfy read request'


#print options.filename
#read data from file

with open(options.filename, 'rb') as f:
    data = f.read()

reader = StringIO(data)

# internal code plug is 0x200 bytes (512) bytes that is at the bottom of the eeprom, and mapped to the internal CPU eeprom

INTERNAL_LENGTH = 0x200
INTERNAL_BLOCK = data[:INTERNAL_LENGTH]





if options.SHOW_INTERNAL == True:
    print "programing block length (hex) = ", "0x%x" % INTERNAL_LENGTH
    print "programing block start (hex) = ", "0x%x" % 0x0
    print "programing block end (hex) = ", "0x%x" % 0x1ff
    print INTERNAL_BLOCK.encode('hex')

#setup the Internal List
    INTERNAL_LIST = list()
    reader = StringIO(INTERNAL_BLOCK)
    for size, type, chunk, checksum, offset in chunks(reader):
        print "\nOffset:", "0x%x" % offset
        print "size:", "0x%x" % size
        print "type:", "0x%x" % type
        print "data:"
        print hexprint(chunk)
        #print chunk.encode('hex')
        INTERNAL_LIST.append(chunk)
        print "checksum:", "0x%x" % checksum
    
    
#
#    print "number of programing block = ", "0x%x" % len(INTERNAL_LIST)
#    print "PRG-BLK-0 = ", INTERNAL_LIST[0].encode('hex')
#    PRG_BLK_1 = INTERNAL_LIST[1].encode('hex')


if options.SHOW_PROGRAMING == "False" and options.SHOW_FEATURE == "False" and options.SHOW_INTERNAL == "False":
    print "no data shown"



