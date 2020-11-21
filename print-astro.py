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



CHUNK_TYPES = {
    0x01 : "MODEL/SERIAL/POINTER DATA",
    0x02 : "CONFIGURATION",
    0x03 : "POINTER TO HW CONFIG",
    0x04 : "CONVENTIONAL HARDWARE CONFIG",
    0x05 : "SECURE DEVIATION",
    0x06 : "POINTER TO TXDEV/SQL/BW SOFT POTS",
    0x07 : "TX POWER/DEV SOFT POT",
    0x08 : "POINTER TO SQUELCH SOFT POTS",
    0x09 : "SQUELCH SOFT POTS",
    0x0A : "POINTER TO BANDWIDTH SOFT POTS",
    0x0B : "BANDWIDTH SOFT POTS",
    0x0C : "INTERMEDIATE FREQ DATA",
    0x0D : "MDC TIMING/HW CONFIG",
    0x0E : "FREQ TUNING VALUES",
    0x0F : "FRAC-N SYNTHESIZER",
    0x11 : "BUTTON/SWITCH A/D",
    0x15 : "BBRIC",
    0x0E : "FREQ TUNING VALUES",
    0x10 : "FEATURE DESCRIPTOR",
    0x13 : "ASTRO DATA PERIPHERAL",
    0x30 : "MODEL/SERIAL/POINTER DATA",
    0x31 : "RADIO WIDE OPTIONS",
    0x33 : "KP STAT/RADIO LOCK PW/CURRENT AFFIL",
    0x34 : "POINTER TO MOBILE MORE OPTIONS",
    0x35 : "RESERVE DATA AREA (OLD)",
    0x36 : "RADIO WIDE DISP/POINTER TO PTTID/VIP",
    0x37 : "# ZONES/POINTER DATA",
    0x38 : "CHANNEL NAME TEXT PER ZONE",
    0x39 : "POINTER TO PHONE NUMBER TEXT/DATA",
    0x3A : "PHONE LIST TEXT",
    0x3B : "PHONE DTMF ACCESS/DEACCESS",
    0x3C : "BUTTON/SWITCH/KEYPAD LOGIC CONFIG",
    0x3D : "POINTER CONV/MDC/TRUNK/SEC/ASTRO/MODAT/AUX",
    0x3E : "POINTER CONV BUT/MENU CONV RADIO WIDE STAT/MSG",
    0x3F01 : "CONV BUTTON CONFIGURATION/OPTIONS",
    0x3F02 : "TRUNK BUTTON CONFIGURATION/OPTIONS",
    0x4101 : "CONV MENU OPTIONS",
    0x4102 : "TRUNK MENU OPTIONS",
    0x42 : "MPL POINTER/DATA",
    0x43 : "MPL TEXT",
    0x44 : "POINTER TO MDC SYSTEM/REPEATER ID/CALL LIST",
    0x47 : "# MDC SYSTEMS/POINTER TO SYSTEM",
    0x48 : "MDC SYSTEM DATA/POINTER TO REVERT",
    0x49 : "MDC EMERGENCY REVERT DATA",
    0x4A : "POINTER TRUNK BUT/MENU RADIO WIDE DATA/SMARTZONE",
    0x4B : "# TRUNK SYSTEMS/POINTER TO SYSTEM",
    0x4C : "POINTER TO MULTIKEY HW ENC",
    0x4D : "MULTIKEY PAR DATA/POINTER TO HW KEY DATA/INDEX",
    0x4E : "MULTIKEY # OF KEYS/POINTER TO TEXT",
    0x4F : "MULTIKEY ENCRYPTION KEY INDEX",
    0x50 : "MDC OTAR DATA",
    0x51 : "SCAN POINTER/OPTIONS",
    0x52 : "# SCAN LISTS/POINTER TO LIST",
    0x53 : "SCAN LIST CONFIG/MEMBERS",
    0x54 : "ZONE POINTER TO PERSONALITY #",
    0x55 : "# CONV/TRUNK PERSONALITIES/POINTER",
    0x56 : "CONVENTIONAL PERSONALITY DATA",
    0x56FF : "CONVENTIONAL PERSONALITY DEFAULT DATA/POINTER TO TUNING",
    0x57 : "# ZONES/TALKGROUP DATA",
    0x58 : "POINTER TO TRUNK CALL LIST TEXT/DATA",
    0x59 : "TRUNK CALL LIST TEXT",
    0x5A : "TRUNK SYSTEM DATA",
    0x5B : "TRUNK LAB DYNAMIC SYSTEM DATA",
    0x5E : "PTR TO TRNK OB CH ASSIGN/OTHERBAND CONTROL CHANNELS",
    0x5F : "TRUNK OTHERBAND CHANNEL ASSIGN",
    0x60 : "TYPE I RESERVED DATA AREA",
    0x61 : "800/900 MHZ CONTROL CHANNELS",
    0x62 : "TRUNK PERSONALITY OPTIONS",
    0x63 : "TRUNK PERSONALITY TALKGROUP DATA",
    0x64 : "TRUNK PERSONALITY SUBFLEET DATA",
    0x65 : "TRUNK PERSONALITY FAILSOFT DATA",
    0x66 : "TRUNK PERSONALITY OTHERBAND FAILSOFT DATA",
    0x67 : "TRUNK PERSONALITY EMERGENCY REVERT DATA",
    0x6C : "SMARTZONE ENABLED IN TRUNK SYSTEM",
    0x6D : "800 SMARTZONE DATA",
    0x6E : "VHF/UHF SMARTZONE DATA",
    0x6F : "SMARTZONE ENV",
    0x70 : "POINTER TO TRUNK STATUS ALIAS TEXT/DATA",
    0x71 : "POINTER TO TRUNK MESSAGE ALIAS TEXT/DATA",
    0x72 : "POINTER TO TRUNK SITE ALIAS TEXT/DATA",
    0x73 : "TRUNK STATUS ALIAS TEXT",
    0x74 : "TRUNK MESSAGE ALIAS TEXT",
    0x75 : "TRUNK SITE ALIAS TEXT",
    0x76 : "# OF TG IN TRUNK PERSONALITY",
    0x77 : "EXTENDED DEK ZONE/MODE DATA",
    0x78 : "EXTENDED DEK STATUS BUTTON INDEX",
    0x79 : "EXTENDED DEK MESSAGE BUTTON INDEX",
    0x7A : "RADIO VIP OUT CONFIG",
    0x81 : "ASTRO RADIO WIDE/CAI DATA",
    0x82 : "# ASTRO SYSTEMS/POINTER TO SYSTEM",
    0x83 : "ASTRO SYSTEMS DATA",
    0x87 : "SOFTWARE ENCRYPTION KEY DATA",
    0x88 : "ASTRO CALL LIST ID",
    0x89 : "ASTRO CALL LIST ALIAS TEXT",
    0x8A : "ASTRO EMERGENCY REVERT",
    0x8B : "OTACR DATA",
    0x8C : "PTT ID PREFIX TEXT",
    0x8D : "MODAT DATA",
    0x8E : "CONVENTIONAL STATUS ALIAS DATA",
    0x8F : "CONVENTIONAL STATUS ALIAS TEXT",
    0x90 : "CONVENTIONAL MESSAGE ALIAS DATA",
    0x91 : "CONVENTIONAL MESSAGE ALIAS TEXT",
    0x92 : "MDC CALL LIST DATA",
    0x93 : "MDC CALL LIST TEXT",
    0x94 : "SOFT ID TEXT",
    0x95 : "HARDWARE ENCRYPTION KEY TEXT",
    0x96 : "SOFTWARE ENCRYPTION KEY TEXT",
    0x97 : "PA/SIREN DATA",
    0x98 : "VRS-EP CONFIG/DATA",
    0x99 : "HHCH DATA",
    0x9B : "800 SMARTZONE DATA",
    0x9D : "REAR CONTROL HEAD OPTION",
    0x9E : "VHF/UHF SMARTZONE DATA",
    0x9F : "MDC REPEATER ID",
    0xA0 : "AUX SYSTEM POINTER",
    0xA1 : "SINGLETONE SYSTEM",
    0xA2 : "SINGLETONE TIMING DATA",
    0xA3 : "SINGLETONE TONE DATA",
    0xA4 : "QCII SYSTEM",
    0xA5 : "QCII DATA",
    0xA6 : "GE STAR SYSTEM",
    0xA7 : "GE STAR DATA",
    0xA9 : "GE STAR HW CONFIG",
    0xAB : "VRM100/VRM500 DATA",
    0xAC : "OMNILINK PREF SITE",
    0xAE : "TRC OPTION",
    0xAF : "MULTI RADIO OPTION",
    0xB0 : "POINTER TO ASTRO SYSTEM",
    0xB1 : "POINTER TO ASTRO TALKGROUP/ALIAS",
    0xB2 : "ASTRO CONV TALKGROUP ID",
    0xB3 : "ASTRO CONV TALKGROUP ALIAS TEXT",
    0xB4 : "RESERVE DATA AREA",
    0xB5 : "RESERVE DATA AREA",
    0xB6 : "RESERVE DATA AREA",
    0xB7 : "RESERVE DATA AREA",
    0xB8 : "RESERVE DATA AREA",
    0xB9 : "RESERVE DATA AREA",
    0xBA : "SMART MESSAGE",
    0xBC : "SMART MESSAGE POINTER TO TEXT/DATA",
    0xBD : "SMART MESSAGE TEXT",
    0xBE : "SMART MESSAGE OPTIONS",
    0xC1 : "APCO25 PHONE LIST TEXT",
    0xC2 : "FACTORY OVERIDE ENABLE/POINTER",
    0xC3 : "APCO25 POINTER TO PHONE NUMBER TEXT/DATA",
    0xC6 : "FACT OVER FGU SYNTH RX",
    0xC7 : "FACT OVER FGU SYNTK TX",
    0xC8 : "FACT OVER HOST CLOCK SHIFT",
    0xC9 : "FACT OVER DSP CLOCK SHIFT",
    0xCA : "FACT OVER SECURE CLOCK SHIFT",
    0xCB : "APCO25 CONTROL CHANNELS",
    0xCC : "APCO25 BASE FREQUENCY",
    0xCD : "APCO25 TRUNK CALL LIST/POINTER TO TEXT",
    0xCF : "APCO25 # TALKGROUP IN TRUNK PERSONALITY",
    0xD0 : "APCO25 TRUNK PERSONALITY TALKGROUP DATA",
    0xD8 : "CKR KEY MANAGMENT DATA",
    0xD9 : "ASTRO OTAR DATA"
}

#pdb.set_trace()

def chksm8 (s):
    sum = 0
    for c in s:
        sum += ord(c)
        sum = sum % 0x100
    #    return '0x%2x' % (sum)
    return sum  # this returns it as an int.


#print options


def chunks(f):
    skip = 0
    global offset
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
            calcsum = chksm8(
            print "calculated checksum8 = ", "0x%x" % calcsum
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

FEATURE_LENGTH = 0x80
FEATURE_BLOCK = data[0x200:(INTERNAL_LENGTH+FEATURE_LENGTH)]

PROGRAMING_BLOCK = data[0x280:]
PROGRAMING_LENGTH = len(PROGRAMING_BLOCK)


if options.SHOW_INTERNAL == True:
    print "INTERNAL block length (hex) = ", "0x%x" % INTERNAL_LENGTH
    print "INTERNAL block start (hex) = ", "0x%x" % 0x0
    print "INTERNAL block end (hex) = ", "0x%x" % 0x1ff
    print INTERNAL_BLOCK.encode('hex')
    global offset
    offset = 0x0
#setup the Internal List
    INTERNAL_LIST = list()
    reader = StringIO(INTERNAL_BLOCK)
    for size, type, chunk, checksum, offset in chunks(reader):
        print "\nOffset:", "0x%x" % offset
        print "size:", "0x%x" % size
        print "type:", "0x%x" % type, "-", CHUNK_TYPES.get(type)
        print "data:"
        print hexprint(chunk)
        #print chunk.encode('hex')
        INTERNAL_LIST.append(chunk)
        print "checksum:", "0x%x" % checksum


if options.SHOW_FEATURE == True:
    print "FEATURE block length (hex) = ", "0x%x" % FEATURE_LENGTH
    print "FEATURE block start (hex) = ", "0x%x" % 0x0200
    print "FEATURE block end (hex) = ", "0x%x" % 0x027F
    print FEATURE_BLOCK.encode('hex')
    global offset
    offset = 0x200
    #setup the FEATURE List
    FEATURE_LIST = list()
    reader = StringIO(FEATURE_BLOCK)
    for size, type, chunk, checksum, offset in chunks(reader):
        print "\nOffset:", "0x%x" % offset
        print "size:", "0x%x" % size
        print "type:", "0x%x" % type, "-", CHUNK_TYPES.get(type)
        print "data:"
        print hexprint(chunk)
        #print chunk.encode('hex')
        FEATURE_LIST.append(chunk)
        print "checksum:", "0x%x" % checksum


if options.SHOW_PROGRAMING == True:
    print "PROGRAMING block length (hex) = ", "0x%x" % PROGRAMING_LENGTH
    print "PROGRAMING block start (hex) = ", "0x%x" % 0x0280
    print "PROGRAMING block end (hex) = ", "0x%x" % 0x027F
    print PROGRAMING_BLOCK.encode('hex')
    global offset
    offset = 0x280
    #setup the PROGRAMING List
    PROGRAMING_LIST = list()
    reader = StringIO(PROGRAMING_BLOCK)
    for size, type, chunk, checksum, offset in chunks(reader):
        print "\nOffset:", "0x%x" % offset
        print "size:", "0x%x" % size
        print "type:", "0x%x" % type, "-", CHUNK_TYPES.get(type)
        print "data:"
        print hexprint(chunk)
        #print chunk.encode('hex')
        PROGRAMING_LIST.append(chunk)
        print "checksum:", "0x%x" % checksum



    
#
#    print "number of programing block = ", "0x%x" % len(INTERNAL_LIST)
#    print "PRG-BLK-0 = ", INTERNAL_LIST[0].encode('hex')
#    PRG_BLK_1 = INTERNAL_LIST[1].encode('hex')


if options.SHOW_PROGRAMING == "False" and options.SHOW_FEATURE == "False" and options.SHOW_INTERNAL == "False":
    print "no data shown"



