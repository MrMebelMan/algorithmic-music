# https://soundcloud.com/kitty_clock/flash-gitz

Clock.bpm = 133

hk >> play('-', dur=1, delay=0.5, sample=var([2, 1], [128, 64, 128, 32]), amp=1 * var([0, 1], [256, 512, 128, 64, 64, 128]))
ho >> play('-', dur=1, delay=0.75, sample=hk.sample, amp=P[0.5, 0, 0, 0, 0, 0, 0, 0] * hk.amp)
ww >> play(var(['X', 'M', 'm', 'x', 'v'], [[128, 64, 256], [256, 128]]), sample=var([0, 1], [128, 256, 128, 64, 64, 32, 128, 128]), delay=0, rate=var([1, 1.05, 0.95, 0.85, 1, 0.9, 1], [8, 8, 16, 16, 32, 32, 64, 64, 128, 128]), dur=1, amp=var([0, 1], [128, 256, 64, [32, 64, 128, 256], 32, 64, 32, 128, 64, 256, 64, 128])).every([64, 32, [16, 8], [16, 8], 64, 128], 'stutter', 2)
tn >> play('b', room=1, mix=0.25, lpf=expvar([400, 500], [64, 0]), lpr=0.25, rate=1, bend=0, sample=0, dur=0.25, delay=0, amp=P[[0.5, [0, 0.75, 0, 0], 0.5, 0.75], [0.25, [0.5, 0, 0.25, 0.5], [0.25, 0.5], 0.35]] * expvar([0, 0, 1], [[128, 64, 256], 256, 0]))
su >> play('s', sample=3, pan=[-0.85, 0.85, 0, -0.5, 0.5, 0], dur=1, delay=0.5, amp=P[1, [0.8, 0.9]] * var([1, 0], [16, 32, 64, [128, 64, 32], 256, [128, 32, 32], 64, 32, 128, [256, 64, 32, 32], 128, 128]))
sy >> play('s', sample=4, sus=0.01, dur=1, delay=0.75, amp=P[1, [0.5, 0.75], 1, [0.75, 0.75, 0.5, 0.25]] * 1 * hk.amp)
ds >> play('B', rate=var([0.75, 0.5], [64, 32]), sample=5, dur=1, hpf=var([100, 80], 128), hpr=0.25, bend=-0.5, amp=var([0, 1], [32, 64, 64, 128, 32, 32, 128]))
ln >> play('L', sample=3, rate=1, sus=0.1, dur=1, amp=var([0, 1], [128, 256, 128, 128, 64, 128, 64, 32])).every([32, 64, 128], 'stutter', 2)
kd >> play('v', bend=var([0, -0.25, 0.25, 0, -0.15, 0.15], 32), rate=var([1, 0.9, 1.05, 0.95, 1.025, 0.88, 1.1, 0.85, 1.15], [[64, 128, 256], [[32, 64, 128], [16, 32], 8, 8]]), room=P[1, 0.85, 1, 0.75] * var([1, 0], [28, 4]), mix=P[0.25, 0.15, 0.1, 0.15], sample=1, dur=1, hpf=90, hpr=0.25, lpf=200, lpr=0.25, amp=2.25).every(256, 'stutter', 2)
k2 >> play('v', bend=kd.bend, rate=kd.rate - int(var([0, 0.05], [128, 128, 256, 64, 23])), room=kd.room, mix=kd.mix, sample=var([1, 2], [[64, 128, 256], 32, 16, 8, 8, 128, 64]), dur=1, sus=P[0.15, 0.1, 0.1, 0.1], hpf=var([80, 800], [30, 2, 60, 4]), hpr=0.25, amp=var([1, 0], [[127, 255], 1]) * 1.25)
k8 >> jbass(dur=0.25, hpf=var([P[[100, 85], 90, [110, 87], 95, 80], 80], [32, 2]) + var([0, [5, 5, 10, 10, -5, -5, -10, -10]], 8), hpr=0.25,
    drive=P[0, var([0, 0.25, 0.5], [64, 128, 256]), var([0, 0.5, 0, 0.25], 64), var([0, 0.5], [28, 4])] * 0,
    amp=P[
        P[var([0.25, 0.5], [128, 256]), 0.25], expvar([0.25, 0.8], 256), [[0.5, var([0.5, 0.75], [64, 32, 64, 128])], 0.5, var([0.5, 0.25, 0.75], 64), 0.25], 0.75
    ] * var([1, 0.5], [256, 64, 128, 32]) * 0.95
)
pn >> jbass(P[-1, 0], oct=5.5, lpf=expvar([250, 1500], [[64, [32, 64], 128, 64], 0]), lpr=0.5, sus=P[0.15, 0.25], bend=var([-0.25, -0.5], [256, 128, 128]), delay=P[0.5, 0.25, 0.25], dur=[0.5, 0.25, 0.25], amp=var([0, 1], [[64, 256, 128], [128, 64, 128], 128, 128]))
k3 >> play('X', bend=kd.bend, rate=var([1, 1.5, 0.95, 1.25, 1, 1.05, 0.9], [64, 32, 128, 128]), room=kd.room, mix=kd.mix, sample=1, dur=kd.dur, hpf=var([150, 300, 125, 350, 200, 100, 400, 200], [28, 4, 31, 1, 64, 0]), delay=0, hpr=0.25, amp=var([0, 1], [128, 256, 64, 128]) * var([1, 0], [[127, 255], 1]) * 1.25)
vb >> play('V',
    rate=var([1.1, 0.9, 1, 0.95, 1.05], 128),
    sus=0.05,
    bend=var([0.15, 0, 0.1, -0.1], 32),
    sample=var([0, 1], [64, 256, 128, 128, 32, 256]), dur=0.25,
    amp=P[[1, 1.1], 0, P[0.5, 0.25, 0.75, 0.5] * 0.75, 0.15] * expvar([0, 0, 1, 1], [256, 128, 256, 0]) * var([1, 0], [31, 1, 28, 4, 31, 1, 56, 0, 64, 0, 28, 0, 64, 0]) * 1
)
v8 >> play('v', sample=2, dur=1, bend=0.1, rate=1, hpf=80, hpr=0.25, amp=expvar([1, 0], [256, 0]))
ks >> play('v', rate=var([1, 0.95, 1.05, 0.9, 1.1], 128), dur=1, delay=0.5, amp=var([0, 1], [256, 256, 64, 128, 128, 128]) * P[1, [1, [0.65, 0.75]]])
ob >> play('V', sample=2, dur=1, drive=0, rate=var([1.5, 1.45, 1.5, 1.4], [64, 128]), sus=0.04, hpf=120, hpr=0.25, amp=var([0, 1, 2, 3, 3.5], 128))

h1 >> play('-', room=kd.room, mix=kd.mix, sample=1, dur=kd.dur, delay=0.5, amp=var([0, 1.25], [[32, 64, 128, 256, 512], [64, 128, 32], 64, 128]))
h2 >> play('-', pan=PWhite(-0.25, 0.25), sample=2, dur=16, delay=0.75, amp=P[0.25, 0.5] * h1.amp)
cl >> play('H', sample=1, rate=0.8, dur=8, delay=0.5, amp=P[1, 0.85] * 0.7 * var([0, 1], [[64, 128, 256, 64], 128, 32, 128]))
rs >> play('I', sample=2, hpf=80, hpr=0.25, lpf=1500, lpr=0.5, dur=var([8, 2, 4, 2, 1], 64), amp=var([1, 0], [[256, 128, 64], 128, 128, 64]))
sh >> play('s', pan=PWhite(-0.5, 0.5), dur=1, delay=0.5, amp=var([0, 1], [[64, 128, 256], [128, 64], 64, 32, 32, 128]))
rk >> play('X', sample=2, rate=-1, dur=1, amp=var([0, 1], [[63, 127, 255], 1]))
tt >> play('t',
    sample=P[0, 1, 1, [2, 1]] + var([0, 1, 2, 3], [64, 128, 256, 64, 64]),
    rate=P[1, 1.01, var([0.95, 1, 1.05], 32), var([1, 0.9], [32, 16])],
    dur=0.25,
    pan=PWhite(-0.75, 0.75),
    hpf=P[[1, 0.5], var([0.85, 0.5, 1, 0.9, 0.7], 32), var([1, 0.85, 0.5], 16), var([0.95, 0.5, 0.8, 1], 8), var([1, 0.5], 64)] * expvar([800, 300], [32, 0]),
    hpr=0.25,
    amp=P[var([1, 0], [7, 1, 7, 1, 31, 1]), [[0.75, 0, 0, 0], 0.5], PWhite(0, 1), var([0.25, 0.5, 0.75, 1], 8)] * var([1, 0], [[64, 128], [32, 64, 128, 256], 128, 64, 32, 32]) * PWhite(0.25, 1) * 0.5
)

r2 >> play('u', sample=var([0, 1], 256), pan=PWhite(-0.75, 0.75), dur=0.25, lpf=expvar([300, 500, 2500], [64, [32, 64], 0]), lpr=0.35, amp=PWhite(0.5, 1) * expvar([0, 0, 1], [[64, 128, 64, 32, 256], [32, 64], 0]))
tr >> play('S', pan=PWhite(-0.5, 0.5), rate=var([1, 0.95, 0.95, 0.9], [56, 8]), dur=0.5, amp=P[0.25, 0.5] * var([0, 1], [[128, 64, 32], 64, [256, 128, 64, 32], [128, 256]]) * var([0, 1], [31, 1, 28, 4, 56, 8, 64, 0]))
cw >> play(var(['t', 'u'], [512, 256, 256, 128]), sample=1, dur=1, delay=0.5, amp=expvar([0, 0, 1, 1], [[128, 256, [128, 64], 32], [64, 32, 128, 128], [256, 128], 0]) * var([1, 0], [31, 1, 28, 4, 56, 8, 64, 0, 30, 2, 32, 0]) * 1.5)
rc >> play('~', pan=PWhite(-0.75, 0.75), sample=var([0, 1, 2], 256), dur=0.25, lpf=4500, lpr=0.4, amp=expvar([0, 0, 1.25], [[128, 256, 512, 64], [64, 128, 32, [64, 128, 256]], 0]))

ru >> play('o', sample=0, rate=0.7, dur=2, delay=1, amp=var([0, 0.75], [[128, 64, 32], 64, [128, 32], [256, 128, 64, 32, 32], [256, 128], [128, 64, 32, 64]]))
rz >> play('o', sample=1, rate=0.7, dur=4, delay=0.75, amp=0.85 * ru.amp)
hy >> play('-', rate=var([1, 0.8], [64, 64, 128, 128]), sample=4, dur=0.25, delay=0, amp=P[0, 0, 1, 0] * expvar([1.8, 0], [128, 0, 256, 0, 64, 32, 64, 0, 32, 0, 128, 0, 256, 0]))
hh >> play('-', rate=var([1, 0.9, 0.8], 128), sample=2, dur=0.25, delay=0, amp=hy.amp)
hf >> play('u', sample=4, dur=0.25, amp=P[1, var([1, 0], 128), expvar([0.15, 0.5], [0, 64]), [0.85, 0.5]] * var([1, 0], [32, 128, 32, 64, 64, 128]))
cz >> play('*+n(xu)uuvx', sample=P[2, 0, 1, [1, 0, 2, 3]], dur=0.25, lpf=expvar([1000, 3000], [128, 0]), lpr=expvar([0.75, 0.25], [64, 0]), rate=P[0.85, [1, 0.85, 1.1, 1], [1.1, 0.85, 0.9, 0.9], 1], amp=expvar([0, 0, 1, 1], [256, 128, 256, 0]))
