# by KittyClock and Noodl.exe

Clock.bpm = 133

xx >> play('x',
    sample=var([2, 2], 32),
    rate=P[1, 1.05, 1.03, 0.99] * 1.1,
    dur=0.25,
    lpf=expvar([2000, 3500], [4, 0]), lpr=0.15, 
    amp=P[
        1,
        [0.15, 0.1],
        P[0.5, 0.25, 0.75, 0.65],
        var([1, 0], [31, 1, 28, 4]) * P[0.25, 0.75, 0.25, 0.35,  0.15, 0.5, 0.75, 0.15]
    ] * 1.25 * expvar([0, 0, 1, 1], [128, 128, 128, 0])
)

var.brk = var([1, 0], [31, 1, 28, 4])

ww >> play('h', sample=0, rate=0.95, dur=8, tremolo=8, lpf=0, amp=0.75)

bt >> play('e', tremolo=8, sample=1, dur=2, delay=P[0, 0.5], amp=0.75)

tt >> play('t', sample=1, dur=[4] * 7 + [1, 1, 1, 1], delay=var([0, 0.5], 128), amp=0.95)

oo >> play('o', room=1, mix=0.25, dur=2, delay=P[0, 0.5], amp=0.85 * var([1, 0], [[64, 128], [128, 256]]))

vv >> play('v', sample=0, drive=0, sus=0.05, dur=[0.5, 0.5] + [1] * 7, bend=-0.15 * 0, rate=P[1, 1.05, 1.03, 1.07] * 1, amp=1 * 1.25 * var.brk)
x2 >> play('X', rate=1, sus=0.01, sample=0, dur=0.25, hpf=80, hpr=0.25, amp=P[1, [0.25, 0.15, 0.25, 0.1], [[0.5, 0.5, 0.5, 0], 0.75], [0.75, 0.5, 0.45, 0.7]] * 1.95 * var.brk * 0.5 * 0)

od >> play('V', dur=1, sample=2, sus=0.05, rate=0.8, drive=0, hpf=75, hpr=0.015, amp=0)

# we killed my SC server lol

# RIP

x3 >> play('X', rate=P[1.1, 1, 1.05, 0.95], sample=0, dur=var([2, 1, 0.5], 128), lpf=2000, lpr=0.25, amp=P[1, 1, 0, 1,  1, 0, 0, 0] * var.brk)

h1 >> play('n', dur=1, delay=0.5, amp=var([0.85, 0], [[32, 64], [64, 128]]) * var.brk).every(8, 'stutter', 2)

ft >> play('t', room=1, mix=0.15, sample=0, dur=0.25, lpf=P[1500, 2000, 800, 1200], lpr=0.25, amp=P[[1, 0, 0.5, 0.75], [0.15, 0.5, 0.25, 0.75], 0.75, [0.15, 0.5, 0.75, 0]] * 1.25 * expvar([0, 1], 128))

rc >> play('~', dur=0.25, lpf=expvar([3000, 3000, 6000], [128 + 32, 32, 0]), amp=expvar([0, 0, 1], [128 + 32, 32, 0]))

n0 >> play('Xo', dur=PDur(3,8), lpf=expvar([300,600, 900, 1200], [4, 0]), lpr=var(4,[0.15, 0.35]), hpf=250, amp=var([1, 0], [32, 64, 32, 128, 32, 256]) * linvar(1.5,[0,2]) * var.brk, echo=Pvar([0.1,0.02],2), room=0.15)

ss >> play('S', dur=0.5, amp=P[[0.5, 0.45], [1, 0.9]] * 0.85 * var([0, 1], [128, 256, 32, 64]))

o0 >> sinepad([0], oct=sinvar(6,[4,6]), bend=Pvar([0,-0.25]), amp=expvar([0, 0, 0.45, 0.45], [[32, 64], 64, 128, 0]), pan=PWhite(-1,1), rate=0, room=expvar(24,[0,1]), mix=-0.25).every(6, 'stutter', 2, echo=0.25).stop()

dl >> play('0xFEED..',
    sample=P[var([0, 1, 2, 3], 32), var([1, 2, 3, 4], 8), 0, [2, 1, 0, 2]],
    dur=0.25,
    rate=expvar([1, 0.75, -1], [[16, 0],8,2]),
    hpf=expvar([800, 200], [4, 0]),
    hpr=0.25,
    tremolo=var([4, 2, 0, 8], 32),
    chop=4*PWhite(-0.5,0),
    amp=var([1, 0], [[3, 7], 1, [2, 4], 1, 2, 2, [4, 8], 2, 4, [1, 2, 4, 8], 3, 1, 1, 2, 2, 1, 3, 1]) *0.35 * var.brk,
    echo=expvar([0.1,0.25])
).every(5, 'mirror').stop()

ex >> play('..[ExE](CUTE~)', amp=expvar([0,0,0.25,sinvar([0.1,0.25], 1),0.3])*var.brk, chop=2, bit=4, crush=4, spin=2, pan=expvar([-0.75, 0.75], 16), dur=4, sus=2, lpf=Pvar([1500,2000,1000,3000]), lpr=0.25).every(16, 'stutter', 0, echo=0.2).stop()

# I guess this is end :D

#seee yaaaa
