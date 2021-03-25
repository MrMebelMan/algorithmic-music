# https://soundcloud.com/kitty_clock/torn-diaphragm

Clock.bpm = 133

var.hpf = expvar([0, 0, 800, 180, 120], [[48, [112, 96]], 0, [14, [14, 28]], [2, [2, 4]], 0])

vv >> play('[vv]',
    rate=P[-1, var([0.9, -1], [256, 128])] - var([0, 0.05], [256, 128]),
    bend=P[0, var([0, -0.1], 16) * var([0, 1], [256, 128]), 0, 0],
    dur=0.5,
    hpf=var.hpf,
    lpf=P[expvar([220, 500], 4), 400, expvar([200, 800], 8), [500, 450, 520, 430]],
    amp=0.82 * var([1, 0], [[63, 127, 64], [1, 1, 0]])
)
xx >> play('X', rate=1, sample=11, dur=var([1, 0.5], [[63, 127], 1]), hpf=var.hpf, amp=var([[1, 0.95], [1.1, 1.2]], 32))
x2 >> play('X', rate=1, sample=17, dur=xx.dur, hpf=var.hpf, amp=var([1, 0], [[128, 256], [[32, 0], [64, 32]]]))
x3 >> play('X', sample=13, dur=3/4, hpf=var.hpf, amp=P[1, 1, 0, [0, 1], 1, [1, 1, 0]] * var([1, 0], [[128, 64], [16, [32, 0]]]))
x4 >> play('X', sample=var([3, 4, 5, 6, 7], 16), hpf=var.hpf, dur=2, delay=0.5, amp=0.75 * var([1, 0], [8, 8, 8, 8, 16, 8, 16, 8, 32, 16, 32, 16]))
x5 >> play('X', sample=7, dur=var([4, 2, 1], [32, 16, 8]), hpf=var.hpf, delay=0.75, amp=0.5 * var([1, 0], [[128, 128, 64], [[64, 64, [32, 128]], 32]]))
cl >> play('x', sample=19, dur=1, hpf=var.hpf, amp=P[1, 0] * 0.85 * expvar([0, 0, 1, 1], 64))
bu >> play('U', rate=0.5, dur=2, tremolo=4, pan=PWhite(-0.5, 0.5), amp=0.3 * expvar([0, 1, 1], 256))
c2 >> play('W', sample=33, dur=2, hpf=var.hpf, amp=0.4 * var([0, 1], [[256, 128, 64], [128, 64, 32]]) * expvar([0, 1, 1], 256))
mm >> play('m', dur=1.5, sample=10, hpf=var.hpf, lpf=110, sus=0.1, lpr=0.5, amp=expvar([0, 1, 1], 64) * expvar([1, 0], [128, 32, 128, 64, 256, [64, 32]]))

nn >> play('s', sample=var([0, 21], [[128, 256], [32, 64]]), dur=0.25, room=PWhite(0, 1), mix=PWhite(0, 0.2),
  amp=PEuclid(3, [8, 6, 9, 7]) * var([0, 1], [32, 64, 32, 128, 64, 128])
)
n2 >> play('n', sample=2, dur=1, delay=0.5, amp=1 * expvar([0, 1, 1], 128))
n3 >> play('s', sample=1, dur=0.5, amp=PEuclid(3, 8) * expvar([1, 1, 0], [128, 128, 64, 64]))
n4 >> play(var(['~', 'd'], [128, 64]), pan=expvar([0.35, -0.35], 32), sample=6, room=1, mix=0.2, lpf=P[2400, 3000] * expvar([0.5, 1.25], 64), dur=0.5,
    amp=1.25 * expvar([0, 1, 1], [128, 128, 0])
)
ff >> play('t', sample=4, dur=0.25, amp=expvar([0, 0, 0.4, 0.4], [64, 32, 64, 128]) * var([1, 0], [63, 1, 56, 8, 64, 0, 28, 4, 128, 0]))
k9 >> play('n', dur=0.25, room=1, mix=0.5,
    amp=expvar([1, 0, 0], [[4, 4, [8, 32]], [0, 0, [0, 2, 4, 8]], [8, 4, 16], 0]) * var([0, 1], [64, 128, 64, 64, 32, 32, 64, 32, 64, 128])
)
rh >> play('-', dur=1, delay=-0.1, rate=-1, amp=0.5 * var([0, 1], [[128, 64], [[64, 128], [32, 64]]]) * var([1, 0], [[63, 127], 1]))
ss >> play('[ss]', rate=2, dur=0.5,
    amp=expvar([0, 0, 1, 1], [64, [64, 0], 64, [64, 0], 128, [128, 128, 0], 128, [128, 64, 32, 0]]) * var([1, 0], [31, 1, 28, 4, 56, 8, 63, 1, 127, 1, 64, 0, 63, 1, 128, 0])
)
bb >> play(PEuclid2(3, 8, 'd', 't'), sample=PRand(0, 3), dur=0.25, amp=0.45 * expvar([0, 0, 1, 1], [[128, 64], [64, 0, 32], [256, 128, 128], 0]))

cs >> cs80lead(-5, hpf=expvar([700, 180], 64), fatk=PWhite(0.1, 1), fdec=PWhite(0.1, 2), frel=expvar([0.005, 0.05], 16), dtune=expvar([0.05, 0.002], 16),
    cutoff=expvar([100, 1500], 32), dur=4, room=1, mix=0.3, sus=8, hpr=0.25, tremolo=var([0.75, 1.5], 128), formant=0, amp=0.8 * expvar([0, 1, 1], [64, inf])
)
sp >> spacesaw(atk=0.0001, filterLo=expvar([100, 200], 128), balance=expvar([0, 0, 0.25], 64), sus=1, rel=0.3,
    lpf=expvar([320, 300, 230], [64, 32]), lpr=0.3, vib=P[5, var([5, 10], 256)], vibdepth=0.25,
    amp=P[1, [PWhite(0.85, 1), 1]] * 0.27 * expvar([0, 1, 1], 128) * expvar([1, 1, 0, 0.2, 0.5], [[48, [112, 96]], 0, [14, [14, 28]], [2, [2, 4]], 0])
)
