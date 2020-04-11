Clock.bpm = 150
Scale.default = "minor"
Root.default = -2

print(SynthDefs)

ra >> play('drums drums drums drums', dur=[0.25,0.25,0.5,0.5,1,1,1,1], chop=)

var.brk = var([1, 0], [[31, [28, 56], 31, 32], [1, [4, 8], 1, 0]])

ar >> sawbass([[-2, -1, 0, 1, 2], var([0, 2, 4, 8, -2, -4], [64, 32, 32]), 0, -1, -0.5],
    dur=0.25,
    room=P[1, 0.5, 0] * var([1, 0], [[32, 64], 128]), mix=0.15,
    lpf=P[300, 1250, [500, 250, 850]] * 2.5,
    lpr=0.25, drive=[0.05, 0.08, 0, [0, 0.08]],
    hpf=P[150, 200, 180, 180] * var([1, 0.5, 0.75, 1.25, 2], [64, 32, 32]), hpr=0.25,
    amp=P[[0.75, 1], 0.85, 1, 1] * [1, var([0, 0.5, 1], [128, 64, [32, 64]])] * P[1, 0, 0.25, 1] * var([0.75, 0], [[256, 128, 64], [128, 64, 32]])
) + (0, -3, -2, 0)
ar.stop()


h1 >> play('-', sample=var([2, 1], [256, 128, 64, 32, 32]), dur=1, delay=0.5, amp=var([0, 1], [[64, 128], [32, 64]]) * var.brk)
kd >> play('X', sample=var([1, 2], 128), dur=1, lpf=1250, lpr=0.25, delay=0, amp=P[1, 0.85] * var([0, 1], [[128, 256], [64, 32]]) * var.brk)
sk >> play('X',
    sample=1,
    dur=1, delay=0.5,
    amp=P[var([0, 1], [64, 32, 32]), var([1, 0], 256), 0, 0,  0, 1, [0, var([0, 1], [64, 32, 128])], 0] * var([0.75, 0], 64) * kd.amp * var.brk
)
cl >> play('*', dur=var([4, 2], [128, 64]), delay=var([0.5, 0.75], [128, 64, 64, 64, 32, 128, 64]), amp=var([0, 1], [128, 64, 32, 32, [128, 64], [32, 128, 128]]))
rs >> play('I', dur=var([2, 1], [256, 128]), amp=expvar([0.25, 1], [[128, 64], [64, 128]]))
rk >> play('X', sample=2, rate=-1, dur=1, lpf=1500, amp=var([0, 1.25], [[63, 127, 63], 1]))
tm >> play('m',
    dur=0.25,
    lpf=P[[500, 250, 300], 750, [1000, 600, 300], [350, 1500]],
    amp=P[0.25, 0.75, [1, 0.75], 0.85, 0.5, 0.25] * expvar([0.5, 2], 4) * var.brk * expvar([0, 0, 1], [32, 128, [256, 128, 64, 32]])
)

Master().hpf = var([0, 200, 400, 600, 800], [[112, 56], [4, 2], [4, 2], [4, 2], [4, 2]])

Master().hpf = 0

Master().hpr = 0.25

hs >> play('$', sample=2, dur=1, hpf=var([150, 200, 500, 350], 64), hpr=0.25, amp=P[var([0.5, 0, 0.25], 32), [0.25, 0], 0.5, [0.5, 0.5, 0, 0]] * var([1, 0], [64, 32, 64, 32]))
ks >> play('D',
    pan=PWhite(-0.5, 0.5),
    dur=0.25,
    hpf=expvar([200, 1500], [128, 0]), hpr=0.25,
    amp=P[
        1, var([0.75, 1], [64, 32, 128, 128]), var([0, 0.25], [[128, 64], [64, 128]]), var([0, 0.75], [[128, 64], [64, 128]])
    ] * expvar([0, 1], [[128, 64, 256], 0])
)
rc >> play('~', pan=PWhite(-0.5, 0.5), dur=0.5, amp=P[1, 0.75] * expvar([0, 0, 1, 1], [[32, 64], [32, 64], [64, 128], 0]) * 1.5)

@next_bar
def stop():
    Group(kd, sk, rs, h1, xx, xy, tm, b1, bp, kk).stop()


xx >> play(
    "<awertyui>< -- --  ><XxVv><[oooo]       >"
    , amp=P[1, 0.8, 0.7, 0.9]
    , chop=[5,6,7,8]
    , pan=linvar(PSine(2))
    , room=linvar(0.6)
    , lpf=[500, 1000]
    , dist=0.4
    ).every(16,'stutter')
xy >> space(
    [(3,4,[0,1,2,5],7)]
    , dur=[1,2,4,3,5,4,3,2]
    , lpf=800, hpf=1000
    )


b1 >> play("X",
    dur=0.5,
    sample=var([2, 1], [[256, 128], [128, 64, 128]]),
    rate=var([2, 1.85], [[31, 28], [1, 4]]),
    drive=1,
    hpf=P[200, 150, 230, 200] * 1, hpr=expvar([1, 0.25], 64),
    lpf=linvar([200,1200],8),
    amp=P[
        1, [0.25, 0.5, var([0, 0.25, 0.5], [128, 64, 32, 32]), 0], [[0.75, 0], 0.5, 0.25, 0.25], [0.25, var([0, 0.25], [64, 32, 32])]
    ] * var.brk * var([1, 0], [256, 128, 64, 64, 128, 64, 32])
).spread()
bp >> blip(var([-2, -1, -2, 0], [[128, 256], [64, 128]]), dur=0.5, lpf=500, lpr=0.5, amp=P[1, [0.75, 0.3], 1, [0.5, 0.25]] * expvar([0, 2], [128, 256, 256]))
kk >> play('X', dur=1, sample=1, hpf=180, hpr=0.25, amp=P[1, 0.85] * var([0, 1], [256, 128, 128, 32, 32]))
h2 >> play('-', dur=0.25, sample=1, amp=expvar([1, 0.15], 1/3) * var([0, 1], [[64, 128, [64, 32]], [128, 64]]))


b2 >> play(".i",rate=var([1,2],[12,4]),dur=1,sample=2,formant=3,amplify=2/3,amp=1*var.brk)

b3 >> play("-",sample=-1,rate=PRand([5/6,1],2),amplify=2/3,amp=1*var.brk).every(PRand([4,8,16]),"stutter",2)

b4 >> play("n",dur=1/4,rate=2,hpf=expvar([900,2000],16),amplify=1/3)

b5 >> play("V....V..",rate=3/5,sample=3,formant=2/3,lpf=linvar([500,1200],16),amplify=2/3*var.brk)

b6 >> play("..o.",sample=4,formant=PRand([0,1,2,3],var([8,4,16,12,32])),amplify=2/4*var.brk)


note=PRand(Scale.default)

s1 >> dab(
    [var([-1, 0, 1, 2], [32, 64]), var([2, 0, 1], [8, 16, 8, 8]), 1, var([0,1,-1,-2,3],[64,32,16,8,8])],
    lpf=P[[400, 600, 1000], expvar([500, 750, 400, 300], [32, 64]), 600, 700].reverse(),
    lpr=expvar([0.25, [0.5, 0.25, 0.5, 0.5]], [16, 16, 8, 8]),
    chop=var([4, 2, [0, 2, 0, 0]], [64, 32, 32, 128]),
    formant=[0.25, 0, [0, 0.25, 0, 0,], var([0, 0.15], 64)],
    tremolo=[var([0, 2, 4], [128, 64, 32, 32]), 0, 0, 0],
    amplify=P[2/3, 4/5, 1/3, 4/3] * var.brk * var([1, 0], [[256, 128, 64], [128, 64, 32]]) * 0.25
)

s2 >> pulse((s1.degree,note),oct=4,dur=PRand([1/2,PDur(3,5),PDur(5,8),1],1/2),chop=var([4,2,[3,2,4]],[64,32,32,128]),formant=3,lpf=linvar([800,1200],8),amplify=2/3,amp=1*var.brk)

s3 >> donk(s2.degree,oct=7,dur=PDur(5,8),sus=1/2,shape=linvar([1/7,1/5],16),formant=PRand([0,1],8),room=2/3,mix=1/2,amplify=1/4,amp=1*var.brk)

s4 >> arpy(s2.degree,dur=1/4,shape=1/3,formant=2,echo=6/5,pan=PWhite(-2/3,2/3),amplify=6/5,amp=1*var.brk)

s5 >> prophet(s1.degree,dur=4,sus=1/4,shape=1,echo=1/2,room=1/3,mix=1/4,amplify=2).offbeat()


# amp and amplify is the same attribute

#Yeah and no. Amplify is the instrument amplification, while amp can be used for master volume and mixing

# hmmm

# I thought in 

