Clock.bpm = ???

print(Samples)

print(SynthDefs)

print(Attributes)

# Check if player name is already in use:
print(p1)

#############################

db >> dub(dur=[4, 2, 2],
    pan=0, #PWhite(-0.75, 0.75),
    tremolo=4,
    sus=[8, 2, 4],
    lpf=expvar([5000, 3500, [2500, 500], [6000, 1000]], 16),
    amp=expvar([0.35, 0], 128) * 1
)

Master().lpf = expvar([5000, 500], 32)

Master().lpf = 100

# Niiiice!

# thanks everyone!

# <3

var.bass_hpf = 0
bd >> play('V', sample=var([1, 2], [[128, 256, 64], [64, 128, 32]]), dur=1, lpf=1200, hpf=var.bass_hpf, amp=var([1, 0], [[28, 56], [4, 8]]))
sd >> play('v', dur=1, delay=0.5, hpf=var.bass_hpf, amp=P[1, var([0.25, 1], [[64, 128], [32, 64]])] * bd.amp)
s2 >> play('m', sample=1, dur=var([2.75, 1.75, 0.75], [[64, 128], 128, [32, 128], 32]), hpf=var.bass_hpf, hpr=0.25, delay=1, amp=2)
si >> play('$', bend=0.15, sample=var([0, 1], [[28, 56], [4, 8]]), dur=1, lpf=100, lpr=0.35, hpf=var.bass_hpf, amp=1)
sb >> play('X', dur=1, delay=0.85, hpf=var.bass_hpf, amp=P[0.25, 1.5])


@next_bar
def bass_off():
    Group(bd, sd, s2, si, sb).stop()


sh >> play('s', pan=PWhite(-0.75, 0.75), dur=0.25, amp=expvar([2, 0], [[8, 16, 32], 0]) * PWhite(0.5, 1.5) * var([1, 0], [[256, 128, 64, 32], [64, 32, 128]])).stop()

t1 >> play('t',
    room=1, mix=0.25,
    dur=[int(var([1.5, 0.5], [[128, 256, 64], [64, 128, [64, 32]]])), 0.5, 0.5],
    hpf=expvar([1200, 200], [128, 0]), hpr=0.5,
    amp=var([0, 1.3], [[256, 128, 64], [128, 256, 64, 64, 128]])
).stop()

sr >> play('O', pan=PWhite(-0.5, 0.5), dur=0.25, amp=P[0.15, [0.75, 0.5, 0.3], 0.5, [0.3, 0.5, 0.75], 0.85] * var([0, 1], [[28, 56, 28], [4, 8, 4]]) * expvar([0.15, 1], [[4, 8, 4], 0])).stop()

rs >> play('I', room=1, mix=0.2, dur=var([8, 4, 2, 1], [64, 32, 64, [32, 16, 8]]), amp=var([1, 0], [[128, 256, 64, 32], [32, 64, 32, 128, 32]])).stop()

cl >> play('H', sample=1, dur=var([4, 2], [[32, 64], [64, 128]]), delay=0.75, lpf=2500, amp=var([1, 0], [[256, 128, 64], [128, 64]])).stop()
h1 >> play('-', sample=2, dur=1, delay=0.5, amp=var([1, 0], [[64, 128], [32, 64]])).every(16, 'stutter', 2).stop()


kd >> play('X', rate=P[1, 0.98, 1, 0.95] - var([0, 0.05, 0.1, 0.15], 128),
    sample=1, dur=1,
    lpf=var([1000, 800, 600, 400], 64),
    amp=P[
        1, 1, var([0, 1], [128, 64, [32, 64, 128, 256]]), var([1, 0], [512, [32, 64, 128]])
    ] * var([1.1, 0], [[28, 56, 28, 126], [4, 8, 4, 2]]) * var([1, 0], [[512, 256, 128], [256, 128, 64]])
).stop()
sk >> play('X', sample=1, dur=1, delay=0.5, lpf=400, amp=P[1, 0, 0, [0, var([1, 0], 64)],  1, 0, var([0, 1], [64, 32, [16, 32], [16, 64, 8], 32]), 0] * 0.5 * kd.amp).stop()

nb >> play('b', sample=0, dur=1, delay=0.5, tremolo=8, lpf=expvar([1200, 300], [[128, 64, 32], 0]), amp=[0.75] * 3 + [var([1, 0], [[28, 56], [4, 8]])])
n2 >> play('b', dur=1, delay=1, amp=P[1, [0, 0, 0, 0.75], [0, 1], 0.25] * var([0.5, 0], [[256, 128], [64, 32, 16, 8]]) * nb.amp)
n3 >> play('T', sample=0, dur=1, delay=0.25, lpf=300, amp=P[1, 0, 0, 0, 0, 1, 1, 0] * 0.25 * nb.amp)

sn >> play('o', sample=1, dur=[1] * 7 + [0.5, 0.5], hpf=0, hpr=0.5, amp=1)

@next_bar
def foo():
    Group(nb, n2, n3).stop()

fb >> play('T', slide=[0.1, 0, 0, 0], dur=0.25, lpf=[[400, 200, 650], 500, 350, 600], hpf=800, hpr=0.25, amp=P[1, 1, [0, 1], 1] * 0.15).stop()



d1 >> play('{-:}',dur=PDur(var([7,13,9],[4,2,1]),16), amp=PRand([1,0.5]),rate=1,room=0.5).spread().every(Cycle([6,4]),'stutter',6,dur=3,pan=[-1,1],rate=1)

p1.reset() >> bell(var([0,-2],8),dur=P[3/2,1/2,1/2,1/2].mirror(),oct=(4,5),chop=0,delay=PRand([0,0.25]),hpf=PRand([666,333,111]),amp=var([0.1,0],[12,4]),pan=PWhite(-1,1)).every(6,'stutter',6,dur=3,pan=[-1,1],oct=6) + P[0,0,2,0].mirror()

p1.stop()


# Learned a lot,I'll share some stuff on the group later.


sp >> space(PRand([0,-1,-2]),dur=PRand([2,4,7]),lpf=777).stop()

bs >> bass(drive=0.1,shape=0.1,dur=[4,2,2],amp=0.7,cut=0.9,pan=[1,-1],chop=var([2,4],8)).stop()

xc >> play('#',dur=8,rate=-1/2,amp=var([1,0],8)).stop()

rr >> play('r', sample=PRand([2,1]),dur=0.5, delay=0, amp=n2.amp * var([1, 0], [[256, 128], [128, 64]]), rate=1/2).every(6,'stutter',3,dur=1,hpf=(0,555)) # You can put almost anything I didn't know you could put the hpf inside the every method~!! :D # oh lol
!


# Same!!!
