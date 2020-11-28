from chunks import chunkBaseclass, CHUNK_TYPES
from hexdump import hexdump
from struct import *

class chunk_55(chunkBaseclass):
    def __init__(self, data):
        super().__init__()
        self.description = CHUNK_TYPES[0x55]
        print(f"Parsing {self.description}")

        pairs = []
        numOfPairs = unpack_from(">B", data)[0]
        for x in range(numOfPairs):
            pairs.append( unpack_from(">H", data, (2 * x) + 1)[0])

        # Breakout the rest of the data
        self.data['convNumPers'] = numOfPairs
        self.pointers.extend(pairs)

        hexdump(data)
