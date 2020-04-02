"""
    demo各种结构的类对象
"""


# 头部
class DemoHeader:
    demo_version = 0
    network_version = 0
    map_name = ''
    game_dll = ''
    dir_offset = 0

    def __str__(self):
        return "Demo Version: " + str(self.demo_version) + "\n" + \
               "Network Version: " + str(self.network_version) + "\n" + \
               "Map Name: " + self.map_name + "\n" + \
               "Game Dll: " + self.game_dll + "\n"


# DirEntry
class DirEntry:
    type = 0
    title = ''
    flags = 0
    play = 0
    time = 0.0
    frames = 0
    offset = 0
    length = 0


# 每一帧头部
class FrameHeader:
    type = 0
    time = 0.0
    frame = 0

    def __str__(self):
        s = 'type: ' + str(self.type) + '\n' + \
            'time: ' + str(self.time) + '\n' + \
            'frame: ' + str(self.frame) + '\n'
        return s


# NetMsgHeader
class NetMsgHeader:
    ResolutionWidth = 0
    ResolutionHeight = 0
    Length = 0


# Cvars
class Cvars:
    gravity = 0.0
    stopspeed = 0.0
    maxspeed = 0.0
    spectatormaxspeed = 0.0
    accelerate = 0.0
    airaccelerate = 0.0
    wateraccelerate = 0.0
    friction = 0.0
    edgefriction = 0.0
    waterfriction = 0.0
    bounce = 0.0
    stepsize = 0.0
    maxvelocity = 0.0
    footsteps = 0

    def getCvars(self,handle):
        handle.byte_file.seek(60, 1)
        self.gravity = handle.ReadFloat()
        self.stopspeed = handle.ReadFloat()
        self.maxspeed = handle.ReadFloat()
        self.spectatormaxspeed = handle.ReadFloat()
        self.accelerate = handle.ReadFloat()
        self.airaccelerate = handle.ReadFloat()
        self.wateraccelerate = handle.ReadFloat()
        self.friction = handle.ReadFloat()
        self.edgefriction = handle.ReadFloat()
        self.waterfriction = handle.ReadFloat()
        handle.ReadFloat()
        self.bounce = handle.ReadFloat()
        self.stepsize = handle.ReadFloat()
        self.maxvelocity = handle.ReadFloat()
        handle.ReadFloat()
        handle.ReadFloat()
        self.footsteps = handle.ReadInt()

    def __str__(self):
        s = 'sv_gravity: ' + str(self.gravity) + '\n' \
            'sv_stopspeed: ' + str(self.stopspeed) + '\n' \
            'sv_maxspeed: ' + str(self.maxspeed) + '\n' \
            'sv_spectatormaxspeed: ' + str(self.spectatormaxspeed) + '\n' \
            'sv_accelerate: ' + str(self.accelerate) + '\n' \
            'sv_airaccelerate: ' + str(self.airaccelerate) + '\n' \
            'sv_wateraccelerate: ' + str(self.waterfriction) + '\n'\
            'sv_friction: ' + str(self.friction) + '\n' \
            'edgefriction: ' + str(self.edgefriction) + '\n' \
            'sv_waterfriction: ' + str(self.waterfriction) + '\n' \
            'sv_bounce: ' + str(self.bounce) + '\n' \
            'sv_stepsize: ' + str(self.stepsize) + '\n' \
            'sv_maxvelocity: ' + str(self.maxvelocity) + '\n' \
            'mp_footsteps: ' + str(self.footsteps) + '\n'
        return  s


class Player:
    slot = 0
    userId = 0
    userInfo = ''

    def __str__(self):
        s = 'slot: ' + str(self.slot) + '\n' +\
            'userId: ' + str(self.userId) + '\n' + \
            'userInfo: ' + self.userInfo + '\n'