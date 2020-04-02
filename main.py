from DemoClass import *
from bitio import bit_open
from MsgDataParser import *


dh = DemoHeader()
dirEntryList = []
fh = FrameHeader()
NetMsg = NetMsgHeader()
cvars = Cvars()
cvars_flag = 0
Player = {}
enginefps = []
realfps = []

f = bit_open('/Volumes/Zhanghd/2.dem', 'r')

# 开始解析
magic = f.ReadString(8)
# print(magic)
if magic != 'HLDEMO':
    print('demo格式不支持')
dh.demo_version = f.ReadInt()
dh.network_version = f.ReadInt()
dh.map_name = f.ReadString()
dh.game_dll = f.ReadString()
map_crc = f.ReadInt()
dh.dir_offset = f.ReadInt()
f.byte_file.seek(dh.dir_offset)
# dirEntry数量
entryNum = f.ReadInt()
for i in range(entryNum):
    dirEntry = DirEntry()
    # type
    dirEntry.type = f.ReadInt()
    # title
    dirEntry.title = f.ReadString(64)
    # flags
    dirEntry.flags = f.ReadInt()
    # cd track
    dirEntry.play = f.ReadInt()
    # time
    dirEntry.time = f.ReadFloat()
    # frame count
    dirEntry.frames = f.ReadInt()
    # offset
    dirEntry.offset = f.ReadInt()
    # length
    dirEntry.length = f.ReadInt()
    # 用数组来存放dirEntry对象
    dirEntryList.append(dirEntry)


f.byte_file.seek(dirEntryList[0].offset)
fh.type = f.ReadUint8()
fh.time = f.ReadFloat()
fh.frame = f.ReadInt()
print(fh)
if fh.type == 0:
    f.byte_file.seek(220, 1)
    NetMsg.ResolutionWidth = f.ReadInt()
    NetMsg.ResolutionHeight = f.ReadInt()
    # print(NetMsg.ResolutionWidth, NetMsg.ResolutionHeight)
    if cvars_flag == 0:
        cvars.getCvars(f)
        # print(cvars)
        f.byte_file.seek(108, 1)
        NetMsg.Length = f.ReadInt()
        # print('----------------')
        # print(f.byte_file.tell())
        # print(NetMsg.Length)
        cvars_flag = 1
    else:
        f.byte_file.seek(236, 1)
        NetMsg.Length = f.ReadInt()
        # print(NetMsg.Length)

dataParser(f,Player)
f.byte_file.seek(-1,1)

# print(Player)

#
currentFame = -1
f.byte_file.seek(dirEntryList[1].offset, 0)
while True:
    type = f.ReadUint8()
    time = f.ReadFloat()
    frame = f.ReadInt()
    # print('-------------------------')
    # print("type:", type)
    # print("time:", time)
    # print("frame:", frame)
    if type == 1:
        f.byte_file.seek(64, 1)
        ftime = f.ReadFloat()
        # print(ftime)
        realfps.append(ftime)
        f.byte_file.seek(170, 1)
        msec = f.ReadUint8()
        enginefps.append(msec)
        # print(msec)
        f.byte_file.seek(225, 1)
        # f.byte_file.seek(196, 1)
        length1 = f.ReadInt()
        f.byte_file.read(length1)
    elif type == 2:
        continue
    elif type == 3:
        # f.byte_file.read(64)
        str = f.ReadString(64)
        # if str == '+use':
        #     print(str)
        #     print(time)
        #     currentFame = frame
    elif type == 4:
        f.byte_file.read(32)
    elif type == 5:
        break
    elif type == 6:
        f.byte_file.read(84)
    elif type == 7:
        f.byte_file.read(8)
    elif type == 8:
        f.byte_file.read(4)
        length8 = f.ReadInt()
        f.byte_file.read(length8)
        f.byte_file.read(16)
    elif type == 9:
        length = f.ReadSInt()
        f.byte_file.seek(length,1)



EngineFpsMax = 1000.0 / min(enginefps)
RealFpsMax = 1.0 / min(realfps)
print(EngineFpsMax, RealFpsMax)




