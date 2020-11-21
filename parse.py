#!/usr/bin/env python3
from crccheck.checksum import Checksum8, Checksum16
from struct import *
from hexdump import hexdump
import chunks
import json

class read:
    chunks = {}
    pointers = []


    def __init__(self, filename):
        with open(filename, "rb") as file:
            self.file = file.read()

    def readChunk(self, offset):
        chunkSize = unpack_from(">B", self.file, offset)[0]
        if chunkSize > 0x03:
            chunkType, chunkData, chunkChecksum = unpack_from(f">B{chunkSize-1}sB", self.file, offset+1)
            cs = Checksum8.calc( self.file[offset:offset+chunkSize+1] )
            cshex = (cs - 0x55 & 0xff)
        else:
            chunkSize = unpack_from(">H", self.file, offset)[0]
            chunkType, chunkData, chunkChecksum = unpack_from(f">B{chunkSize-1}sH", self.file, offset+2)
            cs = 0
            for x in self.file[offset:offset+chunkSize+2]:
                cs += x & 0xFFFF
            cshex = (cs - 0x5555) & 0xffff

        print(f"Reading: {hex(chunkSize+2)} of Type: {hex(chunkType)}")
        print(f"Checksum: {hex(chunkChecksum)}, PreCalc: {hex(cs)}, Calculated: {hex(cshex)}")
        # Find a parser for the chunk
        if chunkType in chunks.CHUNK_PARSER:
            print("Found Chunk Parser")
            parser = getattr(chunks.parsers, chunks.CHUNK_PARSER[chunkType])(chunkData)

            # Get any Pointers from the parsed chunk and add it to the internal parser list
            self.pointers.extend(parser.getPointers())

            # Add parsed chunk to our chunks
            if chunkType not in self.chunks:
                self.chunks[chunkType] = []
            self.chunks[chunkType].append(parser)

            while len(self.pointers):
                self.readChunk(self.pointers.pop())
        else:
            print("Unknown Chunk")
            hexdump(chunkData)
        return chunkSize+2


test = read("Astro-saber test cp.bin")
newoffset = test.readChunk(0)
newoffset = test.readChunk(0x1188)
#test.readChunk(newoffset)
print(test)
