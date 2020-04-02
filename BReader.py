from bitio import *

f = bit_open('/Volumes/Zhanghd/2.dem', 'r')


f.byte_file.read(540)
dir_offset = f.ReadInt()
print("dir offset:", dir_offset)

type = f.ReadUint8()
time = f.ReadFloat()
frame = f.ReadInt()

print(type, time, frame)

f.byte_file.seek(220, 1)

ResolutionWidth = f.ReadInt()
ResolutionHeight = f.ReadInt()
print(ResolutionWidth, ResolutionHeight)

f.byte_file.seek(236, 1)

length = f.ReadInt()
print(length)

print('---------type----------')
msgtype1 = f.ReadUint8()
print(msgtype1)  ## 0x08: print
p = f.ReadCharStr()
print(p)

print('---------type----------')
msgtype2 = f.ReadUint8()
print(msgtype2)  ## 0x0b server info

serverversion = f.ReadInt()
servercount = f.ReadInt()
server_crc = f.ReadInt()
client_dll_crc = f.byte_file.read(16)
maxclients = f.ReadUint8()
playernum = f.ReadUint8()
uk_b5 = f.ReadUint8()
gamedir = f.ReadCharStr()
remotehost = f.ReadCharStr()
map1 = f.ReadCharStr()
map2 = f.ReadCharStr()

extraflag = f.ReadUint8()
print(serverversion,servercount,maxclients,gamedir,remotehost,map1,map2)
print(extraflag)

print('---------type----------')
msgtype3 = f.ReadUint8()
print(msgtype3)  ## 0x36  'sendextrainfo'

text = f.ReadCharStr()
uk_b6 = f.ReadUint8()
print(text)

print('---------type----------')
msgtype4 = f.ReadUint8()
print(msgtype4)  ## 0x0e  'deltadescription'

structure_name = f.ReadCharStr()
print(structure_name)
entry_count = f.read_bits(16)
print(entry_count)
for i in range(entry_count):
    elength = f.read_bits(3)
    datal =   f.read_bits(8*elength)
while f.ReadUint8() == 0:
    continue
f.byte_file.seek(-1,1)
# f.ReadCharStr()
# print('---------type----------')
# msgtype5 = f.ReadUint8()
# print(msgtype5)

# print('---------type----------')
# msgtype6 = f.ReadUint8()
# print(msgtype6)
#
# print('---------type----------')
# msgtype6 = f.ReadUint8()
# print(msgtype6)
#
print('---------type----------')
msgtype6 = f.ReadUint8() # 0x27  'newusermsg'
print(msgtype6)

usermsg_id = f.ReadUint8()
default_msg_length = f.ReadInt8()
usermsg_description = f.ReadString(16)
# uk_b7 = f.ReadUint8()

print(usermsg_id, default_msg_length, usermsg_description)



print('---------type----------')
msgtype7 = f.ReadUint8() # 0x27
print(msgtype7)
usermsg_id = f.ReadUint8()
default_msg_length = f.ReadInt8()
usermsg_description = f.ReadString(16)
# uk_b7 = f.ReadUint8()

print(usermsg_id, default_msg_length, usermsg_description)

print('---------type----------')
msgtype7 = f.ReadUint8() # 0x27
print(msgtype7)
usermsg_id = f.ReadUint8()
default_msg_length = f.ReadInt8()
usermsg_description = f.ReadString(16)
# uk_b7 = f.ReadUint8()

print(usermsg_id, default_msg_length, usermsg_description)

print('---------type----------')
msgtype7 = f.ReadUint8() # 0x27
print(msgtype7)
usermsg_id = f.ReadUint8()
default_msg_length = f.ReadInt8()
usermsg_description = f.ReadString(16)
# uk_b7 = f.ReadUint8()

print(usermsg_id, default_msg_length, usermsg_description)

print('---------type----------')
msgtype7 = f.ReadUint8() # 0x27
print(msgtype7)
usermsg_id = f.ReadUint8()
default_msg_length = f.ReadInt8()
usermsg_description = f.ReadString(16)
# uk_b7 = f.ReadUint8()

print(usermsg_id, default_msg_length, usermsg_description)

print('---------type----------')
msgtype7 = f.ReadUint8() # 0x27
while msgtype7 == 39:
    print('---------type----------')
    print(msgtype7)
    usermsg_id = f.ReadUint8()
    default_msg_length = f.ReadInt8()
    usermsg_description = f.ReadString(16)
    print(usermsg_id, default_msg_length, usermsg_description)
    msgtype7 = f.ReadUint8()
# uk_b7 = f.ReadUint8()
print('---------type----------')
print(msgtype7) ## 9 stufftext
stufftext = f.ReadCharStr()
print(stufftext)

print('---------type----------')
msgtype8 = f.ReadUint8() # 'updateuserinfo'
print(msgtype8)
slot = f.ReadUint8()
userid = f.ReadInt()
userinfo = f.ReadCharStr()
ud_data = f.byte_file.read(16)

print(slot)
print(userid)
print(userinfo)



# # offset
# demoSegment_offset2 = ReadInt(f)
# print("off set:", demoSegment_offset2)
# #
# f.seek(demoSegment_offset2, 0)
# while True:
#
#     type = ReadUint8(f)
#     time = ReadFloat(f)
#     frame = ReadInt(f)
#
#     if type == 9:
#         Read9(f)
#     elif type == 4:
#         Read4(f)
#     elif type == 1:
#         print('-------------------------')
#         print("type:", type)
#         print("time:", time)
#         print("frame:", frame)
#         Read1(f)
#     elif type == 2:
#         continue
#     elif type == 3:
#         Read3(f)
#     elif type == 8:
#         Read8(f)
#     elif type == 7:
#         Read7(f)
#     elif type == 6:
#         Read6(f)
#     elif type == 5:
#         break
