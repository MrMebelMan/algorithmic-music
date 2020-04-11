Clock.set_time(0)


Clock.bpm = 150

# ok, let's play with them a little bit

u1 >> play('U', sample=8, dur=1, lpf=expvar([200, 800], 32), amp=expvar([0.25, 1], 64))
u3 >> play('U', sample=6, dur=1, delay=0.5, lpf=200, amp=[0, 1, 0, var([0, 0.5], 64),  0, [0, 1], 0, 0])
h1 >> play('-', pan=PWhite(-0.5, 0.5), dur=0.25, amp=expvar([0, 1], 1/3) * var([0.5, 0], [64, 32]))

u4 >> play('U', sample=45, dur=4, lpf=var([5000, 4000, 3000, 6000], 4), amp=var([0.45, 0], [32, 64, [32, 64]]))
u5 >> play('U', sample=48, dur=1, delay=0.5, hpf=expvar([5000, 200], [64, 0]), hpr=expvar([0.5, 0.25], 32), amp=0.35)

k1 >> play('X', sample=1, dur=1, lpf=200, amp=var([1, 0], [[64, 128, 256], [32, 64, 128]]))
k2 >> play('X', sample=1, dur=1, delay=0.5, lpf=200, amp=[var([0.85, 0], [[64, 128], [32, 64]]), 0, 0, 0])

h2 >> play('-', sample=1, dur=1, delay=0.5, amp=var([0, 1.25], [64, 64, 64, 32, 128, 64]))
sh >> play('s', dur=var([2, 1], 64), amp=0.8)

u6 >> play('U', sample=38, dur=[0.5, 0.25, 0.25], sus=[0.5, 0.25, 0.25], lpf=2500, lpr=0.5, amp=var([0, 0.25], [[128, 64], [64, 128]]))
u8 >> play('U', pan=PWhite(-0.5, 0.5), dur=0.25, sus=0.25, sample=51, lpf=[5000, 3500, 2500], hpf=expvar([200, 1500], [32, 64, 64]), hpr=expvar([0.25, 0.5], [16, 16, 32]), amp=0.9)

u9 >> play('U', sample=58, dur=8, amp=0)
rs >> play('I', room=1, mix=0.2, dur=2, amp=var([0.9, 0], [[128, 64], [64, 32]]))
sh >> play('sss', sample=[2, 2, 1], dur=[0.25, 0.25, 0.5], amp=var([0, 1], [[128, 64], [64, 64, 32]]))
bd >> play('V', sample=0, dur=1, lpf=250, amp=1)

# ok, let's try to gradually stop it

Group(k1, k2, h2, sh).stop()

# I've got a nice recording!


u2 >> play('U',
    sample=32,
    dur=PDur(3,5),
    lpf=[1000, PWhite(800, 3500)],
    amp=linvar([0.05,0.35],64),
    lpr=var([0.1, 0.5, 0.75], [32, 16, 16]),
    room=0.25, mix=0.5, echo=var([0, 0.005], [64, 32]))

p1 >> play(P['X'].shuffle(2), amp=linvar([0.25,0.45],64), lpf=var([300, 500],16))

u9 >> play('U', sample=50, amp=sinvar([0,0.25],16), dur=2, pan=[-1,1])

u7 >> play('U', sample=60, amp=expvar([0,0.5],[64,16,128]), hpf=var([150, 300],[64,16,128]), hpr=0.01)

# lol

u7.stop()

u8 >> play(P['U'].stutter(4),
    sample=35,
    amp=linvar([0.25,0.5], 64),
    bpf=var([300,3000],16),
    echo=0.002,
    room=expvar([0,1],32),
    mix=0.5, pan=[-1,1] )

# uh

hi >> play(P['[m m m]'].stutter(4), amp=[0])



Master().rate = 1

# you meant rate?

# sick

# :D <3

print(Samples)

print(SynthDefs)

print(Attributes)
