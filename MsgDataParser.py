from enum import Enum

class MsgType(Enum):
    svc_nop = 1
    svc_disconnect = 2
    svc_event = 3
    svc_version = 4
    svc_setview = 5
    svc_sound = 6
    svc_time = 7
    svc_print = 8
    svc_stufftext = 9
    svc_setangle = 10
    svc_serverinfo = 11
    svc_lightstyle = 12
    svc_updateuserinfo = 13
    svc_deltadescription = 14
    svc_clientdata = 15
    svc_stopsound = 16
    svc_pings = 17
    svc_particle = 18
    # // svc_damage = 19
    svc_spawnstatic = 20
    svc_event_reliable = 21
    svc_spawnbaseline = 22
    svc_tempentity = 23
    svc_setpause = 24
    svc_signonnum = 25
    svc_centerprint = 26
    # // svc_killedmonster = 27
    # // svc_foundsecret = 28
    svc_spawnstaticsound = 29
    svc_intermission = 30
    svc_finale = 31
    svc_cdtrack = 32
    # // svc_restore = 33
    # // svc_cutscene = 34
    svc_weaponanim = 35
    # // svc_decalname = 36
    svc_roomtype = 37
    svc_addangle = 38
    svc_newusermsg = 39
    svc_packetentities = 40
    svc_deltapacketentities = 41
    svc_choke = 42
    svc_resourcelist = 43
    svc_newmovevars = 44
    svc_resourcerequest = 45
    svc_customization = 46
    svc_crosshairangle = 47
    svc_soundfade = 48
    svc_filetxferfailed = 49
    svc_hltv = 50
    svc_director = 51
    svc_voiceinit = 52
    svc_voicedata = 53
    svc_sendextrainfo = 54
    svc_timescale = 55
    svc_resourcelocation = 56
    svc_sendcvarvalue = 57
    svc_sendcvarvalue2 = 58


def dataParser(f,pDic):
    while True:
        type = f.ReadUint8()
        if type == 7:
            f.byte_file.read(4)

        elif type == 8:
            MessagePrint(f)
        elif type == 11:
            MessageServerInfo(f)
        elif type == 15:
            MessageClientData(f)
        elif type == 54:
            MessageSendExtraInfo(f)
        elif type == 14:
            MessageDeltaDescription(f)
        elif type == 39:
            MessageNewUserMsg(f)
        elif type == 9:
            MessageStuffText(f)
        elif type == 13:
            MessageUpdateUserInfo(f, pDic)
        elif type == 45:
            f.byte_file.seek(8,1)
        elif type == 58:
            MessageSendCvarValue2(f)
        # elif type == 43:
        #     MessageResourceList(f)
        else:
            break






def MessagePrint(f):
    bData = f.ReadCharStr()
    str = bytes.decode(bData,encoding='utf-8')
    # print(str)

def MessageServerInfo(f):
    f.byte_file.read(28)
    maxclients = f.ReadUint8()
    # playernum
    f.ReadUint8()
    f.ReadUint8()
    gamedir = f.ReadCharStr()
    remotehost = f.ReadCharStr()
    sRemotehost = bytes.decode(remotehost,encoding='utf-8')
    f.ReadCharStr()
    f.ReadCharStr()
    # extraflag
    f.ReadUint8()
    # print(sRemotehost)

def MessageSendExtraInfo(f):
    # text
    f.ReadCharStr()
    f.ReadUint8()
    # print(text)

def MessageDeltaDescription(f):
    # structure_name
    f.ReadCharStr()
    # print(structure_name)
    entry_count = f.read_bits(16)
    # print(entry_count)
    for i in range(entry_count):
        elength = f.read_bits(3)
        datal = f.read_bits(8 * elength)
    while f.ReadUint8() == 0:
        continue
    f.byte_file.seek(-1, 1)


def MessageNewUserMsg(f):
    # usermsg_id
    f.ReadUint8()
    # default_msg_length
    f.ReadInt8()
    # usermsg_description
    f.ReadString(16)

def MessageStuffText(f):
    f.ReadCharStr()


def MessageUpdateUserInfo(f,pDic):
    slot = f.ReadUint8()
    userid = f.ReadInt()
    userinfo = f.ReadCharStr()
    s = bytes.decode(userinfo,encoding='utf-8')
    pDic[slot] = s
    f.byte_file.read(16)
    # print(s)

# def MessageResourceList(f):
#     nEntries = f.read_bits(12)

def MessageSendCvarValue2(f):
    f.byte_file.seek(4, 1)
    f.ReadCharStr()

def MessageClientData(f):
    return



