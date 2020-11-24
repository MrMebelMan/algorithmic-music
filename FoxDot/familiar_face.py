# https://soundcloud.com/kitty_clock/familiar-face

Clock.bpm = 90
v1 >> play('v', rate=var([[1.1, 1], 0.9], 64), lpf=expvar([80, 180, 180], 128), lpr=expvar([1.6, 1.1], 64), sample=0,
    dur=P[1, [1, 1, 1, var([1, 1], [32, 32, 64])], var([1, 1], [32, 32, 64])],
    amp=var([0.5, 0.55, 0.6], 128) * var([0, 1], [64, 128, 64, 256]) * 1.2
)
v3 >> play('v', rate=1, lpf=80, lpr=1.6, sample=0, bend=-0.25, delay=0.5, dur=1, amp=P[0.4, 0])
v2 >> play('v', rate=P[0.95, 1, 0.9, 1] * 1.2, lpf=expvar([5000, 500], [32, 8, 8]), lpr=expvar([1, 0.2], 128), sample=1, dur=0.25,
    amp=P[0, 0.75, 0.85, 0.8] * 1.5 * var([0, 1], [[3, [3, 3, 2]], 1])
)
sn >> play('I', room=0.7, mix=0.1, dur=2, amp=P[PWhite(0, 0.25), 1] * var([0, 1.1], [32, [32, 64], 32, 64, 32, 128, 64, 256]))
sh >> play('s', room=1, mix=0.2, dur=4, delay=0.5, amp=P[0, 1] * var([2, 0], [256, 64]))
h1 >> play('-', sample=var([3, 4], [128, [64, 32]]), pan=PWhite(-0.5, 0.5), lpf=expvar([2500, 5500], [64, 128]), echo=P[0, 0, 0, 0.125], echotime=expvar([0.25, 0.125], 8), dur=0.125,
    amp=expvar([1, 0.5], [3, 1]) * P[1, 0, 1, 1,  1, 1, 1, 1] * var([1, 0], [3, 1, 3, 1, 2, 2, 1, 3]) * var([0, 1], [[64, 128], 128, 32, 128, 64, 256])
)
xx >> play('x', sample=1, dur=1, amp=var([0, 1.25], [[64, 32], [256, 128]]))
bp >> blip(dur=8, sus=4, delay=0.5, chop=16, striate=0, tremolo=0.125, formant=0.25, room=1, mix=0.25, lpf=600, lpr=0.2, amp=expvar([0, 1, 1], [64, 128, 256]))
sb >> sawbass(
    oct=var([5, 7], 128),
    tremolo=4,
    dur=[4, 2],
    hpf=expvar([0.5, 0.15], [32, 16]) * P[650, 700], hpr=expvar([1, 0.25], 128) * expvar([0.7, 0.5], [4, 0]),
    amp=expvar([0.5, 1], [2, 0]) * 0.8
)
nn >> play('n', dur=1, delay=0.5, amp=0.7 * var([0, 1], [[32, 64, 128], [64, 128, 256]]) * var([1, 0], [[28, 64], [4, 0], [31, 63], 1, 56, 8]))
cl >> play('H', sample=2, dur=1, delay=P[0.25, 0], amp=P[[0, 0, 0, 0.5], 1] * 0.3 * var([0, 1], [[64, 32], 128]) * var([1, 0], [56, 8, 32, 0, 8, 8, 8, 8, 32, 16, 16, 120, 8, 128, 0]))
rc >> play('~', rate=P[[0.75, PWhite(0.5, 0.75)], 0.5, PWhite(0.2, 0.35)], room=P[0.25, 0.5, 0.75], mix=0.5, sample=1, dur=0.5, amp=0.8 * var([0, 1], [[5.5, 5.5], 1.5]) * expvar([0, 1, 1], [64, inf])) # 5.5 -> 4.5?
tt >> play('T', rate=0.5, dur=var([6, 5, 3, 2], [64, 64, 128, 256]), delay=P[0, var([0, 0.5], [[64, 32], [128, 64]])] - 0.025, tremolo=2, formant=expvar([1, 0.25], [64, 128]), room=expvar([0.5, 1], 128), mix=expvar([0.2, 0.4], 64), amp=expvar([0, 1], [64, inf]) * 0.75)
b2 >> jbass(dur=0.25, sus=2, chop=8, hpf=var([1500, 500], [28, 4]) * PWhite(0.9, 1.1), hpr=0.05, amp=var([1, 0], [1, 3]) * expvar([0, 1, 1], [64, 128, 128]) * var([1, 0], [[64, 56], [0, 8]]))
