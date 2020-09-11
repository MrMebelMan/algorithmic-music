# https://soundcloud.com/kitty_clock/expanding-symmetry

Clock.bpm = 125
var.bass_drop = var([1, 0], [[512, 256], [128, 64]])
bs >> bass(bend=-0.25, tremolo=4, delay=var([0, 0.5], 512), slide=0.1, lpf=var([500, 400, 300, 200], [32, 64, 64]), lpr=0.1,
    amp=P[
        1, [expvar([0, 1, 1], [256, inf]), expvar([0.25, 1, 1], [256, inf]), 1, 1], var([0, 1, 1], [64, inf]), expvar([0.5, 1, 1], [128, inf])
    ] * var.bass_drop # * expvar([1, 1, 0, 0], [2496, 16, inf])
)
b2 >> bass(dur=1,
    sus=P[var([0.5, 0.1, 0.25, 0.1, 0.5], 64), 0.25, expvar([0.15, 0.75], [128, 0]), 0.25],
    oct=P[5.25, var([5.20, 5.25], [32, 64, 32])],
    tremolo=P[var([4, 2], [16, 8]), 2, var([2, 4, 2, 8], 16), var([2, 4], 8)],
    amp=expvar([0, 0, 1, 1, 1], [64, 32, 128, inf]) * var.bass_drop * var([1, 0, 0], [2304, inf])
)
kb >> bass(dur=1, sus=0.5, delay=0.5, lpf=500, lpr=0.5, amp=P[1, 0, 0, 0] * var([0, 1, 0, 0], [1280, 256, inf]) * var([1, 0, 0], [2496, inf])) # * bass_drop?
sb >> sawbass(dur=0.25, sus=2, chop=4, lpf=300, lpr=0.1, hpf=400, hpr=0.1, amp=expvar([0, 0, 0.5], [[32, 16, 8, 8, 32], 1, [15, 31]]) * var([1, 0, 0], [2496, inf]))
jb >> jbass(dur=0.25, cut=1, sus=2, chop=4, hpf=P[700, 500, 800, 350], hpr=0.15, amp=expvar([0, 0, 1, 1], [64, 8, 56, [32, 16, 8, 4]]) * var([1, 0, 0], [2496, inf]))
vv >> play('V', rate=P[1, 0.99, 1, 0.95] - var([0, 0.05], 64), dur=1, sample=8, hpf=60, hpr=0.25, lpf=5000, lpr=1,
    amp=expvar([0, 0, 1, 1], [[512, 128], 8, [120, 248]]) * var.bass_drop * var([1, 0, 0], [2496, inf])
)
xx >> play('x', sample=3, dur=1, lpf=950, lpr=0.1, amp=P[var([0, 1], 512), 1] * var([1, 0, 0], [2496, inf]))
sn >> play('I', sample=var([2, 1], [256, 128]), dur=var([1, 2, 2], [2048, inf]),
    delay=[[0, var([0, 0.5], [64, 128])], var([0.5, 1.5], 256)],
    room=1, mix=0.25,
    echo=0.5, echotime=1,
    amp=expvar([0, 0.65], [128, 64])
)
oo >> play('-', sample=2, room=1, mix=0.25, dur=2, delay=[0.5, 0], amp=var([0, 1], [128, 256]) * var([1, 0, 0], [2048, inf]))
h1 >> play('s', dur=1, delay=0.5, lpf=expvar([3000, 6500], [128, 256]), lpr=0.25,
    amp=expvar([0, 1.5], [0, 128]) * var([0, 1, 1], [128, inf]) * var([1, 0, 0], [1536, inf])
)
cl >> play('*', delay=1, dur=2, amp=expvar([0, 0, 0.5, 0.5], [128, 128, 128, 0]) * var([1, 0, 0], [2048, inf]))
tt >> play('t', sample=2, dur=0.25, lpf=1250, lpr=0.1, amp=expvar([0.25, 1, 0.5, 1.25], [2, 0]) * expvar([0, 1, 1], [128, inf]) * var([1, 0, 0], [1920, inf]))
fl >> feel(dur=8, sus=4, oct=6, tremolo=2, drive=0.1, lpf=700, lpr=0.25, amp=expvar([0, 3.5, 3.5], [64, inf]))
ee >> play('E', dur=[1] * 15 + [0.5, 0.5], lpf=expvar([450, 350], [64, 0]), lpr=0.1, amp=var([0, 0.35], [256, 64, 128, 32, 128, 64, 128, 32]) * var([1, 0, 0], [1664, inf]))
sw >> play('w', room=1, mix=0.25, sample=1, rate=0.35, dur=PWhite(8, 32), amp=0.65)
ta >> play('m', dur=8, amp=var([0, 1], [256, 128]) * var([1, 0, 0], [2304, inf]))
rc >> play('~', dur=0.25, amp=var([0, 1], [[28, 56, 31, 31, [64, 7]], [4, 8, 1, 1, [0, 1]]]) * expvar([0.05, 1.5], [[4, 8, 1, 1, 1], 0]) * var([1, 0, 0], [2304, inf]))
fs >> play('h', dur=var([8, 4], 256), delay=0.5, amp=expvar([0, 0.6], 512) * var([1, 0, 0], [2304, inf]))
cb >> play('T',
    rate=var([1, 1.15], [32, 64]),
    sample=1,
    lpf=expvar([700, 1100], [[64, 32], 0]),
    dur=0.5,
    amp=P[0.5, 1] * 0.5 * expvar([0, 0, 1, 1], [[128, 64], [64, 128], [128, 256], 0]) * var([1, 0, 0], [1536, inf])
)
wb >> play('d', dur=[4, 4, 4, 2], delay=[0, 0.5], amp=expvar([0, 0, 1, 1], [[256, 64], 128, [256, 128], 0]) * var([1, 0, 0], [1920, inf]))
tb >> play('p', sample=1, dur=0.25,
    amp=P[1, 0.5, expvar([0.25, 0.85], [8, 4]), P[0, var([0.5, 0], [128, 64]), 0, 0.15]] * var([0, 1], [512, 256, 128, 64, 128, 128]) * var([1, 0, 0], [1920, inf])
)
sc >> play('S', dur=0.5, amp=P[0.5, 1] * 0.5 * var([0, 1], [[640, 128, 256], [256, 64, 128]]) * var([1, 0, 0], [2304, inf]))
ll >> play('L', sample=1, dur=1, delay=0.5,
    amp=0.25 * var([0, 1], [[[1024, 128], 128, 64], [128, 64, 32]]) * var([1, 0], [[28, 32, 31, 32], [4, 0, 1, 0]]) * var([1, 0, 0], [2176, inf])
)
