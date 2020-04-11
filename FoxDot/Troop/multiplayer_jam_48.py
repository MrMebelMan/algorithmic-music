Clock.bpm = 120

# Clock.set_time(0) # to sync everyone's clock when they're here
# we forgot to sync

var.brk = var([1, 0], [31, 1, 28, 4, 31, 1, 56, 8])

p1 >> play(Pvar(['X', "(\).*.@.*.V(O.)(.O).X.*."[:-1]], 128), sample=list(range(100)), hpf=var.hpf_all, hpr=0.25, amp=var([1, 0], [[256, 128], [128, 64]]) * var.brk)
p2 >> play("(V.).-.", sample=1, hpf=var.hpf_all, hpr=0.25, amp=var([0, 1], [64, 128]) * var.brk)
p7 >> play("X(.X)I.", amp=var([1, 0], [256, 128, 64, 64]))
p3 >> bass(linvar([[0,-2],var([2, 1, 0], 32)],1/4), dur=[1, 0.5, 0.5], bend=[0, var([0, -0.25], [128, 64])], tremolo=2, hpf=expvar([150, 130], 1/3), hpr=0.25, amp=0.75 * var.brk)

p4 >> keys([0,2,3,4,3,2,-2,2], dur=.5, amp=.4,shape=.5 , chop=var([0, 2], [28, 4])).every(4,"rotate")

p5 >> play("(W[tt])(o[**])[----](t)",amp=var([1.2, 0], [[128, 64, 32, 64], [64, 128, 64]]) * var.brk)

Master().hpf=var([0,500,1000],[56,4,4,28,2,2])
Master().hpr = 0.25

oh >> play('-', sample=1, dur=1, delay=0.5, amp=var([0, 1], [64, 32]))

# I think ve should have a separate variable for multiplying hpfs instead of using Master
var.hpf_all = var([0,500,1000],[56,4,4,28,2,2])

kd >> play('X', sample=1, dur=[1, var([0.5, 1], 64), var([0.5, 1], 64)], hpf=var.hpf_all, hpr=0.25, amp=var([0, 1], [[64, 128, 256], [32, 64]]))
qq >> jbass(dur=0.25, hpf=[[250, 1200], [150, 500, 1000, 1500], [800, 150, 1500], [750, 130]], hpr=0.25, sus=0.25, amp=expvar([0, 1], 128) * var([1, 0], [[256, 128], 128]))
sb >> sitar(
    P[[1, var([1, 2], [128, 64, 128])], 1, var([1, 0.5], [128, 32]), 1, 1, 1, 1, 1],
    bend=[
        var([-0.15, 0], [64, 32]), 0, [0, var([0, 0.25], 128)], 0,
        0, var([0, 0.15, 0, -0.15], [32, 16, 16]), 0, var([0, 0.25, 0], [8, 8, 16, 32])
    ],
    drive=P[0.05, 0, [0, var([0.03, 0], [64, 32])], 0,  [0, var([0, 0.15], 64)], 0, var([0, 0.02], [128, 64]), 0],
    dur=[0.75, 0.25, [0.25, 0.5], [0.25, 0.5]],
    sus=[0.5, var([0.25, 0.5], [256, 128]), var([0.25, 0.5], [256, 128])],
    hpf=P[
        [var([600, 1200], 64), 800], 300, [450, 650, 400, 400],
        [1200, 1000], [800, 1250], [[450, 700], [650, 300, 250], [400, 200, 150], [400, 200]]
    ] * expvar([0.5, 1.5], 64),
    lpf=[
        var([600, 800, 1200, 450], 32), var([1200, 700], 8), var([900, 1200, 700, 1000]), 1500,
        2000, var([1500, 350, 600], [64, 32]), var([1300, 850], 16), [350, 800]
    ],
    lpr=expvar([0.25, 0.5, 0.25], 32),
    hpr=[0.25, var([0.25, 0.5, 0.2], 64), 0.25, [0.25, var([0.25, 0.15], 128)]],
    amp=var([0, 1], [[32, 64, [128, 64]], [[64, 128], 128, 256]])
)


s1 >> dub(P[0,-1,0,1],dur=var([2,4],16),chop=8,slide=[-1,0,1],amplify=P[1/3,1/5,2/5,1/6,1/4],amp=var([1, 0], [[256, 128], [64, 32, 64]]))

s2 >> sinepad(p3.degree,oct=6,dur=1/4,sus=1/2,delay=[0,1/2],formant=linvar([0,3],8),lpf=500,pan=PWhite(-2/3,2/3),amplify=2/5,amp=var([1, 0], [[512, 256], [256, 128]]))

s3 >> marimba(var([PRand(Scale.default),oct=PRand([5,6]),dur=PRand([1/4,1/2,PDur(3,5),1],1/4),shape=2/3,formant=2,amplify=3/5,amp=1)

print(SynthDefs)

p6 >> star([0,-2],dur=4,chop=[0,2],echo=[0,1],room=1/3,mix=1/3,amplify=4/5,amp=1)





