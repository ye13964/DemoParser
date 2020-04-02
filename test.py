from bitio import *

f = bit_open('/Volumes/Zhanghd/1.dem', 'r')


print(f.read_bits(1))
# print(f.byte_file.seek(1))
print(f.read_bits(8))
print(f.read_bits(12))