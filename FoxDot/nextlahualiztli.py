# https://soundcloud.com/kitty_clock/nextlahualiztli

Clock.bpm = 125

var.brk = var([1, 0], [[31, 28, [128, 64]], [1, 4, 32]])
var.hi_amp = var([1, 0], [[256, 128], [128, 256]]) * 0
var.pt_2 = var([0, 1, 1], [64, inf]) * 0
var.pt_3 = var([0, 1, 1], [128, inf]) * 0
var.pt_4 = var([0, 1, 1], [192, inf]) * 0

sh >> play('s', sample=0, dur=0.25, amp=P[1, [1, var([0, 1], [32, 64, 32])], 1, var([0, 0.25, 0.5, 0.75, 1], 64)] * expvar([1, 0], 1/3) * expvar([0, 0, 0.35], [[0, 64, 128], 120, 8]))
jb >> jbass(
    dur=0.25,
    drive=P[0, 0, var([0, 0.035], [128, 64]), 0],
    oct=P[4, var([5, 5.1], [16, 8]), 5, 5],
    sus=0.5,
    chop=8,
    hpf=P[[800, 300], 600, 500, 400] * var([1, 1.25, 0.75, 0.9], 32),
    hpr=0.05,
    amp=P[1, [0, 1], [0, var([0, 1], 4), 0, 1], [0.5, 1]] * 0.85 * var([1, 0], 256)
)
j3 >> jbass(
    dur=var([0.25, 0.5], [196, 64]),
    oct=P[4, 4, 4, 5],
    sus=2,
    chop=[4, 4, var([16, 8], [128, 64]), 4],
    hpf=P[350, [600, 700, 300, 400], 1200, 200] * expvar([1.05, 1.5], [30, 2]),
    hpr=0.1,
    amp=P[1, [0, 1], [0, var([0, 1], 4), 0, 1], [0.5, 1]] * 0.85 * var([0, 1], 256)
)
j2 >> jbass(dur=8, sus=4, tremolo=4, lpf=5000, lpr=0.1, amp=0.38 * expvar([0, 1, 1], [32, inf]))
xx >> play('x', dur=0.5, amp=P[1, 1, 0, 1, 0] * 0.5)
x2 >> play('x', drive=var([0, 0.05], [[128, 256], [64, 128, 32, 32]]), sample=1, dur=[0.5, 0.5] + [1] * 63, amp=0.95 * var.brk * var.pt_3)
oh >> play('-', room=1, mix=0.1, sample=2, dur=1, delay=0.5, amp=0.65 * var([1, 0], [[32, 64, 128, 256], [[64, 128], 128, 64, 256]]) * var([0, 1, 1], [196, inf]) * var.hi_amp * var.pt_2)
bs >> bass(dur=0.5, sus=P[1, 0.25, 0.25, 0.25], lpf=700, lpr=0.75, amp=P[[0.6, 0.55], [0.8, 0.7]] * 0.6 * var.brk * var.pt_2)
nn >> play('n', dur=2, delay=[0, var([0.5, 0], [64, 32])], amp=0.35 * var([0, 1], [64, 32, 64, 128, 64, 256, 32, 64, 32, 128]) * var.hi_amp)
rs >> play('I', room=1, mix=0.15, dur=var([8, 4, 2], 64), amp=0.5 * var([0, 1], [32, 128, 32, 64, 64, 128]) * var.hi_amp)
cl >> play('H', sample=1, dur=4, delay=0.5, amp=0.025 * var([0, 1], [128, 256, 64, 128, 32, 128, 32, 64]) * var.hi_amp)
ss >> play('S', dur=0.5, amp=P[[0.5, 0.35], [1, 0.95]] * expvar([0, 0, 0.45, 0.5], [128, 128, 128, 0]) * var.hi_amp)
tt >> play('t', dur=0.25, sample=var([0, 2], 128),
    room=1, mix=0.1,
    lpf=expvar([0.5, 1.5], [128, 0]) * P[expvar([600, 1200], [32, 0]), [1200, 650], [400, 250], expvar([650, 200], [16, 0]),  var([700, 900, 1200, 300, 500], 8), 350, [800, 450], var([500, 200], 8)],
    lpr=0.25,
    amp=var([1, 0.75], [6, 2]) * expvar([0, 1, 1], [128, inf]) * var([1, 0], [512, 256])
)
s2 >> play('s', dur=var([1, 2, 1, 4, 8, 2, 1], [128, 32, 64, 32, 32, 128, 128, 64, 128]), delay=0.5, amp=var([0, 1], [64, 128, [64, 32], 64]) * 0.85 * var.pt_3 * var.hi_amp)
rr >> play('r', lpf=500, lpr=0.5, rate=0.15, dur=[1, 2], delay=P[0, 0.5], amp=expvar([0, 0, 0.5, 0.5], [128, 128, 256, 0]) * var.hi_amp)
cr >> play('ziuaktun', sample=var([0, 4, 2, 1], 128), rate=-1, tremolo=P[4, 4, 4, 4, 8, 8], bend=-0.5, dur=0.25, lpf=2250, hpf=expvar([180, 800], [128, 0]), hpr=0.1, amp=expvar([0, 0.25, 0.25], 256) * var.hi_amp)
bx >> play('X', dur=var([0.25, 0.5], [120, 8]), sample=0,
    lpf=expvar([900, 1900], [[4] * 32 + [8] * 4 + [16] * 2, 0]), lpr=0.5,
    #lpf=expvar([1000, 2000], [4, 0]), lpr=0.5,
    amp=Pvar([
        P[1, 0.1, [0.5, 0.25, 0.5, 0.65], [0.75, 0.5, 0.25, 0.3]],
        P[1, 0.5, 0.25, 0.15],
        P[1, 0, 0, 0],
        P[1, [0.15, 0.5, 0.25, 0.75], [0.75, 0.5], [0.15, 0, 0.75, 0.25]],
        P[1, 0, [0, [0, 0, 0, 0.5], 0, 0, [0, 0.5], 0.5], 0]
    ], [256, 64, 64, 64, 64]) * 0.75 * var([1, 0], [128, 64, 128, 32, 64, 64, 256, 32]) * var.pt_3,
)
x3 >> play('X', bend=var([0, 2], 256), rate=var([1, 0.95, 0.9, 0.8], [128, 16, 16, 64]), sample=1, dur=x2.dur, hpf=var([0, 800], [[112, 28, 31], [16, 4, 1]]), amp=var.pt_4)
ta >> play('m', rate=P[2, 1.9, 2.1, 1.8], tremolo=P[4, 8], dur=1, delay=0, amp=var([0, 1], 512) * var.brk)
t2 >> play('T', room=1, mix=1, sample=var([1, 0], [64, 64, 128, 128]), dur=var([32, 16, 8], 256), delay=0.5, amp=0.05 * var.pt_3)
ww >> play('w', rate=0.25, dur=2, delay=0.5, lpf=500, amp=var([0, 0.5], 256) * var.pt_4)
o2 >> play('=', rate=-0.5, dur=2, amp=var([0, 1], [[7, 15, 31], 1]) * 0.5 * var.hi_amp * var.pt_3)
rc >> play('~', dur=2, rate=-0.25, tremolo=4, amp=0.25 * expvar([0, 0, 1, 1], [[128, 256, 64], [128, 256], [64, 32], 0]) * var([1, 0], 256))
sa >> play('G', sample=1, tremolo=4, room=1, mix=0.25, rate=1, dur=2, delay=P[0, 0.5], amp=expvar([0, 0.35, 0.43], [[128, 512, 256], [256, 64, 128], 0]))
