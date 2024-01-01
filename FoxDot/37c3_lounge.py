Clock.bpm = 150

s5 >> loop('/home/vlad/Music/belo/relic_1.wav', 0, rate=0.25, dur=4, tremolo=4, lpf=300, amp=1)
s1 >> loop('/home/vlad/Music/belo/8.wav', 4, rate=[var([0.25, -0.25], 32), 0.25], dur=2, tremolo=4, amp=0.3 * var([1, 0], [256, [32, 64]]) * 1)
s4 >> loop('/home/vlad/Music/belo/s1.wav', 0, dur=4, rate=0.25, tremolo=0, amp=1)
s6 >> loop('/home/vlad/Music/belo/s1.wav', 4, dur=0.25, rate=var([3, 4], [16, 16, 32, 32]), tremolo=var([0, 2, 4], 64), lpf=linvar([300, 1500], 16), lpr=linvar([1, 0.5], 64), amp=0.85 * 0.3 * 1)
Group(s1, s5, s4, s6).amplify = 1

Master().hpf = 0
h1 >> loop('/home/vlad/Music/belo/s2.wav', 2, dur=1.5, rate=2, amp=0.25 * 0.7 * linvar([0, 1], 256) * 1) # wheeeu

Master().hpf = 300
Master().hpr = 0.5

Master().hpf = 0
h2.stop()

# start with dur 2
ii >> play('I', sample=11, sus=1, dur=var([0, 1], 128), echo=[0, 0, 0.5 * var([0, 1], 8)], amp=P[0, 1] * 0.5)

xx >> play('x', sample=1, dur=PDur([3, 5], 8), amp=P[1, var([0, 1], [28, 4, 31, 1]), [var([0, 1], 16), 0], [0, 0, 0, var([1, 0], [32, 64, 128])]] * 2.5 * 0.7)
x2 >> play('X', sample=2, dur=PDur([3, 5], 8), amp=xx.amp * 1 * var([0, 1], [64, 128, 128, 128]) * 0.7)
Group(xx, x2).amplify = 1
sk >> play('z', dur=0.25, sample=4, pan=PWhite(-0.8, 0.8), rate=3 * P[-1, 1, 0.5, -0.5, 0.25, -0.25, -0.1, 0.1, 0.5], amp=0.5 * PWhite(0, 1) * var([1, 0], 2) * var([0, 1], [32, 64]))


Group(xx, x2).stop()

oh >> play('-', sample=4, dur=0.25, delay=0, pan=PWhite(-0.5, 0.5), amp=linvar([0.25, 1], 1/3) * 0.75 * linvar([0, 0, 1, 1], [16, 16, 32, 0])) #.stop()

Group(xx, x2).stop()

var.brk = var([1, 0], [31, 1, 28, 4, 56, 8])
xx >> play('x', sample=4, dur=var([1, [0.5, 0.5, 0.5, [0.5, 0.25]]], [7, 1]), amp=1.2 * var.brk) # P[1, var([0, 1], [28, 4, 31, 1]), [1, 0], [0, 0, 0, var([1, 0], [32, 64, 128])]] * 2.5 * 0.7)
x2 >> play('X', sample=12, dur=xx.dur, amp=1.2 * var([1, 0], [31, 1, 28, 4]) * var.brk) #xx.amp * 1 * var([0, 1], [64, 128, 128, 128]) * 0.7)
x3 >> play('X', sample=21, dur=0.25, amp=P[0, 0.25, 0.5, 0.75] * 0.95 * var.brk * 1) # rolling kick

Group(xx, x2, x3).stop()


Master().hpf = 0

Master().hpf = 0
s1.stop()
# ob hihat

h2 >> play('=', sample=1, sus=P[1, 0.5] * 0.10, rate=var([1.3, 2], [32, 64, 128]), dur=1, delay=0.5, amp=P[1, 0, 0, 0] * 0.85 * var([1, 0], [31, 1, 28, 4])) #.stop()

Master().hpf = 0
w1 >> loop('/home/vlad/Music/belo/s2.wav', 3.5, dur=1.5, sus=2, rate=-2 * 0.25, chop=8, room=1, mix=0.25, lpf=linvar([500, 3800], 16), amp=0.5)
oh >> play('!', sample=3, rate=2, dur=1, room=1, mix=0.1, amp=P[1, 0, 0, 0] * 0.3 * linvar([0, 1], [32, 64, 32]))
f1  >> play('!', sample=13 + 2, rate=2, dur=1, room=1, mix=0.1, lpf=linvar([500, 3500], 32), pan=linvar([-0.5, 0.5], 6) + PWhite(-0.25, 0.25), amp=P[0, 1] * linvar([1, 1], 32) * 0.75)

Group(xx, x2, x3).stop()

Group(w1, oh, f1).stop()

Group(s1, s5, s4, s6, h1, h2, ii, xx, x2).amplify = 0

############

Group(s2, x5, b3, b5, b1, b2, x3, xx, x2, s1).stop()
Group(s2, x5, b3, b5, b1, b2, x3, xx, x2, s1).reset()

s2 >> loop('/home/vlad/Music/samples/sdg/fx/SYNTH/29.wav', var([4, 8, 2], 32), rate=P[3, 2, 1, 1, 4, 4, 2, 2] * 2.5, pan=PWhite(-0.7, 0.7), dur=0.25, delay=0.5, sus=P[0.5, 0.75, 0.5, 0.25, 0.25, 0.25, 0.1, 0.1] * linvar([0.25, 0.5], 8), amp=P[1, 0, 1, 1,  0, 1, 0, 1] * 0.5 * linvar([0, 0, 1, 1], [32, 32, 32, 32, 64, 64, 64, 64, 16, 16, 16, 16]) * var([1, 0], [31, 1, 28, 4, 30, 2, 15, 1, 14, 2, 56, 8]) * P[1, 0, 0] * 1)
b3 >> loop('/home/vlad/Music/samples/xtratrash/Bass/bass_8.wav', 2, dur=1.5, sus=1.5, rate=1, lpf=linvar([7000, 300], 16), amp=0.20 * linvar([1, 0], 64) * 1)
# b5 is howl
b5 >> loop('/home/vlad/Music/samples/xtratrash/Bass/bass_7.wav', 0, dur=1, rate=1, sus=1, lpf=500, amp=P[1, 0] * 0.9 * linvar([0, 0, 1, 1], 64) * 1)
b1 >> loop('/home/vlad/Music/samples/xtratrash/Bass/bass_7.wav', 0, dur=1, rate=var([1, 0.4], [6, 2]), sus=1, chop=0, lpf=linvar([500, 2500], 16), room=0.5, mix=0.2, amp=P[0, 1] * 0.8 * 1)
b2 >> loop('/home/vlad/Music/samples/xtratrash/Bass/bass_7.wav', 1, dur=1, delay=0.5, rate=1, sus=0.5, lpf=linvar([2500, 500], 32), amp=P[1, 0] * 0.8 * linvar([1, 0], [128, 64, 32]) * 0) # turn this off later
Group(s2, b3, b5, b1, b2).amplify = 1

s1 >> loop('/home/vlad/Music/samples/xtratrash/Snare/snare_11.wav', 0, rate=0.25, dur=1, delay=0.5, lpf=1000, amp=P[0, 0, 1, 0] * 0.5)

x5 >> loop('/home/vlad/Music/samples/xtratrash/Kick/kick_23.wav', 0, dur=1, sus=P[1.3, 0.95] * 0.95, hpf=linvar([240, 150], 16), hpr=0.75, amp=1 * linvar([1, 0.5], [128, 0]) * linvar([0, 1], 64))

Group(b5, b1, b2).sus = linvar([0.25, 1], [[16, 32, 64, 128], 0])

# Group(b5, b1, b2).sus = P[1, 0.25, 0.25, 0.25]
Group(b5, b1, b2).stop()

Group(b5, b1, b2, x2, xx, x3).hpf = var([0, [300, 250, 350, 400]], [[28, 31, 56], [4, 1, 8]])
# Group(b5, b1, b2, x2, xx, x3).hpf = 300
Group(b5, b1, b2, x2, xx, x3).hpr = 0.5

x3 >> loop('/home/vlad/Music/samples/xtratrash/Kick/kick_10.wav', 0, dur=0.25, sus=0.2, lpf=linvar([300, 200], [1, 0]) * linvar([1, 10], [32, 0]), lpr=0.5, amp=P[0.25, 0.5, 0.75, 1] * 0.65 * 1) # filler
xx >> loop('/home/vlad/Music/samples/xtratrash/Kick/kick_8.wav', 0, dur=1, bend=var([0.3, 0], 64), sus=P[0.3, 0.2], lpf=3000, rate=P[1.05, 1, 1.02, 0.99], amp=1 * 1) # main punch
Group(xx, x3).amplify = 1

x2 >> loop('/home/vlad/Music/samples/xtratrash/Kick/kick_1.wav', 0, rate=1, dur=0.25, lpf=linvar([1000, 3000], 16) * linvar([2, 1], [16, 0]), amp=P[0.3, 0, 0.5, 0, 0.1, 0.2, 0.1, 0.5] * 0.85 * 1) # subkicks

x3 >> loop('/home/vlad/Music/samples/xtratrash/Kick/kick_10.wav', 0, dur=0.25, sus=0.2, lpf=linvar([300, 200], [1, 0]) * var([1, 2, 1, 4, 1, 8], 16), lpr=0.5, amp=P[0.25, 0.5, 0.75, 1] * 0.65 * 1) # fat

# 5 bpm slowdown trick
x5.stop()
Master().room = 1
Master().mix = 0.25
Master().rate = P[1, 0.5]
Clock.bpm = 5

Clock.bpm = 2

f1.reset()
f1 >> loop('/home/vlad/Music/samples/xtratrash/Snare/snare_11.wav', 0, rate=0.25, dur=1, delay=0.5, lpf=1000, amp=P[0, 0, 1, 0] * 0.5)
f2 >> loop('/home/vlad/Music/samples/sdg/fx/SYNTH/29.wav', var([4, 8, 2], 32), rate=P[3, 2, 1, 1, 4, 4, 2, 2] * 2.5, pan=PWhite(-0.7, 0.7), dur=0.25, delay=0.5, sus=P[0.5, 0.75, 0.5, 0.25, 0.25, 0.25, 0.1, 0.1] * linvar([0.25, 0.5], 8), amp=P[1, 0, 1, 1,  0, 1, 0, 1] * 0.5 * linvar([0, 0, 1, 1], [4]) * var([1, 0], [31, 1, 28, 4, 30, 2, 15, 1, 14, 2, 56, 8]) * P[1, 0, 0] * 1)
f3 >> loop('/home/vlad/Music/samples/xtratrash/Bass/bass_8.wav', 2, dur=1.5, sus=1.5, rate=1, lpf=linvar([7000, 300], 16), amp=0.20 * linvar([1, 0], 8) * 1)
f4 >> loop('/home/vlad/Music/samples/xtratrash/Bass/bass_7.wav', 0, dur=1, rate=1, sus=1, lpf=500, amp=P[1, 0] * 0.9 * linvar([0, 0, 1, 1], 4))
f5 >> loop('/home/vlad/Music/samples/xtratrash/Bass/bass_7.wav', 0, dur=1, rate=var([1, 0.4], [6, 2]), sus=1, chop=0, lpf=linvar([500, 2500], 16), room=0.5, mix=0.2, amp=P[0, 1] * 0.8)
f6 >> loop('/home/vlad/Music/samples/xtratrash/Bass/bass_7.wav', 1, dur=1, delay=0.5, rate=1, sus=0.5, lpf=linvar([2500, 500], 32), amp=P[1, 0] * 0.8 * linvar([1, 0], 16))

Master().amplify = 0.
