Clock.bpm = 143
Scale.default = "minor"
Root.default = -2

print(SynthDefs)

print(Samples)

print(Attributes)

h1 >> play(':', room=1, mix=0.2, dur=1, delay=0.5, amp=var([0, 0.45], [[[128, 64], 64, 32], [[256, 64], 128, 64]]) * var.brk * kd.amp)
sh >> play('n', room=1, mix=0.25, sample=2, dur=1, delay=0.5, amp=h1.amp * var([0, 1], [[32, 64, 32], [64, 128, 32]]) * var.brk)
rs >> play('I', room=expvar([0, 1], [128, 0]), mix=0.2, dur=1, amp=expvar([0, 0, 1], [[32, 64], 128, 0]))
cl >> play('*', sample=0, dur=var([8, 4], [128, 64]), delay=0.5, amp=var([0.85, 0], [[128, 64], [64, 32]]))
kd >> play('X', sample=var([1, 2], [256, [128, 64]]), rate=1.05, dur=1, lpf=var([650, 500, 700, 450], 128), lpr=var([0.5, 0.25], 64), amp=P[1, 0.85] * var([1, 0], [[128, 256], [64, 128]]) * 0.9)
tt >> play('t',
    pan=PWhite(-0.5, 0.5),
    dur=0.25, sample=1, lpf=P[250, PWhite(200, 500), [300, 500], [250, 300, 450, 200, 700]] * expvar([2, 5], [128, 0]),
    amp=Pvar(
    [
        P[[0.75, 0.35], 0, 0, 0, 0.25, 0.5, 0.75, 1],
        P[1, 0.85, 0.5, [1, 0.5, 0.25], 0.25, 0.5],
    ], 128) * var([2, 0], [[512, 256, 64], [256, 128, 32]])
)

ss >> play('s', pan=PWhite(-0.75, 0.75), dur=0.25,
    amp=expvar([1, 0], [4, [8, 4, 0]]) *
        P[PWhite(0, 1), [0.25, 0.5], 0.25, 0.75] *
        var([2, 0], [256, 64, 128, 64, 32, 64, 64, 32])
)

p0 >> play('2', 
    lpf=var([1600,800],[16,32]), 
    lpr=0.45, 
    amp=linvar([0.2, 0.45],16), 
    dur=4, room=expvar([0,1],16), 
    mix=0.2, echo=linvar([0.02,0.35],32), 
    chop=4, 
    sus=4).every(8, 'alt', var([3,1],4))

cl >> play('*', 
    amp=var([0, 0.35], [128, 64, 32, 32]) *var.brk, 
    dur=var([8, 4, 2], [[64, 128], [64, 128], [32, 64]]), 
    echo=0.2).every(16, 'stutter', lpf=1500, lpr=0.45, echo=0.45)

sn >> play('!',
    room=1, mix=0.2,
    pan=PWhite(-0.75, 0.75),
    rate=[0.35, 0.25, 0.3],
    chop=4, sus=4, echo=0.2, dur=P[2,4,[16, 2]], )


xx >> play(
    "I  V  M  ", room=1, mix=0.35, dur=1
    , lpf=var([200,800],8) * 3
    ).every(16,'stutter')
xy >> space(
    P[2,4,6,9], dur=[8,8,4,4]
    , room=var([0.3,0.6],16)
    )
xz >> ripple(
    P[0,1,2], dur=1    , pan=PSine(5)
    , chop=22
    )
yy >> sawbass( [0], dur=4, pan=PStep(3,[-0.5,0.5])
    , chop=10
    ).every(16,'stutter')


var.brk = var([1,0],[31,1,28,4,56,8,31,1,32,0,32,0,31,1])
var.notes = var([0,1,0,3,0,1,0,4],4)
note = PRand(Scale.default)

s1 >> blip(var.notes,oct=6,echo=var([1,1/2],[14,2]),room=1/3,mix=1/3,amplify=3/3,amp=1)

s2 >> karp((var.notes,var.notes+P[:2]),oct=PRand([4,5]),dur=var([1/2,PDur(3,5)],[24,8]),shape=1/3,pan=PWhite(-1,1),amplify=2/3,amp=1*var.brk)

s3 >> arpy((var.notes,note),oct=5,dur=PDur(5,8),shape=1/3,formant=linvar([1,3],[4,8,4,16,32,8,16,8]),lpf=linvar([400,2000],[4,8,4,16,32,8,16,8]),amplify=4/6,amp=1*var.brk)

s4 >> space(var.notes,oct=5,dur=1,sus=1/2,formant=1,room=1/3,mix=1/3,hpf=linvar([400,1200],16),hpr=2/3,amplify=6/5,amp=1*var.brk).offbeat()

