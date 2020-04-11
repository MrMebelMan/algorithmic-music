Clock.bpm = 150
Scale.default = "minor"
Root.default = -2

print(Samples)

print(SynthDefs)

print(Attributes)

var.brk = var([1, 0], [[31, 28, 56, 28, 31, 32], [1, 4, 8, 4, 1, 0]])

mm >> pads(var([0,3,-1,0], 4) + (0,2,4,10),
    oct=3, dur=[0.5, 0.25, 0.25],
    amp=P[0.25, 0.5, 0.75] * expvar([0, 1.25], 128),
    glide=var([0.5,2], 4), drive=P[0.15, 0.05] * 0.5,
    hpf=linvar([500, 200], 12), hpr=0.25
)
p2 >> pads(
    P[1,3,4] + var([0,1,3],[16,16]),
    amp=0.5 * var.brk,
    dur=[0.25, 0.25, var([0.5, 0.25], [128, 64]), 0.25],
    oct=var([4, 5], [256, 218]),
    pan=linvar([-1,1], 8),
    formant=var.brk + 1
)
p4 >> space(amp=linvar([0,2],5) * var.brk, dur=[0.5,[1,1,1,1,0.5]], chop=var([5,1],[1,5])).accompany(p2)

p5 >> sinepad(P[1,[3,5]], dur=[1,3], pan=[-1,1], tremolo=2)
p6 >> sinepad(P[[5,9],[8,6]], dur=[1,7], tremolo=var([1,3],[[16,4],16,20]), amp=var.brk * linvar([1,3],12))

p3 >> play('T', 
        sample=0,
        pan=PWhite(-0.5, 0.5),
        dur=0.25,
        lpf=P[2500, 750, 1000, var([750, 500, 1000], 64)],
        amp=var([1.5, 0], [[128, 64, [32, 128]], [64, 32, [16, 64]]]) * var.brk,
        rate=P[2,-2,1,-1],  
        pshift=0,
        env=0.8,
        formant=1,      
).every(3, "stutter", 1)

bd >> play('X',
    sample=var([0, 1], [[128, 64, 32], [64, 128, 128]]),
    dur=1,
    lpf=P[1500, 1250] * 0.85,
    lpr=0.25,
    amp=P[1.15, [0.85, 0.95]] * 1.25 * var.brk * var([0, 1], [[512, 128], [256, 64]])
)
# Master().hpf = 0
# Master().hpr = 0.5
cl >> play('*', dur=var([8, 4, 2], 64), delay=0.5, amp=var([1, 0], [128, 64]) * var.brk)
rc >> play('~', pan=PWhite(-0.75, 0.75), dur=0.25, amp=expvar([0, 0, 1], [[32, 64, 128], [128, 64, 128], 0]))
m2 >> play("--- - [---]", pan=PWhite(-0.5, 0.5), dur=0.25, amp=var([0,1],[6,24]) * var.brk * expvar([0, 1], [128, 64, 64]), rate=linvar([1,3],6))
d2 >> play("t", sample=PRand(4), dur=0.25, amp=var.brk * var([0.5, 0], [[256, 64], [128, 32]]) * var([0,1],[[4,2],3]))
fl >> feel(dur=[8, 16, 16], lpf=P[500, 350, [150, 250, 500, 750]] * 2, tremolo=2, amp=var([0, 0.75], [128, [64, 128]]))
rs >> play('I', dur=var([1, 8, 4, 2], [128, 64, 64, [64, 128]]), room=1, mix=0.25, amp=expvar([0, 0, 1], [[32, 64], [128, 64], 0]))
tm >> play('m',
    rate=var([1, 0.98, 1.02, 1, 1, 0.97], [64, 128]),
    dur=0.25,
    lpf=P[300, 250, 350, 300],
    amp=P[1, [0.75, 0.5], 0.15, 0.25, 0.25, 0.5, var([0, 0.85], 128), 0] * var([0, 1.15], [64, 128, 64, 32, 64, 128]) * var.brk
)
h2 >> play('-', sample=var([1, 0, 2, 1], [128, 64]), dur=0.25, amp=expvar([1, 0.25], 1/3) * var([0, 1], [128, 64, 32, 32]) * var.brk)
kd >> play('X', sample=var([1, 2], [[256, 128], [128, 64]]), dur=1, lpf=500, lpr=0.5, amp=P[1.25, 0.95] * var.brk * var([1, 0], [[256, 64, 128], [128, 32, 64]]))
h1 >> play('-', sample=var([2, 1], [[256, 128], [128, 64, 64]]), dur=1, delay=0.5, amp=var([0.65, 0], [[128, [256, 64]], [64, 128, 32, 32]]) * var.brk * kd.amp)
sk >> play('X', sample=kd.sample, dur=1, lpf=350, delay=0.5,
    amp=P[0, var([1, 0], [128, 64, 128, 32, 32]), [0, var([0.5, 0], [128, 32, 64, 64])], 0] * var([0.75, 0], [64, 32, 64, 64, 128, 64]) * kd.amp
)
rk >> play('X', sample=2, rate=-1, dur=1, amp=var([0, 1], [[63, 127, 63], 1]))
sb >> sawbass(
    0,
    dur=0.25,
    hpf=expvar([200, [1200, 300]], [64, 32, 32]),
    hpr=0.25,
    drive=P[
        var([0, 0.025], [[128, 64], [64, 32]]), [0, 0.08], var([0, 0.03, 0], 128), var([0, 0.06], 64),
        var([0, 0.05], [128, 64, 32, 64]), 0, 0.05, var([0, 0.02], [64, 32, 8, 8])
    ],
    amp=P[1, 1, 1, 1] * expvar([0.05, 0.5], [128, 0])
)
sh >> play('s',
    pan=PWhite(-0.75, 0.75),
    dur=0.25,
    amp=P[1, 1, 1, 1, [1, 0.75, 0.5, PWhite(0.25, 1)]] * var([0, 1.25], [[256, 128], [128, 64]])
)

k1 >> blip(
    dur=[0.25, var([0.5, 0.25], 128)],
    lpf=expvar([2500, 250], [16, 32, 32]),
    amp=var([0.25, 0], [[128, 64], 64]) + sb.amp * var([0,1],[16,16]) * var.brk, oct=var([6, 5.5, 5], 64),
    formant=0.1
).accompany(p2)


@next_bar
def stop():
    Group(cl, rc, d2, kd, h1, sk, rk, sb, sh, k1, h2, rs, tm).stop()
