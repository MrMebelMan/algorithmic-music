Clock.bpm = 137

print(sorted(SynthDefs)) # <3

print(Samples)

print(sorted(Attributes))

print(Clock.bpm)
print(Scale.default)

# henlo


var.chords =
var.brk = var([1, 0], [31, 1, 28, 4, 56, 8, 31, 1, 32, 0, 32, 0, 31, 1])
var.drp = 
var.


# no=[q,g,h,j,k]

xx >> play("X", dur=1, pan=PSine(5), lpf=150).every(PRand(5,8),'stutter')
xy >> play("wertyuiopasdflzx").every(16,'stutter')


m0 >> bass([0,7,2,4],dur=4,chop=1,pan=[-2/3,2/3],amplify=2/3,amp=1)

m1 >> pluck([6,7,8,9],dur=4, lpf=linvar(600,10000), pan=[-3/7,3/7],amplify=3/4)

Clock.bpm = 133 * 2

Scale.default = "minor"

kc >> bug(
    PZip(
        P[0, -0.5, -1, 0,  0, 0, 0.5, -0.5,  -0.5, -1, -1.5, -0.5], P[0.5, 0.25, -0.15, -0.05]
    ),
    dur=0.25,
    lpf=P[
        500, [750, var([250, 500, 1250], 256), 500, 800], 1500, [300, 2000, 1500, 1250],
        1250, 400, var([800, 1800, 500, 1500], 32), var([var([500, 750, 1300], [128, 64, [128, 32]]), 500, 750, 1000], [64, 32])
    ] * [2, int(var([0, 0.25, 0, 0.5, 1], [64, 128, 256, 182, 32])), 0.25, 0.5, 1, var([1, 2, 3], 64), 1, var([1, 1.5], [32, 64, 64])],
    lpr=P[var([0.25, 1], 128), var([0.25, 1], [128, 64, 32, 32]), 0.5, 0.25,  var([0.85, 1, 0.25], 64), 0.5, var([1, 0.25], [32, 32, 64]), 0.25],
    drive=P[expvar([0, 0.05], [128, 64, 256]), [0, var([0, 0.07], [64, 32, 8,8, 128])], var([0, 0.025], 256), 0.07] * 0.5,
    hpf=P[
        [750, 900, 800, 800], 800, var([850, 500, 400, 900], [32, 64, 8, 8, 8, 8]), 800,
        800, 800, 800, 890
    ] * var([1.25, 1, 1, 0.75, 0.5], [64, 32, 128, 128]),
    hpr=P[0.5, 0.25, 0.25, [0.25, 0.5]] * var([1, 0.5, 0.75, 1.25, 1], [64, 32, 32, 128, 64]),
    room=[1, 0.5, 0.25, 0], mix=[0.25, 0.15, 0.15, 0],
    oct=[5, var([5.98, 5], 128), 5, [5, 4.95]],
    sus=[[0.5, 0.25], 0.25, 0.25, 0.25],
    slide=P[0, 0.05, 0, 0,  -0.1, -0.1, 0.1, 0.1] * var([0, 1], [[28, 56, 28], [4, 8, 4]]),
    amp=P[
        [0.25, var([0.25, 0.85], [128, 64, 32])], var([0, 0.8, 0.5, 0.7], [32, 64, 32, 64]), 0.15, 0.5,
        [0.5, 0.25, 1, 1], 0.75, 0.75, 1,
        0.85, 0.75, 0.9, 1,
        0.25, 0.25, 0.5, 0.75
    ]
) + (var([0, 2, 4], 128), var([0, 6, 10], 64)) + (var([-2, 0], [128, 64]), var([10, 0], [64, 64, 128]), var([0, 7, 14], [[64, 128], 32, 128]))


#Custom Synth test

xx.reset()

xx >> play(
    "<XxVv><  -  -  >"
    , pan=linvar(PSine(3))
    , lpf = ([150,800],10)
    , chop=6
    ).every(32,'stutter')



# reset it if you want, I've aplied some lpf 
and lpr

s0 >> play('m', dur=PDur(3,11), dist=0.2, amplify=var([0.5,1],1)).stop()

s1 >> play('m', dur=PDur(3,11), dist=0.2, amp=var([0.5,1],1)).every(16, 'stutter', lpf=300, lpr=0.25)

b0 >> play('X', dur=PDur(3,8), lpf=300, lpr=0.25, amp=var([0.5,1],1))

b1 >> play('X', dur=PDur(3,11), lpf=150, lpr=0.25, amp=var([0.5,1],1)).every(16, 'stutter')

h0 >> play('-', dur=1, amp=[1,0], lpf=expvar([0,1500],[16, 32]))
h1 >> play('-', dur=1, amp=[1,0], lpf=1500).every(3, 'stutter')


sp >> sinepad(P[0,2,4,3].amen(), 
    shape=0.2, 
    drive=0.02, 
    echo=0.02,
    lpf=1500,
    lpr=0.30,
    hpf=300,
    hpr=0.25,
    mix=0.4,
    room=0.02,
    amp=var([1,0.5],1)
    ).every(4, 'stutter', lpf=1500, lpr=0.25)

cb >> play('T', coarse=4, echo=0.02, dur=4, spin=4, pan=[-1,1], sus=4, nudge=0.5).every(4, 'stutter')




print(Scale.chromatic)

####################################################
# yeah i read about it i tlooked coool :)



