Clock.set_time(0)

Clock.bpm = 150


# sound?

print(Samples)


print(SynthDefs)

db >> dub(
    bend=[-0.25, 0.25, 0, 0],
    lpf=expvar([1000, 100], 32),
    lpr=expvar([0.35, 0.85], [16, 32]),
    tremolo=var([0, 4, 8], [64, 32, 16]),
    dur=0.25,
    delay=0,
    amp=P[0.15, 1, 1, 0.85] * expvar([0.25, 1], 128) * var([1, 0], [256, [512, 256]])
) #.stop()

# lel

Master().hpf = var([0, 200, 250, 350], [128, [8, 16], [4, 8], [4, 8]])
Master().hpr = 0.25

Master().lpf = 0  # expvar([2000, 200], [32, 0])



kd >> play(P['X'].shuffle(2),
    rate=var([1.25, 1, 0.95, 0.9], [64, 32, 32, 16, 8, 8]), drive=0.1,
    sample=var([2, 1], [[64, 128], [32, 64]]),
    dur=[0.25, 0.25, 0.5], lpf=var([0, 200, 400], [64, 32, 32]), lpr=0.15,
    amp=var([4, 2], [[28, 56], [4, 8]]) * var([1, 0], [256, [128, 256]]),
    pan=PWhite(-1,1),
    bend=[[-0.25, 0], [0, 0.15], 0, 0],
    delay=[0.25, 0.5, 0, 0.5]
).every([8, 16], 'stutter', 2)

kd.amp=expvar([0, 1], 128)

je >> play('{-:oIr}[:-]', pan=PWhite(-0.75, 0.75), dur=0.25, hpf=[150, 500, 200, 750], hpr=expvar([0.25, 1], [16, 32]), amp=P[1, 1.25] * var([0, 1], [128, 128, 256]))

bd >> play('(V^Vx)', sample=var([0, 1, 0, 2], [64, 64, 32, [64, 32]]), rate=var([0.9, 1], [32, 64, 64]), dur=0.25, lpf=var([400, 300, 200], 64), amp=P[0.5, 0.25] * expvar([0, 1], [126, 64, 64])).every([8, 16], 'stutter', 2)

sq >> play('z', sample=2, dur=0.25, lpf=expvar([1000, 2500], 64), amp=[0.25, 0.85]).stop()


Group(kd, je, bd, sq).stop()

s9 >> play('V', dur=1, delay=0.5, lpf=200, amp=P[0.5, 0.25])

me >> play('e', dur=[0.5, 0.25, 0.25], lpf=[4000, 3000, 4500], amp=var([0.85, 0], [[28, 56], [4, 8]]))

Group(kd, bd).stop()

ss >> play('O', room=1, mix=0.25, rate=0.8, dur=1, amp=0.45).every(8, 'stutter', 2)
h1 >> play('[-s]', sample=(0, 1), dur=1, delay=0.5, amp=var([2, 0], [[64, 32, 128], [32, 32, 64]]))

Group(s9, me, ss, h1).stop()

h2 >> play('-',
    rate=var([1, 0.95, 0.9], [64, 32, 128, 128]),
    sample=var([0, 1, 2], [64, 32, [32, 16, 16, 8, 8]]),
    dur=0.25,
    amp=expvar([1, 0.25], 1/3) * var([0, 1], [[64, 128], [128, 64]])
)

rs >> play('I', dur=var([2, 1, 4, 8], [60, 4, 32, 64]), amp=var([0.95, 0], [64, 32]))
sk >> play('v', dur=0.25, lpf=200, amp=P[1, [0.8, 0.9], 1, 0.5] * 0.75)
tm >> play('r', dur=1, delay=0.5, amp=var([0, 1.25], [32, 16, [32, 128], 64, 64]))
jj >> play('lol^kek', dur=0.25, hpf=linvar([200, 1500], [16, 16, 8, 8]), hpr=expvar([0.25, 0.5], 32), amp=P[0.25, 0.15, 0.3] * 2.5)

bl >> blip(-5, dur=1, delay=0.5, tremolo=2, amp=expvar([1, 4], [128, 256])).stop()
la >> donk([2, -2, 5, 1, 0, 0, 3], oct=[5, 5.25, 4.98, 5, 5], dur=PStrum([3, 4]) / 2, lpf=1500, amp=var([1.5, 0], [64, 32, 32])).stop()
pd >> bug(dur=1, oct=4.7, amp=var([1.15, 0], [128, 64]), hpf=expvar([200, 2000], [32, 64, 64]), hpr=0.25).stop()
p2 >> bug(dur=1, oct=4.5, sus=0.25, delay=0.5, amp=P[0, 1, [0, 1], 0] * pd.amp).stop()
oh >> play('=', dur=0.25, amp=expvar([1, 0, 0], [0, [[32, 64, 128], 64], [32, 64]]))

ke >> play('X', sample=2, dur=1, rate=0.95, lpf=[200, 150, 125, 100], amp=[1.5, 1]).every(64, 'stutter', 2)

# EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEe


Group(sk, oh, ba, wr).stop()

# :D

Group(rs, tm, jj).stop()

# }:D
ba >> jbass(dur=2, sus=0.5, amp=expvar([0,1],4), room=linvar([0.1,0.5],4), lpf=[1500, 3000], lpr=0.2)


wr >> play('weirdo',
    rate=[[1, 0.95], var([1, -1], [[4, 16, 8], [8, 2]]), [0.85, 0.95, 1], 1, [1, 1.25]],
    dur=[0.25, 0.25, [0.25, 0.25, 1/8], [0.25, 0.25, 1/8]],
    bend=[[-0.25, 0.5], -0.5],
    lpf=[expvar([200, 2000], [32, 16, 16]), 500, var([1500, 200], [32, 4, 8]), var([200, 400, 600, 800, 1000], [32, 16])],
    lpr=expvar([0.25, 1], 64),
    tremolo=[[2, 0, 0, 0], [0, 4], 0, [0, 2, 0, 4]],
    fmod=expvar([0.25, 1, 0], 32),
    vib=[0.15, 0, [0, 2], 0, 0], vibdepth=0.25,
    amp=[0.15, 0.1, 0.15, expvar([0.05, 0.15], 32)]
)

lo >> play('lonely', rate=[[-1, 1], 1, 1, 1], sample=[0, 1, [1, 0]], dur=[1, 0.25, [0.25, 0.5], [0.75, 0.25]], amp=0.5)


print(Attributes)


#kd >> play('X', dur=1, lpf=300, amp=var([1, 0], [[64, 128], [128, 256, 512]]))
#k2 >> play('X', dur=1, delay=0.5, lpf=200, amp=P[0.5, var([1, 0], 128), var([0, 0.5], [32, 16, 16]), 1] * kd.amp)
#h1 >> play('-', dur=1, delay=0.5, amp=var([1, 0], [[64, 32, 128], [32, 32, 64]]))
#cb >> play('T', rate=0.7, dur=4, lpf=200, lpr=0.5, amp=expvar([0, 0.75], [[128, 64], [64, 128]]))
#br >> play('v', dur=0.25, lpf=200, amp=P[0.25, 0.15, 0.65, 0.35, 0.15] * var([0.5, 0.3, 0.5, 0.1], [32, 8, 32, 16#, 64]))
#sn >> play('o', room=1, mix=0.3, dur=2, amp=var([0.3, 0], [[64, 128, 256], [32, 64, 128]]))

rv >> rave(
    [-7, [5, 4, 3], 2, 1, 0, 0, 4],
    dur=0.25,
    oct=[4.8, 5, 4.8],
    slide=[expvar([0, 1], 16), [0, 0, 1]],
    bend=[[-0.25, 0], 0, 0, 0],
    lpf=[2500, 3000, 1500, [500, 2500, 5000]],
    hpf=[200, [300, 700]] * expvar([1, 1.5], 32),
    hpr=expvar([0.25, 0.75], 8),
    amp=[
        expvar([0.3, 0.7, 0.65], [32, 64, 128]) * var([1, 0], [[128, 64], [32, 32, 128, 64]]),
        expvar([0.15, 0.5], 64),
        0.3
    ]
)


tp >> play("[x x][: x]", amp=sinvar([0.1,-0.1],[1,3]), echo=0.75, sus=0.75, lpf=var([150,300],2), lpr=0.1, striate=3)
t2 >> play("[x x][: x]( ^):", amp=sinvar([0.1,-0.1],[1,3]), echo=0.75, sus=0.75, striate=2, bend=-1, dur=var([0,2,4],[1/4,1/4,1/4]))

# hehe
# <3

Group(tp,t2).stop()

bg >> bug(amp=0.2)

bg.stop()

o8 >> play('[m m][: :x]', amp=linvar([0,0.25],[64,128]), striate=2, lpf=expvar([1500,3000],[32,64]))

o8.stop()

p0 >> play('p0', amp=var([0.25,0.5],32), striate=2)
rn >> play('[rn]', amp=linvar([0.25,0.5],24), striate=2)

Group(p0,rn).amp=0

sb >> sawbass(dur=[1/3,1/3,1/3,1/4,1/4,1/2,1/2], amp=[0.75, 0.25, 0.25, 0.75,0.25,0.75,0.75], echo=0.2, sus=0, lpf=var([150,300],[32,64]))

rb >> play('N(ood)l.[exe] vs. KittyClock',
    sample=[var([0, 1, 2, 3, 4], [8, 16]), var([1, 0, 2], 32), [2, 0, 1]],
    rate=[-1, 1, 0.85, 1],
    dur=[0.25, [0.5, 0.25], 0.25],
    lpf=[PWhite(500, 2000), 2000],
    amp=0.5
)


kl >> play(

r2 >> play('[t tt][: ]', amp=linvar([0.25,0.5], 4), lpf=var([150,300],16))

r2.stop()

print(Samples)

print(SynthDefs)
