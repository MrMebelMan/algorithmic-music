# https://soundcloud.com/kitty_clock/collective-commitment

Clock.bpm = 120
Clock.reset()

var.brk = var([1, 0], [31, 1, 28, 4, 31, 1, 56, 8, 128, 32]) * var([0, 1], [128, inf])
xx >> play('X', rate=var([1, 0.85], 64), sus=0.05, dur=1, sample=23, amp=var.brk)
x2 >> play('V', rate=1, dur=1, sample=9, amp=var([1, 0], [28, 4, 56, 8, 31, 1]) * var.brk)
x3 >> play('X', rate=var([1, 2], 128), dur=1, sample=6, amp=var.brk)
x4 >> play('X', rate=0.85, sample=1, lpf=P[500, 400, 450, 300], lpr=0.15, sus=0.0005,
    dur=4,
    #dur=var([4, 1], [4, 12]),
    delay=2 * PWhite(-0.05, -0.04), amp=var.brk
)
vv >> play('v', sample=3, rate=PWhite(0.95, 1), dur=0.5, delay=0,
    lpf=P[
        var([100, 110], 128) * var([1, 1.25, 1.5], [32, 16, 16]),
        P[
            var([70, [90, 90, 70, 90]], 128), 70
        ] * var([1, 0.5], [28, 4, 31, 1, 64, 0]) * var([1, 0.5], [64, 0, 3, 1, 3, 1, 2, 1, 1, 1, 2, 2, 2, 2])
    ] * 1,
    bend=(-0.25, 0),
    lpr=P[PWhite(0.25, 0.5), 0.5],
    amp=1.2 * var.brk
    # * P[1, [0, 0.5, 0, [0.5, 0]]]
    # * P[1, [0.25, 0, 0, 0], 1, [0, [0, 0.25], 1, [0, 0, 0, 1]]]
    # * 0
)
jb >> bass(dur=0.5, lpf=70, bend=1, sus=P[0.5, 0.25, 0.15, 0.5,  0.5, 0.25, 0.5, 0.1], amp=expvar([0.7, 0.4], [4, 0]) * var.brk * var([0, 1], [32, 32, 64, 64]) * vv.amp)

cp >> play('HHHHH <H >HH[HH]', sample=PRand(0, 1), fmod=1, pan=P[-0.25, 0.25], lpf=P[1500, 4000, 2000, 3000] * 1.15 * expvar([0.5, 2], 32), dur=0.25, amp=1 * var([0, 1], [31, 1, 28, 4, 31, 1, 60, 4]))
#cp.degree = 'wHHwHH<wH>'
cb >> play('~', room=1, mix=0.1, rate=P[1, 1.25, 0.95, 1], sample=20, pan=PWhite(-0.5, 0.5), lpf=expvar([1500, 8000], [2, 0]), dur=0.25,
    amp=var([1, 1, 0], [128, 128, 0]) * expvar([0, 1], [128, 128, 0, 256]) #* var.brk
) # remove brk?
oh >> play(('-', '='), delay=0.5 + PWhite(-0.025, 0.025), pan=P[-0.25, 0.25] * var([1, 0], 32), sample=(11, 5), sus=0.05, dur=1, lpf=6000,
    amp=var([0, 1], [32, 64, 32, 32, 64, 64, 32, 128]) * var([0, 1], [64, inf])
)
sh >> play('s', sample=1, dur=1, delay=0.5, amp=var([0, 1], [64, 128, 64, 64, 32, 128]))
sn >> play('o', dur=2, delay=PWhite(-0.025, 0.025), sample=11, lpf=7000, amp=1.5 * var([1, 0], [64, 32, 128, 64, 64, 64, 256, 64]) * expvar([0, 1], [64, inf]))
jn >> play('L', rate=1, sample=19, dur=0.25, cut=0.25, room=0.5, mix=P[0.1, 0, 0], lpf=expvar([1500, 3000], 16), lpr=P[0.2, 0.5], delay=0.5, amp=P[1, 0.75] * expvar([0, 0, 1, 1], 128))
fh >> play('n', delay=PWhite(-0.015, 0.015), sample=14, fmod=1, pan=expvar([-0.25, 0.25], 4), rate=expvar([1, 0.75], [0.5, 0]) * P[1.1, PWhite(1, 1.05), 1, 1], dur=0.25,
    lpf=P[1, 1.25, 1.5, 1] * expvar([4000, 2000], [1, 0]),
    amp=expvar([0, 0, 1, 1], [64, 64, 64, 0])
)
ww >> play('w', sample=0, tremolo=4, rate=0.5, formant=1, lpf=expvar([200, 800], 128), dur=2, delay=P[0, 0.5], amp=0.65 * expvar([0, 0, 1, 1], 64))
ee >> play('<euTT><[ee]>', sample=5, dur=0.5, tremolo=4, lpf=expvar([500, 2500], 16), lpr=0.3, fmod=0.85, amp=0.8 * P[1, expvar([0, 1], 128), 1, 1] * expvar([1, 0.5], 128) * expvar([0, 1], [64, inf]))
b2 >> play('b', sample=5, fmod=1, formant=1,
    lpf=P[var([300, 200], [31, 1, 28, 4, 31, 1, 56, 8]), 400] * expvar([1, 1.25], 32), lpr=PWhite(0.7, 1),
    amp=expvar([0, 0, 1, 1], [128, 128, 128, 0]) * P[1, 1, 1, 1, 0, 1, 1, 1]
)
ww >> play('T', sample=11, rate=P[0.5, PWhite(0.5, 1.5)], formant=1, room=1, mix=0.2,
    lpf=expvar([300, 800, 900], 24), dur=1.5 * var([2, 1], [32, inf]), amp=PWhite(0.3, 0.45) * 0.75 * expvar([0, 1], [64, inf])
)
b1 >> play('b', sample=PRand(2, 8), dur=8, room=1, mix=0.2, hpf=50, amp=1)
sr >> siren(oct=var([[6, 5], 7], 64), room=1, mix=PWhite(0, 0.25), fmod=PWhite(0, 1), chop=1,
    hpf=P[expvar([300, 8000], 24), 500, 400, 250, [300, 800], 450, 200] * expvar([1.5, 1], 16),
    hpr=expvar([0.8, 0.25], 28), dur=0.25,
    amp=P[[1, var([0, 1], 32)], var([0, 1], 16), 1, 1] * expvar([0, 0, 1], [64, 64, inf]) * var([1, 0], 256)#* var([1, 0], [3, 1, 2, 1, 4, 2, 2, 2])
)
d3 >> play("n(...n)(..[nn])(.n)n", dur=1,
    rate=1 + P[7/12, 3/12, 8/12],
    lpf=6000,
    sample=[2, PRand(8)], cut=var([2/4, 3/4], 4), echo=0.25,
    amp=PwRand([0.2, 1], [2, 8]) * expvar([0, 1], [64, inf])
)
so >> play('S', rate=P[1.1, 1.05, 1], sample=27, lpf=expvar([4000, 10000], [64, 0]), sus=1, dur=P[0.5, 0.25, 0.25], amp=P[0.5, 1] * var([1, 0], [1.5, 2.5]) * var([0, 1], 256))
er >> klank(dur=8, rate=linvar([0.6, 1.2], 128), oct=(3, PStep(16, 5, 4)), lpf=3000, amp=0.35)

Group(xx, x2, x3, x4, vv, jb).stop()
Group(cb, oh, sh, sn, jn, fh, ee, so).stop()
