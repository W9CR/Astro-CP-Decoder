from chunks import chunkBasecalss, CHUNK_TYPES
from hexdump import hexdump
from struct import *

class chunk_30(chunkBasecalss):
    def __init__(self, data):
        super().__init__()
        format = [ 
            "28s",      # Unknown Data
            "5s",       # Prog Date YYMMDDHHMM  # TODO FIX THIS
            "B",        # Prog SRC
            "B",        # Unknown Byte
            "B",        # CP Version
            "H",        # CP Length
            "6H",       # 6 Pointers
            "2H",       # 2 Unknown Shorts
            "5H",       # 5 Pointers
            "3H",       # 3 Unknowns
            "7H",       # 7 Pointers, Some are currently Null
        ]
        self.description = CHUNK_TYPES[0x02]
        print(f"Parsing {self.description}")
        parsedData = self.unPack(format, data)

        self.addPointers(parsedData, [6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 22, 23, 24, 25, 26, 27, 28])

        # Breakout the rest of the data
        self.data['progDate'] = parsedData[1]
        self.data['prodSRC'] = parsedData[2]
        self.data['cpVersion'] = parsedData[4]
        self.data['cpLength'] = parsedData[5]

        hexdump(data)
