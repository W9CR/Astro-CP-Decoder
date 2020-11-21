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
            "13H",      # Read 13 Pointers, Some may be Null, which we filter out
        ]
        self.description = CHUNK_TYPES[0x01]
        print(f"Parsing {self.description}")
        paserdData = self.unPack(format, data)

        # Get all the pointers, and shove them into the local pointer list
        for pointer in [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
            if paserdData[pointer] != 0x00:
                self.pointers.append(paserdData[pointer])

        # Breakout the rest of the data
        self.data['version'] = paserdData[2]
        self.data['Model'] = paserdData[3]

        hexdump(data)
