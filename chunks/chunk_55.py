from chunks import chunkBaseclass, CHUNK_TYPES
from hexdump import hexdump
from struct import *

class chunk_55(chunkBaseclass):
    def __init__(self, data):
        super().__init__()
        format = [ 
            "B",        # Number of conventional pers
            "9H",       # B Pointers, this should be the above time H
        ]
        self.description = CHUNK_TYPES[0x55]
        print(f"Parsing {self.description}")
        parsedData = self.unPack(format, data)
	#again this should be based on the number of conv pers 
        self.addPointers(parsedData, [2, 3, 4, 5, 6, 7, 8, 9])

        # Breakout the rest of the data
        self.data['convNumPers'] = parsedData[1]

        hexdump(data)
