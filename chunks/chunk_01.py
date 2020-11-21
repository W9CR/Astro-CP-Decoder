from chunks import chunkBasecalss, CHUNK_TYPES
from hexdump import hexdump
from struct import *

class chunk_01(chunkBasecalss):
    def __init__(self, data):
        format = [ 
            "H",        # Pointer to CP start
            "26s",      # Unknown Data
            "L",        # Version
            "B",        # Model Type
            "H",        # Unknown Nulls
            "H",        # Pointer to Block 2
            "H",        # Pointer to Black 7
        ]
        self.description = CHUNK_TYPES[0x01]
        print(f"Parsing {self.description}")
        paserdData = self.unPack(format, data)

        # Get all the pointers, and shove them into the local pointer list
        for pointers in [0, 5, 6]:
            self.pointers.append(paserdData[pointers])

        # Breakout the rest of the data
        self.data['version'] = paserdData[2]
        self.data['Model'] = paserdData[3]

        hexdump(data)
