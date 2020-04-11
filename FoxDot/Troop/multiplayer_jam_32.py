Clock.clear()
Clock.reset()
Clock.set_time(0)

Clock.bpm = 150



print(SynthDefs)


s1 >> ripple(var([0,[0,0,3,-2]],[12,24]), dur=0.5 * P[3,[3,6],6], shape=0.2, amp=0.1, tremolo=expvar([1,4],[20])).stop()

s2 >> glass(P[5,3,2], amp=2, dur=[12,6,6], formant=2)

s3 >> nylon(s2.pitch[0] - var([0,3],[6,12]), dur=[0.5,0.25], amp=0.5, oct=[[5,4,4],4], formant=var([0.1,1],[6,6,12])).stop() 
s4 >> zap(1, amp=var([0,1],[12,12,6]), dur=[0.25,0.5])
s5 >> zap(amp=2-s4.amp, dur=0.25, formant=2).offbeat().stop()
s6 >> blip(P[5,2,5,3,5,2,5,3] + var([0,4],[20,6]), dur=[0.5] - var([0,0.25],[[20,8],[2,3]]), amp=var([1,0],[[12,3],[0,1]])).every(6, 'stutter', 3)
s7 >> pasha(dur=[0.5,0.5,0.5,[0.5,0.5,1]], formant=s6.dur, amp=s6.amp, oct=[4,4,6], tremolo=3, pan=PWhite(1)).accompany(s6) 

#okie i go eat now 

# amazink

@next_bar
def stahp():
    Group(bi, bp, sb, rs, tt, sk, kd, bb, cl).stop()



bi >> ambi(var([0, 0.5, -1], 64), dur=32, sus=40, lpf=expvar([1000, 5000], 128), lpr=0.25, tremolo=(0, 8), amp=var([0.5, 0], [[128, 256, 64], [64, 128, [32, 128]]]))

h1 >> play('-', sample=2, room=1, mix=0.25, dur=16, amp=1)
sh >> play('s', dur=0.25, pan=PWhite(-0.75, 0.75), lpf=0, lpr=0.25, amp=P[PWhite(0.25, 0.85), [1, 0.85, 0.5], [0.25, 0.75], [1, 0.75]] * expvar([1.35, 0], [[4, 0], 0]))
bp >> blip(dur=1, room=1, mix=0.35, lpf=[300, 280, 300, 290], oct=4.9, amp=var([1.5, 0], [[128, 64], [64, 32]])).stop()
sb >> blip(dur=0.25, lpf=[280, 300, 310, 300], amp=P[[1, 0.75], 0, var([0, 0.5, 1], [32, 32, 8]), 0,  0, [0.5, 0.25, 1], 1, 0] * 0.5 * bp.amp).stop()
rs >> play('I', room=1, mix=0.2, dur=1, amp=var([1.25, 0], [128, [64, 32, 64]]))

kd >> play('X', sample=2, dur=1, lpf=180, lpr=0.5,
    amp=P[
        1, 1, [var([0.25, 1], [256, 512]), var([0, 1], [64, [128, 256]])], [var([0, 1], [128, 256]), 1]
    ] * var([0.75, 0], [[512, 256, 128, 64], [256, 128, 64, 32]]) * 0.85
) 

sk >> play('X', sample=kd.sample, dur=kd.dur, delay=0.5, lpf=200, lpr=0.5, amp=P[0, 1, 0.5, 0] * var([0.25, 0], [64, 64, 128, 128]) * kd.amp)
tt >> play('t', sample=1, dur=0.25, lpf=expvar([1500, 5000], [128, 0]), amp=expvar([1.25, 0.25], 1/3) * var([0, 1], [[128, 64, 64], [64, 128]]))
h2 >> play('-', sample=2, dur=kd.dur, delay=0.5, amp=kd.amp * var([1, 0], [[128, 64, 64], [64, 32, 32]]))
h3 >> play('s', sample=1, dur=kd.dur, delay=0.5, amp=h2.amp)
rk >> play('X', sample=2, rate=-1, dur=1, amp=var([0, 1], [63, 1]))
bb >> sawbass(dur=0.25, drive=P[expvar([0, 0.05], [32, 64]), 0], hpf=[200, 800, [500, 350]], hpr=0.25, amp=P[1, 0.75, 0.5, [0.25, 0.75]] * 0.25)
cl >> play('H', sample=1, dur=[8, 8, 4, 4, 4, 4], delay=0.5, amp=var([0.75, 0], [[256, 128], [64, 32]]))

