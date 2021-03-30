# https://soundcloud.com/kitty_clock/disengagement

Clock.bpm = 110

cb >> play('#', dur=1, room=1, mix=0.25, sample=1, amp=var([1, 0, 0], [5, inf]) * 0.75)
cl >> play('H', pan=PWhite(-0.5, 0.5), sample=1, lpf=1800, dur=8, delay=P[0, 0.5], room=1, mix=0.2, amp=0.2 * var([0, 1, 1], [32, inf]))
xx >> play('m', rate=-1, echo=0.25, echotime=2, sample=0, dur=1, lpf=110, amp=0.3 * P[1, 0])
sh >> play('s', dur=1.5, rate=-0.2, room=1, mix=0.4, pan=PWhite(-0.75, 0.75), amp=PWhite(0.1, 0.3) * expvar([1, [0.5, 0.75, 1, 1]], 3) * expvar([0, 1, 1], [32, inf]))

fs >> filthysaw(dur=2, room=1, bend=expvar([0, -0.01], 24), benddelay=0.9, mix=PWhite(0.25, 0.3), oct=4, t_bd=PWhite(0, 0.05) + expvar([0.0, 0.15], 32), t_sd=expvar([0, 0.2], 128), pw=PWhite(0.4, 0.6), lpf=PWhite(400, 1200) * expvar([1, 1.5], 128), lpr=PWhite(0.2, 1), atk=expvar([0.01, 0.00001], 16), sus=1, amp=0.4)
f2 >> filthysaw(dur=4, oct=4, lpf=PWhite(400, 700) * PRand([1, 1, 1, 1, 2, 3], 2), pw=expvar([1, 0.7], 32), lpr=0.2, atk=1, tremolo=4, amp=expvar([0.3, 0.2], 32) * expvar([0, 1, 1], [64, inf]))
db >> dafbass(dur=1, ffmod=expvar([0.6, 0.4], 8), oct=7, peak=1, rel=0.1, lpf=expvar([2000, 1000], 8), amp=expvar([0.2, 0.05], [7, 9]) * 1.25 * expvar([0, 1, 1], [128, inf]) * expvar([0, 1, 1], 64))
sb >> sosbell(dur=0.5, oct=12, chop=8, tremolo=4, ringAmp=1, ringRel=0.5, wobbleMin=PWhite(0.25, 1), sus=PRand([4, 2, 1]), strikeHarmonic=expvar([2, 2, 2.5], 16), strikeDec=0.01, strikeAmp=1, pan=0, amp=expvar([0.25, 0.05], [7, 9, 13]) * expvar([0, 1, 1], [128, inf]))

var.click_amp = expvar([0, 1, 1], [64, inf])
ck >> click(dur=4, oct=expvar([6, 8], 64), sus=0.01, hpf=0, hpr=0.5, amp=0.2 * var.click_amp)
c2 >> click(dur=3/4 * ck.dur, oct=ck.oct, sus=0.01, hpf=0, hpr=0.5, amp=0.1 * var.click_amp)
c3 >> click(dur=[2, 4], delay=[0.5, 0.75], oct=ck.oct, sus=0.01, hpf=0, hpr=0.5, amp=0.07 * var.click_amp)

kk >> play('k', dur=1, pan=expvar([-0.3, 0.3], 8), sus=var([0.005, 0.1], [3, 1]), lpf=expvar([1000, 5000], 64), sample=8, amp=0.1 * expvar([0, 1, 1], [256, inf]))
k2 >> play('k', dur=2, pan=PWhite(-0.5, 0.5), sample=12, tremolo=([4, 4, 2, 2], [2, 2, 2, 4]), lpf=expvar([1000, 4000], [16, 32, 64]), lpr=0.5, rate=(1, 2), room=1, mix=0.35, amp=0.1 * expvar([0, 1, 1], [128, inf]))
vv >> play('v', sus=P[0.05, 0.05, 1, 0.05], lpf=80, lpr=1.1, dur=1, amp=0.5 * expvar([0, 0, 1, 1], [64, 64, 128, 128]))
oh >> play('n', sample=2, dur=1, lpf=expvar([2000, 7000], [16, 32, 24, 8, 8]), pan=P[-0.25, 0, 0.25], delay=0.5, amp=0.1 * expvar([0, 1, 1], [256, inf]))

# one-shot vocals
vc >> play('!', rate=0.9, sample=12, sus=1, dur=8, amp=0.1 * var([0, 1, 0, 0], [128, 2, inf])) # please, don't flush
v2 >> play('!', rate=-1, sample=22, dur=8, amp=0.1 * var([0, 1, 0, 0], [192, 2, inf])) # self-destruct initiated
v3 >> play('!', rate=1.15, sample=40, room=1, mix=0.2, dur=4, lpf=2200, amp=0.15 * var([0, 1, 0, 0], [256, 2, inf])) # calm down
