# https://soundcloud.com/kitty_clock/street-smarts

Clock.bpm = 150

u2 >> play('uuu u uu  uu'.replace('u', 'A'), sample=9, sus=0.05, drive=1, dur=0.25, amp=var([1, 0], [[2, 16], 2, 6, 2]) * var([0, 1], [32, 64, 16, 16, 32, 32]))
ss >> play('s', dur=0.125, drive=P[0, var([0, 0.1], [3, 1]), 0.125, 0], sample=6, lpf=expvar([3000, 7000], [[3, 6, 9, 12, 18], 0]), lpr=0.5, amp=PEuclid(3, var([8, 7, 6, 5])))
uu >> play('U', dur=var([1, 0.5], [3, 1]), rate=var([1, 0.5], [30, 2]) * P[PRand([-3, -2, -1], 2), -2, -1, -2], drive=PWhite(0, 1), sus=1, lpf=expvar([200, [2000, 1500, 2250, 500]], [4, 0]) * 2, lpr=0.85, sample=12, amp=0.5)
u7 >> play('u', dur=0.25, pan=PWhite(-0.5, 0.5), amp=P[1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1] * var([0, 1], [32, 64, 32, [32, 128]]))

o2 >> play('u', dur=2, amp=1.5 * var([1, 0], [64, 32, 64, 16, 128, 32]))

jk >> play('U', dur=0.25, drive=0, sample=15, sus=0.15, amp=var([0, 1], [3, 1]) * expvar([0, 0, 1, 1], [32, [32, 0], 32, 0]) * var([0, 0.5, 1], 8))
eu >> play(PEuclid2(3, 8, 'M', 'I'), sample=8, dur=P[1, 0.5, 0.5, 1, 1], amp=var([1, 0], [8, 4, 16, 8]))

# Master().hpf = 0
# Master().hpr = 0.25

oh >> play('-', sample=13, pan=P[-0.25, 0.25], dur=var([1, 0.25], [[6, 31, 28], [1, 1, 2]]), delay=0.5, amp=1.5 * var([1, 0], [8, 3, 16, 4, 9, 3]))
u3 >> play('U', sample=11, rate=0.15, sus=0.02, dur=1 * var([1.5, 1], [16, 16, 32, 32]), amp=1.25) # * var([0, 1], [32, 64, 32, 128, 32, 64, 64]))

vv >> play('v', sample=3, drive=0, dur=var([1, 0.25], [63, 1, 31.5, 0.5]), hpf=40, hpr=0.25, amp=1 * var([1, 0], [3, 1, [7, 3], 1, 31, 1]))
xx >> play('A', dur=vv.dur, sample=33, drive=0, hpf=var([0, [500, 300, 600, 250]], [[30, 28], [2, 4]]), hpr=0.25, amp=1.75 * vv.amp * 1)

Group(sy, jj, eu, oh, u2).stop()
Group(oh, o2, u3, u2).stop()

jj.stop()

sy >> play('W', rate=P[1, -1], dur=var([0.5, 0.125, 0.25], [[6, 14, 6, 30], 1, 1]), formant=0, drive=0, sample=35, hpf=var([[200, 210, 190], [500, 600, 450, 800]], [6, 2]), hpr=0.5, amp=2 * var([0, 1], [64, 64, 32, 128, 32, 32]))
jj >> play('A', dur=var([1, [0.5, 0.5, 0.25, 0.5]], [7, 1]), sample=10, amp=1.3 * expvar([0, 1, 1], [[64, 32, 0], 64, [0, 0, 32]]) * var([1, 0], [31, 1, 28, 4]))
fs >> vibass(dur=1, fmod=var([0, 1], [7, 1]), amp=expvar([0, 0, 1, 1], [64, 64, 64, 0]) * var([1, 0], 2) * 0.75)

Group(uu, u2, ss, uu, oh, o2, u3).stop()

bx >> play('I', sample=9, dur=vv.dur * 2, amp=2 * var([0, 1], [32, 64, 32, 32, 32, 128]))
ll >> play('L', dur=0.75, sus=0.02, sample=22, pan=expvar([0.5, -0.5], 8), amp=expvar([1, 0], [[4, 3, 8, 8], [0, 4, 6, 0, 2]]))
gg >> play('g', sample=12, drive=var([0, 1, 0], [7, 0.5, 0.5]), dur=0.5, amp=1.25 * var([1, 0], [[28, 30], [4, 2]]))
sh >> play('S', sample=16, pan=PWhite(-0.5, 0.5), dur=0.5 * var([1, 2], [64, [32, 16, 8], 28, 4]), amp=P[0.5, 1] * expvar([0, 1, 1], [[32, 16, 8], [32, 16, 64], 0]))
s2 >> play('s', echo=P[0, 0, [0, 0.5], 0], echotime=2, sample=12, dur=1, delay=0.5, amp=2)

gg.stop()
vv.stop()
jj.stop()

Group(bx, ll, gg, sh, s2, jj, fs).stop()

# Master().hpf = 600
Master().hpf = 0

Group(oh, o2, u3, u2, uu).stop()
