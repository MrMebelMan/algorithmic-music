Clock.bpm = 125

print(SynthDefs)

o2 >> play('V',
    sample=P[6, 7, 7, 7] - 0,
    dur=0.25,
    amp=P[1, 0.25, 0.5, 0.75] * var([0, 1.5], [256, 128])
).stop()


var.kik_rate = var([1, 0.9, 0.8], 128)
var.kik_stop = var([1, 0], [[512, 256, 128], [128, 64, 32]])

var.pat = [[31, 31, 31, 31, 28, 28, 56], [1, 1, 1, 1, 4, 4, 8]]
var.brk = var([1, 0], var.pat)
var.drop = expvar([0, 0, 1], [[32, 32, 32, 32, 32, 32, 64], [32, 32, 32, 32, 32, 32, 64], 0])

o2 >> play('V',
    dur=0.25,
    sample=7,
    lpf=P[[300, 600], 350, 290, 280] * expvar([1, 1, 2, 2], [[32, 64], [32, 64], [32, 64], 0]),
    lpr=0.25,
    amp=P[1, 0.75, 0.25, 0.5,  0.25, 0.15, 0.1, 0.05] * expvar([0, 0, 1, 1], [64, 64, 128, 0]) * var.brk * var.kik_stop
)

ch >> play('-', sample=var([4, 5], [256, 128]), dur=1, delay=0.5, amp=var([0, 3], [64, 128]))
kd >> play('X', rate=var.kik_rate, sample=4, dur=1, amp=4 * var.brk * var.kik_stop)
k3 >> play('X', rate=var.kik_rate, sample=var([5, 6], var.pat), dur=1, amp=var([2, 3], 256) * var.brk * var.kik_stop)
k2 >> play('X', sample=5, rate=var.kik_rate, dur=1, delay=0.5, amp=P[1, var([0, 0.5], [[128, 64], [64, 32]]), [0, 0.25], 0] * 0.5 * kd.amp * var.brk * var.kik_stop)
tt >> play('t', sample=2, dur=0.25, lpf=[1000, 1250, 850, 1000], lpr=0.25, amp=P[1, 0.85, 1, 0.75, 0.5, 0.25, 0.85, 1] * var([0, 2], [[256, 128], [128, 64]])) 
bd >> play('V', sample=2, dur=1, hpf=var([120, 150], var.pat), hpr=0.25, amp=var([0, 1.35], [[512, 256], [256, 128, 256]]) * var.kik_stop)
sb >> sawbass(
    dur=0.25,
    hpf=var([800, 400], 128), hpr=0.25,
    amp=P[[var([0, 1], 32), var([1, 0], 32), 0.5, 0.75], [0, var([0.25, 0], 64), 0, 0.25, 0.5, 0.25], [1, var([0, 1], 8)], 0.75] * expvar([0, 0, 2, 2], [[64, 128], 64, [128, 256], 0])
)
oh >> play('=', sample=7, dur=0.25, amp=var([2.5, 0], [[128, 256, 64, 64], [64, 128, 32, 32]]) * var.drop)

n0 >> play('V[x x]', sample=P[6,4,6], dur=0.5, drive=0, shape=0.5, echo=0.02, amp=0.25*var.brk, lpf=var([1500,0],[31,1]), bend=var([0,-1],[31,1])).every(8, 'stutter')
s0 >> play('V[x x]', amp=0.25*var.brk, samepl=n0.sample, dur=0.5, rate=-1, lpf=1500)


od >> play('L', dur=1, sample=var([0,4],[32,16]), amp=linvar([0.25,1],16)).every(8, 'stutter', echo=0.2, echotime=2)
os >> play('L', lpf=1500, dur=1, sample=od.sample)

cb >> play('T', echo=0.02, sample=var([4,7],2), amp=var([0.35,0.5],1), bend=var([0,-1],[15,1]))

# I think it was when I changed the duration to 0 it broke everything

le >> play('~', lpf=expvar([300,3000],[127,1]), lpr=var([0.45, 0.25], var.pat), sample=var([0,4],16), amp=0.75, echo=0, room=expvar([0,10],16), echotime=0, mix=0.2)


b1 >> play("s",dur=1/4,rate=var([2, 1.9], var.pat),sample=var([-1,2,0,5],[8,4,16,6,4,12]),delay=[0,1/2],bend=1,coarse=4,drive=2/4,amplify=2/3,amp=1)

b2 >> play("-",sample=3,dur=1/4,drive=1/7,slide=0,formant=1,amplify=2/5,amp=1).every(6,"stutter",3)


s1 >> dub([0,1,0,-1],dur=8,oct=6,sus=16,shape=3/4,chop=32, coarse=linvar([0,5],[64,32]), bit=16, formant=5,pan=PWhite(-1,1),amplify=3/8,amp=1, spin=var([16,4],16))

s2 >> dbass(s1.degree,oct=7,dur=1/2,drive=2/4,coarse=4,formant=linvar([2,3,4],8),hpf=linvar([500,900],16),amplify=2/7,amp=1)

s3 >> arpy(s1.degree+P[:3],oct=8,dur=[1/4,PDur(5,8)],drive=2/3,lpf=expvar([500,1200],32),pan=(-2/3,2/3),room=1/2,mix=1/3,amplify=2/8,amp=1)

s4 >> donk(s1.degree,oct=6,dur=1,delay=[0,1/2],shape=1,echo=0,formant=0,amplify=4/5,amp=1)


print(SynthDef)






