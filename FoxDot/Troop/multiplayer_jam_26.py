Clock.bpm = 140

# AFK 5m

Master().rate = 1

var.brk = var([1, 0], [[56, 28, 28, 31, 31, [31, 32], [31, 32]], [8, 4, 4, 1, 1, [1, 0], [1, 0]]])

cl >> play('*', sample=var([1, 0], [128, 64]), dur=var([16, 8, 4, 2], [64, 128, 128, 64]), delay=0.5, amp=var([1, 0], [[256, 128], [128, 64, 128, 256]]) * var.brk)
h1 >> play('-', sample=var([2, 1], [[56, 28, 31], [8, 4, 1]]), dur=0.25, amp=expvar([1, 0.15], 1/3) * expvar([0, 1], [[[8, 64], 16, 32], 0]) * var([1, 0], [[128, 256], [64, 128]]) * var.brk)
rc >> play('~', sample=([0, 1], [64, 32, 128]), pan=PWhite(-0.75, 0.75), dur=0.5, amp=var([0, 1], [128, 256, 64, 32, 32, 64, 64, 128]) * expvar([0, 0, 1.5, 1.5], [[32, 64, 32, 128], [32, 64], [64, 128], 0]))
kd >> play('X', rate=1.1, dur=var([2, 1], [[128, 256], [64, [128, 32]]]), sample=1, lpf=350, lpr=0.25, amp=var([1.35, 0], [[512, 256, 128], [256, 128, 64]]))
bp >> blip(P[-2, -1, -1, [0, 2, 4]], dur=1, amp=P[1, 0.75, [1, var([1, 0], [128, 64])], [0.75, 0.5]] * var([0, 1.5], [[256, 128], [128, 64]]) * var.brk)
sb >> blip(degree=bp.degree, dur=1, delay=0.5, amp=P[0, [0, 0.85], 0, 0, 0, 1, 0, 0] * 0.5 * bp.amp)
sr >> play('u',
    sample=[3, [2, 1, 3], [3, 1, 3]],
    pan=PWhite(-0.75, 0.75),
    dur=0.25,
    amp=P[
        [0.25, 0.5], 0.5,
        [1, 1, 1, 0], [0.75, 0.5],
        [0.25, 0.5, 0.75], [0.15, 0.75],
        [PWhite(0.25, 0.75), PWhite(0.5, 1)]
   ] * var([1.5, 0], [[64, 128, 256], 32, [32, 64, 128], [32, 64], 32, 32, 32])
)

bd >> play('V', rate=1.1, sample=var([2, 1], [256, 128]), lpf=var([350, 750, 500, 250, 800], [64, 32, 64]), lpr=0.25, dur=1, amp=P[1, 0.85] * expvar([0, 0, 1], [[32, 64, 128, 256], 256, 0]) * var.brk)
bs >> play('V', sample=bd.sample, dur=1, lpf=bd.lpf, lpr=bd.lpr, delay=0.5, amp=P[0.5, [0, 0, 0, 1]] * bd.amp)
Group(bd, bs, cl, g1, g2, rc, kd, sr).stop()

tt >> play('t', pan=[-0.5, 0, 0.5, 0.25, 0, -0.25, 0], sample=1, dur=0.25, amp=P[0, 0, 0, 0, 0.25, 0.5, 0.7, 1] * expvar([0, 0, 4, 4], [[64, 32], [64, 32], [128, 64], [128, 64]]))
  
print(Samples)

print(SynthDefs)

sh >> play('s', sample=2, dur=1, delay=0.5, amp=1.5)

dk >> donk(var([0, 0.25, 0.5], [28, 2, 2]), dur=1, sus=[1, 0.75], amp=[1, 0.9])
d2 >> donk(dur=1, delay=0.5, lpf=500, amp=P[0, 1, [0, 0, 0, 1], 0] * 0.75)

var.melody=var([0,1,0,2,0,1,0,3])


b1 >> play("<(V....V..)(v....[vv]..)><(..i.)(..[ii])><(.-)(-)([--])>",
            rate=var([1,2/3],[28,4]),
            sample=var([2,-1],[28,4]),
            amplify=4/5,
            amp=1*var.brk
            ).every(16,"stutter",3)

s2 >> karp(melody,oct=(4,PRand(5,6)),dur=var([1,1/2],[24,8]),sus=2,chop=PRand([4,8],8),formant=linvar([2,4],[28,4]),amplify=3/4,amp=1*var.brk)

s5 >> bug((melody,melody+2,melody+4),oct=5,dur=1,sus=1/2,shape=2/5,formant=linvar([1,3],16),room=1/3,mix=1/2,pan=PWhite(-2/3,2/3),amplify=3/5,amp=1*var.brk)

s7 >> arpy(s6.degree,oct=7,dur=1/4,shape=1/6,formant=expvar([0,0.5],16),slide=1,vib=2,pan=[-3/4,3/4],amplify=linvar([1/3,2/4],8),amp=1*var.brk)

s0 >> bell(melody,oct=(7,8),dur=PRand([1/2,PDur(5,8)],1/2),room=2/3,mix=1/2,pan=PWhite(-1,1),amplify=linvar([0,2/6],32),amp=1*var.brk)

Group(b1, s2, s0, s7, d2, tt, sh).stop()

# ayyy

s1 >> sinepad(dur=var([0.5,[1,0.25,0.5],0.25],[8,PRand(16)]), formant=var([1,3],PRand(8)), oct=var([4,5],[6,6]), amp=var([0,1],[8,16]) * linvar([1,2],8)).accompany(p1).every(8, "stutter", 2).stop()
s3 >> play("~ ~~  x  (x )", amp=1 * var.brk, sample=3, dur= var([0.5,0.25],[4,16]), rate=var([1,2],[16,4]))
s4 >> ambi(var.melody + var([0,2],[4,2]), dur=var([2,4],[6,12]), formant=linvar(1,3), sus=2, blur=2, pan=PWhite(1), chop=4, tremolo=3).stop()
s6 >> sinepad([7,4,2,[3,3,5]], dur=4, formant=var([1, 0.75, 0.5, 0.25, 0], [64 ,128, 32, 32]), oct=4, amp=1 * var.brk * linvar([0,1],16), chop=4, tremolo=3)

s8 >> bug(var([4,2],PRand(8)), dur=4, amp=2*(1-var.brk), oct=4, shape=0.3)
s9 >> play("            e ee", dur=0.25, amp=var.brk * 3)
db >> dbass(-3,dur=0.5)

Group(s1, s3, s4, s6, s8, s9, db).stop()

s0 >> sinepad(lpf=expvar([4,0],32)*var([800,1600],[31,1])*expvar([0,4],32), lpr=0.25, amp=var([0.5,0.25],1), dur=1, echo=0.02, mix=0.2, room=0.5).every(4, 'stutter', 3, lpf=1500, lpr=0.45, echo=0.2).stop()

cb >> play('T[ss]', echo=0.02, dur=4, amp=0.5*bp.amp, drive=[0, -1], hpf=800, hpr=0.35).every(2, 'stutter', echo=0.2)
d0 >> play('T', dur=2, pan=[-1, 1], amp=0.5*bp.amp * var.brk)
d1 >> play('X', lpf=expvar([2000,0,5000,0,3500,0], 32)*var([0,1], 128), dur=var([1,0.5],[64,128]), amp=P[[0.25, 0.5], var([0.75, 0.5],[15,16])] * var.brk, lpr=0.45, echo=0.02, room=0.5, mix=0.25).stop()

a0 >> play('!', dur=4, chop=8, echo=0.02, amp=var.brk*linvar([1,0],16)).every(16, 'stutter', 3, hpf=(300,3200,1500), hpr=0.35, bend=[0,-1,0], drive=[0,1,0]).stop()

n0 >> sinepad(var.melody, echo=0.2, amp=[1,0.5], chop=4, coarse=8, oct=4, sus=2, dur=1, lpr=0.25).every(2, 'stutter', 3, lpf=1500, echo=[0,0.02,0]) + var([0,1,4])

dl >> play('X', dur=PDur(3,11), amp=0.25 * var.brk)
o0 >> play('V', dur=PDur(3,11), amp=0.25)

Group(cb, d0, d1, a0, dl, o0).stop()

# 's back!



