Clock.bpm = 133
#Clock.set_time(0)
Scale.default = "minor"
Root.default = -2

print(Samples)

print(SynthDefs)

Clock.clear()


var.dp = P[[8, 16], [4, 8], 2,1, 3, 1, [6, 12], [2, 8], 5, 4, [4, 32], [2, 8, 16], 3, 2, 3, 1]
var.d2 = P[16, 8, 5, 3, [4, 8], [2, 16], [8, 32], [1, 8], 2, 3]

# Based on traditional electro tracks
var.note = var([0,7,4])
var.bl = var([0,-1,0,1,0,-1,0,3])

var.brk = var([1, 0], [31, 1, 31, 1, 28, 4])

trad = P[128,64,64,128,64,64,128,128]
tl1 = P[1,0,1,1,0,1,1,1]
tl2 = P[0,1,1,1,1,1,1,0]
tl3 = P[0,0,1,1,0,1,1,0]
tl4 = P[0,1,0,1,1,0,1,1]
tl5 = P[1,0,0,1,0,0,1,0]

var.pat = P[3, 1, 8, 4, 2, 2, 4, 2, 5, 3, 8, 2]
zz >> play(
    'zz-',
    sample=[2, 2, 4],
    lpf=P[[500, 800], 1200, 750] * expvar([1.5, 3], 64),
    lpr=P[[0.85, 0.25], 0.75, 0.75, 0.95] * 0 + 1,
    dur=[0.5, 0.25, 0.25],
    amp=P[0.25, 0.35, [0.4, 0.5]] * var([1, 0], var.pat)
)
nn >> play('t',
    sample=4,
    dur=0.25,
    lpf=P[750, 1250, 800, 900] + var([0, 100, 50, 150, -50], trad), lpr=0.25,
    amp=P[
        1, [var([0, 1], [64, 32]), 0.85], [var([0, 0.85], 128), 0.5], [0.25, 0.75], var([0.5, 0.75, 0.25, 0.75], 8), var([0.25, 0.5]), 0.75, [1, var([0.85, 1], 32)]
    ] * var([0, 1], var.pat)
)
sn >> play('I', sample=1, room=1, mix=0.2, dur=[4, 2, 8, 4, 8], amp=var([0, 0.9], trad))
mm >> play('u',
    sample=0,
    rate=1.05,
    dur=0.25,
    amp=P[
        [0, 0.5], [0.25, var([0.15, 0.25, 0.5, 0.75], 64)], [0.5, 0.25, 0.75, 0.5], [var([0, 1], 128), 0.5, 0.25, var([0.15, 0.75], [128, 64])],
        var([0, 1, 0.5, 0.25], 64), 0.75, var([0.5, 0.25, 0.75], 64), var([0.25, 0, 0.5], 128),
        0.5, 0.25, [0, 0.5, 0.25, 0], var([0, 0.25, 0.5], 8),
        0.25, 0.5, var([0.75, 0.25]), var([0.5, 0.25, 0.75], 32)
    ] * var([0, 0.75], [32, 128, 64, 256])
)
cl >> play('H', sample=1, dur=0.25, lpf=P[1500, [800, var([800, 1000, 1200], 64)], 1250, 600,  450, [500, 1250, 1500], var([350, 500, 700], 32), var([340, 600], 8)], lpr=0.5, amp=P[0.25, [0.5, 0.25], 0.15, 0.15, 0.75, 0.5] * 0.75)
sh >> play('s', sample=1, dur=0.25, amp=P[[0] * 30 + [0.5, 0.5, 1]] * var([1, 0], [[128, 256], [32, 64]]))
k1 >> play('X', dur=Pvar([P[2, 0.5, 0.5, 1, 2, 1, 1, 4, 1, 1, 2], P[[1] * 15 + [0.5, 0.5]]], 128), sample=1, lpf=400, lpr=0.45, amp=var([0.7, 0], trad))
ks >> play('X', sample=1, dur=k1.dur / 4, amp=P[0.75, 0.5, 0.25, 0,  0.75, [0.5, 0.75], 0.25, 0.5] * k1.amp * var([1, 0], [64, 32]))
oh >> play('t', sample=1, dur=[1] * 7 + [0.5, 0.5], delay=0.5, amp=var([0, 1.1], [[64, 128], [128, 256]]) * k1.amp)
tm >> play('I', dur=[1] * 31 + [0.5, 0.5], sample=0, bend=-0.15, hpf=115, hpr=0.25, amp=expvar([0, 0, 1, 1], [[128, 64], 64, [128, 256], 0]) * 0)
bd >> play(var(['X', 'X'], 256), dur=1, sample=var([2, 1], [112, 16]), hpf=120, hpr=0.25, slide=0.05, tremolo=var([0, 2], [28, 4, 31, 1]), amp=var([0, 0.5], [256, 128, 128, 64, 128, 128, 64, 32, 64, 32, 32]))
rs >> play('m', dur=[1] * 30 + [0.125] * 4 + [0.5] * 2, amp=P[1, 0.85] * var([0, 1], [[32, 64, 128], [64, 128, 256]]))
t2 >> play('X', bend=-0.1, dur=tm.dur, delay=0.5, hpf=tm.hpf, hpr=tm.hpr, amp=P[1, 0, [0.5, 0.25, 0, 0], [0.25, 0.15],  1, 0, 0, [0, 0, 0.25, 0.15]] * 0.85 * tm.amp)
rr >> play('I', dur=[1] * 15 + [0.5, 0.5], room=1, mix=0.2, lpf=expvar([200, 5000], [128, 0]), lpr=0.5, amp=expvar([0, 1], [128, 0]) * var([0, 1.85], [[256, 128], 256]))

Group(sh, tm, rs, t2, cl, sn, mm, oh).stop()
Group(k1, ks, tm, bd, zz, nn, cl, sh).stop()
Group(k1, ks, tm, rs, t2, rr).stop()

var.notes = P[0,-1,0,3]
var.bassl = P[0,-2,0,1]
note=PRand(Scale.default)

s1 >> swell(PStutter(var.notes,2),dur=8,drive=2/9,vib=4,tremolo=4,room=3/4,mix=1/2,pan=(-3/4,3/4),amplify=2/5,amp=var(tl1,trad))

s2 >> bug(var.notes,oct=4,dur=16,sus=12,shape=1/3,echo=6/5,bend=1,slide=[-1,0,1,0],room=2/3,mix=1/2,pan=PWhite(-1,1),amplify=2/4,amp=var(tl1,trad))

s3 >> dbass(var.notes,oct=5,dur=4,chop=8,drive=0,formant=linvar([0,7],32),lpf=expvar([500,900],16),amplify=1/5,amp=var(tl2,trad))

s4 >> jbass(Pvar([var.bassl,var.bassl+P[:7]],32),dur=2,oct=7,echo=1/2,formant=1/5,room=2/3,mix=1/2,amplify=linvar([0,3/9],16),amp=var(tl3,trad))

s5 >> sitar(note,oct=5,dur=1/4,delay=[0,1/2],formant=expvar([0,4],8),lpf=linvar([500,1800],64),pan=[-3/4,3/4],amplify=3/5,amp=var(tl4,trad))

s6 >> karp(var.notes,oct=6,dur=PRand([1/4,1/2,1],PRand(4)),sus=2/3,echo=1/2,shape=2/5,tremolo=3,coarse=2,room=2/4,mix=1/3,pan=[-2/3,2/3],amplify=3/4,amp=var(tl3,trad))

s7 >> varsaw(s4.degree,oct=5,dur=PDur(3,5),sus=1/4,drive=1/4,room=2/3,mix=1/2,lpf=var([600,1400],16),amplify=2/5,amp=var(tl5,trad))

s8 >> bell((var.bassl,P[:2]),oct=6,dur=4,sus=1/2,delay=[0,1/2],echo=1/2,lpf=900,room=2/3,mix=1/2,amplify=2/6,amp=var(tl3,trad))

s9 >> donk(var.bassl,oct=6,dur=8,sus=1,shape=2/7,drive=1/3,echo=1/2,amplify=2/8,amp=var(tl4,trad))

s0 >> klank(var.notes,dur=2,sus=2,delay=1/2,chop=2,drive=1/20,lpf=600,room=2/3,mix=1/3,amplify=4/9,amp=var(tl5,trad))


t1 >> star([var.bassl,Pvar([P[:2],P[:8]],32)],oct=6,dur=1/2,shape=0,echo=1/2,formant=linvar([0,2],16),room=1/3,mix=2/3,amplify=5/6,amp=1).stop()

Group(s1, s2, s3, s4, s5, s6, s8, s9, s0).stop()


#Ok do that

print(Attributes)

print(SynthDefs)

#ute


