iClock.bpm = 180

print(Samples)

print(SynthDefs)

print(Attributes)

p1 >> varsaw([-2]*6+[[0,1],-3],amp=var([1,0],[28,4]) * var([1, 0], [[[256, 128], [128, 64]], [128, [64, 32]]]), dur=1, shape=.5, echo=.5).spread()
p2 >> varsaw([2,1,0,-1], amp=var([0,1],[28,4]) * var([256, 128]), dur=1, shape=.5, echo=0).spread()

b1 >> sawbass([-2,-2,0,0], dur=PDur(4,8))
p1.amp=.5
p2.amp=.5

#yeahhh

note1=Pvar([var([0,2,0,1],[6,2]),4],[30,2])

note2 = PStrum([int(var([4, 2, 10, 12], 32)), 3, 5, 7])

Scale.default.set(Pvar([Scale.major,Scale.minor], [32,32]))

Scale.default.set(Scale.major)

Scale.default=Scale.major



k1 >> play("(Vv).X.", amp=var([1, 0], [[256, 64, 64], [128, 32, 64]]))

print(Clock)

k2 >> play("[@@]",amp=var([.7, 0], [[32, 64, 32], [8, 4, 16, 32]]), hpf=linvar([200,3000],8))

k3 >> play("($)(X.)(VO).")
k4 >> play("..*.")
k5 >> play(".-")

rp >> ripple([0, 1], dur=16, tremolo=var([0, 2], 128), amp=expvar([1, 0, 0], [128, [64, 128], [64, 128]]))

pk >> pluck(note2, oct=[5, 4.85, 5.15, 5, 5.2], sus=[0.5, 1, 0.25, 0.25, 2], glide=[0.25, 0, 1, 0], amp=var([1, 0], [[128, 64], [64, 32, 128, 64, 256]]))
pp >> pluck(note1, dur=1, delay=0.5, amp=P[1, 1, 0, 0] * 0.85 * pk.amp)

Group(pk, pp).stop()


bp >> blip(note2, dur=8, oct=5, echo=0.5, echotime=0.5, amp=expvar([0, 0, 1], [128,128,256]))

bd >> play('X', sample=1, dur=1, lpf=800, hpf=0, hpr=0.25, amp=P[0.4, 0.95] * 1)
sb >> play('v', dur=1, delay=0.5, amp=P[0, 1] * 0.5)
s3 >> play('X', sample=1, dur=2, delay=0.75, amp=0.75)

hh >> play('=', dur=0.25, amp=expvar([0, 0, 1.5], [[32, 64, 128], [32, 64, 128], 0]))

Master().lpf = 0

Master().lpr = 0.15


@next_bar
def off():
    #Group(rp, pk, pp, bp, bd, sb, s3, hh).stop()
    #Group(bd, sb, s3).stop()
    #Group(h1, rs, cl, h2).stop()

oi >> sitar((-3, 0) + PStrum([7, 6, 5]), pan=PWhite(-0.75, 0.75), dur=PStrum([15, 2, 1, 3, 6, 12]) / 2, hpf=expvar([100, 1000], [32, 0]), hpr=0.25, amp=var([0.75, 0], [32, 32, 64, 8, 8, 32, 16, 8, 64, 128])).stop()

b1 >> star([[-3,-1],0,1,0], dur=PDur(5,8), shape=0, amp=2.5)

Master().hpf = var([0, [200, 400, 600]], [[28, 56, 56], [4, 8, 8])

print(Clock)


h1 >> play(':', dur=1, delay=0.5, amp=var([1, 0], [[64, 32, 128], [32, 32, 64, 32]]))

rs >> play('I', room=[1] * 7 + [0.5, 0.5], mix=0.25, dur=1, amp=var([1, 0], [[128, 32, 32, 256], [64, 8, 8, 128]]))

cl >> play('*', dur=2, delay=0.75, amp=var([1.5, 0], [[64, 128], [32, 64]]))

h2 >> play('-', dur=0.25, amp=expvar([0, 2.5], 1/3) * var([1, 0], [[256, 128, 64], [128, 64, 32]]))

s2 >> zap(note2,oct=PRand([4,5]),dur=var([1/2,PDur(3,8)],[12,4]),shape=linvar([1/4,2/3],16),formant=expvar([0,3],4),amplify=var([1,0],[64,32],amp=1)

s4 >> pasha(note1,oct=var([5,6],[30,2]),dur=1,formant=5,lpf=800,amplify=var([0,3/5],[32,64]))

t1 >> play("<x...><[XX]....X..>",dur=1,sample=-1,shape=1/3,amplify=2/5)

t2 >> play(Pvar(["..[rr].","..r.r.r."],[12,4]),dur=var([1,PDur(3,8)],[12,4]),rate=1,sample=2,amplify=3/4)

t3 >> play(".../",dur=32,shape=3/4,amplify=1)

t4 >> play()

#i quit#


n0 >> play('~', amp=expvar([0,1],[[256,128],0,0,0,0]), rate=expvar([0,5],[[256,128],0,0,0,0]), room=10, shape=1, bend=1).stop()

o0 >> blip(P[2],dur=4, sus=2, echo=0.02, echotime=0.02, chop=4, coarse=4, bit=16, spin=64, drive=1, room=10, amp=0.5, pan=[-1,1]).every(4, 'stutter',2, hpf=(1500,3000), hpr=0.25)

dl >> play('V', dur=var([2,4],[4,32]), echo=0.25, sus=4, spin=128, shape=1, bend=1, echotime=0.25).every(4, 'stutter',2, lpr=0.35)

ex >> play('!', amp=expvar([0,1],[[256,128],0,0,0,0]), rate=expvar([0,5],[[256,128],0,0,0,0]), room=10, shape=1, bend=1, delay=0.5).offbeat().every(32,'stutter',2,spin=128, pan=(-1,1))

e3 >> play('V', dur=var([2,4],[4,32]), echo=0.25, sus=4, spin=128, shape=1, bend=1, echotime=0.25).every(4, 'stutter',2, hpr=0.25)

ex.stop()
