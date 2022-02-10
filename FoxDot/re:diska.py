# https://soundcloud.com/kitty_clock/rediska

Clock.bpm = 120
Clock.clear()
Clock.set_time(0)

# 4/4
k8 >> play(('X', 'V'), sample=(7, 2 + 4), rate=0.75, dur=var([2, 1], [384, 256]), krush=2, amp=0.5 * var([0, 1], [256, 384]) * var([1, 0], [28, 4, 31, 1])) # start with dur=2, kd amp=p2 and kd.amplify = 1 * var([1, 0], [4, 4, 4, 4, 2, 2, 2, 2])
# k8.amplify = 1
# k8.amp = 0.5
# k8.dur=2

# kick
kd >> play(('X', 'V'), sample=(7, 2 + 4), dur=PDur([3, 5], 8), krush=2, amp=P[1, [0, 0, 0, [0, 1]], [0, 1, 0, 0], 0, 1, 0, P[0, 1], [1, 0, 0, 0]] * 0.5)
kd.amplify = Pvar([P[1], var([1, 0], [3, 1])], [256, 128, 0, 256])
p1 = P[1, P[0, 0, 1, 0], P[1, 0, 0, 0], 0, 1, 0, 0, 0] * 0.5
p2 = P[1, 0, 1, 0, 1, 0, P[0, 0, 0, 1], 0] * 0.5
p3 = P[1, 0, [0, 1], [1, 0], 1, 0, 0, 1] * 0.5
p4 = P[1, 1, 1, 0, P[[1, 1, 1, 0], 1], 0, 0, 0] * 0.5
p5 = P[1, 0, P[0, 1], [1, 0], [1, 0], P[0, 0, 0, 0, P[0, 1, 0]], 0, [1, 0]] * 0.5
# kd.amplify = 1
kd.amp = Pvar([
    p5, p1, p5, p2, p4, p4, p2, p1, p3, p1, p3, p2,
    p4, p2, p4, p5, p1, p2, p1, p2, p5, p3, p5, p1,
], [32] * 4 + [16] * 8 + [8] * 16) * var([1, 0], [28, 4, 31, 1]) # * var([1, 0, 0, 0], 4)
Master().hpf = 0
#sm >> play(('O', 'u'), sample=(13, 16), dur=PDur([3, 5], 8), delay=0.25, room=0.5, mix=expvar([0.2, 0], 32), echo=P[0, var([0, [0.5, 0.25]], [14, 2])], amp=P[0, var([1, 0], [192, 64, 128, 128]), 0, 0, 0, 1, 0, 0] * 0.9)

# snare
sm >> play(('O', 'u'), sample=(13, 16), dur=PDur([3, 5], 8), delay=0.25, room=0.5, mix=expvar([0.2, 0], 32), echo=P[0, var([0, [0.5, 0.25]], [14, 2])],
    amp=P[0, var([1, 0], [320, 64, 128, 128]), 0, 0, 0, 1, 0, 0] * 0.9
)

# bass
fs >> filthysaw(dur=PDur([3, 5], 8), oct=3, cf=expvar([5500, 500], 16), vib=1, vibdepth=0.25, room=1, mix=0.15, sus=0.75, lpf=500, amp=P[0, 0, 0, 0, 0, 0, 0, 1] * 0.8) # TODO: remove lpf?
f2 >> filthysaw(dur=PDur([3, 5], 8), oct=3, cf=P[500, 200, 1500], t_bd=expvar([0.1, 0.95], 8), vib=0, vibdepth=0.5, room=0.7, mix=0.1, sus=0.25, echo=P[0.25, [0.5, 0.25]], amp=P[0, 0, 0, 1, 0, 1, 0, 0] * 0.7)
f3 >> filthysaw(dur=PDur([3, 5], 8), oct=3, cf=var([200, 500], [15, 1, 56, 8]), t_sd=1, lpf=expvar([800, 1400], [[16, 32, 64], 0]), lpr=expvar([1, 0.2], 32), amp=0.55)
cl >> cluster(dur=0.25, mult=expvar([5, 2], 3), pstep=var([0.15, 0.8], [3, 1]), oct=4, rel=0.01, blur=2, lpf=expvar([1500, 600], 8), lpr=0.3, para1=expvar([4, 7], [4, 0]), amp=2.25 * PWhite(0.25, 1) * expvar([0, 1, 1], 64))

# highs
var.hi_amp = var([1, 0], [128, 64, 64, 32, 256, 128]) * var([1, 0], [31, 1, 32, 0, 28, 4, 32, 0, 56, 8, 64, 0])
tn >> play('nnn.', sample=P[2, 2, 3, -1], dur=0.25, pan=PWhite(-0.5, 0.5) * expvar([1, 0], 8), room=1, mix=expvar([0.2, 0.05], 32), lpf=expvar([4000, 1500, 1500], [64, 32, 32]), amp=expvar([0.75, 1, 1], [1, 0, 0]) * 1 * P[1, 1, 1, 1, 1, expvar([0, 1], 16), expvar([0, 1], 16), 1] * var.hi_amp * var([0, 1], 2))
sk >> play('t', sample=2, dur=0.5, pan=expvar([-0.5, 0.5], 3), amp=expvar([0.9, 0.3], [16, 0]) * P[0, 0, 0.5, 1, 0, 0.5, 0.75, 1,  1, 0.5, 0, 0,  0, 0.25, 0.5, 0.75] * var.hi_amp * var([0, 1], 4))
nn >> play('n', sample=4, dur=0.25, room=0.5, mix=0.1, amp=1.5 * var([0, 1], [3, 1]) * var([1, 0], [64, 32, 32, 16]) * expvar([0, 1, 1], [128, 128, 0]) * var.hi_amp)
ss >> play('s', sample=P[0, 1] * 2, dur=PDur([5, 3], 8), echo=P[0.25, 0, 0], amp=0.8 * var([0, 1], [6, 2]) * expvar([1, 0], [64, 64, 0]) * var.hi_amp)
di >> play('uI{o.}{u.}', sample=PRand([4, 9], 0.25), dur=PDur(3, 8) * 2, pan=PWhite(-0.75, 0.75), amp=0.5 * expvar([0, 1], 128) * var.hi_amp)
db >> dblbass(oct=4, dur=0.5, fmod=1, crv=-2, vel=P[1.5, 1.5, 2, 3, 2, 2, 1.75, 1.5], lpf=expvar([500, 150], 32), lpr=expvar([0.1, 0.5], 16), atk=P[0.2, 0.05, 0.5, 0.01], amp=expvar([0.25, 0.75], 32) * 0.75 * expvar([0, [1, 1, 0]], 128))
cs >> cs80lead(oct=6, dur=1, delay=0.5, cutoff=200, dtune=0.35, frel=0.5, amp=P[0, 0, [0, 1], 0] * 1 * expvar([0, 1, 1], 128))
io >> play('%', rate=PWhite(0.5, 2), sample=1, sus=2, dur=16, delay=[0.85, 0.85, 0.5], room=1, mix=0.3, amp=1)
ll >> play('l', sample=4, dur=1.5, pan=PWhite(-0.75, 0.75), amp=1.3 * expvar([0, 0.5, 1, 1], 64) * PWhite(0, 1))
cp >> play('H', sample=1, dur=1, delay=0.5, lpf=PWhite(2500, 4500), room=0.75, mix=0.25, amp=P[0, 0, [0, 1], 0] * 1.25 * var([0, 1], [32, 64, 32, 128, 64, 128]))
sj >> play('*', sample=var([11, 25], 32), dur=0.25, sus=0.01, lpf=expvar([6000, 1000], [64, 0]), pan=PWhite(-0.5, 0.5), room=1, mix=0.15, amp=P[PWhite(0.05, 0.3), PWhite(0.15, 0.25), 1, 0.15] * 1.85 * var([0, 1], [64, 128, 128, 256, 32, 64]) * 0)
Group(fs, f2, f3, cl, tn, sk, nn, ss, di, db, cs, io, ll, cp, sj, sm).amplify = expvar([0, 1, 1], [64, inf])

Group(fs, f2, f3, cl, tn, sk, nn, ss, di, db, cs, io, ll, cp, sj, sm, k8, kd).amplify = expvar([1, 0, 0], [64, inf], start=Clock.now())

print(k8.amplify)

#Group(fs, f2, f3).stop()

Master().hpf = 350
Master().hpr = 0.5

Group(nn, ss, io, di, ll, cp, sj).stop()

Group(nn, ss).stop()

#va >> alva(dur=PDur([3, 5], 8), lpf=7000, oct=[3, 4, 5], fmod=2, room=0.75, mix=0.1, amp=P[PWhite(0, 0.5), 0, 0.25, [0, 0, 0, 1],  0.5, 1, 0.1, 0.2] * 0.7 * var([0, 1], [24, 8]) * 0)
#tt >> play('t', sample=9, dur=0.25, lpf=expvar([1000, 7000], [128, 64, 32]), lpr=0.8, pan=PWhite(-0.5, 0.5) * expvar([0, 1], 16), amp=P[0.2, PWhite(0.1, 0.3), 1, PWhite(0.1, 0.5)] * expvar([0, 0, 1, 1], 128))

# Master().hpf = var([0, 350, 0], [28, 3, 1,  92, 0, 0,  56, 7, 1,  28, 3, 1,  128, 15, 1]) # FIXME: this shit is off, possibly because of PDur

###########################
#      LIVE TWEAKS        #
###########################

kd.amplify = var([1, 0, 0, 0], 4)

Master().hpf = 0

kd.amplify = var([1, 0], 4)

kd.amplify = 1

Master().hpf = 0

#kd.amplify = Pvar([P[1], var([1, 0], 4)], [128, 128, 0, 256])

kd.stop()

Master().hpr = 0.5
Master().hpf = 0
k8.amplify = 0

Master().hpf = 350


kd.amp = p3
Master().hpf = 0

p7 = P[1, 1, 1, 0, 0, 0, 0, 0] * 0.5

# nice
p7 = P[1, 1, 1, 0, 0, 0, 0, 0] * 0.5
kd.amp = p7
sm.amp = P[0, 0, 0, 0, 0, 1, 0, 0]
Master().hpf = 0

Master().hpf = 350
Master().hpr = 0.5

Master().hpf = 0

print(fs.amplify)


Master().hpf = 0

Group(kd, k8, sm).stop()

sm.amp = P[0, 0, 0, 0, 0, 1, 0, 0]

Master().hpf = 0

kd.amplify = 0
kd.amp = 0

