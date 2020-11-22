from chunks import chunkBaseclass, CHUNK_TYPES
from hexdump import hexdump
from struct import *

class chunk_01(chunkBaseclass):
    def __init__(self, data):
        super().__init__()
        format = [ 
            "H",        # Pointer to CP start
            "26s",      # Unknown Data
            "L",        # Version
            "B",        # Model Type
            "13H",      # Read 13 Pointers, Some may be Null, which we filter out
        ]
        self.description = CHUNK_TYPES[0x01]
        print(f"Parsing {self.description}")
        parsedData = self.unPack(format, data)

        # Get all the pointers, and shove them into the local pointer list
        self.addPointers(parsedData, [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

        # Breakout the rest of the data
        self.data['version'] = parsedData[2]
        self.data['Model'] = parsedData[3]

        hexdump(data)
