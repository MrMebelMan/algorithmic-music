Clock.bpm = 160
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

#Sat Apr  4 20:51:00 2020: ERROR: JackEngine::XRun: client = SuperCollider was not finished, state = Running
#Sat Apr  4 20:51:00 2020: ERROR: JackAudioDriver::ProcessGraphAsyncMaster: Process error
# oh

b1 >> play("V",rate=var([1, 1.05, 1, 0.98, 1, 0.95], var.d2),dur=2,delay=[0,1/2],drive=2/4,lpf=var([1400, 1300, 1200, 1100], var.dp),amplify=2/3,amp=1)

b2 >> play("o",dur=1/4,cut=1/2,sample=2,amplify=[0,[0,0.15],2/5,0],amp=1)

b3 >> play("(-)([--])",sample=var([-1,PRand(4),4,PRand(4)],8),drive=1/9,room=3/4,mix=1/2,amplify=2/5,amp=1).every(PRand([4,8,12,16]),"stutter",3)

b4 >> play("s",dur=1,delay=[1/2,PDur(3,5)],sample=expvar([-1,5],64),room=3/4,mix=1/2,amplify=2/3,amp=1)

b5 >> play("j",dur=1,delay=[1/2,[1/4,1/4]],room=1/2,mix=[0.15,0.25,0,0],lpf=linvar([400,1200],16),pan=PWhite(-1,1),amplify=3/6,amp=1)

b6 >> play("N",dur=4,sample=-1,echo=1/2,coarse=3,room=2/3,mix=1/3,amplify=3/5,amp=1)

b7 >> play("b",rate=6/5,dur=8,delay=0.5,echo=1/2,sample=PRand([1,2]),slide=1,room=2/5,mix=1/2,amplify=2/9,amp=1)

b8 >> play("H",sample=1,delay=1/2,bend=2,amplify=1/5,amp=1).every(3,"stutter",2)

gB = Group(b1,b2,b3,b4,b5,b6,b7,b8)

gB.amp = var([tl1,tl3],trad)


s1 >> pulse([r2.degree,r4.degree+P[:2]],oct=6,dur=PDur(5,7),sus=1/8,echo=[0,1/2],drive=1/7,chop=2,lpf=([400,1200],64),formant=linvar([1,5],32),room=2/5,mix=1/3,pan=[-2/3,2/3],amplify=2/5,amp=var(tl4,trad))

s2 >> varsaw(s1.degree,oct=7,dur=1/2,sus=1/4,delay=[0,PDur(5,7)],drive=2/7,formant=1,slide=[-1,0,1,0],pan=PWhite(-2/3,2/3),amplify=1/4,amp=var(tl5,trad))


sb >> sawbass(
    [var([0, -1, 0, 0], var.d2), var([0.15, 0.05, 0.1], 64), var([0.05, 0.025], 8), var([0.05, 0.08], 32)],
    dur=0.5,
    sus=P[[0.25, 1], 0.5, 0.75, 1, [1, 2], 0.5, 0.5, var([1, 2], [128, 64]), var([0.25, 0.5], var.dp)],
    lpf=P[
        var([1500, 1000], var.dp), var([2000, 1500], 8), var([1250, 1500]), 1000,
        [1500, 1500, 1500, var([1500, 3500], [[32, 64], [64, 32]])], 2000, 1250, [1000, 3000]
    ] * expvar([1.5, 0.75], 256),
    lpr=P[var([0.25, 0.5], tl1), 0.25, [0.25, 0.13, 0.13, 0.3], 0.25],
    bend=P[-0.05, 0, var([0, -0.2], [58, 6]), 0,  0, [var([0, 0.1], [32, 8, 8]), var([0.05, 0])], [0, 0, 0, 0.06], 0.03] * 0,
    drive=P[var([0, 0.05], 128), 0, 0, 0,  0, [0, var([0.01, 0], [32, 64, 128])], [0, var([0, 0.03], var.d2)], 0],
    hpf=P[var([0, 400], [58, 6]), var([0, 450], [31, 1]), [0, 120], sinvar([400, 500], [64, 32])], hpr=0.25,
    amp=P[
        [var([1, 0.5], [[32, 64], 8]), 0.85], [0.25, 0.75], var([1, 0], [8, 4, 4]), 1, 0.25, var([1, 0], [[64, 128], 32]),
        [0, var([0, 0.5, 0.75], var.dp), var([0, 0.25, 0.5], var.dp), 0.75], [0.5, 0.75, 0.5, 0.25], [0.25, 1, 0, 0.5], var([1, 0], [128, 32])
    ] * sinvar([0.9, 0.6], [128, 64])  * 1 #var([0.75, 0], [[8, 32], [4, 8], [3, 64], [1, 32], 6, 2, 8, 2, 14, 2, 14, 6, 4, 2, 3, 1])
)
bb >> jbass(dur=0.5, sus=P[2, 1, 1], lpf=P[850, 1200] * 2, amp=P[[1.1, 1], [0.85, 0.8]] * 0)
var.kk = var([1, 0], [256, 64])

kk >> play('X', rate=P[1, var([0.95, 1], 32), 1, var([0.9, 1], 32)], sample=var([2, 1], [256, 128, 64, 32]), dur=[1, 1, var([1, 1], [64, 256]), 1], lpf=var([200, 500, 700], [8, 32, 32]), lpr=0.25, amp=P[1, var([0.85, 1], [64, 256]), var([0.5, 0.75], [64, 256]), 0.9] * var.kk * var.brk * 1.1)
kk.dur=[4, 2, 2]
k2 >> play('V',
    rate=var([0.95, 1, 0.98, 1.02], [32, [8, 16, 64], [8, 32]]),
    sample=var([1, 2], [128, 256]),
    dur=kk.dur,
    lpf=P[var([650, 800], [28, 4]), 600, var([650, 500], 8), 700] * 1,
    lpr=var([0.5, 0.4, 0.3], 128),
    amp=var([0.65, 0], [128, 32]) * var.kk * var.brk * P[var([1.5, 1.3], 32), 1.5] * expvar([0, 1, 1], [128, 32, 0])
)
sk >> play('I', sample=1, dur=[kk.dur] * 15 + [0.5, 0.5], delay=0.5, lpf=300, lpr=0.5,
    amp=P[[var([1, 0], 128), 0.75], [var([0, 0.5], 8), var([1, 0.5], [256, 128]), var([0.25, 0], 4), 0], [var([0.25, 0.5, 0.75], 64), var([0.25, 0.5], 16), var([0, 0.5], 8), var([0.75, 0.25], 8), 0, var([1, 0.5])], [1, 0.75, 0.5, 0.5]] * var([0.5, 0], var.dp) * var.kk * var.brk
)

oh >> play('-', sample=var([2, 1, 0, 2], 64), dur=1, delay=0.5, amp=var([0, 1], var.dp))
k3 >> play('m', rate=var([1, 0.98, 0.95, 0.93], [64, 32]), sample=var([0, 1], [14, 2]), dur=kk.dur / 4, cut=0, amp=P[[1, 1.1], [0.85, 0.65], [0.25, 0.25, 0.5, 0.5], [0.75, 1]] * var([0, 1], [32, 32, 64, 128, 32, 64]) * kk.amp * 1)
tt >> play('t', rate=P[1, var([1.1, 1], 8), var([0.95, 1]), [0.9, 0.95, 1, 1]], sample=0, dur=0.25, amp=1.5 * P[[0.85, 0.5, 0.25], [0.5, 0.75], 0.25, [0.5, 1], 0.75, [0.25, 0.15], [0.5, 0.25, 1], [0.75, 1]] * var([1, 0], [3, 1, 4, 2, 3, 1, 4, 2, 6, 3, 8, 4]))
sr >> play('u', dur=0.25, lpf=P[[800, 1750], 2500, [3500, 3000], [2000, 4000, 3500]], amp=var([0, 1.25], [28, 4, 31, 1, 31, 1, 56, 8, 28, 4]))
ll >> play('L', sample=[1] * 28 + [0.25] * 8 + [0.5] * 4, dur=1, lpf=expvar([1500, 3500], [[64, [32, 128]], [128, 64], 0]), amp=expvar([0, 0, 1], [[64, 32], [128, 64], 0]))
he >> play('-', pan=PWhite(-0.5, 0.5), room=1, mix=[0.15, 0.2, 0, 0], sample=2, dur=0.25, amp=P[[1, 0.25], [0.85, 0.5, 0.25, 0.25], [0.75, 0.85, 1], [1, 0.25, 0.75, 0.25],  [1, 0.25, 0.5, 0.75], 0.85, [1, 0.5], [0.5, 1, 0.25, 0.25]] * var([1, 0], var.dp))
kd >> play('m', dur=[0.5] * 31 + [0.25, 0.25, 0.25, 0.25], lpf=0, lpr=1, hpf=100, hpr=0.25, amp=P[[1, 0.75, 0.85, 0.5], 0.25, [0.5, 0.25, 0.25, 0.5], 0.75] * var([0. 1.5], [64, 32]))

sn >> play('x', rate=0.85, sample=2, dur=k3.dur * 2, amp=var([0, 1], [[32, 64], [64, 128]]) *  0)

dk >> donk(dur=4, sus=4, tremolo=4, bend=-0.25, benddelay=0.5, lpf=650, lpr=0.25, amp=0)

@next_bar
def stahp():
    Group(oh, k3, tt, sr, ll, k2, sk, kk, sn, kd, dk, kd, r1, r2, r3, r4, r6, r7, sb, r8).stop()


kk.stop()
k2.stop()
sk.stop()

Group(oh, k3, tt, ll, he).stop()

Group(kk, k2, sk, oh, k3, bb).stop()

r1 >> ripple(P[0,3,0,3,[5,7]] + var([4 + PRand(4)],[8,16]), dur=[0.5,0.5,0.25], amp=2*var.brk, formant=1)

r2 >> ambi(var([0,3,2,1],[1,3]), amp=var.brk, dur=var([1,4,8],[[4,2,4],[1,1,3]]), tremolo=var([2 + PRand(2),PRand(2)],[16,[3,4]]))

r3 >> bass(P[var([3,2],128),3,var([3,2.5],8),var([2,1],64)]-3, amp=var.brk, drive=var([0.05,0.02],[[2,4,2],[12,6]]), formant=1, dur=var([0.5,0.25],[[4,8,4,11],[1,1,1]])).every(7, "stutter" ,3)
r4 >> space(P[5,4,3,2]-2, dur=[0.5,0.5,0.5,14.5], oct=5, blur=2, sus=8, amp=var([0,1],[[32,16],16]))
r5 >> star(P[0,[1,1,0,[1,1,4]]]-1, dur=0.5 * P[0.5,1], formant=expvar([1,2],[16,8]), amp=var.brk).every(6,'stutter', 2)

r6 >> sitar(dur=[0.25,0.25,[0.5,0.25,0.5]], oct=6, amp=var.brk * linvar([0.5,0.75],16), formant=1 + var.brk, drive=expvar([0.02, 0.05],12)).every(8, "offadd", [2,4]) 

r7 >> sinepad([4,7], dur=[1,7], oct=5, tremolo=var([1,[4,2,4,1]]), sus=4, blur=3, amp=var([0,1],[[16,8],8]))
 
#ye

