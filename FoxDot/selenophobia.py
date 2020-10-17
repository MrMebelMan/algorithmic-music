# https://soundcloud.com/kitty_clock/selenophobia

Clock.bpm = 120

eeri = SynthDef('eeri')
rhodes = SynthDef('rhodes')
supersaw = SynthDef('supersaw')
cluster = SynthDef('cluster')

var.brk = var([1, 0], [[256, 31, 28, 31, 56], [[32, 16, 64], 1, 4, 1, 8]])

rd >> rhodes(oct=4, chop=P[0, 2], lpf=P[200, 150] * expvar([1, 0.4], 256), lpr=expvar([0.25, 0.2], 32), bend=P[-0.25, -0.5] * var([0.9, 0], [[512, 256], [256, 128]]) * 0.5)
cs >> cluster(lpf=expvar([1500, 6000], [120, 8]), lpr=0.25, tremolo=var([0, 1], [[128, 256], [64, 128, 32]]), amp=expvar([0.25, 1], [4, 0]) * expvar([0.25, 1, 1], [[256, 128], 256, 0]))
ss >> supersaw(dur=0.25, oct=P[4.25, 4, 4.5, 4.25], lpf=180, lpr=0.05, amp=expvar([0, 1], [2, 0]) * 2)
er >> eeri(dur=0.25, sus=P[expvar([2, 4], [64, 128, 128]), 2], chop=var([4, 16, 32], 128), tremolo=4, lpf=expvar([200, 200, 280, 280], 128), lpr=PWhite(0.08, 0.1),
    amp=P[1, PWhite(0, 0.25)] * var([1, 0.5], [[120, 56], 8]) * var.brk #* 0.65
)

bs >> bass(dur=1, bend=var([-0.25, -0.35], [128, 64]), lpf=expvar([400, 200], [128, 0]), lpr=expvar([0.8, 0.15], 64), amp=P[1, 0.5] * var.brk)
b2 >> bass(dur=1, oct=P[5.05, 5, 5.05, 4.98], bend=var([-0.25, -0.35], 32), lpf=expvar([400, 200], [120, 8]), lpr=expvar([0.8, 0.15], 64),
    amp=P[PWhite(0.25, 0.5), var([1, 1], [256, 512])] * var.brk
)

x1 >> play('X', rate=expvar([0.9, 0.75], [4, 0]), sample=1, dur=0.5, lpf=300, lpr=0.25,
    amp=P[2, 1.25, var([0, 2], [[256, 128], 512]), var([0, 1], [[256, 128], 512])] * var([1, 0], [28, 4, 31, 1]) * var([0, 1, 1], [64, inf])
)
x2 >> play('X', rate=0.85, sample=1, sus=0.05, dur=0.25, lpf=300, lpr=0.15, amp=P[PWhite(0, 0.25), 0, 0, [1, 0, 0, 0]] * var([0, 1, 1], [196, inf]))
x3 >> play('X', dur=0.5, sample=1, sus=0.05, lpf=285, lpr=0.1,
    amp=expvar([0, 1, 1], [256, [128, 256], 0]) * P[1, PWhite(0.25, 0.5)] * var([0, 1], [32, 64, 64, 128, 32, 256]) * var([0, 1, 1], [196, inf])
)

nn >> play('n', pan=PWhite(-0.65, 0.65), rate=P[P[1, 0.975, 1.025, 0.985], 1, 1, 1], sample=1, room=1, mix=0.15, lpf=expvar([3000, 6000], [32, 32, 64, 64]), lpr=0.75, dur=0.25,
    amp=P[1.1, 0.1, PWhite(0.25, 0.5), var([0.5, 0], [[256, 128], [128, 64]])] * var.brk * var([0, 1], [128, 128, 128, 256, 256, 512])
)
sh >> play('s', pan=nn.pan * -1, sample=2, room=nn.room, mix=nn.mix, dur=nn.dur, delay=0.5, bend=PWhite(0, -1), amp=nn.amp)
cl >> play('H', room=1, mix=0.25, sample=0, dur=0.25,
    pan=PWhite(-0.85, 0.85),
    lpf=expvar([4500, 7000], [16, 0]), lpr=PWhite(0.5, 0.75),
    amp=var([0, 1, 1], [128, inf]) * PWhite(0.1, 1.25) * expvar([1, 0.25], [4, 0]) * var([0, 1], [[3, 8, 16, 32], 1, [8, 16, 32, 64], 2, [16, 32, 64], 3, [4, 64, 128], 2, 1, 3, 3, 2, 3, 1])
)
bp >> play('b', room=2, pan=PWhite(-0.25, 0.25), mix=0.15, formant=1, sus=0.15, bend=-0.25, dur=var([8, 4, 2], 256), delay=P[0.5, 0], amp=P[0.3, 0.25] * expvar([0, 1, 1], 128) * 1)
b2 >> play('q', room=1, mix=0.1, drive=0.1, dur=1, delay=0.8, amp=var([0, 1, 1], [255, inf]) * var([0, 1], [[127, 64], 1])) # rare beep
rr >> play('w', rate=expvar([-0.5, -0.25], [120, 8]) * P[0.9, 0.9, 1, 1,  1, 1.1, 0.95, 0.95], room=P[1, 0.15, 0.25, 0], mix=expvar([0.25, 0.5], 2),
    lpf=expvar([200, 400], [8, 8, 16, 16]), lpr=0.15,
    dur=0.25, delay=0.5,
    bend=-0.25, sus=0.05, slide=-0.5,
    amp=P[1, 1, 1, 1,  0, 1, 1, 0.5,  0, 0, 1, 0.5] * expvar([0, 1, 1], [256, inf]) * 0.25
)
oo >> play('o', room=1, mix=0.25, dur=2, delay=P[0, var([0, 0.5], [[28, 56], [4, 8]])], amp=var([0, 0.15], 256))
