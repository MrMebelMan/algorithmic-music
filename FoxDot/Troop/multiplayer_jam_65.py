# By KittyClock and GGERKK

Clock.set_time(0)

print(SynthDefs)

print(Samples)

db >> dafbass(dur=0.5, lpf=P[500, 400, 450, 475] * 1.5, drive=0.05, chop=0, sus=P[0.5, 0.25, 0.25, 0.25] * 1, amp=1.25 * 0.0000)
d2 >> dafbass(dur=4/3, lpf=db.lpf, hpf=1000, hpr=0.5, sus=P[0.25, 0.1, 0.2, 0.2], amp=0.75 * db.amp)

aa >> play('X', rate=var([1, 1.5], [28, 4, 31, 1, 28, 4]), pan=PWhite(-0.5, 0.5), sample=4, room=1, mix=0.1, lpf=1200, lpr=0.1,
    dur=2 * P[[1] * 7 + [0.5, 0.5] + [1] * 2 + [0.5] * 4 + [1] * 16],
    amp=P[1, 1, 1, 1] * 1.25 * var([1, 0], [[31, 28, 56, 128], [1, 4, 8, 64]])
).stop()

xx >> play('x', sample=2, dur=4, lpf=700, delay=0.75, amp=1 * aa.amp * var([1, 0], [64, 32, 128, 64])).stop()
x2 >> play('x', sample=[0,3], dur=2, lpf=900, delay=0.5, amp=P[1, [0.25, 0.3, 0.25, 0.5]] * aa.amp).stop()
mm >> play('v', sample=0, dur=0.25, amp=expvar([0.25, 1], [1, 0]) * 1 * aa.amp).stop()

rs >> play('s', pan=PWhite(-0.25, 0.25), rate=PWhite(0.99, 1), sample=6, dur=1, delay=0.5, amp=0.75 * 0.85 * var([0, 1], [32, 64, 32, 128, 64, 64])).stop()
fh >> play('-', dur=0.25, amp=expvar([1, 0.25], 1/3) * rs.amp * expvar([0, 1, 1], [128, 64, 0])).stop()
ss >> play('S', sample=1, dur=0.5, amp=P[0.5, 1] * 0.35 * 0)

fs >> sawbass(P[0, 0, -1], dur=0.5, sus=P[0.1, 0.25, 0.1], formant=var([1, 0], 32), room=1, mix=0.25,
    hpf=var([[200, 250, 180, 300], [700, 600, 500, 800]], 16) * 1,
    hpr=0.5, drive=var([0.05, 0], [28, 4]) * 0, amp=0.85 * 0.1,
    glide=var([var([4,-3,0],[2,1,5]),0],16)
)

# very excited to dive into these samples etc.!! Thanks for your help sorting it out.

# thank you for the jaaaam!

#beautiful

# <3

# AGAIN SOON!!! Peace!


g1 >> play("c", sample=P[6,2,var([3, 2], 32),var([4, 2], [28, 4])] + var([0, 1, 2, 0, 3], 8), dur=var([2,3],[12,4]), chop=P[2,4,8].shuffle(3), rate=var([1,-1],[26,4]), formant=[0,0.2], amp=P[1, 0] * expvar([1, 0, 0], [128, 128, 0]), pan=PWhite(-0.5,0.5), room=0.8, mix=0.7)

g2 >> xylo(P[2,5,8,8.2].shuffle(10), room=1, mix=0.25, echo=P[0.5, 0, 0, 0], amp=0, oct=7,  pshift=linvar([0,3],32))

g3 >> jbass([var([7,9],[6,2]),2,var([-4,-5],8),PStep(4,-3)], room=1, mix=0.25, dur=0.5, amp=0, oct=5, formant=1, hpf=expvar([800, 300], 128), hpr=0.2, shape=0.5 * 0, lpf=0 * P[750, 500, 1200, 800], lpr=1.1)

