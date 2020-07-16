# https://soundcloud.com/kitty_clock/bahrovik

rhodes = SynthDef('rhodes')
rp1 = P[var([-1, -2, -3, -4], 4), var([0, 4], [56, 8, 28, 4, 64, 32]), -1, var([1, 2, 3, 4], 8)]
rp2 = rp1.reverse()
rp3 = P[var([-5, -2, -1, -3], [4, 8]), var([4, 1, 0, 2], [56, 8, 28, 4, 64, 32]), [var([2, 1, 0, -1], 32), 0.5], var([2, 1, 1, 0], [8, 4, 4])]
rp4 = P[var([0, -1, 1, -2], 16), 1, [3, 2.5], 0, var([-2, -1, 1.5, 0], 32), 1.5, var([-2, -3, -1, -0.5], 64), -3]
var.r_p1 = var([rp1, rp2, rp3, rp4], 128)
var.kg1_amp = var([1, 0], 512)
var.kg2_amp = var([0, 1], 512)

rd >> rhodes(
    sus=P[var([0.25, 0.5], [32, 64]), 0.5, [0.5, 0.75], var([0.25, 0.5], [32, 64])],
    dur=var([0.5, 0.25], [256, [128, 64]]), #[0.5] * 16 + [var([0.5, 0.25], [256, 128])] * 4,
    drive=(P[0, 0, 0, 0.1] * var([0, 1], [128, 64, 64, 32]), P[0.035, 0.15] * var([0, 0.5], [128, 64, 64, 32])),
    hpf=P[[1, var([1, 0.5], 8)], 0.95, [1, 0.85, var([1, 0.75, 0.5, 0.25], 32), 0.65], [var([0.8, 0.4], [28, 4]), 0.95]] * sinvar([100, [700, 1000]], [32, [0, 4]]),
    oct=var([[5, 6, 7], [4, 4.25], [5, [5, 5, 4.5, 4.75], 7.5], 4, 5, 5.25], [[16, 16, 32, 64, 64], 8]),
    amp=P[1, var([0, 1, 0.25, 1], [32, 64, 64, 128]) * 0, 1, P[1, var([0.5, 1], 128)],  [1 * 0, 1 * 0], 1 * 0, P[1, var([0, 1], [64, 128])], 0]
) + (var([[-5, -5, -4, -4, -2, -2, -4.5, -4.5], 0], [[56, 64], [8, 0], 31, 1, 32, 0, 32, 0]), var.r_p1)

tm >> play('X', sample=(0, 2), rate=expvar([0.9, 1, 0.95, 1.05, 0.93], [64, 0]), cut=[1, P[0.25, 0.3], 0.5], dur=[var([0.5, 1], [256, 128]), var([0.5, 1], [256, 128]), 1], lpf=5000, amp=P[1, [1, var([1, 0], [128, 64, 256, 128]), 1, var([0, 1], [128, 64])], 1] * var([0, 1], [128, 256, 64, 128, 32, 64]) * 0.9 * var.kg1_amp)
t2 >> play('m', sample=tm.sample + var([0, 1], [64, 64, 128, 128]), rate=var([0.9, 1, 0.95, 0.88, 0.9], 32), cut=tm.cut, dur=tm.dur, lpf=0, amp=var([1, 0], [56, 8, 28, 4, 32, 0, 31, 1, 31, 1]) * var([1, 0], [256, 128, 128, 64]) * tm.amp * var.kg1_amp)
t3 >> play('X', sample=1, dur=1, delay=-0.15, amp=P[0, 1, 0, 0] * tm.amp * var([0, 1], [[256, 64], 128, 128, 64, 128, 128, 64, [32, 128], 32, 64]))
h1 >> play('-', sample=2, room=1, mix=0.1, dur=1, delay=0.5, amp=var([0, 1], [[64, 128, 32], [128, 64, 128], 32, [64, 128, 32], 64, 64, 128, 128]))
h2 >> play('-', sample=1, dur=0.25, amp=P[1, 0.25, [0.5, 1], [0.3, 0.15]] * var([0, 1], [64, 128, 32, 128, 64, 64]) * expvar([0, 1.5], [64, 0, 32, 0, 32, 0]))
sp >> soprano(lpf=500, lpr=0.75, tremolo=4, oct=4.5, amp=expvar([0, 1], [64, 64, 64, 0]))
sh >> play('s', dur=0.25, sample=PRand([0, [1, 0, 2, 3], [2, 0, 0, 1], 3, [4, 2, 1, 1]], [3, 1, 2, 2, 1, 3]), pan=PWhite(-0.8, 0.8), lpf=2500, amp=P[1, 0.25, 1, 0.5] * expvar([0.35, 1], 1/3) * var([1, 0], [128, 128, 256, 64]))
r2 >> play('o', sample=0, dur=var([4, 2], [64, 32]), delay=0.5, amp=var([0, 0.5], [128, 64, 64, 128]) * kd.amp * var.kg1_amp)
rs >> play('I', sample=var([1, 0], 128), rate=var([0.75, 0.85, 0.9], 64), dur=var([4, 8, 2], [32, 64]), delay=var([0, 0.5], [[64, 128], 32]), amp=expvar([0, 0, 1.25, 1.5], [64, 64, 128, 0]))
sn >> play('u', sample=var([0, 1], [28, 4]), pan=PWhite(-0.75, 0.75), dur=0.25,
    amp=P[
        1, [var([0.85, 0.25, 1], 8), 1], [var([0.25, 1]), var([0.5, 1], 16), 0.75, var([0.75, 0.5, 1], 32)], var([1, 0.75])
    ] * expvar([0, 0, 1], [[128, 32, 64], 32, 0])
)
ee >> play('t', rate=expvar([1, 0.85], [64, 0]), pan=PWhite(-0.75, 0.75), sample=[[var([0, 1], 32), 1], 1], dur=0.25, amp=P[1, var([0, 1], [128, 64, [64, 128], 32]) * P[0.25, 0.25, 1, 0.75, 0.25, 0.5, 0.25, 0.5, 0.5], [0.5, 0, 1, [1, 0.25]], [0.75, 0, 0.15, 0.5]] * expvar([0, 0, 1.25, 1.25], [[128, 64, 128], [64, 32, 64], [128, 64, 256], 0]))
t4 >> play('X', dur=[2, 2, 2, var([2, 0.5], [128, 64]), var([2, 0.5], [128, 64])], sample=(0, 2), rate=var([1, 0.95, 0.93, 0.9], 32), amp=var.kg2_amp)
t5 >> play('I', dur=[2] * 7 + P[0.5, 0.5] * int(var([1, 2], [[64, 128], [32, 64]])), delay=1, amp=1.75 * t4.amp * var.kg2_amp)
rc >> play('~', sample=2, pan=PWhite(-0.5, 0.5), dur=0.25, amp=expvar([0, 0, 1.5], [[448, 192], 64, 0]) * var([1, 0], [31, 1]))
ss >> play('S', dur=1, delay=0.5, amp=var([0, 1.25], [256, 128, 128, 64, 256, 64])).every(32, 'stutter', 2)
ww >> play('w', dur=8, delay=0.5, sample=1, amp=var([0, 1], [128, 64, 256, 64, 128, 128, 256, 32, 256, 64]) * tm.amp)
ko >> play('H', sample=1, rate=1, bend=-0.5, dur=2, delay=var([1, 0.5], [128, 32]), amp=var.kg2_amp * expvar([0, 0, 1], [[64, 128], [32, 64], 0]))

e2 >> play('E', room=1, mix=0.15, rate=1, dur=1, lpf=700, amp=expvar([0, 0, 1, 1], [[[256, 512], 128, 64], [128, 64], [128, 64, 128], 0]))

bl >> dab(dur=0.25, sus=1, chop=2, lpf=P[var([200, 400]), var([300, 125], [32, 64]), 150, var([350, 500, 200, 150], 32)], amp=P[1, [0.75, 0.5, var([0, 0.75], [32, 64, 32, 128]), 0.25]] * expvar([0.75, 0.75, 1, 1], [[512, 256], [256, 128], 256, 0]) * 0.09)
bl.lpf = P[var([500, 1500, 2000, 300], 8), [1250, 2500, 500, 700], [var([2100, 1000, 2000, 500], [32, 16]), var([250, 1000], 4)], [[1500, 500, 200, 500], [1000, 2500], 1000, 300]] * expvar([0.5, 2], [0, 32])
tm.hpf = var([0, 600], [[32, 64, 128], 0, 31, 1, 28, 4])
tm.hpr = 0.25
t2.hpf = var([0, 600], [[32, 64, 128], 0, 31, 1, 28, 4])
t2.hpr = 0.25

print(Clock)

vv >> play('V', sample=var([0, 1], [28, 4, 56, 8, 31, 1, 31, 1]), dur=1, bend=0, rate=var([0.88, 91], [31, 1, 28, 4]) + var([0, 0.02, 0, 0.04], 32), amp=P[1, [0.9, 1.02]] * var([1, 0], [31, 1, 28, 4, 32, 0, [64, 56], [0, 8]])).every(64, 'stutter', 2)
vv.lpf = 1200
vv.hpf = 190
vv.rate = 0.8
vv.amp = 1

vv.lpf = 1000
vv.amp=P[1, [0.85, 1]] * 0.3
vv.hpf = 120
vv.hpr = 0.45
vv.sample = 2
tm.hpf = 800
t3.hpf = 800
t4.hpf = 800

s5 >> play('s', sample=0, dur=1, delay=0.5, amp=0.8).stop()

Group(r2, rs, ko, rc, ww, sn, t5, h1, ss, ee, sh, t3, sp, h2, rd t4).stop()
