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
trad = P[128,64,64,128,64,64,128,128]
tl1 = P[1,0,1,1,0,1,1,1]
tl2 = P[0,1,1,1,1,1,1,0]
tl3 = P[0,0,1,1,0,1,1,0]
tl4 = P[0,1,0,1,1,0,1,1]
tl5 = P[1,0,0,1,0,0,1,0]


s1 >> rave(var.note+P[:2],dur=1/4,sus=1/8,delay=[0,1/2],echo=[0,1/2],shape=1/8,formant=linvar([1,8],8),lpf=PRand([PWhite(400,1200)]),room=1/3,mix=1/3,amplify=2/5,
    amp=var(tl1,trad))

s2 >> fuzz(var.note,dur=1/2,sus=1/4,echo=1/2,lpf=linvar([400,900],16),room=1/3,mix=1/2,amplify=2/3,amp=var(tl5,trad))

s3 >> dub(var.bl,dur=4,chop=4,shape=1/5,formant=2,lpf=linvar([300,900],32),amplify=2/3,amp=var(tl2,trad))

s4 >> dub(var.bl,dur=4,chop=2,amplify=1/3,amp=var(tl2,trad))

s5 >> saw(var.note+P[:8],oct=6,dur=1/4,sus=1/8,delay=[0,PDur(3,5)],drive=2/3,room=1/3,mix=1/2,pan=PWhite(-1,1),amplify=var([2/5,PRand([0,2/5],1/4)],[24,8]),
    amp=var(tl4,trad))

s6 >> sawbass(var.bl,oct=5,dur=PDur(3,5),drive=1/3,formant=linvar([1,8],PRand(16)),lpf=PZip([PRand(2000),PRand(1200)],[500,800]),amplify=2/8,
    amp=var(tl3,trad))

s7 >> soprano([var([0, 1, 2], 64),var([7, 6], 8),0,var([5, 4, 2], [32, 64, 32]),0,var([-1, 0], 4),[0, var([1, 0, 2], [64, 32])],3],dur=2,sus=2,chop=8,echo=[0,PDur(3,5)],slide=-2,drive=1/3,room=1/3,mix=1/2,pan=(-2/3,2/3),amplify=2/4,
    amp=var(tl3,trad))

s8 >> pasha(var.bl,oct=6,dur=var([1,1/2],[6,2]),sus=1/2,delay=1/2,drive=2/3,chop=16,lpf=([800,1200],[4,8,2,16,12,4,2]),amplify=4/5,amp=var(tl4,trad))


sb >> sawbass(dur=1, bend=-0.05, hpf=100, hpr=0.25, tremolo=4, amp=var([1, 0], var.trad))

cr >> play(
    var(['(Vrn)(aV)VhgLL(aX)f(nL--)[n-:]LLLLLLnnnnnn-----', 'outttnLLL'], [128, 256, 32, 32]),
    rate=var([1, 0.8, 0.95, 1.05, 1, 0.95], [32, 8, 4, 5, 3, 2, 1, 1]),
    sample=[
        var([0, 1, 0, -1], [3, 2, 5, 2, 4, 2, 9, 5, 6, 2, 1]),
        [1, 0, 2, 2],
        var([1, 0, -1, -2], 32), [2, 2, 2, var([2, 0, 1], 64)],
        #
        var([3, 2, 1], 4), var([0, 2, 1, 0, 3], 8), var([1, 2], 32), var([2, 1, 0], 64), var([3, 4, 0], [4, 8])
    ],
    bend=[[0, var([-0.15, 0], 16)], 0, 0, 0],
    drive=P[0.05, 0, [0, 0.015], 0],
    dur=var([0.5, 0.25], 128),
    lpf=P[[500, 300, 100, 1500], 800, [350, 2000, 800, 1500], 1250] * 0, lpr=0.5,
    hpf=expvar([800, 250], 4), hpr=0.25,
    amp=P[
        [var([0, 1], [64, 128]), var([0, 1], 256), var([0, 0.75, 0.5], 128), 1],
        [0.85, var([0, 1], [64, 32, 32])],
        [0.25, 0.5, 0, 0],
        [0, var([0, 0.25, 0.5, 0.75], 64), 0, 0.5]
    ] * var([0.65, 0], [[28, 31], [4, 1]]) * var([1, 0], [[256, 64, 8, 5, 2, 6, 1], [128, 32, 6, 2, 4, 5]]) * var([1, 0], var.trad)
)

c2 >> play(
    var(['v(mX)(Xx)mLmLL[uu]DDnLn:LLnmuuttttt','###LLLL:--='], 256),
    dur=var([0.5, 0.25], [[128, 256], [64, 512, 256, 128]]),
    sample=P[var([0, 1, 2], 4), var([1, 2], 8), 0, var([0, 2, 1, 0], [32, 8, 8])],
    room=1, mix=[0.25, 0, 0, [0.25, 0.15, 0, 0]],
    lpf=var([2000, 3000, 1500, 4500], 32) * 1.25, lpr=0.25,
    amp=P[0.25, 0.75, [0.5, 0], 1, 0.25, 0.5, 0, 0] * var([1, 0], [4, 2, 5, 1, 3, 2, 3, 3, 8, 4, 6, 1, 9, 5, 4, 2, 3, 3, 4, 5, 2, 3, 1, 2]) * var([0, 1], var.trad)
)

tm >> play('I', sample=var([1, 0, 2, 0], [[32, 16], [8, 4, 4], 8]),
    dur=[
        var([1, 0.5, 0.25, 0.5], [28, 2, 2, [24, 8, 4, 2], 4, 4])
    ] * 56 + [0.5] * 6 + [0.125] * 8,
    hpf=150, hpr=0.25, lpf=500, lpr=0.75, bend=-0.25,
    amp=var([1, 0], [[256, 128], [128, 64]]) * var([0, 1], var.trad)
)    
dh >> play('v', hpf=80, hpr=0.25, dur=[0.25, 0.25, [0.5, 1], [0.5, 1], 0.25, 0.25], amp=P[0.85, 0.25, 0.15, 0.2] * var([0, 0.75], [64, 32, 32, 64, 128]))

he >> play(var(['L', 't', 'm', '-'], [[256, 64, 128, 32], 128]), rate=var([1, 2], [28, 4, 31, 1, 56, 8]), sample=0, dur=0.25,
    lpf=[[250, var([800, 400, 200], 64)], [500, 200, var([1000, 500, 250, 500], 8), 1200], [650, 500, 400, 300]],
    amp=P[
        1, [0.75, var([0.55, 0.85], 32)], [1, 0.9], [0.1, 0.2]
    ] * expvar(
        [0, 0, 1, 1], [[64, 32, 128], [64, 32, 16], [128, 64, 32, [64, 256]], 0]
    ) * var([1, 0], [31, 1, 28, 4, 31, 1, 56, 8]) * var([1, 0], var.trad)
)
sh >> play('s', echo=0.25, echotime=2, sample=1, dur=var([2, 8, 4, 16, 8], 64), amp=var([1, 0], 256) * var([1, 0], var.trad))

kd >> play('X', rate=var([1, 0.95, 0.9], 64), dur=1, sample=2, lpf=var([500, 400, 300, 250], 32), hpf=0, hpr=0.25, lpr=0.25, amp=P[1, 0.85] * var([0, 1], [64, [32, 64, 128], 32, 128, 32]) * var([1, 0], var.trad))
sk >> play('X', dur=1, delay=0.5, sample=1, lpf=400, lpr=0.5, hpf=var.hi, hpr=0.25, amp=P[1, [[0, 0.45], 0.25]] * var([1, 0], [[64, 128], [32, 64, 64]]) * kd.amp)
nn >> play('n', sample=2, dur=1, delay=0.5, amp=kd.amp * var([0, 1], [64, 128]) * var([1, 0], var.trad))
sn >> play('X', dur=2, amp=var([1.25, 0], var.trad) * kd.amp)
ss >> play('s', sample=1, dur=0.25, lpf=P[[1500, 4500, 3000, 2500], 2500, 3500, 4000], lpr=0.25, amp=var([2.5, 0], var.trad))
bl >> bass(slide=var([0.5, 0.25, 0.5, 0.75], var.trad), dur=1, oct=4.8, lpf=expvar([300, 600], 64), lpr=0.25,
    amp=P[1, [0, var([0, 0.5], 8)]] * var([0, 1], [[128, 64, 32, 32], [256, 128]]) * var(tl2, var.trad)
)
rk >> play('X', dur=1, sample=2, rate=-1, lpf=1000, lpr=0.25, amp=var([0, 1], [63, 1]))


