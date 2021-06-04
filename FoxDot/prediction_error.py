# https://soundcloud.com/kitty_clock/prediction-error

Clock.bpm = 120

var.amp2 = 1
f2 >> play('U', sample=34, rate=expvar([0.1, 0.1, 0.3], 128), bend=PWhite(0, 1.5), comp=0, lpf=PWhite(2000, 6000), lpr=0.2, hpf=160, hpr=0.5, sus=P[0.08, 0.04], dur=0.25, amp=P[0.5, [0.4, 0.1]] * var.amp2)
do >> play('do', sample=8, rate=0.2, lpf=P[2200, 5000, 2350, 1500] * 4, lpr=0.5, dur=0.125, amp=P[expvar([0.1, 0.15], 16), 0.05] * var.amp2)
vv >> play('[vv]', rate=1, dur=0.5, comp=[2, 0], bend=0.25, amp=0.8 * var.amp2)
hh >> play('t', sample=32, krush=2, rate=PWhite(0.25, 0.85) * PWhite(0.2, 0.35), sus=0.01, bend=PWhite(0.5, 2) * 0, lpf=expvar([2500, 1000], [1, 0]), lpr=expvar([0.5, 0.25], 8), echo=P[0, [0.125, 0], [0, 0.125, 0, 0], 0] * 0, dur=0.25, amp=0.2 * P[1, 1, [0.5, 0.8]] * var.amp2)
kr >> play('n', rate=-2, lpf=0, lpr=0.25, sample=10, sus=0.05, dur=0.25, pan=PWhite(-0.5, 0.5), amp=0.05 * P[1, 1, PWhite(0, 0.3)] * expvar([0, 1], 64) * var.amp2)
s2 >> play('{sn.}(nsn..nn).[ss](s..n)(ss(.s))', rate=PWhite(-0.75, 0.75), dur=PDur([1, 6], 8) * 4, sus=0.05, lpf=PWhite(1000, 3000), room=0.5, echo=0.25, mix=0.2, amp=0.3 * var.amp2)

var.amp1 = 0
fa >> triwave(P[P**(var([-15, -8], 8), 2, -5, -0.5), -5], oct=4, dur=1, sus=0.25, lpf=expvar([1, 8], 16) * P[expvar([300, 1200], 16), linvar([1300, 350], 32), linvar([350, 1200], 64)], lpr=0.5, chop=1, amp=var([0.15, 0], 16) * var.amp1)
ff >> play('uuup', sample=12, rate=0.15, bend=PWhite(0, 1.5), lpf=PWhite(2000, 6000), lpr=0.8, hpf=expvar([0, 0, 200], [0.5, 0.5, 0]), sus=0.05, dur=0.25, amp=0.5 * var.amp1)
ff.rate = P[0.15, 0.145, 0.135, 0.15]
dd >> play('d', rate=PWhite(0.25, 0.85), bend=PWhite(0.5, 2), lpf=expvar([2500, 1000], [1, 0]), lpr=expvar([0.5, 0.25], 8), echo=P[[0.125, 0], 0, 0, 0], dur=0.25, amp=0.2 * var.amp1)
sh >> play('s', sample=17, dur=0.25, delay=0.5, echo=0.25, lpf=3000, spin=0.25, amp=0.3 * PWhite(-1, 1) * var.amp1)
so >> play('{sn}nn:-', sample=PRand(9), dur=PDur([1, 6], 8), lpf=2000, lpr=0.25, room=0.7, mix=0.2, amp=0.35 * var.amp1)
e1 >> play('e', rate=0.3, lpf=380, lpr=0.5, sample=20, chop=16, dur=4, amp=0.35 * var.amp1)
v2 >> play('[vv]', rate=1, dur=0.5, comp=[2, 0], bend=0.05, amp=0.75 * var.amp1 * 0.8)
