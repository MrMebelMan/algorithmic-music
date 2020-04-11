def foo():
    k1 >> play('X', sample=1, dur=0.25, amp=[[0.75, 1], 0.25, 0.5])
    Clock.schedule(lambda: k1.stop(), 32)

Clock.set_time(0)
print(Clock.beat)
Clock.schedule(foo, 8)


# yo

# I'm in for a quickie

# lemme just reset the clock and run your players

print(Samples)

print(SynthDefs)

print(Attributes)

# AYEE

#guys i have to go... now its 2am :D

#nice to have meet u

#we have to repeat ;)


#lol i dont understand the clock xDDDD

# I just reset the time to 0, so we got the same sound at the right time

Clock.bpm = 150

Master().hpf=var([0,4000],[32,8])

var.pat = var([1, 0], [[28, 56], [4, 8]])

bl >> play('m', dur=0.25, lpf=[200, 300, 250, 300, [200, 250]], amp=P[0.25, 0.5, 0.75, 0.65, 0.15] * 2 * var.pat)

bp >> blip(dur=1, oct=5, delay=0.5, amp=1)

# dani, instead of doing p2.solo you'd better alter the other players with var, so they stop playing when you need

# hehe, it's perfectly ok to experiment


#ok, it was because i didnt understand what it played :)

#someone of you is recording?

#;)

# I'll start recording the SC output now

Master().hpr = expvar([0.25, 0.45], [32, 16, 16])
Master().hpf = var([0, 500, 200], [[[120, 28], 56, [60, 28]], [[8, 4], 8, 4], [8, 8, 4]])


b0 >> play('X.', amp=0.75 * var.pat, lpf=var([300,1500],4), lpr=0.2, echo=0.02, pan=[-1,1]).every(2, 'stutter')

b1 >> play('X', amp=var([0, 0.75], [128, 64, 32, 32]), lpf=var([300,1500],4), lpr=0.2, echo=0.02)
b2 >> play('X.', amp=0.75 * var.pat, lpf=var([300,1500],4), lpr=0.2, echo=0.02, pan=[1, -1]).every(2, 'stutter')
b3 >> play('X', sample=var([0, 1, 2], [64, 128]), amp=0.75, lpf=var([300,1500],4), lpr=0.2, echo=0.02)

h1 >> play('-', sample=1, dur=0.25, amp=expvar([1, 0], 1/3) * var([1, 0], [[32, 64], [64, 32]]))
h2 >> play('-', pan=PWhite(-0.5, 0.5), sample=2, lpf=PWhite(3000, 5000), dur=0.25, amp=var([0, 1.25], [[32, 64, 64], [32, 128, 64]]))

ss >> play('S', dur=1, delay=0.5, amp=var([1, 0], [32, 64, 128, 32, 32]))

k1 >> play('V', sample=var([2, 1, 0], [32, [64, 128], 32, 32]), dur=1, lpf=400, amp=var([1.5, 0], [64, 32, 32]))
k2 >> play('v', dur=1, delay=0.5, amp=0.75)

sn >> play('O', sample=1, dur=var([2, 1], [[28, 56], [4, 8]]), amp=var([0.75, 0], [[128, 64], [64, 32]]))
sr >> play('o', dur=0.25, amp=P[0.15, 0.5, 0.25, 0.3, 0.75, 0.5] * var([0, 1.5], [[24, 56], [4, 8]]))

jb >> jbass(dur=0.25, lpf=expvar([180, 80], 1/3), lpr=0.5, amp=P[1, 0.75, 0.5, 0.25] * var([0, 1], [128, 256, 32, 32, 32]))

cb >> play('T', dur=0.25, lpf=P[350, [200, 400, 600], 250, 300, 400] * expvar([1, 3], 128), amp=[1, [0.5, 0.75], 0.9])

ml >> play('r', dur=[0.5, 0.25, 0.25], lpf=expvar([5000, 200], [[64, 32], 0]), lpr=0.5, amp=expvar([0, 1.15], [256, 64, 128, 64, 32, 32]))

u1 >> play('U', pan=PWhite(-0.75, 0.75), sample=26, dur=0.25, lpf=500, amp=[1, 0.75, 0.5, 0.25])

u3 >> play('U', dur=2, sample=40, bend=[-0.5, -0.25], amp=var([0.3, 0], [32, [16, 64], 32]))

kk >> play('X', sample=1, dur=1, lpf=400, hpf=var([0, 200], [[28, 56], [4, 8]]), amp=1)

ko >> play('X', sample=2, lpf=650, dur=1, amp=1.5)

so >> soprano(dur=16, sus=20, tremolo=4, lpf=400, lpr=1.1, amp=0.25)

s0 >> sinepad(amp=var([0.15, 0], [[64, 128], [32, 64]]), tremolo=4, vibdepth=0.2, bend=0.25)

c0 >> play(P['* '].shuffle(2), amp=sinvar([0.25,0.5],16), dur=1, lpf=300, echo=0.02, mix=0.2, room=1, pan=[-1,1]).every(2, 'stutter', 4)

k1 >> play('v', lpf=1500, lpr=0.15, amp=var([0.75,5,0],[128,64,[32, 16, 32, 64]]), dur=PDur(5,16), echo=0.02, mix=0.02).stutter(2)

k1.stop()

c0.stop()

r1>>play("/").stop()


s0.follow(p1)


Group(b0,b1,b2,b3).stop()


p2.reset()



p2 >> play("v.")


p2.solo(0)


p1.stop()

p3 >> play("[...*]", echo=expvar([0.002,0.2],[16,32,64]) )

Scale.default="minor"

u2 >> play('U', sample=16, dur=PDur(5,16), amp=expvar([0, 0, 0.5], [[32, 64], [32, 64], 0]), pan=[[-1, 0], [1, 0]], echo=0.02, lpf=var([300,2000],64))


#It is cool lol

p1>> bass(var([3,4,[2,0],[5,2]],4), amp=0.05 * var.pat * expvar([0, 1], [128, 64, 64]), pan=P*(-1,1), lpf=[500, 300, 250, 400])

p3 >> bass(var([3, 2, 1], [32, 16]), dur=1, delay=0.5, amp=[0, 0.5, 0, 0] * var([0, 1], [128, 64, 32, 32]))


p3 >> pluck(p1.pitch.accompany(), dur=2, amp=var([.25, 0], [64, 32, 32, 128]), delay=0, pan=P*(-1,1))
c1 >> play("..H.", amp=var([1, 0], [64, [32, 128], 32]))


p2 >> pluck([0,2,4], amp=expvar([0.75, 0.25], [64, 32, 32, 16, 128]), delay=[0,.5,.1])

p4.stop()

Group(p1, p3, c1, p2, p4, k4, k5).stop()


k9 >> play('-', amp=expvar([0,1],[128,64]), dur=PDur(5,16), mix=0.2, room=var([0,1],[128,64]), echo=0.02).every(4, 'stutter', 2)

k4 >> play("#", dur=16, room=1, amp=var([0, 1], [[256, 128], [128, 64, 64]]), pan=0.5)
k5 >> play(".@", sample=PRand(P[0:8]), amp=PRand(0,1) * var([0, 1], [64, [32, 64], 32]))
