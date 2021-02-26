# by KittyClock & BBScar

Clock.set_time(0)

print(SynthDefs)

print(Samples)

vv >> play('v', sample=0, sus=P[0.1, 0.05, 0.1], dur=0.5, lpf=P[105, 110, 93, 92], lpr=1, amp=P[1, 0.75] * 0.85).stop()
v2 >> play('v', sus=vv.sus, lpf=vv.lpf, lpr=vv.lpr, dur=vv.dur * 4/3, amp=0.75 * vv.amp).stop()

xk >> play('nkbt', dur=0.25, sample=P[10, [11, 20], [6, 5, 4, 3], [5, 8, 9]] * var([1, 2, 4, 8], 4) + 6, delay=P[0, [0.25, 0.5], [0, 0, 0.25, 0.25], 0], lpf=1000, lpr=0.95, amp=0.75)

var.bl = var([1,2,3,7,5])
var.bl2 = var([4,2,3,5,6])

s1 >> filthysaw(var([var.bl+var([0,-1],32),var.bl2],64), oct=4, dur=4, shape=1/4, room=2/3, mix=1/3, amplify=2/9, amp=1 * var([1, 0], [64, 32, 128, 32]))
s2 >> filthysaw(var([var.bl+var([0,-1],32),var.bl2],64), oct=5, dur=2, shape=1/4, room=2/3, mix=1/3, amplify=2/9, amp=s1.amp * var([0, 1], [128, 64, 128, 32, 64, 32]))
s4 >> pbass(var([var.bl+var([0,-1],32),var.bl2],64), oct=6, dur=1, sus=1/2, tremolo=3, room=1/3, mix=1/2, amplify=var([0,2/4],PRand([32,64,128],seed=7)) * expvar([0.25, 1, 1], 128))
s5 >> sawbass(var([var.bl+var([0,-1],32),var.bl2],64), dur=1/4, chop=var([1,var([0,2],PRand([16,32,64]))],32), bend=[0,0,0,1/2], hpf=P[800, 400, 200, 300] * 1, hpr=0.25, lpf=expvar([1500,3000],[PRand([32,64,128]),32]), amplify=var([0,6/9],PRand([32,64,128])) * 0.75 * expvar([0, 1, 1], [64, 64, 128, 128, 128]))
s7 >> benoit(s4.degree, oct=6, dur=2, sus=3/4, lpf=linvar([200, 1200],[32,0]), room=2/3, mix=1/3, amplify=2/9)
s6 >> benoit(P[:3]+var([0,3],64), oct=5, dur=s7.dur * 2, sus=3/4, chop=var([0,2,3],PRand([16,32,64],seed=12)), room=2/3, mix=1/2, amplify=3/8 * var([1, 0], [128, 64]))

Group(s1,s2,s4,s5,s6, b1, b2, b3, b4).stop()

s8 >> chipsy(s6.degree,dur=var([1/4,PDur(5,8)],[24,8]), lpf=P[1200, 2400, 8500, 2900] * expvar([0.5, 1], 32), lpr=0.4, sus=1/8, room=2/3, mix=1/3, amplify=6/8 * var([1, 0], [31, 1, 28, 4]))
b1 >> play("Z", sample=15, sus=2, dur=2, delay=[0,1/2], rate=1, pshift=var.bl, room=2/3, mix=1/3, amplify=var([0,3/9],PRand([32,64,128],seed=13)) * expvar([0, 1, 1], 128))
b2 >> play("J", tremolo=0, lpf=PWhite(900, 1000) * 0.9, formant=0, lpr=expvar([1/2,1/5],32), amplify=2/5 * expvar([1, 0.25], 1/3) * expvar([0, 1, 1], [64, 64, 128, 128]))
b3 >> play("i", dur=1, delay=1/2, sample=3, room=2/3, mix=1/2, amplify=1/6, amp=var([0, 1], PRand([32,64,16]))).sometimes("stutter", 2, sample=0, delay=1/4, amplify=2/6)
b4 >> play(":", dur=1/2, sample=8, rate=6/5, room=2/3, mix=1/3, amplify=1/6, amp=var([0,1],[64,PRand([16,32,64])])).sometimes("stutter", 3).every(16, "stutter", 2)

Group(b1, b2, b3, b4).dur = P[4]

print(Clock)

Group(s3, ff, oo, s9, s0).lpf = 100

Master().lpf = P[expvar([500, 1500], 1/3), 300, [250, 1800], [600, 300, 250, 200]] * 0.00

Master().lpr = 1

b5.dur = 4

b5 >> play("v", dur=4 * P[([1] * 3 + [0.25] * 4) + ([1] * 3 + [0.5] * 2)], sample=0, amplify=0, amp=hc.amp * 1.25) #noice
h1 >> play('s', dur=b5.dur, delay=0.5, amp=var([0, 1], [32, 64, 64, 128])).stop()
oo >> play('H', sample=1, dur=b5.dur * 2, amp=0.65 * var([0, 1], [32, 128, 64, 128])).stop()
hc >> play('x', dur=b5.dur * 4/3, sample=15, amp=0.75 * var([1, 0], [[128, 64], 32])).stop()

x9 >> play('x', sample=4, lpf=200, lpr=0.4, dur=b5.dur, amp=hc.amp)

s9 >> hoover(var([0,1],16), chop=var([4,0],[6,2]), shape=expvar([1/12,2/8],[PRand([8,16,32]),0]), amplify=1/2, amp=var([1,0],[32,PRand([16,32,48,64])])).offbeat()
s0 >> click(s9.degree, oct=8, dur=PSum(7,2), lpf=expvar([2300,900],PRand([16,32,64])), room=1/2, mix=1/3, amplify=3/7, amp=var([0,1],PRand([32,64,128])))





