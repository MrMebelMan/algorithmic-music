# by BBScar, stepovr & KittyClock

Clock.bpm = 150

var.brk = var([1, 0], [[63, 31, 28, 56], [1, 1, 4, 8]]) #* expvar([1, 0, 0], [128, inf], start=Clock.now())

var.brk = var([1, 0], [2, 2])

var.hpf = var([0, [800, 400, 900, 300]], [[28, 31, 32, [7, 32], 7], [4, 1, 0, [1, 0], 1]])

xx.dur = [1] * 2 + [0.5] * 4

xx.dur = [0.5] * 2 + [1] * 3

xx.dur = 1

#Group(x2, x3).stop()

Master().lpf = 0
Master().hpf = 0

var.brk = 1

fv >> play('V', dur=0.25, lpf=expvar([4000, 5000], [2, 0]) * expvar([0.5, 0.25], 16), lpr=0.5, amp=expvar([0.1, 1], [1, 0]) * 0.75 * var.brk * expvar([1, 0.25], [1, 0]))
xx >> play('x',
    sample=var([4, 0], 64),
    rate=var([[1, 0.97], [0.98, 0.95]], 8) * 1,
    dur=Pvar([
        [1] * 6 + [0.5] * 4,
        [1] * 31 + [0.5, 0.5],
        [1] * 31 + [0.5] * 2,
        1,
    ], 64), hpf=var.hpf,
    lpf=P[1, 2.5, 2.25, 1] * 1500, lpr=0.15, amp=expvar([1, 0.75], [4, 0]) * var.brk
)

#var.hpf = 0
rr >> play('~', dur=0.25, lpf=expvar([2000, 5000], [64, inf], start=Clock.now()), amp=expvar([0, 1], [64, inf], start=Clock.now()) * P[0.5, 1] * 0)

#Group(nn, sh, ll, p2, fv, xx, x2, x3, sh, nn, oo, ll).stop()

x2 >> play('x', rate=1.1, dur=xx.dur * 4, delay=0.75, lpf=P[600, 400, 500, 600], lpr=expvar([1, 0.6], [4, 0]), hpf=var.hpf, amp=0.45 * var.brk)
x3 >> play('x', dur=xx.dur * 2, delay=0.5, hpf=var.hpf, amp=P[0.15, [var([0.1, 0]), 0]] * var.brk)

ce >> play('u', dur=1, amp=P[0, 1] * 0.8 * var([0, 1], [32, 64, 32, 128]))
ck >> play('o', dur=4, delay=[0.75, 0.5], amp=PWhite(0.1, 0.25) * var([0, 1], [64, 128, 32, 64]))
sh >> play('s', sample=0, echo=P[0, 0, [[0.5, 0.25], 0], 0.5] * 0, dur=xx.dur, lpf=expvar([3000, 6000], [16, 0]), lpr=0.25, delay=0.5, amp=0.9 * var([0, 1], [32, 64, 64, 128]))
sh.lpf = 0
nn >> play('n', dur=0.25, lpf=expvar([5000, 2000], [32, 0]), lpr=0.25, amp=expvar([1, 0], 1/3) * 0.2 * var([0, 1], [64, 128, 64, 64, 32]))
oo >> play('o', dur=2, delay=P[0, var([0.5, 0], 32)], room=1, mix=0.1, amp=0.2 * expvar([0, 1, 1], 128))
ll >> play('l', dur=1, echo=P[0, 0, [0.5, 0], [[0.25, 0], 0, 0, 0]], room=1, mix=0.15, lpf=expvar([5000, 3000], [[8, 16, 32, 64, 128], 0]), lpr=PWhite(0.25, 0.75) * expvar([0.75, 1.25], [4, 0]), amp=0.5 * expvar([0.1, 1, 1], 64))

sb >> sawbass(var.bl,dur=0.25, sus=0.01, room=P[1, 0, 0.5, 0, 0], mix=0.15, crop=4,
    hpf=P[var([300, 450], 

# sure
    
    ;8), expvar([550, 200], 32), 400, [600, 350]] * var([0.75, 1, 1.25, 0.5, 1.5], 32),
    tremolo=P[2, 4], drive=0.15, hpr=P[0.1, 0.15], ben

# hehe

# BuBuBum Bum Bum Bum 

Master().lpf = 120 * 0.25
Master().hpf = 250
Master().drive = 0

cp >> play('H', pan=PWhite(-0.75, 0.75), dur=0.25, room=1, mix=expvar([0.1, 0.5], [64, 32]), amp=expvar([0.25, 1], [2, 0]) * var([1, 0], [3, 1, 1, 1, 2, 1, 4, 1, 6, 2, 4, 4, 4, 8]) * 0.5 * expvar([0, 1, 1], [128, 64]))
p1 >> play("[tt]", dur = var([1, 1/2],[16,8]) , amp = 0.5 * var([1, 0], [32, 64, 64, 32, 64, 128, 32, 128]), pan = [-1,1]) 
p2 >> play("--<t><r>", lpf=600, lpr=0.1, amp= 0.5 * var.brk * var([0, 1], [64, 128, 32, 64]) * xx.amp) # pop <3
Group(nn, ll, sb, cp, p1, fv, sb, cp, ce, ck, p3, oo, sh).stop()
#Group(sh, nn, oo, ll, p1, p3).stop()

p3 >> play("vtrtct", dur=xx.dur * 0.5,
    lpf = expvar([400, 700], 16),
    tremolo=P[2, 4, 4, 8] * 0,
    hpf=var.hpf,
    delay=0, lpr=0.5, room=1,
    rate=P[var([0.9, 0.95], 16), 1] * P[1, 0.98, 1, 0.99] * var([1, 0.9, 0.95, 0.85], 64) * var([1, 1.15, 0.9, 1.25], 32),
    bend=P[-0.1, 0, -0.25, 0], mix=(0, 0.1),
    sus=P[0.05, 0.1, [0.025, 0.25], 0.025],
    amp = expvar([0.75, 0.2], [62, 2]) * expvar([1, 0], [32, 0]) * 1
)
p3.pitch = 'vt'
p3.sus=var([0.1, 0.05, [0.025, 0.1]], 32)


p3.pitch = 'vtvv{tv}'

p3.pitch = 'v(tv)tvv{tv}vtvt(vt)tvvt'

p3.pitch = 'vtttvttvvtvtvvvtvtvtv'

ww >> play('M', dur=4, rate=0.5, room=1, mix=0.1, delay=[0, 0.5], lpf=200, lpr=0.5, amp=1 * var.brk)

p4 >> sinepad((0,1),dur= 1/2, lpf = 400, amp = [0.6])

#Clock.set_time(0)
var.bl = var([0,2])
var.nt = var([0,2,3,7,2,5,4])
var.mld = var([3,5,[2,9,4],[5,8,2],7,0])
s1 >> arpy(Pvar([0, -1],[24, 8]) + var([0, 1], 128), echo=P[[0.25, 0], 0, 0, 0], echotime=1, room=1, delay=0.5, mix=expvar([0.1, 0.5], 16), amplify=3/5) #+ (-2, -3)
bp >> blip(var([0, 2], 128), dur=4, tremolo=2, sus=2, delay=0.5, lpf=var([300, 350, 250, 150], 8), lpr=expvar([0.7, 0.1], 32), drive=0.5, bend=-1/18, amp=1/12 * 0.25)
s2 >> charm(var.nt, oct=6 , formant=1, chop=1, lpf=P[2, 1.5, 0.5, 1] * expvar([200, 400], 64), tremolo=(0, 2), lpr=0.5, room=2/3, mix=1/2, amplify=5/6 * 0.35)
b1 >> play("f", delay=[0,[0, 1/2], 0, 1/2], sample=PxRand(1,3), rate=6/5, room=3/4, mix=1/3, amplify=PRand([1/3,0],[32,64,128,64,128,32])*var.brk)
s3 >> prophet(s1.degree, oct=6, dur=1/2, sus=1/4, lpf=expvar([400, 4800], [64,0]), room=var([2/3, 4/5], [52,12]), mix=1/2, amplify=5/8* var([0,1],256))
s4 >> prophet(s1.degree, oct=5, dur=4, sus=12, chop=8, bend=1/12, benddelay=4/5, spin=linvar([-1/2,1/2],32), formant=var([0, 1, 2], 64), room=2/3, mix=1/2, amplify=var([2/8,0],[28,4,32,32,52,12,96,32,16,16])* var([0,1],256))
s5 >> dab(var.bl, oct=var([5,6],[24,8]), dur=8, echo=[0, 1/2], echotime=[1, [4,6,8]], vib=4, room=2/3, mix=1/2, amplify=PRand([0,2/9],PRand([32,64])))
b2 >> play("Z", room=1, mix=1/2, dur=64, rate=1/2, coarse=4, sample=1, amplify=0.2)
b3 >> play("C", rate=-1, dur=8, sus=32, pshift=-16, chop=64, room=1, mix=expvar([0.1, 0.4], 128), echo=1/2, delay=1/2, amplify=3/7*var([0,1],PRand([16,32,64,128])))
s6 >> varsaw(var.mld, oct=5, dur=1/4, formant=2, chop=1, lpf=linvar([400, 3200], 64), room=linvar([1/8,1],32), mix=1/2, pan=PWhite(-1,1), amplify=3/8, amp=var([1,0],PRand([8,16,32,64])))
s7 >> zap(s1.degree, oct=6, dur=1/4, sus=1, spin=linvar([-1/2,1/2],32),
    lpf=P[400, 450, var([410, 850], 8), 420] * var([1, 0.75, 1.25], 32), lpr=expvar([0.5, 0.1], [2, 0]),
    shape=2/3, room=2/3, mix=expvar([1/4, 1/8], 1/3), amplify=3/8
)
b4 >> play("Y", room=1, mix=0.5, dur=2, delay=[0,1/2], spin=linvar([-1,1],32), pan=(-0.75, 0.75),amplify=linvar([4/5,0],128))
b5 >> play("!", echo=P[0.75, 0, 0, 0], dur=4, delay=0, sample=1, slide=linvar([0,1/2],16), lpf=expvar([2000, 700], 64), lpr=0.75, room=2/3, mix=1/3, amplify=1/3, amp=var([0,1],[192,64,32,0])).rarely("stutter", sample=0, rate=3/4)


Master().lpf = 1800
Master().lpr = 0.5

# I am happy 
print(Attributes)
