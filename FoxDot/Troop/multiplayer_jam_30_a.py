Clock.bpm = 143
Scale.default = "minor"
Root.default = -2

print(SynthDefs)

print(Samples)

print(Attributes)

pl >> blip(dur=[16, 8, 8], tremolo=4, oct=4, amp=2)

db >> dub(oct=4.8, dur=0.25, lpf=1500, amp=P[1, 0.75, 0, 0,  1, 0.15, 0, [0, 0.75]] * var([0.75, 0], [[128, 64], [64, 32]]) * var.brk)
kk >> play('x', dur=1, rate=1.25, lpf=var([1250, 550], 256), lpr=0.2, amp=var([1.5, 0], [128, 32, 64, 128, 64, 32]))

print(Clock.beat % 16)

h1 >> play(':', room=1, mix=0.2, dur=1, delay=0.5, amp=var([0, 0.45], [[[128, 64], 64, 32], [[256, 64], 128, 64]]) * var.brk * kk.amp)
sh >> play('n', room=1, mix=0.25, sample=2, dur=1, delay=0.5, amp=h1.amp * var([0, 1], [[32, 64, 32], [64, 128, 32]]) * var.brk)
rs >> play('I', room=expvar([0, 1], [128, 0]), mix=0.2, dur=1, amp=expvar([0, 0, 1.5], [[32, 64], 128, 0]))
cl >> play('*', sample=0, dur=var([8, 4], [128, 64]), delay=0.5, amp=var([0.35, 0], [[128, 64], [64, 32]]))
kd >> play('X', sample=var([1, 2], [256, [128, 64]]), rate=1.05, dur=1, lpf=var([650, 500, 700, 450], 128), lpr=var([0.5, 0.25], 64), amp=P[1, 0.85] * var([1, 0], [[128, 256], [64, 128]]) * 0.85)

u1 >> play('u', dur=[1, 0.5, 0.5, 1, 1,  1, 1, 1, 1], lpf=expvar([500, 5000], [128, 0]), lpr=0.25, amp=0.45)
bd >> play('V', sample=1, rate=1.25, hpf=var([800, 400, 200], [16, 12, 4]), hpr=0.25, dur=1, drive=var([0.15, 0.25], 32), amp=P[1, [0.85, 0.5]] * var([0, 1], [256, [[128, 32], 64, 32]]))
tm >> play('m', dur=0.25, lpf=P[500, 250, [300, 150, 200]], lpr=0.25, amp=P[[0, 0.5], var([0, 1], 128), [0, 1], [1, 0, 0, 0], 0.25, [0.75, 0.5], 0.5] * var([2, 0], [128, 64]) * bd.amp)
cb >> play('T', room=1, mix=0.25, rate=[1, 1, 1, 1.05, 1, 1.05, 1.025, 1], dur=0.25, amp=P[[1, 0.5], 0.25] * var([0, 1], [128, 32, 64, 64, 32]))


# I think amp give the overall time in an composition , managing break drop build up intro outro
# Amplify does the instrument individual timing in that range the it plays
#It is switched on in drop


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
        var([1.5, 0], [256, 64, 128, 64, 32, 64, 64, 32])
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
var.notes = P[var([0,-1,-2,1],[63,32,16,16]),1,0,3,0,1,0,-1]
note = PRand(Scale.default)

s1 >> blip(var.notes,oct=6,echo=var([1,1/2],[14,2]),room=1/3,mix=1/3,amplify=3/3,amp=var([1, 0], [[256, 128], 64]))

s2 >> karp((var.notes,var.notes+P[:2]),oct=PRand([4,5]),dur=var([1/2,PDur(3,5)],[24,8]),shape=1/3,pan=PWhite(-1,1),amplify=var([3/4,0],128),amp=1*var.brk)

s3 >> arpy((var.notes,note),oct=5,dur=PDur(5,8),shape=1/3,formant=linvar([1,3],[4,8,4,16,32,8,16,8]),lpf=linvar([400,2000],[4,8,4,16,32,8,16,8]),amplify=var([3/4,0],128),amp=1*var.brk)

s4 >> pulse(var.notes,oct=4,dur=1,sus=1/2,formant=2,room=2/3,mix=1/3,lpf=linvar([400,1200],[4,8,4,16,32,8,16,8]),hpr=2/3,amplify=6/5,amp=1*var.brk).offbeat()


s5 >> donk(var.notes,dur=1/2,echo=PDur(3,5),room=1/3,mix=1/2,pan=[-2/3,2/3],amplify=1,amp=1*var.brk)

sG1 = Group(s1,s2,s3,s4,s5)

sG1.amp=0

s6 >> sawbass(
    [var([0,-1,-2,1],[63,32,16,16]),1,0,3,0,1,0,-1],
    dur=0.25, oct=[4,5],
    lpf=P[[2500, 1250], [1000, 1250], [1000, 250, 1000]] * 0.3, lpr=expvar([0.5, 0.25], [128, 0]),
    amplify=2/3, amp=var([1, 0],[[128, 64], [64, [32, 64]]])*var.brk*0.85
)


s7 >> arpy(s6.degree,oct=(6,7),dur=1/2,hpf=([400,2000],16),formant=3,amplify=var([0,3/4],128),amp=1) # *var.brk)
s8 >> marimba(var.notes,oct=[5,6],dur=1/4,formant=linvar([3,5],[28,4]),room=1/3,mix=1/2,pan=PWhite(-1,1),amplify=2,amp=1) # *var.brk)

s9 >> bell(s6.degree,oct=4,dur=16,echo=PDur(3,5),amplify=3/5,amp=1) #*var.brk)


