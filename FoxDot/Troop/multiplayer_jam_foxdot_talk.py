# Clock.reset()
# Clock.set_time(0)

var.all_brk = var([1, 0], [31, 1, 128, 32, 28, 4, 64, 64, 56, 8, 64, 32])

xx >> play('x-')


print(SynthDefs)
print(Attributes)

chrds = P[(0, 2), (2, 3), (7, 2), (8, 5), (4, 2), (7, 9), (8, 5), (5, 3)]

s1 >> sawbass(var(P[0, 2, 5, -7], 4), oct=var([5, 6], 32), dur=PDur(3, 8), chop=var([0, 3], [12, 4]), lpf=linvar([200, 1200], 32), pan=(-2/3, 2/3), amplify=1/9 * var.all_brk)

s2 >> arpy(Pvar(chrds, 4), oct=var([6, 7], 128), dur=var([1/3, PDur(5, 8)], 16), echo=1/2, echotime=4, formant=PxRand([0, 3], PRand([8, 16, 32])), room=3/4, mix=1/2, pan=PSine(16), amplify=3/8)
s3 >> donk(x2.degree, oct=var([7, 8], 16), dur=4, echo=1/2, echotime=4, room=3/4, mix=1/3, amplify=4/8 * var.all_brk)
s4 >> soprano(s2.degree, oct=7, dur=var([2, 4], [12, 4]), delay=var([1, 0], [12, 4]), chop=32, formant=3, lpf=var([400, 2000], 32), hpf=2400, hpr=1/2, room=3/5, mix=1/2, amplify=var([1/9, 5/9], 64))
s5 >> lazer(s1.degree, oct=var([4, [5, 6]], 64), dur=16, shape=1/8, chop=8, formant=var([0, 1, 0, 2], 16), room=3/4, mix=1/2, amplify=6/8)
s6 >> dub(s1.degree, oct=(5, 6), dur=4, bend=[0, 3/4, 0, 1/2], coarse=4, amplify=var([0,1], PRand([8, 16, 32, 64]))*2/12)

# <3

br >> play('X', rate=1 * var([0.9, 1, 0.95], 32), dur=var([1, 0.5], [15, 1]), lpf=101, lpr=0.05, amp=0.85 * var([1, 0], [28, 4, 31, 1]) * 1 * var.all_brk)
pc >> play('X', dur=2, delay=[[0, (0, 1/4)], 0, 0,[0, (0, 2/3)]], sample=1, lpf=600, amp=0.5 * var.all_brk * var([1, 0], 8)).stop()
oh >> play('-', sample=1, dur=1, delay=0.5, amp=1.35 * var.all_brk * var([0, 1], [32, 64, 32, 32]))
fh >> play('----.', pan=PWhite(-0.5, 0.5), dur=0.25, amp=0.75 * var([1, 0], 4)  * var.all_brk)
rv >> play('v', rate=var([0.8, 1], 32), dur=0.5, amp=P[1, [0.25, 0.5]] * 0.5  * var.all_brk)
ww >> play('w', sample=2, rate=0.5, bend=expvar([0.05, -0.05], 32), lpf=expvar([150, 230], 32), dur=1.5, amp=expvar([0.25, 0.6], 128) * 0.75  * var.all_brk)

st >> star(dur=4, lpf=150, lpr=1, tremolo=2, amp=0.5)
ss >> play('S', sample=3, dur=0.5, lpf=expvar([2000, 6000], [64, 0]), lpr=0.5, amp=P[0.5, 1] * 0.3 * var([0, 1], [64, 128, 32, 64, 64, 64]) * var([1, 0], [3, 1])  * var.all_brk)
#vv >> play('xxxx x xx.', rate=var([0.65, 0.7, 0.6, 0.6], 8), dur=0.25, lpf=expvar([550, 600, 850, 400], 4), amp=expvar([0.25, 0.5], [2, 0]) * var([1, 0], [31, 1, 28, 4, 56, 8, 28, 4, 31, 1]) * 0.25  * var.all_brk)
kd >> play('x', rate=1.05, dur=P[1, 0.5, 0.5, 1, 1] * 1, lpf=250, amp=0.7 * var([1, 0], [64, 32, 128, 32]) * var([1, 0], [31, 1, 28, 4, 7, 1, 7, 1]) * var.all_brk)
lk >> play('x', dur=1, delay=0.75, amp=P[0, 0, 0, 1] * 0.6 * kd.amp  * var.all_brk)
ok >> play('x', sample=6, dur=3/4 * 2, amp=0.5 * kd.amp  * var.all_brk)
sn >> play('H', sample=1, echo=P[0, 0.25, 0, 0], dur=4, room=1, mix=0.1, amp=0.1 * var([0, 1], [64, 32, 128, 32, 32]) * var.all_brk)
kj >> play('V', sample=1, dur=1, delay=P[0, 0.5], lpf=400, amp=0.6  * var.all_brk)
h1 >> play('-', sample=2, echo=P[0.25, 0.25, 0.5, 0.25], echotime=0.25, dur=var([2, 1, 4, 2], 64), delay=0.5, amp=0.45 * var([0, 1], [32, 64, 32, 128, 64, 64])  * var.all_brk)
bb >> play('b', sample=1, rate=P[1, expvar([1, 0.95], 32), 1, 1], dur=0.5, lpf=P[200, 600, 450, 800], amp=P[1, 0, 1, 1, 1, 1, 0, 0.5] * expvar([0.5, 0.8], 64) * 1)

Group(br, pc, ph, fh, rv, ww, st, ss, vv, kd, lk, ok, kj, h1, fh).stop()


x3 >> creep(P[0,3,2,6,7,4,8,2,4,5,9,7,8,6,5,1],dur=1/4,amplify=0.5,drive=0.05, pan=PSine(2), bend=P[0, 0.05], lpf=P[1500, 2000, 5000, 4500] * expvar([0.75, 1.5], 64),amp=var([1,0],[32,64])).every(4,'mirror')
x5 >> space([0,1,2,5,7],dur=var([1/8,1/3,1/2,1/4],16),amplify=0.4,oct=6,pan=PSine(5),lpf=8000,amp=var([0,1],[64,16]))

y0 >> play('VV vv', rate=P[1, 1.05, 1, 0.98], lpf=1500, amplify=0.4 * var([1, 0], [31, 1, 28, 4, 56, 8]) * var.all_brk)
y1 >> play('  oo o  ', dur=1/4,rate=P[1, 1.05, 1, 0.98], lpf=1500, amplify=0.5 * var.all_brk)
y3 >> play('-',rate=1.5, sample=2,dur=1/5,amplify=var.all_brk * 0.3 * P[1, 1, 1, 0, 1, 1, 1, [1, 0.5]],pan=PSine(8))

z0 >> bass([-7],dur=8,amplify=1.1,amp=var([1,0],[6,2]),drive=0.05)
