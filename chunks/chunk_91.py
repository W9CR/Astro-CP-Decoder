from chunks import chunkBaseclass, CHUNK_TYPES
from hexdump import hexdump
from struct import *

class chunk_91(chunkBaseclass):
    default_stringLen = 0x0E
    default_numOfStrings = 0x10

    def __init__(self, data):
        super().__init__()
        self.description = CHUNK_TYPES[0x90]
        print(f"Parsing {self.description}")
        stringLength, numOfStrings, parsedData = self.parseStringBlock(data)
        print(parsedData)

        hexdump(data)
