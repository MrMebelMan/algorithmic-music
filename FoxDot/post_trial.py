import sys
sys.tracebacklimit=0

Clock.set_time(0)
Clock.reset()
Clock.bpm = expvar([[125, 150], [133, 150], [133, 150], 150], [1024, 2048, 2048])

var.brk = var([1, 0], [31, 1, 28, 4, 56, 8, 31, 1])

sb >> sawbass(
    dur=0.25,
    lpf=P[
        [1500, 2000], var([2500, 1500]), [850, 900, 800, 1000], var([500, 750], 8),  var([1000, 450], [64, 32]), var([850, 400], [16, 8, 8]), 250, [400, 350],
        var([1250, 2500], 16), var([1500, 2500]), [850, 1700, 500, 750], var([500, 750], 8),  [1000, 750, 1250, 1250], [850, 500, 450, 400], [350, 300], [500, 750]
    ], lpr=0.25,
    drive=P[[0, 0.05], var([0, 0.04], 8), [0, 0.08, 0.05, 0.08], var([0.03, 0.05], 16)],
    amp=P[1, 0.85, 1, 0.95] * 0.1
)
ks >> keys(
    dur=0.25,
    sus=1,
    chop=4,
    lpf=P[[var([1500, 1000, 1250, 850], 8), 1250, 900, var([800, 1500])], [var([1000, 750], [32, 16, 8, 8]), 500, 750, 800], expvar([750, 1500], 128), 500],
    lpr=expvar([0.9, 0.25], [128, 64]),
    amp=P[1, 0.85, 1, [0.75, 0.5]] * 1.5
)
t1 >> play('t',
    rate=P[1, 1.05, 1, 1], sample=var([1, 2, 1, 0], 64),
    lpf=expvar([1000, 2500], [32, 8, 16, 8]), lpr=expvar([0.5, 0.25], [32, 64]),
    amp=P[[1, 0.85], [0.5, 0.75], [1, 0.25, 0.5, 0.25], [0.5, 0.25], [0, 0.25, 0.5, 0.75], [0.5, 0.25, 0.75, 0.5], expvar([0, 0.85], 128), [0, 0.5, 0.85, 0.85]] * 0.35
)
sh >> play('s',
    dur=0.25,
    lpf=expvar([2000, 4000], [32, 16, 8, 8]),
    amp=P[[1, 0.85], [0.75, 0.5], [0.5, 0.75], [1, 0.25, 0.5, 1]] * expvar([0, 0.5], [[128, 64, 128, 32], 0])
)
cl >> play('H', sample=1, room=1, mix=0.15, dur=var([16, 8, 4, 2], 128), amp=0.15)
h2 >> play('n', sample=2, room=1, mix=0.2, dur=h1.dur, delay=h1.delay, amp=h1.amp * var.brk)
h3 >> play('-', sample=1, dur=0.25, amp=P[[1, 1.1], [1, var([0.85, 1], 64)], [1, 0.95, 0.85, 0.75], [0.85, 0.5]] * expvar([1, 0.5], 1/3) * var.brk)
r2 >> play('I', dur=[1] * 126 + [0.5, 0.5], room=1, mix=[0.25, 0.15], lpf=expvar([2500, 6000], [128, 0]), amp=expvar([0, 1], [128, 0]))
dc >> play('*', sample=var([0, 2], [64, 32]), dur=2, delay=0.25, amp=var([0, 0.5], [256, 128, 64, 32]))
uu >> play('u', sample=1, pan=PWhite(-0.75, 0.75), dur=0.25,
    lpf=P[1500, 500, 1250, 1000, 850, 750, 1200, 500],
    amp=P[
        [var([0.5, 0.75], [128, 256]), 0.5], var([0.45, 0.3, 0.55], 64), [0.4, var([0.35, 0.5], 8)], 0.4
    ] * 1.75 * var.brk
)
sr >> play('u', pan=PWhite(-0.75, 0.75), dur=0.25, lpf=P[[1500, 750, 1250, 1000], 1000, [2500, 1500], [850, 750]], amp=P[[1, 0.85, 1.1, 1], [0.85, 0.75], 1.1, [0.85, 0.5]] * var([0, 1], [28, 4, 28, 4, 56, 8, 31, 1]))

bp >> blip(dur=1, oct=4.95, lpf=250, lpr=0.45, amp=P[1, [0.95, 0.9]] * 1.2 * var.brk)
b2 >> blip(dur=1, delay=0.5, oct=bp.oct, lpf=bp.lpf * 0.75, lpr=bp.lpr, amp=P[0.85, 0.15] * bp.amp)

bb >> bass(dur=1, sus=[0.85, 0.5], amp=P[1, 0.85] * expvar([0, 0.6], [128, 0]) * var.brk)

l1 >> play('L', dur=1, delay=0.5, sample=1, amp=P[1, 0.85] * 0.25)
h1 >> play('-', sample=2, room=P[1, 0.875], mix=0.15, dur=1, delay=0.5, amp=P[1, 0.9] * var([0, 0.75], [[32, 64], [64, 128]]) * var.brk)
s2 >> play('s', sample=[0, var([0, 1], [64, 128])], dur=0.5, amp=P[1, 0.85] * expvar([0, 0.4], [128, 0]))
ss >> play('S', sample=[0, var([2, 1, 0], 128)], dur=0.5, lpf=sinvar([1800, 3000], 32), lpr=0.5, amp=P[1, 0.85] * var([0, 0.25], [[128, 256], [64, 128]]))

var.kdur = [1] * 127 + [0.5, 0.5]
var.khpf = var(0.15)

tm >> play('m', dur=1, bend=P[0, 0.5], benddelay=0.25, lpf=300, hpf=var([150, 200, 125, 100], [64, 32]) * var.khpf, amp=P[1, 0.85] * 0.3 * var.brk)
bd >> play('V', rate=var([1, 1.05, 0.95, 0.9, 1], 128), hpf=130 * var.khpf, hpr=0.25, sample=1, bend=[0, 0.5], benddelay=0.25, dur=var.kdur, cut=[2] * 127 + [0.5, 0.5], lpf=var([350, 500, 250, 400], 32), amp=P[1, 0.85] * 1 * bb.amp * var.brk)
kd >> play('X', sample=var([0, 2], [[512, 128], 256]), hpf=120 * var.khpf, hpr=0.25, lpf=250, lpr=0.5, dur=1, amp=P[1, 0.85] * 0.65 * var.brk)
k2 >> play('X', rate=P[1, 1.1], sample=1, lpf=400, lpr=0.25, hpf=125 * var.khpf, hpr=0.25, dur=var.kdur, amp=P[1, 0.85] * 0.45 * var.brk)
k3 >> play('X', dur=var.kdur, sample=2, lpf=200, hpf=var([200, 150, 125, 100], 32) * var.khpf, hpr=0.25, lpr=0.5, amp=P[1, 0.85] * 0.7 * var.brk)
r3 >> play('I', sample=1, dur=var([2, 1], [28, 4, 28, 4, 56, 8, 28, 4]), amp=expvar([0, 0, 0.6, 0.6], [32, [64, 128], [128, 256], 0]))
k4 >> play('X', sample=4, rate=-1, dur=0.25, lpf=750, amp=P[1, 0.85, 0.5, 0.25] * 1)
sk >> play('X', sample=0, dur=kd.dur, delay=0.5, lpf=kd.lpf, lpr=0.5, amp=P[1, [0.25, 0]] * var([0, 0.75], [[32, 64], [128, 256]]) * var.brk)
kr >> play('X', sample=4, dur=0.25, cut=1, lpf=[350, 500, 250], lpr=0.25, amp=P[0.25, 0.15, 0.5, 0.75] * expvar([0, 0.85], [128, 0]) * kd.amp * var.brk)
bk >> play('V', dur=1, delay=0.5, lpf=200, lpr=0.25, amp=P[0.5, 0.25] * expvar([0, 1.5], [128, 0]))
oo >> play('o', dur=1, hpf=150, hpr=0.25, lpf=300, lpr=0.5, amp=P[1, 0.85] * 0.5)
r4 >> play('X', sample=2, dur=1, rate=-1, lpf=1750, amp=var([0, 1], [63, 1]))

@next_bar
def stahp():
    #Group(h1, h2, h3, s2, ss, sh, cl, l1, t1, sr, uu, bp, b2).stop()
    Group(bd, kd, k2).stop()
    Group(k3, r3, sk).stop()
    Group(k4, kr, bk, tm, r4).stop()

Master().lpf = P[2050, 500, 1500, 2000] * expvar([0.5, 1.25], 8)
Master().lpr = 0.75
