Clock.set_time(0)

Clock.bpm = 210

print(Samples)

print(SynthDefs)

print(Attributes)

Clock.bpm = var([120, 150], 32)

p0 >> play('t[t d]d',
    dur=0.25,
    amp=[0.25,0.75,0.25],
    tremolo=var([0,4],16),
    lpf=var([300, 600],12),
    lpr=0.15, bend=[0,0,1],
    echo=0.15, room=0.25)

# either k0 or p0

k0 >> play(
    P['I'].stutter([1,4])|P['oOIm'].stutter([1,3])|1,
    rate=[[-1, 1, 0.95, 0.8], 1, [1, 0.75], 1],
    amp=linvar([0.25,0.75],[32, 16]) * var([0, 1], [32, 64, [16, 128], 32, [32, 64]]),
    bend=[-0.5,0,[0, 0.5, 0, -0.5],0,0.25],
    lpf=[100*PWhite(20,10), [1500, 1000, 1250], 750, 1000],
    lpr=var([0.25, 0.15, 0.2], [8, 4]),
    echo=linvar([0.02,0.002],128),
    room=expvar([0.2,2],128),
    dur=0.25
)

# this one!! ^^^

# I changed the sample in k0 and it went crazy

# AAAAAAAAAAAAAAAAAAA

# I can't hear anything?

# TOO MUCH RESONANCE SOMEWHERE
# HOW DO I STOP IT

# I think we're fucking with resonance too much
# I am unable to set the volume on my speaker above minimum
# because it starts to get rekt by resonance

# sorry

# resosnance is dangerous!

# yeah, it takes time for old sound to fade

# idk if you heard it, but on my speakers it was intense

k1 >> play('X',
    amp=sinvar([0.25,0.75],128),
    dur=PDur(5,16)*var([5,11],32),
    drive=0, lpf=300, lpr=[0.15,0.1],
    echo=var([0,0.2],[4,0,4])).stop()


# yes, echo + lpf + lpr + drive :D

# hmm

# I think k1 does this because of the drive & lpr
# or not...

# which player is doing the high pitched whistling sound?

#

Clock.bpm = 220

# <-- here lpr was way below 0.1

n0 >> noise(dur=2, amp=expvar(linvar([0,1], echo=0.2, sus=2, chop=0.25, bend=[-1,1])




# Same

# maybe let's try to make gabber?

# I have no idea how to do it tbh
#

# we need some distorted kicks

kk >> play('V', rate=var([1.85, 1.5], 32), drive=1, sample=1, hpf=var([500, 650, 800], [32, [8, 32], [32, 16], 32]) * var([1, 2], [30, 2]), hpr=0.13, lpr=1, dur=[1] * 7 + [[0.25, 0.5, 0.5], [0.75, 0.5, 0.5], 0.5, 0.5], amp=var([4, 0], [[28, 56, 60], [4, 8, 4]]))

k2 >> play('X', sample=1, dur=1, rate=1.5, drive=1, delay=0.5, hpf=800, hpr=0.25, amp=[1, var([1, 0], 32), var([0, 1], 128), var([0, 1], [64, 32, 32])])

pd >> sinepad([3, 2, 1, 0, 0], dur=0.5, oct=5, vib=0.5, vibdepth=0.5, hpf=400, hpr=0.25, amp=0.25)

cl >> play('H', sample=2, dur=var([2, 4, 1], [32, 16, 4]), amp=0.85)

bd >> play('V', sample=var([1, 0], [64, 32, 32]), dur=var([1, 0.5, 0.25], [[64, 32, 32], 8, 4]), lpf=var([800, 200, 400], [32, 64, 32, 32]),
    amp=[var([1.25, 0], [[32, 64, 32], [4, 8]]), var([0.5, 0.75, 0.5, 1.25], [32, 16, 8])] * var([1, 0], [[64, 32, 128], [32, 64]])
)

# sure!
# it's 6 AM here

# lel



# we gotta learn how to make rave stabs

si >> play('S', dur=1, amp=var([1, 0], [8, 4, 4, 8, 32, 32, 64])).every(8, 'stutter', 2)

sr >> play('o', dur=0.25, amp=P[0.5, 1, 1.25, 0.75, 0.85] * var([0, 0.5], [[28, 56], [4, 8]]))

sn >> play('O', dur=[1] * 7 + [0.5, 0.5], hpf=500, hpr=0.5, drive=var([0.25, 0.75], [8, 4]), amp=var([1, 0], [64, 32]) * var([1, 0], [64, 32, 32, [64, 32]]))

bl >> jbass(dur=0.5, sus=0.5, hpf=100, hpr=0.5, amp=0.85, drive=0.25).stutter(2)

h1 >> play(P['-:'].shuffle(2), sample=2, dur=1, delay=0.5, amp=1)

h2 >> play('-', dur=[0.5, 0.25, 0.25], amp=0.1)

c2 >> play(P['*O'].shuffle(2), dur=[0.5,0.75,0.75], amp=linvar([0.2,0.4],[32,64,16]), drive=0.1)
# ^^ there's nothing to shuffle since there's only one item in tehe array


n1 >> play(amp=var([0.5,0.75],32), dur=PDur(5,11), hpf=300, hpr=0.35)

# hmm, dunnpo what's throwing a TypeError

# YESSS

#ooooooo

# seeee yaaaa

# What happened to the shuffle where is this coming from?

# it's good

# just don't use lpr below 0.1 and echo below 0.1, better >= 0.25

# AFK for a cig

l1 >> play('HELL',
    sample=[var([0, 1, 2], 8), 1, var([2, 0, 0], [32, 16])],
    rate=[1, [-1, 1], 1, 1],
    dur=0.25,
    lpf=[500, 1500, 2000] * expvar([1, 2], [32, 0]),
    tremolo=var([4, 0], [[32, 64], [64, 32]]),
    amp=P[0.75, [0.5, 1, 0.25], [1, var([0, 1], 64)]] * var([1, 0], [[128, 64, 64], [64, 32, 128]])
)

j1 >> play('[---::==X]',
    dur=[0.25, 0.25, 0.25, [0.5, 0.25], 0.25],
    lpf=[500, 250, 750], lpr=expvar([0.25, 0.75], [32, 0]),
    amp=[1.75, 1.5, var([0, 1.8], 32), var([0, 1.5], 32)]
)

h1 >> play('d', sample=1, rate=-1, dur=2, delay=0.5, lpf=400, lpr=0.25, amp=var([1.5, 0], [[128, 64], [64, 64, 32]]))

h2 >> play('t',
    sample=1,
    dur=0.25,
    lpf=[expvar([500, 1500], 32), 1000, 1500, var([250, 1500, 500, 2000], [32, 64])],
    lpr=0.25,
    amp=var([1.25, 0], [32, [64, 128, 256], 128])
)

rr >> play('r',
    sample=var([1, 2, 1, 0], [64, 32, 32]),
    room=1,
    mix=0.3,
    bend=[[0, -0.25], 0, 0],
    dur=[[0.5, 0.5, 0.5, 0.25], 0.25, 0.25],
    lpf=expvar([3500, 1250], [[64, 32], 0]),
    lpr=expvar([0.25, 0.5], 8),
    amp=P[[1, 0.75], 0.85, [0.75, 0.85, 0.95]]
)

s1 >> saw(dur=2, oct=6, tremolo=2, amp=0)


kd >> play('X',
    sample=2,
    rate=var([1, 0.95, 0.9], 64),
    dur=[[1, 0.5, 1, var([1, 2], 32)], [1, 0.25], [1, 0.75], 1],
    lpf=var([300, 200, 500, 250], 32), lpr=0.25,
    amp=var([1.85, 0], [32, 32, 64]) * var([1, 0], [[28, 56], [4, 8]])
)
kd.dur = 1

b2 >> play('t', rate=1.25, drive=var([0.25, 0.15, 0.05, 0, 0], [32, 64, 32, 32]), sample=1, dur=[var([1, 0.5], 64), var([1, 0.5], 64), 0.25, 0.75, 1], amp=var([2.5, 0], [64, 128]))

bd >> play('V',
    sample=[1, [2, 1], 1, [1, 1, 2]],
    rate=P[10, 5, 2.5, 7.5, 1, 1.5, 7.5, 12] * var([1, 0.5], 64),
    drive=[0.1, 0.25, 0.15, 0.1],
    dur=var([0.5, 0.25], [[64, 128], [128, 256]]),
    lpf=var([5000, 2500, 1500, 1000, 750, 300], 32), lpr=0.25,
    hpf=0, hpr=0.15,
    amp=[1, 0.75, [0.25, 0.5], [0.5, 0.25, 0.75]] * var([1, 0], [[28, 56], [4, 8]]))
bd.rate=1
bd.drive=0


Master().hpf = var([0, 200], [[28, 56], [4, 8]])
Master().hpr = 0.25

h3 >> play('-', sample=1, dur=1, delay=0.5, amp=var([1.5, 0], [[64, 32, 128], [32, 16, 64]])).every([8, 16], 'stutter', 2)

rs >> play('I', echo=0.25, echotime=var([0, 0.5], [[128, 64, 32], [64, 32, 32]]), dur=var([2, 4, 2, 1], [64, 32, [60, 26], [4, 8]]), amp=1)


Master().lpf = 0
Master().lpr = 0

# I had to reset the players after applying the Master().lpf
# to reset their filters
