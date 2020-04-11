Clock.bpm = 150
Scale.default = "minor"

print(Samples)

#came :)


print(SynthDefs)

var.brk = var([1, 0], [[32, 31, 28, 56], [0, 1, 4, 8]])

#Welcome :D
p1 >> sawbass(var=Pvar([1,2,3]), mix=0.5, amp=1, room=5/5, delay=1/2, oct=6, echo=1.5, cut=[1/3,1/4]).stop()
p2 >> swell(p1.pitch, amp=0.5, room=3, oct=3).stop()
p3 >> soprano(sb.pitch, amp=0.6, oct=[3,4,5],  lpf=linvar(500,1500),hpf=(5000,7000), sample=2, rate=linvar([1/2,4],8)).stop() #i need some help here # hmm?
p4 >> space([1,5], sample=sinvar([.1,.5],32), dur=4, oct=[4,3,2,1], amp=0.6).stop()
p5 >> klank(PWhite(-4,4)[:15], tremolo=PSine(16), shape=sinvar([.1,.5],32,32), dur=4, oct=[5], amp=0.5, cut=[.5,.5,1]).stop()
d1 >> play(" X--t t ",room=4, arp=0.9,amp=0.1).stop()
d2 >> play("(g [hh]) [--] ", echo=0.5, room=3.5, amp=0.1).stop()
d3 >> play("X-O-X|r8|[--] ", amp=0.35).stop()
d3.stop()

#Fire!!!

sb >> sawbass(
    pan=PWhite(-0.5, 0.5),
    dur=[0.5, 0.5, [0.75, 0.25], 0.25 ,0.25, 0.25, 0.25, 0.25],
    hpf=P[[200, var([500, 400, 300, 250], 32)], 250, 180, 350] * expvar([1, 2], 32), hpr=0.25,
    sus=P[[var([0.25, 0.5], 64), 0.25, var([0.5, 0.25], [128, 64]), 0.25], [0.5, 0.25], 0.25, 0.25],
    drive=P[[[0, var([0, 0.01], [128, 64, 128])], PWhite(0.04, 0.09)], [var([0, 0.1, 0.05], [32, 32, 64, 64]), 0, var([0, 0.08], 128), var([0, 0.04], [64, 128])], 0, 0] * 0,
    room=expvar([1/2, 1], 64), mix=[0.15, 0, 0.25, 0, 0, [0, 0.15], 0, 0],
    amp=P[1, [1, 0.75]] * var([0, 1.0], [[128, 64, 64], [256, 128, 128]]),
    oct=P[5, var([5, 5.6], [[32, 64], [64, 128]]), 4, var([5, 4.8], 32)]
) #.stop()
kd >> play('X', rate=[1.1, 1.05, 1, 0.95], sample=var([2, 1], [[256, [128, 64, 32, 32]], [128, 64]]), dur=1, lpf=var([700, 500, 300, 200], 64), amp=P[1, [0.9, 0.8]] * var([1, 0], [[512, 256, 128, 64], [256, 128, 64, 32]]) * var.brk * 1)
bp >> blip(dur=[1, 1, 0.5, 0.5], oct=4.8, amp=var([0, 1], [256, 128]))
ss >> play('S', pan=PWhite(-0.75, 0.75), sample=1, dur=[1/2,1,1/4], delay=0, lpf=[2500, 3000, 5000], amp=P[0.3, 0.15] * var.brk * var([0, 1], [128, 64, 128, 32, 64, 64]))
sk >> play('X', sample=kd.sample, dur=kd.dur, delay=[0.5, 0.85, 0.85, 0.5], amp=P[1, 0, 0, 0,  [0, var([1, 0], 32)], 0, [0, 0.5], 0] * kd.amp * var([0, 0.75], [[128, 64], [64, [32, 128], 32]]))
r2 >> play('I', sample=1, dur=1, amp=var([1, 0], [[128, 256, 64], [64, 128, 32]]) * var.brk)
h1 >> play('-', sample=var([2, 1, 0, 2], [128, 64]), dur=1, delay=0.5, amp=kd.amp * var([1, 0], [[64, 128], [32, 64]]))
cl >> play('*', dur=var([16, 8, 4], [64, 64, [32, 64, 128]]), delay=0.5, amp=0.75).stop()
h2 >> play('-', sample=var([1, 0], [256, 256, 128, 128]), amp=expvar([1, 0.15], 1/3) * h1.amp * var([0, 1], [[64, 32], [128, 64]]))
sh >> play('n', sample=2, room=1, mix=0.2, dur=1, delay=0.5, amp=h1.amp * var([0.75, 0], [[256, 128, 64], [128, 64, 32]]))
tt >> play('t', sample=[3, 3, [0, 1, 2, 0], 3], dur=0.25,
    amp=P[
        [0.5, 1], 0, var([0, 0.5], [128, 64, 64]), 0,
        [0.25, PWhite(0.25, 0.5)], 0.5, [0.75, var([0.75, 0.25], 64)], 1
    ] * expvar([0, 1.15], 256)
)
rk >> play('X', sample=2, rate=-1, dur=[1/2,1]   , lpf=850, amp=var([0, 0.75], [[63, 63, 127, 127], 1]))
bd >> play('V', sample=2, rate=[1.15, 1], lpf=P[800, [500, 300]] * 1, lpr=0.25, bend=[[-0.15, 0], 0], hpr=0.25, amp=P[[1, 0.85], [0.85, 0.5, 0.75, 0.4]] * 1 * var.brk)
#bd.amp=1

@next_bar
def stahp():
    Group(s2, s3, s4, m1, m2, m4, m5, xx, xy, xz, sb, rk, bd, h1, h2, ss, kd, tt, r2, rs, rk).stop()


var.melody = var([1,2,1,4,1,0],1)
s1 >> dbass(var.melody,oct=4,dur=8,formant=linvar([0,6],16),chop=var([8,16],[24,8]),slide=1,room=2/3,mix=2/3,pan=PWhite(-4/5,4/5),amplify=linvar([0,3/5],32),amp=1*var.brk)
s2 >> bell(Pvar([var.melody,PRand(Scale.default)]),oct=[4,5],dur=8,sus=8,echo=1,vib=PRand([0,2,3,4,6,8]),room=2/3,mix=1/2,amplify=2/3,amp=1*var.brk)
s3 >> prophet((var.melody,PRand(Scale.default)),oct=6,dur=2,sus=1,chop=6,formant=3,room=2/3,mix=1/4,amplify=expvar([3/6,0],32),amp=1*var.brk)
s4 >> blip(P[var.melody,m1.degree],oct=4,dur=PDur(3,5),sus=1/2,shape=1/3,formant=2,amplify=3/5,amp=var([1, 0], [[128, 256], [64, 128]])*var.brk)


m1 >> space([3,7,10], dur=[2,2,4], sus=3, blur=2, oct=4, chop=1 + PRand(6), amp=var.brk * var([1,0],[[16,32,8,16],[8,16,8]]))

m2 >> bug([0,3], dur=sb.dur, amp=linvar([0,0.5],[1,2]), lpf=[500, 1500, 250, 300], lpr=0.25, formant=expvar([0, 1.5], [64, 128]))
m3 >> karp(P[1,3,2,1,3,2,1,3] + var([0,2],[16,8]), dur=[0.25,0.5,0.75], formant=1, sus=2, oct=4, amp=linvar([0,0.75],[8,16]) * var.brk)
m4 >> play('(----[--])', sample=var([1,4],[16,8,4,8]), amp=var.brk * var([1, 0], [256, 64])).offbeat()

m5 >> pads(amp=0.5*var.brk, dur=[0.5,1,[0.25,0.5,0.5]], oct=5, formant=2, rate=1)




xx >> play("<  mmvv  ><   --     --    >", amp=[0.8,0.6,0.7,0.9])
xy >> soft([0],dur=7,chop=var([10,20],32))
xz >> sitar([0,3,7,13]



