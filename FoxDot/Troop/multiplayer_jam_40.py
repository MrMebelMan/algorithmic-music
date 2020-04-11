Clock.bpm = 133

print(Samples)

var.brk = var([1, 0], [31, 1, 31, 1, 28, 4, 56, 8])

vv >> play('v',
    dur=0.25,
    lpf=100,
    lpr=[0.25, [0.25, 0.5], 0.25, 0.25],
    amp=expvar([1, 0.1], 1/3) * 0.85 * var.brk * 0
)
jb >> jbass(dur=1, sus=[1, 0.5], tremolo=4, hpf=100, hpr=0.25, amp=vv.amp * 3)

h1 >> play(':', pan=PWhite(-0.7, 0.7), room=1, mix=0.25, dur=0.25, amp=expvar([1, 0], [4, 4, 2, 4, 8]) * var([1, 0], [4, 8, 4, 16]))
tt >> play('t', dur=0.25, sample=1, lpf=1500, lpr=0.25,
    amp=P[0.75, var([1, 0], [64, 32, 32, 128, 32, 32]), 0.5, 0.25,  [var([0, 1], 196), var([0, 1], 128), var([0, 1], 196), 1], [0.5, 0.25], 0.25, 0] * var([1, 0], [[512, 256], [256, 128]])
)
cl >> play('H', room=1, mix=0.2, sample=1, dur=var([16, 8], [128, 256]), delay=0.75, amp=0.45)
c2 >> play('H', sample=2, dur=var([8, 4], [128, 256]), delay=0.5, amp=0.4)
ss >> play('s', sample=1, room=1, mix=0.15, dur=0.5, lpf=expvar([3000, 9000], [256, 0]), lpr=expvar([0.5, 0.25], [256, 0]), amp=P[1, 0.9] * 0.35)
sh >> play('s', sample=2, room=1, mix=0.15, lpf=ss.lpf, lpr=ss.lpr, dur=0.25, delay=0.5, amp=P[0.9, 1] * 1 * ss.amp)
pd >> pads(
    dur=0.25,
    room=1, mix=0.1,
    sus=var([1, 1/2], [64, 128]),
    chop=var([4, 2], [64, 128]),
    lpf=var([500, 300], [14, 2, 28, 4, 14, 2, 14, 2, 8, 8]), lpr=0.25,
    amp=P[1, 1, 1, 1] * expvar([0, 0.75], 256)
)
bw >> sawbass(dur=[0.5, 0.25, 0.25], hpf=P[[400, 800], [500, 250, 400, 550], [600, 700, 650, 200]], hpr=0.25, amp=P[1, 1, 1, 1, 0, [0, var([0, 0.5], 128)], var([0, 1], 64), 0] * expvar([0, 1], [128, 128, 256, 256]))
kd >> play('X', sample=5, dur=1, room=1, mix=0.1, lpf=500, lpr=0.5, amp=P[1, 1, 1, var([1, 0], [256, 64])] * 1.5 * var.brk)
ch >> play('-', sample=2, room=1, mix=0.15, dur=1, delay=0.5, amp=P[1, [0.9, 0.88]] * var([0, 1.2], [[64, 128], [128, 256]]) * var.brk)
rs >> play('I', dur=var([8, 4, 2], [[64, 128], [64, 128], [32, 64]]), amp=expvar([0, 2, 2], [128, 128, 0]) * var.brk)

@next_bar
def stahp():
    Group(rs, s1, rs, ch, kd, ss, sh, cl, c2, jb, vv, tt, pd, s3, h1).stop()


s1 >> dab([-1,5]+P[:2],oct=5,dur=4,delay=[0,1/2],sus=[2,1/2],echo=1/2,room=2/3,mix=1/3,lpf=linvar([500,1700],16),pan=(-2/3,2/3),amplify=2/5,amp=1)

s2 >> dbass([0,1]+[0,1,-1,3,-2],oct=6,dur=1/4,drive=1/4,formant=linvar([1,5],8),lpf=400,amplify=1/7,amp=1)

s3 >> donk(s2.degree,oct=6,dur=1,sus=1/4,delay=[0,1/2],formant=3,shape=2/7,amplify=6/7,amp=1)






