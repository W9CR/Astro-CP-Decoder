#!/usr/bin/env python3
from struct import *
from hexdump import hexdump
import chunks

# Most common struct Types:
# B - Unsigned Char - 1 Byte
# H - Unsigned Short - 2 Bytes
# L - Unsigned Long - 4 Bytes
# #s - Char of # bytes - Number before the s tells size

class astroDecoder:
    chunks = {}
    pointers = []


    def __init__(self, filename):
        with open(filename, "rb") as file:
            self.file = file.read()

    def read(self, offset=0):
        print(f"Reading at: {hex(offset)}")
        chunkSize = unpack_from(">B", self.file, offset)[0]
        cs = 0
        if chunkSize > 0x03:
            chunkType, chunkData, chunkChecksum = unpack_from(f">B{chunkSize-1}sB", self.file, offset+1)
            for x in self.file[offset:offset+chunkSize+1]:
                cs += x & 0xFF
            cshex = (cs - 0x55 & 0xff)
        else:
            chunkSize = unpack_from(">H", self.file, offset)[0]
            chunkType, chunkData, chunkChecksum = unpack_from(f">B{chunkSize-1}sH", self.file, offset+2)
            for x in self.file[offset:offset+chunkSize+2]:
                cs += x & 0xFFFF
            cshex = (cs - 0x5555) & 0xffff

        print(f"Reading: {hex(chunkSize+2)} of Type: {hex(chunkType)}")
        print(f"Checksum: {hex(chunkChecksum)}, PreCalc: {hex(cs)}, Calculated: {hex(cshex)}")
        # Find a parser for the chunk
        if chunkType in chunks.CHUNK_PARSER:
            print(f"Found Chunk Parser for {hex(chunkType)}")
            module = __import__(f"chunks.{chunks.CHUNK_PARSER[chunkType]}", fromlist=[''])
            parser = getattr(module, chunks.CHUNK_PARSER[chunkType])(chunkData)
            # Get any Pointers from the parsed chunk and add it to the internal parser list
            self.pointers.extend(parser.getPointers())

            # Add parsed chunk to our chunks
            if chunkType not in self.chunks:
                self.chunks[chunkType] = []
            self.chunks[chunkType].append(parser)

            while len(self.pointers):
                pointer = self.pointers.pop()
                if pointer != 0x00:
                    self.read(pointer)
        else:
            print("Unknown Chunk")
            hexdump(chunkData)
        return chunkSize+2


test = astroDecoder("Astro-saber test cp.bin")
test.read()
#test.read(0x0398)
#test.read(0x0496)
