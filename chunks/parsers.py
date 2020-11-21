from chunks import chunkBasecalss, CHUNK_TYPES
from hexdump import hexdump
from struct import *

class chunk_01(chunkBasecalss):
    def __init__(self, data):
        self.description = CHUNK_TYPES[0x01]
        print(f"Parsing {self.description}")
        pointerCP, _, self.data['version'] = unpack_from(f">H26sL", data)
        self.pointers.append(pointerCP)
        hexdump(data)
