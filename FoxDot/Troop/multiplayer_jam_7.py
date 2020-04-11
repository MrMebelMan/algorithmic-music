Clock.set_time(0)

Clock.bpm = 210

print(Samples)

print(SynthDefs)

print(Attributes)

# I will be doing visuals from the Troop screen in hydra >:D

############################

Master().hpf = 0

Master().hpr = 0.25

Master().lpf = 0


# THANKS GUYS!

# was really fun

u1 >> play('r',
    dur=0.25,
    sample=1,
    lpf=expvar([8000, 2500], [0, [32, 64]]),
    tremolo=2,
    amp=[1, 0.75, 0.5, [0.25, 0.5, 0.75]]
)

u2 >> play('U', sample=13, dur=[2, var([4, 1, 1], [32, 64]), 1, 1], amp=[0.25, 0.25, 0.25, [0.25, 0]]).stop()

tm >> play('M', sample=1, dur=var([2, 1], [128, [64, 32]]), amp=var([1, 0], [[64, 128], [32, 32, 64]]))

h1 >> play('-', dur=1, delay=0.5, amp=var([1, 0], [[32, 32, 64], [[64, 128], 32]]))
h2 >> play('-', sample=2, dur=0.25, amp=expvar([1, 0.1], 1/3) * var([0, 1], [[32, 64], [64, 64, 128]]))

r4 >> play('(rtvv)op', dur=[0.5, 0.25, 0.25], lpf=5000, amp=var([1, 0], [[256, 128, 64], [128, 64]])).stop()

rc >> play('~', dur=2, delay=0.5, amp=var([3, 0], [[128, 256, 64], [256, 128, 64]]))
sh >> play('s', dur=0.25, pan=PWhite(-0.5, 0.5), amp=PWhite(1, 3) * var([0, 1], [[256, 64, 32], 128, 64, 64]))

kd >> play('X',
    rate=[1, 0.98, 1, 0.95],
    sample=var([1, 2], [256, 128]),
    dur=1,
    lpf=250,
    amp=var([1.25, 0], [[256, 128, 64], [128, 64, 32]]) * var([1, 0], [[28, 56, 56], [4, 8, 8]])
)

@next_bar
def action():
    Group(u1, u2, tm, h1, h2, r4, rc, sh).stop()
    Group(dd, sk, dk, rs, ac, bp, kd, dd, s0).stop()


dd >> play('S', dur=0.5, amp=P[1.5, 1] * var([0, 1], [128, 64, 32, 32, 256, 32, 32]))

sk >> play('X',
    sample=1,
    dur=1,
    delay=0.5,
    lpf=250,
    amp=P[
        var([1, 0], 128), var([0, 1], [64, 128, 256]), 0, 0,
        var([1, 0], [128, 64, 32]), 0, 0, var([0, 1], [8, 8, 32, 32, 64, 128])
    ] * kd.amp * var([1, 0], [[128, 64], [64, 64, 128]])
)

dk >> play('V', sample=2, rate=var([1, 1.5, 1.25], [64, 32, 8]), drive=1, dur=[1] * int(var([7, 16], 32)) + [[0.5, 0.5, 0.25], [0.5, 0.5, 0.75]], hpf=700, hpr=0.35, amp=var([0.4, 0], [128, 64, [32, 64, 128], 32])).stop()

rs >> play('I', dur=var([2, 1, 4, 2], [32, [8, 16], [64, 32], 32]), amp=2.5)

h2 >> play('=', dur=0.25, amp=expvar([0, 0, 1.25], [[32, 64], [32, 64, 128], 0]))

ac >> sawbass([1, var([3, 2, 1, 0], 32), var([2, 1, 0], 8), var([2, 1, 0, 3], [8, 16])], dur=0.25, sus=[0.25, 0.5, 0.25, 0.25, [0.5, 0.25, 0.75]], hpf=expvar([800, 200], [32, [16, 32, 64]]), hpr=expvar([0.75, 0.25], 32), amp=expvar([1, 0], [256, 512]))

bp >> swell(dur=1, delay=0.5, sus=1, hpf=150, hpr=0.5, amp=P[2, 1.5] * var([0, 1], [32, 16, 32, 32, 64]))
br >> play('v', dur=0.25, amp=P[0.25, 0.85, 1, 0.5,  1, 1, 0.5, 0.75] * var([1.3, 0], [[256, 64, 128], [128, 32, 64]]))


b1 >> dbass([0,2,4,1],dur=1/4,shape=1/3,hpf=linvar([800,1300],16),amplify=1/3)

b1.stop()

b2 >> arpy([0,2,0,4],oct=PRand([5,6],1/8),dur=PRand([1/8,1/4],1/8),shape=1,formant=expvar([3,7],64),amp=2/6)

b2.stop()


p1 >> play('X', amp=0.25)


s0 >> sinepad(P[0,0].stutter(2), amp=var([1,0],[[64,32],16]), lpf=300, lpr=0.25)

s0.stop()



# 

# <333333333333333333333333333333333333333333333333333333333333333

# thank youuuuu

# now let's gradually stop the music

# louder!

############################

# very nice jam!





# XD

print(Samples)

print(SynthDefs)

print(Attributes)

