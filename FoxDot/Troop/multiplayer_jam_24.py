Clock.bpm = 180
Scale.default = "minor"
Root.default = -2

# hello efe, feel free to create your own player, or edit ours!

#blast, can't figure it out

print(Samples)
print(SynthDefs)
print(Attributes)

xy >>  

xz >> bell(
    P[0,4,6,9,12]-1
    , dur=8, sus=12
    , lpf=1000, room=1
    , chop=17
    )
yz >>play(
    "<    m    m><          [pp]    >"
    , dur=1
    , room=1
    , amp=0.6
    , lpf=linvar([200,2000],16)
    , pan=PStep(3,P*(-0.5,0.5))
    ).every(16,'mirror')
zz >> play(
    "<X v >< [ssss]s [ssss]s s>"
    , dur=1, room=0.5
    , amp=[1,0.8,1,0.7]
    , pan=PSine(3)  
).every(32,'stutter')

var.brk = var([1, 0], [[31, 1, 31, 1, 28, 4, 56, 8, 32, 0], 1])

tb >> play('t', 
    pan=PWhite(-0.65, 0.65),
    room=1, mix=0.25,
    sample=3,
    dur=1,
    amp=P[
        1, var([1, 0], [128, 64, 32, 32, 32, 32, 128, [256, 64]]), var([0, 1], [128, 256]), var([0, 1], [128, 256]),
        1, 1, var([0, 1], [[[256, 64, 32], 128, 64], [128, 64, 32]]), 1
    ] * 3.5 * var.brk
)
t2 >> play('t', sample=tb.sample, dur=1, delay=0.5,
    amp=P[
        0, var([0, 1], [[32, 64], [64, 128]]), 0, 0,
        var([0, 1], [128, 64, 32, 64]), 0, 0, 0
    ] * 2 * var.brk
)
rs >> play('I', dur=var([1, 4, 2, [1, 8, 4, 2]], [512, 256, 128, 64]), room=1, mix=0.15, amp=expvar([0, 0, 1, 1], [[32, 64], [32, 64], [64, 128], [64, 128]]))
kd >> play('X',
    sample=var([1, 0, 1, 1], 128),
    dur=var([2, 1], [[256, 128, 64, 64], [128, 256]]),
    lpf=var([450, 750, 1000], [64, 128, 64]), lpr=0.5,
    amp=P[1, [0.75, 0.5]] * var([0, 1], [[128, 256], [64, 128]]) * 1.25 * var.brk
)
sk >> play('X', sample=kd.sample, dur=rs.dur, delay=0.5, lpf=350, lpr=0.25, amp=P[0, 1, 0, 0,  0, 1, 0, 0] * var([0.5, 0], [[64, 128, 64, 32], [32, ) * kd.amp * var.brk)
h1 >> play('-', sample=2, dur=kd.dur, delay=0.5, amp=kd.amp * var([1, 0], [[64, 128], [32, 64, 32]]))
ch >> play('*', dur=var([8, 4, 2], [[256, 128], [128, 64], [64, 32]]), delay=0.5, amp=var([0, 0.85], [[32, 64, 128], [64, 128, 256]]))
rk >> play('X', sample=2, rate=-1, dur=1, amp=var([0, 1], [[127, 63], 1]))

s0 >> sinepad(lpf=expvar([0,4],8)*var([300,1500],[64,32])*expvar([4,0],8), 
    pan=[-1,1], 
    spin=4, 
    sus=2,
    amp=t2.amp, 
    echo=0.02).every(16, 'stutter')    
ss >> sinepad(oct=[4,6], 
    fmod=2, 
    pshift=linvar([-1,0,1],[[64,32],[128,16]]),
    echo=0.2,
    amp=t2.amp,
    mix=0.25,
    room=expvar([0,1],32)
    ).every(4, 'stutter', lpf=300, lpr=0.25)

b0 >> bug(vib=2, 
    vibdepth=2, 
    amp=linvar([0.05,0.25],1)*tb.amp, 
    echo=0.02, 
    pan=[-1,1]*r, 
    spin=var([0,16],[15,1])*t2.amp, 
    sus=2, 
    chop=4, 
    dur=1,
    coarse=4*kd.amp,
    rate=var([1,-1],[127,1])).every(2, 'stutter', pshift=-1)

cb >> play('T', dur=4, echo=var([0.02,0.2],4), hpf=800, hpr=0.25, amp=var([0.25,1],1)*t2.amp).every(2, 'stutter', lpf=1500, lpr=0.35)

p0 >> play('f', dur=8, echo=0.2, mix=0.2, room=1)
p1 >> play('f', dur=4)



#Just a minute. I'm checking my notes


# maybe some filter? :3 You can help, of course. I'm so amateur.

e1 >> space(PDelta([.1,-.1])[:20]+P**(0,1,3,4),amp=0.15, room=1, lpf= sinvar([300,2000],8), bpm=90)
e2 >> klank(PWhite(-4,4)[:15],tremolo=PSine(16), amp=0.3, shape=sinvar([.1,.5],32),dur=4,oct=[4,3,2,1],room=1, mix=.8,spin=16)

e1.stop()


#######################
# Welcome!

#yo
