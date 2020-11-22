from chunks import chunkBasecalss, CHUNK_TYPES
from hexdump import hexdump
from struct import *

class chunk_90(chunkBasecalss):
    def __init__(self, data):
        super().__init__()
        format = [ 
            "H",       # Pointer to Chunk Type 91
        ]
        self.description = CHUNK_TYPES[0x90]
        print(f"Parsing {self.description}")
        parsedData = self.unPack(format, data)

        self.addPointers(parsedData, [0])

        hexdump(data)
