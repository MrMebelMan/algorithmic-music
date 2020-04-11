Clock.bpm = 133
Clock.meter = (3,4)

print(SynthDefs)
print(Samples)
print(Attributes)

###############################

o0 >> play('|u0|', dur=PDur(var([3,5],[4,8]),11).rotate(3), lpf=6500, lpr=0.25, amp=sinvar([0.05, 1], [128, 0]|var.sngvar)*var.brk, room=0.75, mix=0.25).every(4, 'offbeat') #.stop()

dl >> play('~', amp=expvar([0,1],[[255,128],var.sngvar])*var.brk, rate=expvar([0,2],[[255,128],[128,64]]), echo=0.002, pan=[-1,1], spin=64, striate=100, room=expvar([100,0.001],[[255,128],[128,64]]),mix=expvar([1,0.001],[[255,128],[128,64]])).every(128, 'stutter', spin=128)

d2 >> sinepad([3, 2, 0, -1], oct=4.4, lpf=0, dur=1, delay=0.5, amp=P[0, 0.5, [0, 0.5], 0] * var.brk)


nl >> nylon([0, -2, 1, -1, -2], dur=16, sus=10, tremolo=4, amp=expvar([0, 1], [[128, 0], 0]))
vs >> varsaw(-2, dur=[2, 1, 1], tremolo=2, amp=expvar([0.15, 1.25], [[128, 0], 0]))
sh >> play('s', dur=0.25, amp=expvar([1, 0], 8) * var([1, 0], [8, 32]) * var([0,0,1,1,0,1,0,1], var.sngvar) * var.brk)
os >> play('u', dur=1, delay=0, amp=[o0.amp, 0, 0, 0,  0, [o0.amp / 2, 0], 0, 0])
gg >> gong(dur=4, sus=8, tremolo=4, amp=var([1, 0], [128, 64, 64, 128]))
db >> dab(var([0, -0.5, 0.5], [32, 16, 8, 8]), dur=1, sus=0.25, lpf=300, amp=expvar([0, 0.4], [128, 64, 64, 128]))
ks >> keys(room=0.75, mix=[0.15, 0.25], dur=PStrum(var([2, 3, 8, 4], 32)) / 2, lpf=[500, 250, [800, 400, 300], 1000], lpr=0.5, amp=sinvar([1.25, 0], [128, 64, 64, 128, 64, 64, 128, 128]) * var.brk)

Group(nl, vs, sh, os, gg, db, ks).stop()

k3 >> play('X', dur=1, amp=P[1, 1, 1, 1] * var([0,0,1,1,0,1,0,1], var.sngvar) * var.brk)
sk >> play('X', dur=1, delay=[[0.5, 0.75], [0.75, 0.5, 0.5]], amp=P[0, 0.75, 0, 0] * k3.amp)

# too much timevars inside our timevars I guess

ch >> charm(
    room=1, mix=0.25,
    dur=[0.75, 0.25, 0.5, 0.5, 1, 1],
    bend=[[-0.15, 0], 0, [0, 0, 0.05], 0],
    amp=[0.75] * 3 + [var([0, 1], [64, [32, 64, 128]])]
)

rs >> play('I', room=2, mix=0.15, dur=var([2, 4, 8, 1, 2], [64, 128, 32, 8, 8]), amp=var([0,0,1,1,0,1,1,0], var.sngvar))
cp >> play('*', echo=[0, 0.25, 0, 0], echotime=0.5, dur=1, delay=[0.5, 0, 0, 0], amp=expvar([0, 0.8], [64 ,128, 64, 32, 32]))


#That would be with different effects, speeds, and amplitude....I only did that once, so I ll try

#Intro,Break, Buildup, Drop, Break, Buildup, Drop, Outro...repeat!?# nice

var.sngvar=P[128,64,64,128,64,64,128,128]
note1=[0,1,3,PRand(Scale.minor)]
var.brk = var([1, 0], [[[28, 32], [28, 32], [56, 28]], [[4, 0], [4, 0], [8, 4]]])
sngvar=[128,64,64,128,64,64,128,128]

print(Scale.minor)
]

s1 >> dub(note1,oct=(5,6),dur=8,chop=4,formant=0,amplify=1/7,amp=var([0,0,1,1,0,1,1,0],var.sngvar))

s2 >> saw(note1,oct=(5,PRand([6,7])),dur=PRand([1,2,4],1),shape=1/4,coarse=3,formant=2,amplify=2/7,amp=var([0,0,0,1,0,0,1,0],var.sngvar))

s3 >> klank(note1,oct=5,chop=4,tremolo=2,formant=3,amplify=3/7,amp=var([0,1,0,1,1,0,1,0],var.sngvar) * var.brk)

s4 >> fuzz(PRand(Scale.minor),dur=16,formant=3,lpf=linvar([400,1200],16),room=2/5,mix=1/2,amplify=2/7,amp=var([0,0,1,1,0,1,0,1],var.sngvar))

b1 >> play("U....U..",rate=2,amplify=2/9,amp=1)

b2 >> play("..i...[i.].",dur=1,sample=1,echo=var([1/2,6/5],[24,8]),room=3/4,mix=1/2,amplify=1/3)

b3 >> play("f", rate=linvar([0.95, 1.1], var.sngvar), amp=var([0.75, 0], 128))

b4 >> play(".s",lpf=linvar([400,2600],16),shape=2,bend=1,amplify=2/5).spread()

b5 >> play("[--]",sample=-1,rate=var([1/2,1],var.brk),bend=linvar([1,2.4],[4,16,32,8,4]),amplify=2/3)

print(var.sngvar)

# vOverzilla

#Wicked, that sounds like rails

#yes it is for time var arrangements over an entire track struc

ex >> sinepad(note1|P[0,-2,1,-1,-1],
    amp=sinvar([0.25,0.5],sngvar)*linvar([1,0], 128),
    rate=sinvar([0,2],sngvar),
    dur=var([0.25,0.75,0.75,0.75,0.75,1],[10,1,1,1,1,1]),
    bend=var([0,1,-1],[10,2,3]),
    pan=[-1,1]).stop()

e3 >> play(':', dur=PDur(var([3,5],sngvar),11).rotate(3), amp=expvar([0.2,0.5],sngvar)*var.brk, echo=0.02, rate=1).every(3, 'offbeat').every(11, 'stutter')


#Noodle, which was the var for breaks n beats...HOw do I do this with

# oh, it kept throwing errors for me, but I guess not lol
# I think it just makes enables the updates for variable's value

print(var([0,1,-1],[10,2,3]))
