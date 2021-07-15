# https://soundcloud.com/kitty_clock/aes-triplex
# By KittyClock, @gravitaliy, BBScar

Clock.bpm=120

# a synthdef, just try it
# i have no sound ( → still no sound → i go out → thanks =)
# try to use those attrs
# fmod=0, atk=0.001, sus=1, cf=100, vib=0, t_bd, t_sd, pw=0.4

# grav, try those special attributes above

f3 >> filthysaw(oct=6 + 2, room=5, mix=0.2, cf=10, atk=1/4, dur=PDur(3, [8,4]), t_bd=P[0.25, 0.1, 0.15, 0.05], amp=1/6 * expvar([0, 1], 32), pw=1, vib=50) # <-- here okay 

f4 >> filthysaw(dur=0.25, sus=0.15, oct=3, cf=150, t_bd=0.25, t_sd=0.15, lpf=500, amp=0.75 * P[1, [[0.4, 0.2, 0.1, 0.05], 0.25]] * 0).stop()

# I just check github

# but zbdm just gave some hint

v1 >> play('e', sample=2, dur=1.5, room=0.7, echo=P[[0.5, 0, 0, 0], 0, 0, 0], mix=0.3, lpf=2500, amp=0.5 * P[0, 1, 0, 0]).stop()

# beep!!!

# can't hear it

# let's add some swing

# start quiet shure


print(SynthDefs)

print(Samples)

print(Attributes)

# grav, add a hihat maybe? slowly

# filthysaw special attrs:
# fmod=0, atk=0.001, sus=1, cf=100, vib=0, t_bd, t_sd, pw=0.4


ss >> play('s', dur=PRand(1, 8), sample=PRand(2, 10), rate=PWhite(-1, 1), room=1, mix=PWhite(0.25, 0.75), amp=1)

vv >> play('^', rate=0.95, sample=8, dur=PDur([5, 3, 5, 3, 6, 7], 8), lpf=150, lpr=0.8, room=0.2, mix=0, krush=4, amp=0.5 * P[1, 0.2, P[0.5, 0.75], 0.5] * var([1, 0], [[1, 2], [7, 6]]) * 0.75)

v8 >> play('[vv]', rate=P[-1, 1], dur=0.5, lpf=300, amp=0.85 * expvar([1, 0.25], [1, 0]) * P[[1, 0], P[0, 0, 0, 0.75] * 0, 0, 0 * 0.75])

Group(vv, v8).stop()

Master().lpf = 800

# AYYYYY

# you too, tanks!

# I will start checking the synths again soon on amp and also new attributes. is great that you can see em later on

# k speak soon and uplo

# yep! ok, bb, I'll go upload it <3

# sure, it was great, I think I'll actually upload it on soundcloud, lol

# how should we call the track?

vv.rate=P[1, 0.95, 0.98, 0.94] * 1.2

vv.sus=0.05

kx.stop()

print(jx.amp)

jx.amp = 0.1

rc.amp=0
vv.dur=0.5
vv.amp=P[1, [0.25, 0.15]] * 0.6 * P[1, 0.25, 0.75, 0.15]
oh.stop()
kx.stop()


xx.stop()
x2.stop()

rc >> play('S', dur=0.5, pan=PWhite(-0.5, 0.5), lpf=8000, amp=0.6 * P[1, 0.4, 0, 0]).stop()

vv.dur=2
vv.delay=P[1, [0.5, 0.75]]
vv.amp=0.75


oh >> play('n', rate=0.9, dur=4, delay=0.5, echo=P[[0.25, 0, 0, 0], 0, 0, 0], pan=PWhite(-0.7, 0.7), amp=0.9 * var([0, 1], [32, 64, 64, 128]))

ch >> play('H', dur=0.25, room=1, mix=PWhite(0, 0.25), amp=PRand([0.25, 0.5, 0.75, 1, 0], 0.25) * 0.35 * var([0, 1], [28, 4, 56, 8]))

jx >> play('x', dur=4, delay=0.75, amp=0.9)

print(Clock)

# umm


kx >> play('u', sample=6, dur=PDur([3, 5, 5, 3], 8), lpr=0.5, lpf=PWhite(1500, 2250), amp=0.4 * expvar([1, 0.25], 1/3))

rr >> play('r', sample=11, dur=PDur([5, 6, 4, 3, 5, 3], 8), room=0.5, mix=0.2, amp=0.25)

Group(oh, ch, jx, kx, rr, x7, xx, vv, x2).stop()

x7 >> play('X', rate=1.1, sample=6, dur=1, amp=1)
xx >> play('x', rate=P[1.1, 1, 0.95, 1], sample=8, dur=0.5, lpf=500, lpr=0.35, amp=P[1, 0.9, 0.85, 0.9] * 1)

vv.stop()

x2 >> play('V', dur=1, sample=8, rate=0.9, krush=1, amp=1 * var([1, 0], [31, 1, 28, 4]) * 0)

ui >> play('%', sample=4, dur=0.25, sus=2, striate=4, lpf=expvar([1500, 5000], 16), lpr=0.8, amp=0.35)

Group(ui, x7, xx, rr).stop()

v8.stop()

Group(xx, x2, jx, vv, v8).hpf = 0

pp >> play('t', sample=PRand(10, 20), dur=0.25, amp=P[1, 0, 1, 0,  0, 1, 0.25, 0] * 0.5 * P[1, 0.25] * 0.5).stop()


sn >> play('I', sample=1, dur=2, echo=P[0, [0.25, 0, 0, 0], 0, 0], room=1, mix=0.2, amp=0.4).stop()

oo >> play('o', sample=15, dur=4, delay=0.5, amp=0.8 * expvar([0, 1], [128, 0, 256, 0])).stop()

# yeah, makes a good rumble

# also room + mix

# It's sick, BBscar, isnt' it? :D
# all random

f1 >> filthysaw(
    -1,
    dur=4,
    cf=P[250, 100, 50, 250] * expvar([0.5, 2], 16),
    t_sd=P[0.1, 0.15, 0.25, 0.05] * 0.25,
    pw=expvar([0.1, 1], [2, 0]) * 1.5,
    sus=P[0.25, 0.5, 0.25],
    room=1, mix=0.2,
    amp=PRand([0.4, 0], [16, 32, 64, 128], seed=9)
)



f2 >> filthysaw(PWalk(2) + var([0, -1, 0, 1], PRand([4, 8, 16, 32])), oct=var([3, 7], [16, 32, 4, 8, 12, 32]), 
                dur = 8, 
                cf = linvar([200, 800], 8), 
                t_bd = 1/4, 
                pw = PRand([1/2, 1/4, 1/8, 1/7], 16), 
                chop = 16,
                vib = var([8, 16, 32, 0], [24, 8]),
                bend = P[0, 1/8, 0, -1/8, 1/2, -1/4] * P[5/100, 1/3, 1, 1/4, 3/4], # FIRE
                benddelay = PRand([0, 1/2, 0, 3/4]),
                fmod = 1,
                room = 1/3,
                mix=1/2, 
                t_sd = P[0.02, 0.04, 0.1, 0.02],
                pan=PSine(32), 
                amplify=PRand([0, 1/20], [8, 16, 32, 64], seed=13))
                
                
print(SynthDefs)

s3 >> rsin(-4, oct=4, dur=8, formant=4, lpr=0.5, tremolo=P[4, 8, 16], lpf=expvar([200, 1200], [16, 0]), amplify=var([0.07, 0], PRand([4, 8, 16, 32], seed=7)), amp=0.3)

b1 >> play("Z", dur=32, sample=14, rate=-1, pshift=7, striate=0, room=1/2, mix=1/3, amplify=PRand([0, 3/9]))

s4 >> hoover(var([0, 2, 0, -2], 64), oct=4, dur=16, chop=64, formant=5, drive=1/20, lpf=linvar([200, 1800], 32), lpr=1/4, room=2/3, mix=1/2, pan=PWhite(-1, 1), amplify=PRand([0, 1/18], [32, 16, 64], seed=3))

s5 >> sillyvoice(-4, oct=8, dur=1/4, sus=1/8, drive=1/20, coarse=4, room=2/3, mix=var([1/2, 4/5], [6, 2]), amplify=1/9)

# <3

# of course

# it was AMAZINK

# yea!
print_synth(s5)

# Let's maybe end slowly?

Master().hpf = 0
Master().hpr = 0.5


print(SynthDefs)

