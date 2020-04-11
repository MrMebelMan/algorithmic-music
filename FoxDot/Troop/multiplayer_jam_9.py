print(Samples)

print(SynthDefs)

print(Attributes)

##################################

Clock.bpm = 200

Master().hpf = var([0, 200, 400, 800, [100, 80, 40], 150, 200, 800, [1200, 150, 100, 80], 0], [28, 4, 8, 8, 56, [40, 8], [64, 32], 32, 8, [128, 64, 32]])

var.kamp = var([1, 0], [60, 4, 28, 4, 56, 8, 64, 32, 120, 8])

k1 >> play('$', sample=0, drive=expvar([0.01, 0.5, 0.5], [256, 64, 0]), echo=0.1, echotime=0.2, lpf=55, lpr=[0.01, 0.02], dur=0.25, amp=[var.kamp, 1, 1, 0])

os >> play('I', room=1, mix=0.25, sample=1, dur=1, amp=expvar([0.15, 0.25, 2, 2], 128)).solo(0)

v1 >> play('V',
    sample=var([0, 1], [128, 32]),
    drive=var([0.25, 0.05, 0.5, 0.15, 0.45, 0.25], [32, 8, 64, 28, 4]),
    hpf=var([40, [80, 60], 50, 200, 35, 60], [28, 4, 56, 8, 28, 4]),
    hpr=0.25,
    dur=
        [0.5] * 16 +
        [0.75, 0.25, 0.5, 0.5] + [1] * int(var([7, 16], 32)) +
        [0.5, 0.5] * int(var([1, 4], 32)) +
        [1] * 7 + [0.75, 0.25] +
        [1] * 15,
    amp=1.5
).solo(int(var([0, 1], [120, 8])))

sr >> play('I',
    dur=[var([0.5, 1], 64), var([0.5, 1], 64)] + [2] * 8 + [0.5] * int(var([8, 4, 16, 8], 32)),
    amp=var([1, 0], [[28, 112], [4, 16]])
)

kk >> play('X', sample=var([0, 1, 2], [[128, 32, 32, 64], [128, 64, 128, 32], [128, 8, 64, 32, 32]]), dur=[1] * 7 + [0.5, 0.5] + [1] * 16 + [0.25, 0.25, 0.25, 0.25]).solo(int(var([0, 1], [252, 4])))

sn >> play('O', pan=PWhite(-0.5, 0.5), sample=[2, 1, 2, var([2, 0], [32, 64])], room=1, mix=0.5, dur=1, amp=0.25 * var.kamp)
os >> play('I', sample=3, dur=1, delay=0.5, amp=P[0.65, 0.5] * var.kamp)

bl >> jbass(dur=1, lpf=35, lpr=var([0.25, 0.15, 0.05], 32), amp=var([1, 0], [[28, 56, 24], [4, 8, 8]]))

oc >> play('!', rate=0.95, dur=[[0.5, 0.75], 0.5, 0.5, 0.5, [1, 0.25]], cut=1.5, sample=1, lpf=0, amp=0)

rc >> play('~', pan=PWhite(-0.75, 0.75), dur=0.5, amp=P[1, 0.85] * var.kamp * var([1, 0], [[256, 128], [128, [32, 64]]]))

hh >> play('-', sample=2,
    dur=var([1, 0.5, 0.25, 0.5, 1, 0.5], [64, [28, 24], [4, 8], 64, 128, 32]),
    delay=0.5,
    amp=P[1.5, 1.25] * var([1, 0], [[64, 128, 256], [32, 64, 128]])
)

qq >> play('W', sample=var([1, 2], 256), hpf=expvar([1200, 800], 128), hpr=0.35, dur=PStrum(int(var([4, 3, 8, 7, 5, 2, 1], [64, 32, [8, 32], [8, 64], 16]))) * 1, rate=[[1, 0.85, 1.1, 1.2], 0.95, 1.13, [1, 1.15, 0.95, 0.9],  1, 1.25, 0.95], amp=var([1, 0], [60, 4, 56, 8, 128, 64, 64, 32, 28, 4, 28, 4, 128, 64])).solo(int(var([0 if qq.amp == 1 else 0, 1], [[160, 352], 32])))

######################################333

sc >> play('sound check.', dur=0.25)
ay >> play('!', sample=1, dur=1, amp=[1, 1, 0])
a3 >> play('!', sample=1, rate=0.95, dur=1, delay=0.5, amp=[var([1, 0], 64), var([1, 0], 64), 0])
a2 >> play('!', sample=2, dur=var([1, 0.5], [64, 32]), amp=[0, 0, 1])

Clock.bpm=170

Master().hpf = var([0, 400, 800], [[28, 56], [2, 4], [2, 4]])

Master().hpf = 0

Master().hpr = 0.25

Master().lpf = 0

Master().lpr = 0.25


kd >> play('X',
    sample=var([1, 2], [[256, 128], [128, 64]]),
    rate=[1, 0.98, 1, 0.95] - var([0, 0.1, 0.15], 32),
    dur=1,
    amp=var([1.25, 0], [[28, 56, 56], [4, 8, 8]]) * var([1, 0], [[512, 256], [128, 64]])
).every(64, 'stutter', 2).stop()

sr >> play('o', room=1, mix=0.1, pan=PWhite(-0.75, 0.75), dur=0.25, amp=P[0.15, 0.2, 0.35, 0.18, 0.5, 0.3, 0.6] * var([0, 1], [[28, 56, 56], [4, 8, 8]])).stop()

tm >> play('V', sample=var([1, 2], [[128, 256, 256], [64, 128]]), dur=var([2, 1], [64, [128, 256, 512]]), amp=var([1, 0], [[256, 128], [128, 64]])).stop()

rb >> play('v', sample=1, dur=0.25, amp=P[0.5, 0.25, 0.15, 0.35, 0, 0, 0, 0] * var([1, 0], 256)).stop()

ds >> play('W', rate=[1, 0.95], echo=0.25, echotime=1, sample=1, dur=0.5, amp=[1, 1.5]).stop()

ab >> play('G', dur=[var([0.5, 1.5], [[28, 56, 56], [4, 8, 8]]), 0.25, 0.25], hpf=expvar([200, 800], [[32, 64, 128], 0]), hpr=0.25, amp=expvar([0, 2], [128, 256, [128, 64]])).stop()

rh >> play('=', dur=0.25, amp=expvar([0, 0, 1.5], [[32, 64], [32, 64, 128], 0])).stop()

sa >> play('s', pan=PWhite(-0.75, 0.75), dur=0.25, amp=P[[1, 0.25, 0.5, 0.75], PWhite(0, 1)] * var([4, 0], [[256, 128, 64], [64, 128, 32, 32]])).stop()

rc >> play('~', dur=0.5, amp=var([0, 3], [[128, 64, 256, 64, 32, 32], [256, 128, 64, 64]])).stop()

sk >> play('X', sample=var([1, 2], [[256, 128], [64, 32]]), lpf=kd.lpf, dur=1, delay=[0.5, var([0.5, 0.75], [128, 128, 64])],
    amp=P[
        var([0, 1], [256, 64, 32, 32]), var([0, 1], [[256, 128], [32, 128, 64, 32]]), 0, var([0, 1], [[32, 32, 64, 128], [32, 64]]),
        var([0, 1], [32, 64, 32, 128, 32]), var([1, 0], [[32, 64, 128], 32]), 1, var([0, 1], [[256, 128, 64], [32, 64]])
    ] * (kd.amp * var([0.75, 0], [[512, 256], 128]))
).stop()

dh >> play('w', sample=1, dur=[2, 4], delay=0.5, amp=var([1, 0], [[256, 128, 64], [128, 64, 32]])).stop()

ml >> play('r', sample=1, pan=PWhite(-0.5, 0.5), dur=0.25, lpf=[1500, [1350, 1500, 1000], [1200, 2000]], amp=var([2.75, 0], [128, 64, [32, 64, 128], [32, 64, 32, 128]])).stop()

cl >> play('H', dur=var([2, 1], [[128, 64], [64, 32]]), delay=0.75, lpf=4000, amp=var([0.5, 0.15], [[128, 64], [64, 128, 32, 32]])).stop()

h1 >> play('-', sample=var([2, 1], [128, 64, 32, 32]), dur=1, delay=0.5, amp=var([1, 0], [[64, 128, 256], [32, [64, 128], 128]])).every(8,"stutter",2).stop()

sh >> play('S', dur=1, delay=0.5, amp=var([1.1, 0], [[256, 128], 128, 64])).stop()

h2 >> play('-', sample=var([1, 2, 0], [64, 32, 32]), dur=0.25, amp=expvar([1, 0.1], 1/3) * var([0, 1], [[64, 128, [32, 64, 128]], [128, 64, 32, 128]])).stop()

rs >> play('I', dur=var([2, 8, 4, 2, 1], [64, 32, 32, 64, 8]), amp=1).stop()

sc >> play('z', echo=0.25, echotime=1, sample=2, dur=var([8, 4, 2, 1], [128, 64, 32, 16]), amp=P[3, 2] * var([1, 0], [[128, 256, 64, 64], [64, 32, 128]])).stop()

b1 >> play("g",dur=PDur(3,8),lpf=linvar([800,2000],32),amplify=1/3).every(PRand([4,8,16]),"stutter",2)

b2 >> play(".[ss]",rate=var([1,7/5],[12,4]),sample=2,amplify=2/3)

b3 >> play("<..i...[.i].>",dur=1/2,rate=2,sample=0,amplify=var([1, 0], [[64, 128, 256], [32, 64, 128]]))

b4 >> play("[--]",sample=-1,amplify=4/5)


s1 >> dab([0,2,0,4]+P([2,2,4,-1],[8,16,4,32]),oct=(5,6),dur=1/4,chop=var([4,8],[[64,128,256],[32,64,128]]),formant=linvar([0,5],8),amplify=var([2/5,0],[128,64]))

s2 >> arpy(s1.degree,dur=Pvar([PDur(5,8),1/4],[24,8]),shape=1,formant=linvar([0,4],32),hpf=linvar([200,1200],8),amplify=4/5)

s3 >> dbass(([0,2,0,2],PRand([Scale.default])),oct=(4,5),dur=4,sus=2,echo=PRand([1/2,6/5],1/2),chop=4,formant=expvar([1,4],8),amplify=2/8)

s4 >> lazer(P[:8],dur=1/2,oct=var([4,5],16),formant=linvar([0,4],16),amplify=var([0,2],[64,32]))

s5 >> bell(s3.degree,oct=(5,PRand([6,7])),dur=PRand([1/4,1/2]),sus=1/4,formant=1,lpf=linvar([400,900],32),pan=[-2/3,2/3],room=3/4,mix=1/2,amplify=2/6)

# Uhh, a little to much....Master it!!! LOL

# Ahhhhh..we almost killed it 8-D

# And me donkey

# I loved it


# ^^^ GOOVY :D

n0 >> play('V', amp=0.25, lpf=100, drive=0.05, dur=1, shape=0.25, lpr=0.35, sus=0.25, chop=0.75).every(8, 'stutter', 3)
o0 >> play('\\', amp=expvar([0.75,0], [[256,128],0,0,0,0]), rate=expvar([0,5],256), pan=[-1, 1], spin=64, bpf=var([600,3000],256))
dl >> play('T', amp=h2.amp, drive=0.05, dur=var([1,PDur(5,16)],[4,16]), shape=0.25, pan=[-1,1], spin=16, vib=2).offbeat()
ex >> play('!', amp=expvar([1,0],[[256,0],256]), rate=expvar([0,10],256), bend=var([0,10],256))


@nextBar
def stopod():
    o0.stop()
    o0.reset()

Scale.default='minor'

@nextBar
def stopnoodlex():
    Group(n0,o0,dl,ex).stop()

w0 >> play('Q', amp=expvar([0.25,1],256), dur=16, shape=2, echo=1, rate=1, drive=0.25, room=var([0.25,0.02],[128,64])).every(16, 'stutter', 2)

ah >> play('[t t]', amp=0.75)

s1 >> sitar(P[:8]*PStrum([5,16]), drive=0.25, amp=0.25, shape=var([0,10],64), bit=4, chop=8).every(4, 'stutter', 2)
