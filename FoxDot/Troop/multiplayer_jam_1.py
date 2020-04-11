Clock.set_time(0)
Clock.bpm = 133
###################

pl >> pluck(
    P[(0,2,4),(1,3,5),(2,4,6)],
    dur=0.25,
    vib=linvar([0,2],1), vibdepth=1,
    lpf=[
        var([1000, 800, 700, 600, 500], 32),
        var([500, 1500, 250, 2000], [16, 32]),
        var([250, 500, 1000], [8, 64]),
        1250
    ], lpr=0.25,
    amp=linvar([0.25,0.1], [128, 64])
)

zp >> zap(P[0,5,-3,-6], dur=PDur(3,8), amp=0.2, vib=expvar(1,2), tremolo=1)

kk >> play('[xx][ ][* ]/',
    amp=linvar(1/2,1),
    dur=1,
    echo=expvar(0.1),
    lpf=1
)


lk >> play('[X.][qq]', rate=[1, 0.35], dur=1, lpf=expvar([500, 1000], 32), delay=0.1, amp=linvar(1/2, 1), pan=PRand([-1,1]))

#

# me neither. Let's restart supercolliders and reconnct?


# got sound?
# RIP
# my supercollider is going crazy

# let's find the bug

h1 >> play('-', dur=0.25, amp=expvar([1, 0], 1/3) * var([1, 0], [[64, 128], [32, 64]]))
h2 >> play('-', sample=2, dur=1, delay=0.5, amp=1)

kd >> play('X', sample=0, rate=[1, 0.98, 1, 0.95], lpf=200, lpr=0.25, dur=1, amp=var([1, 0], [[28, 56], [4, 8]]))
sk >> play('X', sample=0, lpf=150, lpr=0.25, dur=1, delay=0.5, amp=P[0, 1, 0, 0] * (kd.amp * 0.85))

rs >> play('I', dur=var([8, 4, 2, 1, 2], [64, 32, 28, ]), amp=0.85)

tm >> play('m', dur=1/8, amp=P[0, 0.25, 0.5, 0.15, 0.75, [0, 0.5], 0.25, 0.5] * var([0.75, 0], [64, 32]))

sp >> soprano(
    [-10, -8, -9, -5, -11, -9],
    tremolo=expvar([0, 0, 2], [64, 64, 128]),
    hpf=expvar([1000, 650, 1250, 850], [32, 64]), hpr=expvar([0.75, 0.25], 128),
    dur=[[8, 16], 6, 4],
    amp=1
)

sn >> snick(dur=expvar([0.15, 0.3], 32), room=1, mix=0.25, hpf=1500, hpr=0.25, amp=expvar([0.25, 1], 64))

sw >> swell(
    [-5, -3, -4, -6, -2],
    dur=[[16, 32], [16, 16, 4], [32, 8, 2]],
    slide=-0.15,
    tremolo=var([4, 8], [128, 64]),
    lpf=expvar([1500, 800], 64),
    amp=1
)

sh >> play('s', pan=PWhite(-0.75, 0.75), dur=0.25, amp=P[PWhite(0, 1), PWhite(0.25, 1), 0.5, 1] * expvar([0, 0, 1], [16, 16, 32]))


###################

print(SynthDefs)

print(Samples)

print(Attributes)




#########################################################################################
#################################### CRASHED, ATTEMPT 2 #################################
#########################################################################################

Clock.set_time(0)
Clock.bpm = 133
###################

pl >> pluck(
    P[(0,2,4),(1,3,5),(2,4,6)],
    dur=0.25,
    vib=linvar([0,2],1), vibdepth=1,
    lpf=[
        var([1000, 800, 700, 600, 500], 32),
        var([500, 1500, 250, 2000], [16, 32]),
        var([250, 500, 1000], [8, 64]),
        1250
    ], lpr=0.25,
    amp=linvar([0.5,0.1], [128, 64])
)

zp >> zap(P[0,5,-3,-6], dur=PDur(3,8), amp=0.2, vib=expvar(1,2), tremolo=1)

kk >> play('[xx][ ][* ]/',
    amp=linvar(1/2,1),
    dur=1,
    echo=var([0.25, 0.5], 32),
    lpf=1,
    amp=var([0, 1], [32, 32, 16, 16, 32])
)


sr >> play('z', sample=1, rate=0.75, dur=var([8, 16, 32, 64], 64), amp=0.75)

lk >> play('[X.][qq][po]', rate=[1, 0.35], dur=1, lpf=expvar([500, 1000], 32), delay=0.25, amp=linvar([0, 1/4], 1/2), pan=[-1, 1])

ki >> play('[XX][...][(xxX)]', dur=PDur(5,8), amp=linvar(0.2,[1/4,1]), lpf=expvar([200,30], 32))

h1 >> play('-', sample=var([0, 2, 1, 3], [64, 32, 16, 16, 64]), dur=0.25, amp=expvar([1, 0], 1/3) * var([1, 0], [[64, 128], [32, 64]]))
h2 >> play('-', sample=var([2, 1, 0, 2], 64), dur=1, delay=0.5, amp=var([0, 1], [[128, 64, 64], [64, 128, 128]]))

bp >> blip(dur=1, oct=var([4.5, 5.5], [64, 128]), delay=0.5, amp=var([0.95, 0], [[128, 64, 32], [64, 32, 16]]))
sn >> blip(dur=1, delay=0, amp=P[0, 1, 0, 0] * bp.amp)

kd >> play('X', sample=var([0, 2], [128, 64]), rate=[1, 0.98, 1, 0.95], lpf=200, lpr=0.25, dur=1, amp=var([1, 0], [[28, 56, 112], [4, 8, 16]]))
sk >> play('X', sample=0, lpf=150, lpr=0.25, dur=1, delay=0.5, amp=P[0, 1, 0, var([0, 1], [128, 32])] * (kd.amp * 0.85))

bd >> play('V', sample=1, dur=1, lpf=200, lpr=0.25, amp=var([0.25, 0], [[32, 64], [64, 128]]))
ml >> play('r', rate=0.75, dur=[0.25, 0.25, 0.5], amp=expvar([0.5, 0.25], 1/3) * var([0, 1], [128, 64]))

bs >> sawbass(P[(0,2,4)],dur=1/4, amp=expvar([0,1],[1/4,1]), echo=2, vib=2, vibdepth=0.2, hpf=linvar([0.5,1],4)) # sexy


bl >> sawbass(dur=0.25, oct=[5, 5.5, 5.25, 5.15, 5, 5], hpf=expvar([150, 1000], [32, 32, 16, 8, 8]), hpr=expvar([0.25, 0.75], [16, [32, 32, 16, 8, 16, 32]]), amp=expvar([0, 0, 1.35, 1.25], 128)) # acid sound :DDD I dig it

#:DDDDDDDD sickcis# YO< CHECK OUT THE TRICK

Master().rate = 1 # :D WHOOOOOSH


# feel free to change my players

rs >> play('I', dur=var([8, 4, 2, 1, 2], [64, 32, 28, ]), amp=var([0.85, 0], [[128, 64], [64, 32]]))

#tm >> play('m', dur=0.25, amp=P[0, 0.25, 0.5, 0.15, 0.75, [0, 0.5], 0.25, 0.5] * var([0.75, 0], [64, 32]))

sn >> play('o', pan=PWhite(-0.75, 0.75), dur=0.25, amp=P[0.25, 0.15, [0.5, 0.25], 0.75, 0.25, 0.15, 0.35] * var([int(var([0, 1], [[128, 256], [64, 128]])), 1], [[28, 56], [4, 8]]))

sp >> soprano(
    [-10, -8, -9, -5, -11, -9],
    tremolo=expvar([0, 0, 2], [64, 64, 128]),
    hpf=expvar([1000, 650, 1250, 850], [32, 64]), hpr=expvar([0.75, 0.25], 128),
    dur=[[8, 16], 6, 4],
    amp=expvar([0, 1], 512)
)

sn >> snick(dur=expvar([0.15, 0.3], 32), room=1, mix=0.25, hpf=1500, hpr=0.25, amp=expvar([0.25, 1], 64))

sw >> swell(
    [-5, -3, -4, -6, -2],
    dur=[[16, 32], [16, 16, 4], [32, 8, 2]],
    slide=-0.15,
    tremolo=var([4, 8], [128, 64]),
    lpf=expvar([1500, 800], 64),
    amp=expvar([1, 0], [64, 128, 256])
)

sh >> play('s', pan=PWhite(-0.75, 0.75), dur=0.25, amp=P[PWhite(0, 1), PWhite(0.25, 1), [0.5, 0.75], 1] * expvar([0, 0.25, 1.5], [16, 16, [32, 64, 128]]))

bb >> play('$', dur=1/4, amp=linvar([0,1],1), pan=[-1,1])

dk >> play('[^.^]..', dur=1/3, lpf=sinvar([300, 2000], 32), amp=PWhite(0,1.25)*var([1,2],1))

ps >> pulse(dur=1/3, amp=0.5, striate=100)

# Defintely, have fun at work tomorrow
# alrightty
# ok I should really go sleep now, gonna work tomoorow
# awesome jam, was great fun
# thanks!
# I'll post the recordings in the group
#ICRASHEDIT D::
# RIIIIIIIIIIP

cb >> play('b',
    bend=[0, var([0, 0.25], [64, 32]), var([0, -0.15], [128, 64]), 0.25],
    dur=0.25,
    pan=PWhite(-1, 1),
    lpf=PWhite(200, 2000),
    lpr=expvar([0.25, 1], [128, 64, 32, 32]),
    amp=P[0.25, 0.15, 0.3, 0.5, 0.2] * var([0, 1.5], [[32, 64], [64, 128]])
) :DDDDOMFG


# AFK for a cigarette
#  alright
###################

print(SynthDefs)

print(Samples)

print(Attributes)
