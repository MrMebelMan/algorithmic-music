Clock.set_time(0)

Clock.bpm = 133

print(Samples)

print(SynthDefs)

print(Attributes)

####################################3


Master().hpf = var([0, 800, 600, 400, 200], [[32, 64], [4, 2], [4, 2], [4, 2], [4, 2]])

Master().hpr = 0.25


kd >> play('X', dur=1, sample=var([1, 2], [256, 128]), lpf=0, amp=var([1.25, 0], [[28, 56], [4, 8]]))

sk >> play('X',
    dur=1,
    sample=kd.sample,
    delay=0.5,
    lpf=1000,
    amp=P[
        0, var([1, 0], [[256, 128, 64, 32], [64, 32, 32]]), 0, var([0, 1], [128, 32, 64, 32, 32]),
        0, 1, var([0, 1], [64, 128, 128]), 0
    ] * kd.amp * 0.85
).stop()

@next_bar
def stop():
    #Group(rr, os, sn, rc).stop()
    #Group(h1, h2, tm).stop()
    
Master().amp = 0.00

# gotta go

# thanks!

h1 >> play('=', cut=expvar([0.25, 1.5], [[32, 32, 64], 0]), dur=1, delay=0.5, amp=2.5)

h2 >> play('-', sample=var([2, 1], [128, 64]), dur=0.25, amp=expvar([1, 0.1], 1/3) * var([0, 1], [[32, 64], 64, 32, [128, 32], 64]))

rc >> play(Pvar('-~', 32), sample=var([0, 1], 128), dur=0.5, hpf=expvar([200, 3000], [[32, 64], 0]), hpr=0.25, amp=P[1, 0.9])

sn >> play('I', dur=0.25, amp=P[1, [1, var([0, 1], 64)], var([1, 0], [64, 32, 32]), 1, [0, 1], 1, var([1, 0], [64, [32, 64]]), 1] * expvar([0, 0, 1, 1], [64, 32, 32, [32, 0]]))

tm >> play('m', sample=0, dur=0.25, lpf=500, amp=P[[1, 0.5], 0.5, 0.75, 1, 0.25, 0.5] * var([1.5, 0], [[128, 64], [64, 32]]))

os >> play('O', dur=2, sample=0, lpf=4500, amp=var([0.5, 0], [64, 32, [32, 64], [128, 64, 32], [32, 64, 128], 64]))

rr >> play('r',
    pan=PWhite(-0.5, 0.5),
    sample=0,
    dur=[0.5, 0.25, 0.25],
    lpf=expvar([2500, 1500], [32, 0]), lpr=expvar([0.25, 0.5], 16),
    amp=var([1, 0], [[64, 128, 32, [32, 64]], [32, 64, 32, [64, 32]]])
)


@next_bar
def build():
    k0 >> play(P['V'], amp=P[1, 0.85] * expvar([0,1],[64,0]), sus=2, lpf=[1000, 1500], chop=0.75, lpr=0.3, echo=1)
    
k0.stop()

s0 >> sinepad(P[0,[2,4],2,[4,6]].shuffle(2), 
    amp=0.15, hpf=600, hpr=0.3, shape=1, 
    dur=0.25, cut=1, chop=0.5, 
    drive=var([0.05,0],[[128,0],[32,0]]), 
    pan=[-1,1], echo=0.02).stop()

@next_bar
def weird():
    r0 >> rave(P[0,[2,5]].stutter(2),dur=0.25, amp=0.5, drive=0.05, echo=0.05, room=1)

@next_bar
def action1():
    r0.stop()

Scale.default='minor'

hh >> play('=', dur=0.25, amp=expvar([0, 1], [32, 0])).stop()

#SEEE ya!!!
