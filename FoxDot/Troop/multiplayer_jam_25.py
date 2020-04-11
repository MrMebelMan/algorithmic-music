Clock.bpm = 133 * 2
Scale.default = "minor"
Root.default = -2

print(Samples)
print(SynthDefs)
print(Attributes)

var.brk = var([1, 0], [[31, 1, 31, 1, 28, 4, 56, 8, 32, 0], 1])

rs >> play('I',
    pan=PWhite(-0.75, 0.75),
    dur=0.5,
    amp=P[
        [0.25, 1], 0.5, 1, 0.75, [0.25, var([0.25, 0.5, 0.75], [64, 32])], 0.5, 0.75
    ] * var([0, 1.25], [28, 4, 56, 8, [28, 31], [4, 1]])
)

dl >> play('$', dur=2, amp=P[1, 1] * var([0, 1], [[64, 32, 128], [256, 32, 64]]))
d2 >> play(degree=dl.degree, dur=dl.dur, delay=0.5, amp=P[1, 0, 0, 0] * dl.amp * var([0.5, 0], [32, 32, 64, 128, 64, [64, 32]]))

rr >> play('r',
    rate=0.95,
    pan=PWhite(-0.5, 0.5),
    dur=0.25,
    drive=[0.15, 0.25, [0.15, 0.2], 0.3],
    lpf=expvar([5000, 1500, 4000, 500, 3500, 850], [32, 32, 64, 64, 128, 128]), lpr=expvar([0.25, 0.5], 8),
    amp=P[[0.15, 0.25], [0.25, 0.85], P[0.05, 0.03, 0.06, 0.07] * 1.5, [0.5, 0.25]] * var([0, 1], [128, 64, 32, 64, 32, 64, 128]),
    cut=P[var([[0.25, 1], 0.5, 0.75], 64), var([0.25, [0.75, 1.25], 0.5, 1, 0.5], [128, 64, 64]), var([1.5, [0.5, 1], 0.25, 0.5, 1], [32, 64, 128, 64, 128])]
)

h1 >> play('-', sample=var([1, 2, 0, 2, 2], [64, 128, 64, 64]), room=1, mix=0.25, dur=n0.dur * 2), delay=0.5, amp=var([0, 1], [[128, 64, 32], [256, 128, 64]]) * var.brk)

h2 >> play(':',
    sample=var([0, 1, 2, 1], [128, [64, 128]]),
    dur=0.25,
    hpf=expvar([150, 2500], [[128, 64, 64], 0]), hpr=0.25,
    amp=expvar([1, 0], 1/4) * P[1, 0.85, 1, 0.75, 0.25]
)
kd >> play('X', rate=P[1.1, 1.05, 1.1, 1], drive=0, sample=2, dur=2, lpf=250, lpr=0.25, amp=var([1.25, 0], [[256, 128], [64, 32]]) * var.brk).every(128, 'stutter', 2)
bp >> blip(0, dur=kd.dur, delay=0.5, tremolo=2, amp=P[2, 1, 2, 2, [1, 2], 1, 1, 1] * var.brk * expvar([0, 0, 1], [[128, 64], [256, 128], [256, 64]]))
b2 >> blip(2, dur=kd.dur / 2, delay=0, lpf=[500, 600, 800, 1000], amp=P[0, 1, 0, var([0, 1], [[128, 64], [256, 32, 64]])] * 0.75 * var.brk * bp.amp)
sn >> play('O', rate=0.95, sample=1, dur=4, amp=expvar([0, 0, 0.75, 0.75, 0.75], [[32, 64], [64, 128], [64, 128], 128, 0]))
tt >> play('u', dur=2, delay=1, amp=P[2.5, 2] * var([1, 0], [128, 64, [64, 128], [128, 64], 256])).every(128, 'stutter', 2)
cl >> play('*', dur=var([8, 4, 2], 64), delay=0.5, amp=var([0, 1], [[32, 64], [128, 256]]) * 1.25)
rk >> play('X', sample=2, rate=-1, dur=2, amp=var([0, 1.25], [[63, 63, 31], 1]))

dk >> play('V',
    sample=P[2, 4, var([0, 1, 2, 1, 0], [[32, 128], [16, 64], [8, 128, 64], 8, 4, 4, 4, 4, 16, 32, 32]), var([0, 2], [128, 64, 32])],
    rate=P[1, var([1, 0.95, 0.85], [128, 64]), 1, 1,  [1, var([0.95, 1], [64, 32, 128])], 1, var([1, 1.1, 0.9, 1.15], [128, 64, 32, 32, 32, 32]), 1] * 1.25,
    drive=var([0,1.5],8),
    coarse=var([0,2,4],[256,128]),
    sus=1,
    hpf=var([600, 800, 400, 500, 750, 400, 350, 600], [[32, 4], 8, [8, 4], 8, 8, 16, 16, 64, 32, 8, 8, 16, 32]),
    hpr=[var([0.35, 0.25], 128), 0.25, 0.25, var([0.4, 0.25], 128)],
    amp=P[
        1, [var([0.75, 1], 128)], 1, 0.5, var([0.25, 1], 32), 0.75, [1, 0.5], [0.85, var([0, 0.5], [64, 128, 32, 32])]
    ] * expvar([0, 0, 0.5, 0.5], [[32, 64, 128], [32, 64], [64, 128, 256], 0]) * var.brk
).every(8, 'stutter', echo=0.02)

ss >> play('S', dur=2, delay=0.5, amp=0.75)

n0 >> play('V[ss]', lpf=var([800,1500],[[16,32],4]), lpr=0.25, amp=var([0.75,0.45],1), dur=2).every(2, 'stutter', echo=0.02, room=1, mix=0.25, lpr=0.35)
k2 >> play('X', sample=1, rate=1.5, drive=0.25, dur=2, hpf=var([200, 420, 180, 500, 250, 400], [[128, 64], [64, 32]]), hpr=0.25, amp=P[1, var([1, 0.85], 256)] * 1 * var.brk)

ee >> sawbass(drive=0.05,var=Pvar([2,4]), oct=6, room=0.5, mix=0.35, amp=0.5*expvar([0.25,1],64), lpf=[1500, 3000], lpr=[0.25, 0.45], dur=PDur(var([2,4]),4))
ef >> space([1,1,2,3], echo=0.5, oct=3.25, sample=sinvar(32,53), amp=Pvar([0.5,2]), lpr=[0.3, 0.7], lpf=[1500,3000], dur=[1/2,1])
en >> swell(ef.pitch, room=2, amp=0.6, mix=0.25, lpf=[1000,2500], hpf=[4000,5500], lpr=[0.1,0.2])
ez >> play("z ", amp=0.5, dur=[0.25,1]*expvar([0.3,0.2],2),lpf=[500,1000])
ef.stop()
#it's enough for me, thank y'all guyz
#enjoy
od >> play('T', dur=16, chop=8*var([0.25,1],[32,16]), sus=4, echo=0.02).every(4, 'stutter', echo=0.2, room=1, mix=linvar([0,0.25],4))

le >> bass(
    var(P[0,-2,0,1,3], [[128,64],[255,2]]),
    dur=var([32, 16, 8, 4, 2, 1], [64, 128, 64, 32, 32]),
    lpf=P[1500, 1250, 1000, 1000, 500, 500, 500, 500],
    lpr=expvar([0.75, 0.25], 128),
    drive=P[0, [0, var([0, 0.05], [64, 32])], 0, 0,  0, 0, 0, 0],
    amp=0.25*b2.amp,
    pshift=var([-0.25,0],[2,256]),
    echo=0,
    sus=2,
    chop=16
)

ex >> sinepad(lpf=expvar([0,4],[256,128])*var([800,3000],[[16,32],4])*expvar([4,0],[256,128]), lpr=0.25, amp=var([1, 0], [[256, 128, 64], [128, 64, 32]])*var.brk*expvar([0,1],8)).every(32, 'stutter', pan=[-1,1], spin=64, lpr=0.45)


da >> play('V', rate=var([1,-1],[510,2])).every(16, 'stutter', lpf=1500, lpr=0.45)
mn >> play('X', rate=var([1,-1],[510,2])).every(16, 'stutter', lpf=1500, lpr=0.45)


Master().rate = P[[-1, 1], 1, -1, 1] * var([1,-1],[510,2])


Master().rate = 1
