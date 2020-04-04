# HLDEMO Struct



## 总体框架 
一个HLDEMO的总体框架

<details>
**<summary>Demo总体框架</summary>**

```
Demo{
    DemoHeader{
            char		magic[8];	// 'HLDEMO'
	    uint32 		demo_version;
	    uint32		network_version;
	    char		map_name[260];
	    char		game_dll[260];
	    uint32		map_crc;
	    uint32		directory_offset
    }

    DemoSegment{
        DemoMacroBlock{
            DemoMacroHeader{
                    uint8		type;
	            float		time;
	            uiint32		frame;
            }
            DemoMacroData{
               
            }
        }
        
        ...

    }



    uint32		number;
    DemoDirectoryEntry{
            uint32              type
	    char		title[64];
	    uint32		flags;
	    int32		play;
	    float		time;
	    uint32		frames;
	    uint32		offset;		// points to a DemoSegment
	    uint32		length;     // length of the DemoSegment at offset
    }

    ...


}

```
</details>





## DemoMacroData部分

<details>
**<summary>DemoMacroData</summary>**


```
// Type 0 and Type 1
// Game Data
NetMsg 
{
    Info
    {
        float	   timestamp
        RefParams
        {
            float vieworg[3];
            float viewangles[3];
            float forward[3];
            float right[3];
            float up[3];
            float frametime;
            float time;
            uint32 intermission;
            uint32 paused;
            uint32 spectator;
            uint32 onground;
            uint32 waterlevel;
            float simvel[3];
            float simorg[3];
            float viewheight[3];
            float idealpitch;
            float cl_viewangles[3];
            uint32 health;
            float crosshairangle[3];
            float viewsize;
            float punchangle[3];
            uint32 maxclients;
            uint32 viewentity;
            uint32 playernum;
            uint32 max_entities;
            uint32 demoplayback;
            uint32 hardware;
            uint32 smoothing;
            uint32 ptr_cmd;
            uint32 ptr_movevars;
            uint32 viewport[4];
            uint32 nextView;
            uint32 onlyClientDraw;
        }
        UserCmd
        {
            int16_t lerp_msec;
            uint8_t msec;
            uint8_t align_1;    //填充
            float viewangles[3];
            float forwardmove;
            float sidemove;
            float upmove;
            int8_t lightlevel;
            uint8_t align_2;    //填充
            uint16_t buttons;
            int8_t impulse;
            int8_t weaponselect;
            uint8_t align_3;
            uint8_t align_4;
            uint32 impact_index;
            float impact_position[3];
        }
        MovVars
        {
            float gravity;
            float stopspeed;
            float maxspeed;
            float spectatormaxspeed;
            float accelerate;
            float airaccelerate;
            float wateraccelerate;
            float friction;
            float edgefriction;
            float waterfriction;
            float entgravity;
            float bounce;
            float stepsize;
            float maxvelocity;
            float zmax;
            float waveHeight;
            uint32 footsteps;
            std::string skyName[32];
            float rollangle;
            float rollspeed;
            float skycolor_r;
            float skycolor_g;
            float skycolor_b;
            float skyvec_x;
            float skyvec_y;
            float skyvec_z;
        }
        float view[3];
        uint32 viewmodel;
    }
    uint32 incoming_sequence; 
    uint32 incoming_acknowledged;
    uint32 incoming_reliable_acknowledged;
    uint32 incoming_reliable_sequence;
    uint32 outgoing_sequence;
    uint32 reliable_sequence;
    uint32 last_reliable_sequence;
    uint32 msg_size
    std::vector<unsigned char> msg;
}

// Type 2
// Do nothing.
// Just continue to next frame;

// Type 3 
// A null-terminated string corresponding to a client command such as "+weapon".
ClientCommand{
    char    Command[64];
}

// Type 4
// A null-terminated string. 
32bytes
Unknown{
    char    Unknown[32];
}

// Type 5
// Last in segment
// This macro type marks the end of this segment for verification and switch to the
next one.

// Type 6
// Unknown 84bytes
Unknown{
    uint32     uk_i1;
    uint32     uk_i2;
    float      uk_f;
    char       data[72];
}

// Type 7
// Unkown 8bytes
Unkown{
    uint32    uk_i1;
    uint32    uk_i2;
}

// Type 8
// Play Sound
Sound{
    uint32    uk_i1;
    uint32    sound_name_length;
    char*     sound_name;
    float     uk_f1;
    float     uk_f2;
    uint32    uk_i2;
    uint32    uk_i3;
}

// Type 9
// Unknown
Unknown{
    sint32    chunklength;
    char      data[chunklength];
}

```
</details>

## Game Date(DemoMacroData Type 0/1) Msg
这部分是当前面`DemoMacroData`类型为0或1时，最后尾部`std::vector<unsigned char> msg`部分，只能根据读取的类型进行动态解析。 


<b><details><summary>Type</summary></b>

一共有这么多类型，读到的uint8转化成十进制代表的数据类型，根据类型不同结构不同，解析的方法也不同。

```
Type{
	SVC_BAD                   0
	SVC_NOP                   1
	SVC_DISCONNECT            2
	SVC_EVENT                 3
	SVC_VERSION               4
	SVC_SETVIEW               5
	SVC_SOUND                 6
	SVC_TIME                  7
	SVC_PRINT                 8
	SVC_STUFFTEXT             9
	SVC_SETANGLE              10
	SVC_SERVERINFO            11
	SVC_LIGHTSTYLE            12
	SVC_UPDATEUSERINFO        13
	SVC_DELTADESCRIPTION      14
	SVC_CLIENTDATA            15
	SVC_STOPSOUND             16
	SVC_PINGS                 17
	SVC_PARTICLE              18
	SVC_DAMAGE                19
	SVC_SPAWNSTATIC           20
	SVC_EVENT_RELIABLE        21
	SVC_SPAWNBASELINE         22
	SVC_TEMPENTITY            23
	SVC_SETPAUSE              24
	SVC_SIGNONNUM             25
	SVC_CENTERPRINT           26
	SVC_KILLEDMONSTER         27
	SVC_FOUNDSECRET           28
	SVC_SPAWNSTATICSOUND      29
	SVC_INTERMISSION          30
	SVC_FINALE                31
	SVC_CDTRACK               32
	SVC_RESTORE               33
	SVC_CUTSCENE              34
	SVC_WEAPONANIM            35
	SVC_DECALNAME             36
	SVC_ROOMTYPE              37
	SVC_ADDANGLE              38
	SVC_NEWUSERMSG            39
	SVC_PACKETENTITIES        40
	SVC_DELTAPACKETENTITIES   41
	SVC_CHOKE                 42
	SVC_RESOURCELIST          43
	SVC_NEWMOVEVARS           44
	SVC_RESOURCEREQUEST       45
	SVC_CUSTOMIZATION         46
	SVC_CROSSHAIRANGLE        47
	SVC_SOUNDFADE             48
	SVC_FILETXFERFAILED       49
	SVC_HLTV                  50
	SVC_DIRECTOR              51
	SVC_VOICEINIT             52
	SVC_VOICEDATA             53
	SVC_SENDEXTRAINFO         54
	SVC_TIMESCALE             55
	SVC_RESOURCELOCATION      56
	SVC_SENDCVARVALUE         57
	SVC_SENDCVARVALUE2        58
}

```

</details>
### 具体解析方法：

慢慢研究更新……  
可参考Reference


## Reference:  
>[Half-Life 1 Engine Messages](https://wiki.alliedmods.net/Half-Life_1_Engine_Messages)  
[hl-demofile-spec](https://cgit.sukimashita.com/hl-demofile-spec.git/tree/doc/hl1-demofile-spec.txt)  
[compLexity Demo Playe](https://github.com/jpcy/coldemoplayer)  


