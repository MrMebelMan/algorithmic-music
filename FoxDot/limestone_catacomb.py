# https://soundcloud.com/kitty_clock/limestone-catacomb

Clock.bpm = 150

var.drop = var([1, 0], [[31, 124, 255, 252, 63, 60, 31, 28], [1, 4]])
var.oh_amp = var([0, 1], [64, 32, 32, 128, 32, 128])
var.v_amp = var([0, 1], [[256, 64], 512, 128, 256])

pl >> blip(dur=0.5, bend=0.5, oct=4.8, lpf=680, lpr=0.8, amp=P[1, 0.5, 1, 0] * expvar([0, 0, 1.5, 1.5], [[256, 0], 128, 512, 0]))
xx >> play('V', rate=1, dur=1, sample=2, lpf=expvar([3000, 1500], [16, 0]), amp=var.v_amp * var([0, 0.25, 0.5, 0.8], 128) * var.drop) #.every(128, 'stutter', 2)
xh >> play('V', rate=0.8, dur=1, delay=0.5, sample=2, amp=P[1, PWhite(0, 0.5)] * 0.3 * var.v_amp * var([0, 1], [32, 64, 32, 128, 64, 256]) * var.drop)
kk >> play('U', rate=-1, pan=PWhite(-0.75, 0.75), dur=0.25, delay=0, sample=9,
    amp=P[
        1, var([0.5, 0], [64, 32, 128, [32, 64]]), var([1, 0, 1, 0.5], [128, 64, 64, 32, 32, 28, 4, 28, 4]), var([0.1, 0.5, 0.15, 0.75], [4, 2])
    ] * 0.4 * var([0, 1], [128, 256, 64, 128, 32, 64])
)
bb >> play('V', rate=1, sus=0.08, lpf=0, hpf=50, hpr=0.5, sample=1, dur=1, amp=var([0, 0.75], [256, 32, 32, 64, 32, 128, 64, 32]) * var.drop)
x9 >> play('X', rate=var([1, 0.9, 1.1, 0.95, 1.05, 0.85], 32), sample=[9, 7], dur=1, hpf=var([90, 70], [64, 256]), hpr=0.25, amp=0.55 * var.drop)
x8 >> play('X', rate=var([1, 1.1, 0.9, 1.2, 0.85, 1.3], 64), dur=1, sample=6, hpf=P[90, 80], hpr=0.25, lpf=3000, amp=0.2 * var.drop)
u1 >> play('U', dur=1, delay=0.5, sample=4, amp=0.25 * var([1, 0], [128, 64, 64, 32, 32, 32, 128, 32]) * var([0, 1, 1], [32, inf]))
u2 >> play('U', dur=P[0.5, 0.25, 0.25], delay=0.25, sample=6, amp=0.25 * var([0, 1, 1], [64, inf]) * var([1, 0], [64, [32, 128], 128, [32, 64], 128, 64, 64, 128]))
u4 >> play('U', sample=1, sus=0.75, dur=2, lpf=6000, lpr=0.25, amp=1.25 * var([1, 0], [256, 64, 128, 32, 64, 64]) * expvar([0, 1, 1], [64, inf]))
u3 >> play('U', bend=-0.25, rate=P[expvar([1, 0.75], 8), 0.95, [1.1, 0.5], 0.9] * var([1, 0.5, 0.25], 128), dur=0.25,
    lpf=P[1000, 500, 1250, [200, 800]] * 1.25,
    lpr=0.75, delay=0, sample=11, amp=expvar([0, 0.3, 0.3], [[[256, 32], 128, 256], [256, 128, 64], [0, 0, 8]])
)
u5 >> play('U', sample=4, dur=var([2, 1], [64, 128, 32, 256]), delay=var([1, 0], [64, 128, 32, 256]), amp=expvar([0, 0, 0.5, 0.55], [128, 256, [256, 512], 0]) * var.drop)
u6 >> play('U', pan=expvar([-0.85, 0.85], [16, 16, 16, 16, 32, 32, 8, 8, 8, 8]), rate=1.5, sample=4, dur=0.25, delay=0, lpf=expvar([2000, 5000], [[32, 16, 64], 0]), lpr=0.5, amp=P[0.4, 0.85] * expvar([1, 0.15], [1/2, 1/4, 1/4, 1/2]) * 0.45 * var([0, 1], [32, 64, 16, [16, 64], 32, 16, 16, 128]))
u7 >> play('U', sample=3, dur=1, amp=expvar([0, 0.5], [32, 64, 128, 32, 128, 32, 128, 64, 128, 128]) * var.drop)
nn >> play('n', sample=var([0, 3], [128, 64]), dur=1, delay=0.5, amp=var.oh_amp)
ll >> play('L', sample=1, dur=1, delay=0.5, amp=0.15 * var.oh_amp)
cl >> play('H', room=1, mix=0.15, sample=1, dur=2, amp=0.2 * var([0, 1], [128, 256, 64, 32, 32, 128, 32, 64]))
fs >> play('u', dur=0.25, bend=PWhite(0, 1), pan=PWhite(-0.7, 0.7), rate=PWhite(0.95, 1.05), amp=P[1, PWhite(0.8, 1), [1, PWhite(0.75, 1)], PWhite(0.7, 1)] * expvar([0, 0, 1], [[[128, 64, 32], 32, 128, 256], [32, [64, 32], [64, 32], [128, 64]], 0]))
sn >> play('I', sample=2, dur=var([8, 4, 2, 1], 128), lpf=2000, delay=1)

Group(u5, u6, u7).stop()
Group(u3, u4).stop()
Group(fs, u2, kk).stop()

# Master().lpf = P[200, 500] * 0.1
# Master().lpr = 0.5

