from __future__ import annotations

import struct
from pathlib import Path
from typing import BinaryIO


class BinaryReader:
    def __init__(self, fp: BinaryIO):
        self.fp = fp

    def seek(self, offset: int):
        self.fp.seek(offset)

    def tell(self) -> int:
        return self.fp.tell()

    def read(self, size: int) -> bytes:
        data = self.fp.read(size)
        if len(data) != size:
            raise EOFError("Unexpected end of file")
        return data

    def uint8(self) -> int:
        return struct.unpack(">B", self.read(1))[0]

    def uint16be(self) -> int:
        return struct.unpack(">H", self.read(2))[0]

    def uint32be(self) -> int:
        return struct.unpack(">I", self.read(4))[0]

    def bytes(self, size: int) -> bytes:
        return self.read(size)
