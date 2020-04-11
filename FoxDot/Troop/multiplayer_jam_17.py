Clock.meter = (3,4)

print(Clock.meter)

print(SynthDefs)
print(Samples)

print(Attributes)

we are down 



sc >> play('sound {check}', dur=[0.25,1,2], rate=PStep(13,-1*PWhite(0.2,0.25),PWhite(0.2,0.25)), room=1, mix=0.2, pan=(linvar([-1,1],32), sinvar([-1,1],55)))

ns >> noise(
    room=0.5,
    octave=(5,6),
    mix=[0.25, 0.1, 0.25, 0.25],
    formant=P*[[0.25,1.25], 2.25, 1.2, 3.5],
    dur=PDur([3,5],8),
    lpf=[1050, 1200, 1500, 750], lpr=[0.5, 0.75, 0.75, 0.4],
    amp=0.8,
    pan=linvar([-1,1],24),
    amplify=var([1,0],[2,[6,14,30]]),
    echo=linvar([0.25,0.8],24),
    echotime=4, 
    slide=2,
    slidedelay=0.7
    ).stop()

a1 >> sawbass((PSine(64)*0.2,PSine(45)*0.2), oct=(3,4,[5,6]), lpf=5800,lpr=0.45, sus=a1.dur*linvar([0.7,1.5],[64,0]), dur=4).unison(3, linvar([0.1,0.25],128)).stop()

rs >> play('I', room=1, mix=0.25, dur=var([16, 8, 4, 2], [128, 64, 64, [32, 64]]), amp=1.25)
h1 >> play('~', rate=[var([1.05, 0], [[128, 64], [32, 16]]), 1, 1, 1], sample=var([0, 1], [256, [64, 128]]), pan=PWhite(-0.5, 0.5), dur=0.5, amp=var([1.5, 0], [[256, 128], [[64, 32, 128], [32, 64, 128]]]))

Group(rs, h1).stop()

h2 >> play('-', room=0.85, mix=0.2, sample=2, dur=1, pan=(-0.7,0.7), delay=PWhite(0.48,0.52), amp=var([PWhite(0.9,2), 0], [[64, 128, 256], [32, 64, 128]]))

4), rate=4, pan=[-1,1])
h3 >> play('-', sample=var([1, 0], [64, 32, 32, 128, 16, 16]), dur=0.25, amp=expvar([1, 0.1], 1/3) * expvar([0, 1.75, 1.75], [128, [32, 64, 128], 0]) * 1.5)
h4 >> play('=', room=0.5, mix=0.25, pan=PWhite(-0.5, 0.5), dur=0.25, amp=expvar([0, 0, 2.25], [[64, 64, 32], [128, 64], 0]))

z8 >> sawbass(var.cho[0], dur=PDur([8,[7,5,3]],8), lpf=0, cutoff=PRand(200,500), rq=linvar([0.1,0.3],24)).stop()

z8.room = 0.9
z8.mix=0.5

var.cho = var([I,III], 8)

from .Chords import *  # :o

os >> play('s', room=1, mix=0.35, sample=1, dur=1, delay=0.5, amp=var([0, 1.25], [[32, 128, 64], [64, 64, 32]]) * var([1, 0], [[512, 256, 128], [128, 128, 64]]))

ss >> play('S', dur=1, room=0.75, mix=0.35, amp=expvar([0, 2], [[128, 256, 32, 32], 0]))

tt >> play('m', dur=0.25, delay=0.5, amp=P[0, 0.15, 0.25, 0.5] * var([2.5, 0], [[128, 64, [64, 32]], [64, 32, [32, 64]]]))

bl >> sawbass(dur=0.25,
    cut=[var([0.75, 1, 0.85, 1], [[32, 64, 128], [16, 16, 32]]), var([1, 0.5], 64), 1, 1],
    hpf=expvar([150, [1300, 400]], [[32, 64], [16, 8, 8]]),
    hpr=expvar([0.4, 0.15], [[64, 8, 8], 32, 32]),
    amp=expvar([0, 1], [0, 512])
)

dc >> play('*', dur=2, delay=0.75, amp=var([0.9, 0], [[64, 64, 128, 256, 64], [32, 64, 32, 32]]))

var.brk = var([1, 0], [[31, 28, 32], [1, 4, 0]])

Master().rate = [[[-1, -1, -1, -2], 1], 1, 1, 1]

Master().rate = 1

kd >> play('X', sample=1, dur=1, amp=var([1, 0], [28, 4]) * var([1, 0], [[128, 64, 256], [64, 32, 128]]) * 1.25 * var.brk)
sk >> play('X', sample=1, dur=1,
    delay=[0.5, [0.5, 0.75], 0.5, [0.5, 0.5, 0.75]],
    amp=P[
        var([0, 1], [[256, 128, 64, 32], [64, 32]]), var([0, 0.75, 0, 1], [64, 64, 32, 8, 8]), [var([1, 0], 8), 0], 0,
        var([0, 1], 64), var([0, 1], 64), 0, 0
    ] * var([0.75, 0], [[256, 64], [64, 32], [128, 32], [32, 16]]) * kd.amp
)

Group(bd, b2).stop()
#Group(kd, sk).stop()

bd >> play('V', sample=var([1, 0, 2], [128, 64, 64]), dur=1, lpf=1800, hpf=40, amp=1 * var.brk)
b2 >> play('V', sample=bd.sample, dur=1, delay=0.5, hpf=40, lpf=7500, amp=P[0.85, var([0, 0.85], [128, 64]), 0, var([0, 0.85, [256, 64, 32, 32]])] * bd.amp)

b2.amp = P[var([0.85, 0.5], 32), [0, 0.15], var([0.5, 0], 128), var([0, 0.5], 128)] * 1.25

Master().hpf = [100, 150, 120, 120]

bb >> gong(dur=[1,2], echo=P*[0.25,0.5], tremolo=[2, 2, var([2, 4], 64), 4], amp=0.85, rate=0.2, room=0.7, mix=0.4).unison(5,0.75)
b3 >> blip(dur=1, delay=0.5, amp=[0.35, [0, [0.15, 0.5]], 0, var([0, 0.5], [64, 32, 16, 16, 8, 8])], rate=PWhite(0.2,2)).unison(3,0.25)

sr >> play('u', pan=PWhite(-0.75, 0.75), dur=0.25, amp=P[PWhite(0.1, 0.75), [0.5, 0.25, 0.15, 0.75], 1, [0.75, 0.25]] * expvar([0, 1.15], [128, 0]))
s2 >> play('O', pan=PWhite(-0.75, 0.75), dur=0.25, amp=P[[0.25, 0.5], 0.15, [0.85, 0.15, 0.5], [1, 0.25, 0.5]] * var([0, 1], [[28, 56], [4, 8]]) * 0.75)

z5 >> play("M", amplify=var([0,1],[14,2]), lpf=800, rate=PWhite(0.7,1.5), pan=[-1,1], dur=P*[1,2,1/4,1/2,1/4,1/2,1/8,1/8])

fl >> feel(dur=16, tremolo=8, amp=1)
b2.amp = [[0.85, 0], 0, 0, 0]

z7 >> dbass(dur=PDur([3,5],8), oct=(linvar([4,6],[24,0]),linvar([7,4],[58,0])), slide=PStep(16,PwRand([PRand(2,6),-0.5],[60,40]),0), slidedealy=PWhite(0.7,0.9), amp=db.amp==0, rate=1).unison(3).stop()

sh >> play('s', sample=var([0, 1, 2], 128), dur=0.25, amp=expvar([1, 0], 4) * var([1, 0], [[4, 4, 8], [8, 8, 4, 4]]) * 2).stop()
ml >> play('T', room=1, mix=0.5, dur=15, delay=0.75, lpf=500, amp=0.35).stop()

# StageLimiter.activate(2)
clean everything , too muc lag ok


# 5 min for me

# K

# hi 

# let's start over?

# I'm AFK for a cig




#Ok I will have one too 



