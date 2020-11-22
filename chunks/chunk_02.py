from chunks import chunkBasecalss, CHUNK_TYPES
from hexdump import hexdump
from struct import *

class chunk_02(chunkBasecalss):
    def __init__(self, data):
        super().__init__()
        format = [ 
            "B",      # Base Offset
            "B",      # Freq Band
        ]
        self.description = CHUNK_TYPES[0x02]
        print(f"Parsing {self.description}")
        parsedData = self.unPack(format, data)

        # Breakout the rest of the data
        self.data['base_offset'] = parsedData[0]
        self.data['freq_band'] = parsedData[1]

        hexdump(data)
