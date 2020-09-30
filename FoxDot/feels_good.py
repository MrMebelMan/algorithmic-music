# https://soundcloud.com/kitty_clock/feels-good

Clock.bpm = 150

var.brk = var([1, 0], [28, 4, [31, 31, 31, 63], [1, 1, 1, 1]])

be >> bass(dur=var([2, 1], 64), sus=1, delay=0.5, tremolo=2, lpf=500, amp=P[0.9, 0] * var([1, 0, 0], [128, inf]))
xx >> play('X', rate=var([1, 2, 1.5], [64, 16, 32]), dur=1, sample=var([0, 1], [128, 256]), lpf=900, lpr=0.5, amp=1, amplify=1 * var.brk)
rs >> play('I', pan=PWhite(-0.1, 0.1), sample=1, hpf=500, lpf=1500, lpr=0.5, dur=var([2, 4], 128), delay=var([0, 0.5], 128), amp=1.25 * var([1, 0], [256, 128, 256, 64, 128, 32]))
r2 >> play('o', sample=var([0, 1], [128, 64, 128]), dur=var([[4, 2, 2, 2], 1], [[64, 128], [32, 64]]), delay=P[0, var([0.5, 0], 128)],
    amp=var([0, 0.3], [64, 32, 64, 128, 32, 128, 64, 64, [128, 256], [256, 128]])
)
h1 >> play('-', room=1, mix=0.25, dur=0.25, lpf=expvar([7000, 5000], [64, 0]), lpr=0.5,
    amp=P[
        P[var([0, 0.3], [32, 64]), var([0, 0.25], [32, 64]), [0.6, 0.35], 0.5],
        expvar([0, 0.1, 0.1], 128),
        [var([0.875, 0.95], [64, 128, 32, 32]), 1],
        0
    ] * var([0, 1], [32, 64, 32, 128, 64, 256, 128, 128, 128, 64])
)
h2 >> play('n', pan=linvar(-0.25, 0.25), room=h1.room, mix=h1.mix, dur=h1.dur, amp=h1.amp)
ss >> play('s', sus=0.5, pan=expvar([-0.5, 0.5], 4), dur=0.25, amp=expvar([0, 1], [4, 2, 3, 1, 1, 2, 3, 2, 1, 1]) * expvar([0, 1.25], [7, 1, 15, 1, 14, 2, 6, 2, 30, 2, 28, 4]))
rk >> play('X', dur=1, sample=2, rate=-1, lpf=500, bend=0.1, delay=0, amp=var([0, 1], [31, 1, 31, 1, 63, 1, 31, 1, 127, 1]) * var([0, 1, 1], [63, inf])).stop()
fr >> play(var(['d', 'l'], 256),
    dur=var([[0.5, 0.5, 0.5, 0.25], [0.25, 0.25, 0.25, 0.5]], [28, 4]),
    sample=2,
    rate=P[0.5, 0.5, PWhite(0.5, 0.6), 0.5],
    room=1, mix=PWhite(0, 0.2),
    pan=expvar([-0.5, 0.5], 16),
    lpf=expvar([5500, 2000], [64, [32, 0]]) - var([0, 200], [31, 1, 28, 4]), lpr=expvar([0.5, 0.75], [128, 0]),
    amp=Pvar([
        P[1, 0, 1, 0,  0.25, 0, 0, 0],
        P[1, 0.25, [1, 0.25], 1,  0.5, 0, 0, 0],
        P[1, 0.25, 1, 1,  0.5, 0, [0, 1], var([0, 1], [64, 32])],
        P[0.5, 1],
        P[0.75, [0.5, 0, 1, 1], 0.5, 1],
        P[[1, 0.25, 0.85, 1], [0.25, 0.75, 0.25, 0.25], 0.5, 0.75],
    ], [32, 64]) * var([0, 0.95], [32, 64, 32, 128, 64, 128, 64, 256, 32, 128])
)
vv >> play('v',
    rate=expvar([0.95, 1, 1, 1], [28, 4, 32, 0]) * P[expvar([1, 1.5], [64, 32, 64, 0]), 1.5, 1.25, 1.25],
    bend=P[0, 0, var([0, 0.15], [64, 128]), var([0, 0.15, 0.25], [64, 128, 256])],
    dur=0.25,
    sus=P[0.25, 0.1, 0.1, 0.1],
    amp=P[
        expvar([0.1, 0.25, 0.25], 128), var([0.25, 0.15], [64, 32, 64]), var([0.5, 0.65], [28, 4]), [expvar([0, 0.75, 0.75], [16, [32, 64], 0]), 0.75, 0.75, 0.75]
    ] * var.brk * 1.1 * var([0, 1], 256) * expvar([0, 0, 1, 1], [120, 8, inf])
)

v2 >> play('v', sample=1, slide=var([0, 0.25], [56, 8]), bend=var([0, 0.25, 0.15, 0.05], [32, 64, 64]), dur=0.25, hpf=80, hpr=expvar([0.5, 0.25, 0.25], [4, 32, 28]),
    amp=expvar([1, 4], [1, 0]) * var([0, 0], 256) * var.brk
)

cl >> play('H', sample=1, dur=[var([4, 2], [64, 128, 64, 256])] * 31 + [1, 1, 1, 1], delay=1, amp=var([0, 0.35], [[128, 64, 128, 256], 256]))
s3 >> play('S', pan=PWhite(-0.5, 0.5), dur=0.5, amp=P[0.25, 1] * var([0, 1], [56, 8, 28, 4, 32, 16, 64, 32, 6, 2, 15, 1]) * var([1, 0], [[256, 128, 64], [64, 128]]))
kk >> play('x', dur=1, sample=1, amp=var([0, 2], [28, 4, 31, 1]) * expvar([0, 1, 1], [128, 128, 0]) * var([1, 0], [128, [32, 64]]))
sb >> sawbass(dur=4, sus=4, tremolo=4, delay=0.5, hpf=200, hpr=0.25, amp=expvar([1.25, 0], [256, 0]) * var([0, 1], [256, 512]))
v8 >> play('V', rate=var([1, 1.1], [32, 64, 64, 128]), bend=var([0, -0.1], [28, 4, 31, 1]), sample=8, dur=1, lpf=var([480, 800], [28, 4, 31, 1]), lpr=0.5,
    amp=expvar([0, 0, 1, 1], [28, 4, 120, 8]) * var([0, 1, 1], [128, inf])
)
s8 >> play('s', sample=2, cut=[2, 1, 0.5, 0.75], dur=0.25, amp=P[1, 0, 0.5, 0.75] * var([0, 1], [256, 128, 64, 128, 32, 64, 64, 32]))
oh >> play('n', pan=PWhite(-0.4, 0.4), dur=1, delay=0.5, amp=var([0, 1], [128, 64, 64, 128, 32, 128, 64, 256]))

print(Clock.beat / Clock.bpm)