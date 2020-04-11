Clock.set_time(0)

Clock.bpm = 300

# lololololol

# am back

# let's get weird

# ye

# my supercollider is freezing

# reconnect?

# same

tl >> play('n', sample=var([0, 1], [64, 32, 16, 16, 8, 8]), dur=[0.5, 0.25, 0.25], lpf=[5000, 4500, 4000], lpr=0.25, amp=var([0.75, 0], [64, 32, 128, 64]))

p1 >> pads(
    [-2, -5, var([-5, -4.5], [256, 128]), -5],
    oct=4,
    dur=1,
    hpf=var([0, 150], [28, 4]), hpr=0.25,
    lpf=expvar([300, 1000], [64, 0]),
    amp=expvar([0, 1], [128, 256])
)

p2 >> pads(0,
    oct=[4.5, [4.5, var([4.3, 4.5], 128)], 4.65, 4.5],
    dur=1, delay=0.5,
    bend=var([-0.5, -0.75], [28, 4]),
    echo=0.25, echotime=[0, 0, 0, 1],
    lpf=expvar([50, 1500], 256),
    amp=sinvar([0.05, 1], [128, 256, 64])
)

di >> play(
    'Weird Shit',
    sample=[var([2, 0, 1], 8), 1, var([0, 1, 2, 3, 4], 32), 2, 3],
    bend=P[-0.25, -0.5, 1, 1] * int(var([1, 0], [4, 2])),
    dur=[0.25, 1/8, 1/8, 1/8, 1/8, 0.25, 0.25],
    hpf=PWhite(300, 1000), hpr=expvar([0.2, 0.85], [64, 64, 32]),
    amp=[0.25, 0, 0.5, 0.75]
)

bh >> play('V', rate=[0.88, 0.9, 0.89, 0.9], drive=0.0, dur=1, lpf=expvar([250, 400], 32), lpr=0.35, amp=[3.5, 1.5])

ml >> play('r', rate=(0.5, 0.25, 1), sample=1, dur=0.5, hpf=expvar([200, 1000], 32), hpr=0.25, amp=0.75)

hj >> play('-', dur

sm >> play('O', rate=0.75, amp=P[0, 0.25, 0.15, 0.3] * 1.5)

# SICK

# right

jb >> jbass(dur=1, blur=1.05, delay=0.5, lpf=var([500, 700, 350, 800]), sus=1, tremolo=4, amp=1.25)
h1 >> play('-',
    dur=var([1, 0.25], [128, 256]),
    sample=1,
    rate=0.8,
    lpf=1500, lpr=0.25,
    amp=expvar([1, 0], 1/3)
)

oh >> play(':', dur=1, delay=0.5, amp=var([0.5, 0], [[256, 128, 64], [128, 64, 32]])).every(32, 'stutter', 2)

kd >> play('X', rate=[1, 0.98, 1, 0.95], sample=1, dur=1, lpf=180, lpr=0.35, amp=var([0.75, 0], [[256, 128, 64], [128, 64, 32]]) * var([1, 0], [[28, 56], [4, 8]]))
sk >> play('X', sample=0, dur=1, delay=0.5, lpf=150, amp=P[0, 1, 0, 0,  0, 1, 0, 0] * var([0.45, 0], [64, 64, 128, 128]) * (kd.amp * 1.25))

wd >> play('d', rate=P[0.9, 0.9, 0.9, PWhite(0.85, 0.9)] - var([0, 0.05, 0.1], 64), dur=var([0.5, 0.25], 128), amp=expvar([0, 0.1, 0.35], [64, 64, 128]) * var([1, 0], [[28, 56], [4, 8]]))

oh >> play('=', dur=0.25, amp=expvar([0, 0, 1], [[64, 128], [128, 64], 0])) # raising volume and then sudden drop

tm >> play('m', dur=2, lpf=expvar([200, 700], [64, 0]), lpr=0.25, amp=var([1, 0], [128, 64, 32, 16, 16, 32]))
t2 >> play('m',
     lpf=200, lpr=0.25,
    dur=1, delay=0.25,
    amp=P[1, 0, var([0, 1], [64, [32, 64]]), var([0, 0.5], [[128, 64], [256, 128]])] * tm.amp
)

nb >> play('z', sample=1, dur=[16, 64], sus=1, rate=-2, bend=-1, amp=0.35)

rs >> play('I', dur=2, sample=var([1, 0], 128), amp=var([0.25, 0], [[64, 128], [32, 64]]))

bu >> play('X',
    dur=1,
    sample=1,
    rate=-1,
    amp=P[1.2, var([0.5, 0], [32, 64]), var([0, 1], [128, 64, 32, 32]), 0] * var([0, 1], [[128, 64], [64, 128]])
)

bp >> blip(dur=0.25, lpf=PWhite(100, 1000), amp=P[0.15, 0.25, 0.5, 1] * expvar([0, 1], [128, 64, 32, 64]))

sr >> play('o',
    dur=0.25,
    lpf=PWhite(900, 3500),
    amp=P[
        PWhite(0.1, 1),
        0.25,
        [0.5, 0.75, 0.15],
        var([0.5, 0, 0.15], 32),
        PWhite(0.25, 0.5)
    ] * var([0, 1], [[28, 56], [4, 8]])
)


sh >> play('s',
    sample=[0, [0, 0, 0, 1], 0, 0],
    dur=0.25,
    pan=PWhite(-0.75, 0.75),
    amp=P[
        PWhite(0, 0.75),
        PWhite(0, 1),
        PWhite(0, 0.75),
        [0.25, 0.75]
    ] * var([1, 0], [[256, 128, 64], [128, 64, 32]])
)

es >> play('Q', dur=8, amp=var([0.25, 0], [[64, 128], [32, 128]]))

no >> noise(dur=1/4,
    lpf=PWhite(100, 500),
    striate=100,
    amp=1,
    blur=1/2,
    vib=var([0,1],1/4),
    echo=1,
    pan=[-1,1]
)

am >> ambi(dur=PDur(3,8), amp=var([1/2,1],1/4))

ki >> play('[xxx]..(.[v].)..',
    dur=var([1,1/2,1],8),
    amp=expvar([0,1],[32,64]),
    room=1,
    mix=0.3,
    delay=0.25,
    crush=4,
    bits=2,
    rate=2)

kt >> play('Kitty...',
    rate=[[-2, 1], [1, -2], [1, -1, -2], 1],
    room=expvar([0,1],4),
    mix=0.25,
    dur=0.25,
    amp=0.7)

# crash? I've been disconnected :<
# Yeahhhhh x.x

aa >> play('A([AA][AH])',
    echo=expvar([0,0.15],[2,4]),
    echotime=1,
    rate=[0.8,0.9,2,0.8],
    sample=[0,1,1,0,0,1])

da >> dab(dur=1/4,
    pan=[-0.25, 0, 0.25],
    amp=sinvar([1/8,1/2],1),
    striate=10,
    lpf=var(PWhite(1500, 5500)),
    echo=var([1, 1, 1, 0.5]),
    echotime=0.5
)

st >> sitar(
    PStrum([3, 4, 5]),
    bend=[-0.25, 0, 0, 0],
    dur=PStrum(var([2, 4, 6], 32)) / 2,
    echo=[0, 0.25], echotime=1,
    hpf=expvar([200, 1200], [32, 8, 8, 64]), hpr=expvar([0.25, 0.75], [32, 16]),
    amp=0.75,
)

# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# let it play, was nice



ph >> play('[yyyy][mm][dd]..',
    amp=expvar([1,0],[[16,32],[64,0]]),
    hpf=PWhite(300,600),
    echo=[0,0.2],
    rate=[0.8,0.6,0.4,0.2],
    crush=16,
    bend=-4
)

ex >> play('Noodl.[exe]',
    sample=[0, var([0, 1], [4, 8]), 0, var([0, 1, 2], [4, 16])],
    dur=[1/4, 1/8],
    formant=[[0.25, 0], [0, 0.5]],
    rate=[-2, 1, 1, 1],
    lpf=[1500, [2000, 500]], lpr=0.25,
    amp=sinvar([0.5,0.75],[[8, 8, 4, 4],16]),
    crush=[2, 0],
    bend=-2
)

# Kind of sounds like the crabman from futurama

# :

# hehehehe

# HPR should be between 0.15 and 1 :D

ta >> play('p[pp].', amp=linvar([0.25,2],[[64,128],0]), bend=var([-1,1],[[4,16],0]), dist=0.2)

########
# are you lagging?

# HMM

print(SynthDefs)

print(Attributes)

print(Samples)














##########################################################################
######################### ATTEMPT 2 ######################################
##########################################################################



Clock.set_time(0)

bd >> play('V',
    sample=0,
    dur=var([2, 1], [[64, 128], [32, 64]]),
    lpf=var([150, 200, 150, 300], [16, 32, 8, 8]),
    lpr=0.25,
    amp=2
)
b2 >> play('v', dur=0.25, lpf=200, lpr=0.3, amp=[0, 0.15, 0.25, 0.75])
ml >> play('r',
    rate=[0.25, 0.25, 0.35],
    dur=[0.5, 0.25, 0.25],
    hpf=expvar([100, 1000], [16, 16, 32, 32]),
    hpr=0.25,
    amp=expvar([0.75, 1.5], 128)
)
h1 >> play('S', room=1, mix=[0.25, 0], dur=var([1, 0.5], [128, 64]), delay=0.5, amp=var([0.95, 0], [[64, 128], [32, 64]]))
h2 >> play('-',
    sample=2,
    dur=0.25,
    lpf=PWhite(3500, 5500),
    amp=expvar(
        [int(var([0, 1], [[32, 64], 64])), 1],
        1/3
    )
)
tm >> play('M', rate=var([1, 0.95], [28, 4]), sample=1, dur=1, bend=[-0.15, -0.25], lpf=200, lpr=0.25, amp=2)
ft >> play('m', dur=0.25, lpf=var([250, 150, 350], 32), lpr=0.3, amp=P[0, 0.75, 0.25, 0.5, 0] * var([3, 2, 2.5], [32, 16, 16]))
sh >> play('s', sample=1, pan=PWhite(-1, 1), dur=0.25, lpf=8000, amp=PWhite(0, 1))
k2 >> play('X', delay=0.5, rate=var([-0.8, 0.8], 64), sample=2, lpf=150, lpr=0.25, amp=[1, 0.5, 0.25, 0.75])
ls >> sawbass(dur=1/8, hpf=expvar([200, 700], [32, 16]), hpr=expvar([0.65, 0.15, 0.15], [16, 32, 8]), amp=P[1, 0, 1, 1,  1, 1, 1, 0.5])


st >> play('q',
    rate=var([0.25,0.75],1),
    amp=var([0.25,0.5],[[1,4],[4,16],0]),
    dur=PDur(3,8),
    sample=[0,1,-1],
    mix=0.2)


fp >> play('[f.f]',
    amp=expvar([0.25,[1,4]],var([1,1/2,1])),
    hpf=PWhite(300,500),
    hpr=0.2,
    rate=[0.8,0.6],
    room=linvar([0,1],4),
    echo=0.5)

#

ra >> razz(dur=var([0.25,0.5],1/2), lpf=PWhite(300,600), amp=1/2)

ra.follow(ls)






##################

print(SynthDefs)

print(Attributes)

print(Samples)
