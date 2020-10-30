# https:/soundcloud.com/kitty_clock/untold-tales

Scale.default = "minor"
Clock.bpm = 150
Root.default = var([0, 0.5], 32)
var.all_amp = var([1, 0], [[127, 63, 31, 31, 15, 15, 7, 7, 7, 7], 1])
var.hi_amp = var([0, 1], [96, 64, 32, 64])

sb >> sawbass(
    pshift=(0, 0.125), oct=expvar([5, 4.9], [1, 0]),
    sus=expvar([0.05, 0.85], [1, 0]), dur=var([0.25, 0.5], [28, 4]), room=var([1, 0], [28, 4]), formant=expvar([0, 1], [1, 0]),
    hpf=expvar([100, 250], [1, 0]) * var([1, 4], [28, 4]) * var([1, 4], [[6, 7, 28, 32, 3, 0], [2, 1, 4, 0, 1, 32]]),
    hpr=expvar([0.75, 0.25], [0, 1]),
    drive=expvar([0.025, 0.1, 0.120, 0.120], [32, 32, 0, 32]) * var([1, 0], [248, 8]),
    amp=var.all_amp * var([0, 1], 256) * 1.5 * expvar([0, 1, 1], [64, inf])
)
s2 >> sawbass(
    dur=0.5,
    sus=var([0.5, 0.25], 32),
    drive=1,
    formant=expvar([0.5, 1], [60, 4]),
    hpf=var([120, 220], [[3, 3, 3, 6], [1, 1, 1, 2]]), hpr=0.15,
    chop=0,
    amp=P[0.25, 1] * 0.35 * var([1, 0], 256) * 1.5
)
cl >> play('H', pan=expvar([-0.75, 0.75], 2), rate=var([1, 0.85, 0.5, 0.25], 32), tremolo=4, pshift=PRand(-1, 1), dur=0.25, room=0.5, lpf=expvar([2500, 2750], [16, 0]), lpr=0.25,
    amp=P[1, 1, 1, 1, 0, 1, 1, 1] * 1.5 * var([0, 1], [[128, 64], [256, 128, 64, 32]]) * expvar([0, 0.5, 0.5], 256)
)
yy >> play('y', pan=PWhite(-0.4, 0.4), sample=1, drive=0.5, room=0.75, dur=0.5, amp=P[1, 1, 0, 0, 0, 0, 1, 0] * var([2, 0], [128, 64, 128, 32, 64, 32]) * expvar([0, 1, 1], [64, inf]))
cb >> play('#', pan=expvar([-0.5, 0.5], 8), sample=(0, 1), rate=-0.5, hpf=expvar([500, 1000, 1000], 32), dur=var([2, 4], [128, 32]), room=1, coarse=var([4, 2], [[6, 6, 6, 28], [2, 2, 2, 4]]),
    amp=expvar([0, 1, 1], 128) * 1.75 * var.all_amp * var([1, 0], 4) * var([1, 0], [256, 128])
)
sh >> play('s', pan=PWhite(-0.75, 0.75), dur=PDur(4, 8), drive=expvar([0.15, 0.5], [1, 0]), amp=var.hi_amp * var.all_amp)
oh >> play('~', pan=PWhite(-0.5, 0.5), sample=2, dur=1, delay=0.5, amp=var([0, 2], [64, 64, 32, 32]) * var.hi_amp * var.all_amp * var([0, 1, 1], [128, inf]))
h2 >> play('-', pan=PWhite(-0.5, 0.5), sample=2, dur=1, delay=0.5, amp=2 * var.hi_amp * var.all_amp * var([0, 1, 1], [128, inf]))
o1 >> play('o', dur=var([2, 1], [56, 8]), delay=P[0, var([0, 0.5], 128)], amp=var([0, 1], [[64, 32], [128, 128, 64]]) * var.all_amp)
rc >> play('~', pan=PWhite(-0.5, 0.5), rate=0.5, dur=8, room=2, mix=0.5, hpf=2000, amp=4 * var.all_amp * var([0, 1, 1], [128, inf]))
dd >> play('I', sample=2, dur=[1] * 7 + [0.5, 0.5], lpf=7000, hpf=var([0, 800], [[[28, 64], 31, 128, 28, 63], [[4, 0], 1, 64, 4, 1]]),
    amp=var.all_amp * var([1, 0], [256, 64]) * expvar([0, 1, 1], [64, inf])
)
# dd.dur = [1] * 15 + [0.5, 0.5]
k1 >> play('X', sample=var([1, 2], [64, 128]), dur=dd.dur, hpf=dd.hpf,
    amp=var([2, 0], [[56, 64, 31, [28, 32]], [8, 0, 1, [4, 0]]]) * var.all_amp * dd.amp * var([1, 0.6], [64, 128]) * var([0, 1, 1], [96, inf])
)
k3 >> play('X', sample=5, dur=dd.dur, hpf=dd.hpf, drive=(0.05, 0.00), rate=1.05, sus=var([0.1, 0.25], 128), lpf=3500, lpr=0.85,
    amp=var([2, 0], [[56, 64, 31, [28, 32]], [8, 0, 1, [4, 0]]]) * var.all_amp * dd.amp * 0.15 * var([0, 1, 1], [96, inf]) * 0.5
) # custom sample

