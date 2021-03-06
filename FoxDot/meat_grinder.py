# https://soundcloud.com/kitty_clock/meat-grinder

Clock.bpm = 133

angel = SynthDef('angel')
click = SynthDef('click')
filthysaw = SynthDef('filthysaw')
tworgan = SynthDef('tworgan')
tb303 = SynthDef('tb303')
bchaos = SynthDef('bchaos')

var.brk = var([1, 0], [31, 1, 31, 1, 28, 4, 32, 0])
cl >> click(
    [var([3 -3], [128, 128, 64, 64]), 1, var([0, -0.5], 32), 0],
    room=1, mix=P[0, 0, 0.1, 0],
    oct=var([6, 5, 6, 5.5, 6, 4.5], [128, [64, 32], 32, [64, 128], [64, 32], 32]) - var([0.5, 0], [4, 2, 3, 1, 3, 1]),
    dur=0.25,
    drive=P[0, 0, var([0, 0.15], [[64, 128], [128, 256]]), 0],
    lpf=200, lpr=0.25,
    amp=P[1, var([0, 1], 128), var([1, 0], [128, 64, 32, 32]), var([1, 0], [8, 8, 8, 8, 64, 64]),  1, [1, var([0, 1], 256)], 1, 1] * var.brk * 0.35 * 0
)

ag >> angel(dur=4, sus=8, tremolo=4, amp=expvar([0, 1, 1], [128, 256, 0]) * var.brk).stop()

fs >> filthysaw(
    dur=1,
    sus=var([0.75, 0.5, 1], [64, 32, 128]),
    hpf=expvar([800, 300], [64, 0]),
    hpr=PxRand([0.25, 0.5, 0.25, 0.75, 0.25], [4, 2, 1, 1]),
    bpm=Clock.bpm*8,
    lpf=P[200, 500, 1000, 150] * expvar([8, 1], [64, 0]) * expvar([0.25, 1], 1/2),
    lpr=0.25,
    amp=P[[1, 0, 0, 0], [0, 0.5, 0, 0.25], [0.25, 1, 0.5, 1], [0.5, 0.25, 1, 1]] * 0.5 * 0
)

tb >> tb303(dur=P[0.5, 0.25, 0.25], sus=1, chop=2, hpf=expvar([1200, 600], [64, 0]), hpr=0.25, oct=4.25, amp=P[1, [0, 0.5], 1, 1] * var.brk * var([0, 0.8], [128, 64, 64, 128]))

tm >> play('X', sample=var([0, 1], [64, 128, 128, 256]),
    rate=var([0.9, 0.8, 0.95, 0.85, 1, 0.75, 0.93, 1.05, 0.7, 1.1], [[8, 32, 8, 8], [16, 16, 4, 4, 8, 8]]),
    dur=P[1, [0.25, 0.5], [0.75, 0.5], [1, 1, 1, 0.5], [1, 1, 1, 0.5]],
    amp=1 * var.brk
)
t2 >> play('m', sample=var([1, 0, 2, 1], 64), rate=var([1, 0.9, 1.1, 0.95, 1.05], [64, 32, 32]), dur=1, amp=var([1.5, 0], [[28, 56], [4, 8], 64, 32, 31, 1]) * var.brk * expvar([0, 0, 1, 1], [256, 128, 512, 0]))

Group(tb, tm, rs, t2, ve, bc, h1, h2).stop()

rs >> play('I', drive=0.2, bend=-0.25, dur=4, delay=1.5, amp=0.25)

bd >> play('v', bend=var([0, 0.5], [31, 1, 28, 4, 32, 0]), sample=var([0, 1, 2], [128, 64, 32, 128]), dur=0.25, cut=var([0.25, 0.5, 0.75, 1, 0.5], [[32, 8, 4, 4], [16, 8], 32, [8, 16], 8, 16, 8, 4, 4]), delay=0,
    hpf=var([[70, 80, 75, 90], [150, 200, 180, 120]], [28, 4]), hpr=0.25,
    amp=P[P[1, 0.25, 1, 0.5] * 0.8, [0.25, 0.5]] * var.brk
)
bd.sample=2
bd.amp = P[
    var([0.25, 1.25], [64, 256]) * 1.25,
    var([0, 0.5], [28, 4, 32, 0]) * 0,
    P[0.15, var([0.15, 0.5], [64, 128]), 0.15, 0.5],
    var([0.2, 0.25, 0.3], 32)
] * 0
#bd.amp=P[[1, 0.85, 1, 1.25], 0, P[0.5, 0.35], [0.25, 0.5, 0.25, 0.75]]

ve >> play('V', sample=0, dur=1, rate=P[1, 1] - 0.25, hpf=70, bend=P[-0.25, 0.15], hpr=0.75, amp=1 * var.brk)

#bd.amp = P[1, 0, 0, 0]

h2 >> play(':', pan=PWhite(-0.75, 0.75), room=1, mix=0.15, sample=[1, 3, [0, 1], 0], dur=0.25, amp=expvar([1, 0], [1/3, 1/2, 1/4, 1/8, 1/8, 1/8, 1/8]) * var([0, 1.5], [128, 64, 32, 32, 64, 32, 128]))

ee >> play('E', sample=var([2, 0], [64, 32, 128, 128]), dur=0.5, amp=P[1, [0, 1], 1, [0, 0, 1, 1],  var([1, 0], 64), [0, 1], 1, [var([0, 1], 32), var([1, 0], 32), 1, 0]] * 0.3)

bc >> bchaos(dur=1, sus=2, amp=P[0.75, 0] * expvar([0, 0, 1, 1.25], [[32, 64], 64, 32, 0]))

h1 >> play('-', sample=2, dur=0.5, amp=P[[0.25, var([0, 0.5], [32, 64])], 1] * var([0, 1.25], [64, 32, [128, 64, 32], [64, 128], 32, 32]) * var([1, 0], [56, 8, 64, 0]))

tt >> play('t', sample=1, pan=PWhite(-0.85, 0.85), dur=0.25, lpf=expvar([2100, 1500], [32, 0]), lpr=0.25, amp=P[[1, 1, 1, 0], 0.25, [0.5, 1], [1, 0.5, [0.25, 0.5, 0.25, 0.85], 0.5]] * var([1, 0], [128, 64, 256, 32, 32, 64, 32, 64, 128]) * 0.9)
