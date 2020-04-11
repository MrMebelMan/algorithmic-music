Clock.bpm = 150

print(SynthDefs)

var.bassl=var([0,-1,0,3,0,-1,0,4])
var.chords=var([(0,2),(-1,1),(0,2),(3,5),(0,2),(-1,1),(0,2),(4,7)])
note=PRand(Scale.default)

vl >> viola(dur=[16, 8], pan=PWhite(-0.5, 0.5), sus=16, oct=4.5, tremolo=4, amp=0.75) + (var([-1, 0, 1], 32), var([-2, -3], 64))

dk >> donk(dur=1, delay=0.5, sus=0.5, lpf=300, lpr=0.5, room=1, mix=0.15,
    amp=P[
        1, [0.5, 0], 1, var([1, 0], [128, 64]),  var([0, 0.75], [128, 64]), 1, 1, 1
    ] * 0.9
)
#dk.amp = [[1, 1.1], 0.85]
tt >> play('r', pan=PWhite(-0.5, 0.5), dur=0.25, amp=P[[0.25, 0.5], 0, 0, 0,  [0.25, 0.5], [0.5, 0.5, 0.75, 0.75], 0.75, 1] * 1)
kd >> play('X', rate=[1, 0.95, 1, 0.9, 1, 1, 1, 1], dur=var([2, 1], [[256, 64], [128, 256]]), sample=var([2, 1], [[256, 128], [64, 32, 128]]), lpf=var([350, 400, 250], 32), amp=[1.75, [1.5, 1.5, 1.5, 1.75]])
h1 >> play('-', sample=2, room=1, mix=0.15, dur=kd.dur, delay=kd.dur / 2, amp=var([0, 1], [[128, 64], [256, 128]]))
sh >> play('s', sample=1, dur=0.5, lpf=2800, amp=P[1, [1.5, 0.75]] * var([1, 0], [[64, 128], [128, 256, 64]]))
rs >> play('I', dur=var([2, 1], [[256, 128], [64, 32]]), amp=1.5)

sf >> soft(dur=1, sus=[1, 0.5, 0.5, 1], amp=0)

s1 >> dab(var.bassl,oct=(4,5),dur=1,drive=1/2 * var([0.25, 0.5, 0.75], 32),hpf=var([200, 220], [[28, 56], [4, 8]]),amplify=1/3,amp=var([1, 0], [[256, 128, 64], [128, 64, 32]]))
s2 >> dbass(var.bassl,dur=16,chop=16,hpf=linvar([400,800],16),amplify=4/5,amp=var([1, 0], [[256, 128], [128, 64]]))

s3 >> pulse((var.bassl,P[:2]),oct=7,dur=PDur(3,5),chop=1/2,formant=3,hpf=800,amplify=1/7,amp=var([0, 1], [32, 64, 128, 128, 32, 64]))

s4 >> creep(var.chords,dur=1/2,sus=1/4,echo=1/2,shape=2/3,bend=2,hpf=200,formant=4,room=1/3,mix=1/3,amplify=2/6,amp=1).offbeat()

s5 >> jbass(var.chords,oct=5,dur=1/4,sus=1/4,formant=2,drive=1/7,lpf=linvar([200,800],32),pan=[-2/3,2/3],amplify=1/4,amp=1)

s6 >> sawbass(amplify=1/5)

Group(s6, s5, s3, s4, s2, s1).stop()

b1 >> play("V",dur=2,delay=[1,1/2],sample=2,rate=2,drive=1/2,lpf=200,amplify=2/3,amp=1)

b2 >> play("<i>",dur=2,sample=0,delay=[1/2,1/2,1])

b3 >> play("[--]",sample=-1,lpf=linvar([400,1200],32),amplify=4/5,amp=1).stop()


b3.st

p0 >> play('X', amp=0.55, lpf=1500, lpr=0.25, dur=4, echo=0.02, echotime=2).every(4, 'stutter', 2)


p1 >> play('*', amp=var([0.25,0.5],1), striate=10, rate=-1) 

#I am going to brb I am starving



