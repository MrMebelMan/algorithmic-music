Clock.bpm = 180
Clock.meter = (3,4)

print(SynthDefs)
print(Samples)
print(Attributes)

###############################



help(Clock.meter)

var.brk = var([1, 0], [28, 4])

kd >> play('X', dur=[2, 1], delay=[0, 0.5], amp=1 * var.brk * var([1, 0], [[256, 128, 32], [64, 64, 32]]))
sn >> play('O', dur=2, delay=1, amp=kd.amp)

kd.dur=1
kd.delay=0
sn.dur=4
sn.delay=0

hh >> play('-', dur=0.5, amp=var([1.5, 0], [[64, 128], [32, 64, 128, 256]]))
h2 >> play('-', sample=2, dur=2, delay=[0, 0.75], amp=var([1, 0], [[128, 64], [64, 32, 32, 128, 128]]))

sh >> play('s', dur=0.5, amp=var([0, 1], [[[32, 128], 64], [64, 128]]))
s2 >> play('s', sample=2, dur=0.5, delay=1, amp=sh.amp)

cl >> play('*', dur=1, delay=[0, var([0, 0.5], 64), 0, var([0.5, 0], 64)], amp=var([1, 0], [64, 128, 32, 32, 32]))

var.tm_hpf = 120
var.tm_hpr = 0.25

tm >> play('m', dur=2, hpf=var.tm_hpf, hpr=var.tm_hpr, amp=1.5)
st >> play('m', dur=1, delay=0.5, hpf=var.tm_hpf, hpr=var.tm_hpr, amp=[var([0, 1], [256, 128]), 0, [var([1, 0], 64), 0], 0])

kk >> play('X', sample=1, dur=[4, 2], amp=1 * var.brk)
ke >> play('X', sample=0, dur=1, delay=0.75, amp=0.85 * var.brk)

ss >> play('S', dur=1, delay=var([0.5, 0.25], [64, 32]), amp=1 * var.brk)

oh >> play('-', sample=2, dur=1, delay=0.5, amp=var([1.5, 0], [[32, 64], [128, 256]]))

# let's maybe start over since BBScar joined?

Group(sh, s2, cl, tm, st, kk, ke, ss).stop()
Group(kd, sn, hh, h2, oh).stop()

sb >> sawbass(
    [0, var([-1, 0], 64), 0, var([-2, -1, 0], 32), 0],
    drive=expvar([0.1, 0.3], [64, [0, 2]]),
    sus=[[0.5, 0.25, 0.5, 0.25, 0.25], 0.25, 0.25, 0.25],
    dur=0.25,
    bend=[[-0.1, 0.25], 0, 0, 0],
    oct=[[5, 5, 5, 6], 5, 5, 6, 5.5, 5.5, 5, 5],
    amp=0.00
)


n0 >> play('|V2|', dur=PDur(var([3,5],[4,8]),11).rotate(3), lpf=8000, sus=2, lpr=0.45, coarse=0.15, chop=0.25, amp=sinvar([0.05,0.2],28)*var.brk, pan=[-1,1], drive=0.05).every(4, 'stutter', spin=64).every(16,'alt', '|V4|').stop()

o0 >> play('|u0|', dur=PDur(var([3,5],[4,8]),11).rotate(3), lpf=6500, lpr=0.25, amp=sinvar([0.05, 1], [128, 0]|var.sngvar)*var.brk, room=0.75, mix=0.25).every(4, 'offbeat') #.stop()

dl >> play('~', amp=expvar([0,1],[[255,128],var.sngvar])*var.brk, rate=expvar([0,2],[[255,128],[128,64]]), echo=0.002, pan=[-1,1], spin=64, striate=100, room=expvar([100,0.001],[[255,128],[128,64]]),mix=expvar([1,0.001],[[255,128],[128,64]])).every(128, 'stutter')


# I didn't see lol

# kek

d2 >> sinepad([3, 2, 0, -1], oct=4.4, lpf=0, dur=1, delay=0.5, amp=P[0, 0.5, [0, 0.5], 0] * var.brk)

# that is cool!


# nice
