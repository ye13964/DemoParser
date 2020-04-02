# -*- coding: utf-8 -*-
#
# bitio/bit_file.py
#
import struct

class _BaseBitFile(object):
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return False
    def __del__(self):
        self.close()

class BitFileReader(_BaseBitFile):
    
    def __init__(self, name):
        self.name = name
        self.byte_file = open(name, "rb")
        self.rack = 0
        self.mask = 0

    @classmethod
    def from_file(cls, byte_file):
        if not hasattr(byte_file, "read"):
            raise TypeError("must have 'read' method")
        reader = cls.__new__(cls)
        reader.name = None
        reader.byte_file = byte_file
        reader.rack = 0
        reader.mask = 0
        return reader
    
    def close(self):
        if hasattr(self.byte_file, "close"):
            self.byte_file.close()
    
    def _read_byte(self):
        c = self.byte_file.read(1)
        if c == '':
            raise IOError("Bit file is empty!")
        return ord(c)
        
    def read(self):
        if self.mask == 0:
            self.mask = 0x80
            self.rack = self._read_byte()
        ret = 1 if (self.rack & self.mask) else 0
        self.mask >>= 1
        return ret
    
    def read_bits(self, count):
        if count <= 0:
            return 0
        ret = 0
        mask = 1 << (count - 1)
        while mask > 0:
            if self.mask == 0:
                self.mask = 0x80
                self.rack = self._read_byte()
            if self.rack & self.mask:
                ret |= mask
            self.mask >>= 1
            mask >>= 1
        return ret


    def ReadString(self,n=260):
        buf = self.byte_file.read(n)
        info = struct.unpack('' + str(n) + 's', buf)
        infotoStr = bytes.decode(info[0])
        return infotoStr.strip(b'\x00'.decode())

    def ReadInt(self, n=4):
        buf = self.byte_file.read(n)
        number = struct.unpack('I', buf)
        return number[0]

    def ReadSInt(self, n=4):
        buf = self.byte_file.read(n)
        number = struct.unpack('i', buf)
        return number[0]

    def ReadFloat(self):
        buf = self.byte_file.read(4)
        number = struct.unpack('f', buf)
        return number[0]

    def ReadUchar(self):
        buf = self.byte_file.read(1)
        char = struct.unpack('b', buf)
        return char[0]

    def ReadUint8(self):
        buf = self.byte_file.read(1)
        number = struct.unpack('B', buf)
        return number[0]

    def ReadInt8(self):
        buf = self.byte_file.read(1)
        number = struct.unpack('b', buf)
        return number[0]

    def ReadUint16(self):
        buf = self.byte_file.read(2)
        number = struct.unpack('H', buf)
        return number[0]

    def ReadInt16(self):
        buf = self.byte_file.read(2)
        number = struct.unpack('h', buf)
        return number[0]

    def ReadFloat3(self):
        buf = self.byte_file.read(12)
        data = struct.unpack(("%df" % (3)), buf)
        return data

    def ReadCharStr(self):
        data = b''
        while True:
            rdata = self.byte_file.read(1)
            if rdata != b'\x00':
                data += rdata
            else:
                return data









class BitFileWriter(_BaseBitFile):
    
    def __init__(self, name):
        self.name = name
        self.byte_file = open(name, "wb")
        self.rack = 0
        self.mask = 0x80
    
    @classmethod
    def from_file(cls, byte_file):
        if not hasattr(byte_file, "write"):
            raise TypeError("must have 'write' method")
        writer = cls.__new__(cls)
        writer.name = None
        writer.byte_file = byte_file
        writer.rack = 0
        writer.mask = 0x80
        return writer

    def _flush_byte(self):
        self.byte_file.write(chr(self.rack))
        self.rack = 0
        self.mask = 0x80
        
    def close(self):
        if self.mask != 0x80:
            self._flush_byte()
        if hasattr(self.byte_file, "close"):
            self.byte_file.close()
        
    def write(self, bit):
        if bit:
            self.rack |= self.mask
        self.mask >>= 1
        if self.mask == 0:
            self._flush_byte()
    
    def write_bits(self, code, count):
        if count <= 0:
            return
        mask = 1 << (count - 1)
        while mask > 0:
            if code & mask:
                self.rack |= self.mask
            self.mask >>= 1
            mask >>= 1
            if self.mask == 0:
                self._flush_byte()
