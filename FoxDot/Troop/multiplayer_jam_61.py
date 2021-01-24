# By KittyClock & GGERKK

Clock.bpm = 120

# start with lower amp0 until you're sure that your synth sounds nice

g1 >> klank(oct=4, chop=var([0, 4], 64), lpf=expvar([200, 2000], 32), amp=0.5)

n1 >> nylon(2, drive=expvar([0.25, 0], 1/3), dur=0.25, amp=0.4, oct=(4,5), lpf=expvar([300, 1500], [32, 0, 28, 4]), shape=expvar([0.2,0.5],[32,8,265,1]))

# let's make dis shit harder, make melodies more minimal and add harsh sounds

g2 >> bass(
    P[var([0,[2, 1, 0, -1],[4, 6, 0.5, -0.5],-2], 4) + var([0,-2,3,1],[3,1])].reverse(),
    dur=P[0.25 * 8],
    chop=var([4, 2], [28, 4]),
    sus=PWhite(2,4),
    room=[1, 0, [0, PWhite(0, 1)], 0],
    mix=P[.45, 0, 0, 0.15],
    shape=expvar([0.3, 0], 1/3) * var([1, 0], 64),
    lpf=P[[500, 250, 550, 600], 450, 600, 750] * var([1, 2, 1.5, 2.5], [3, 1]) * 0.25,
    lpr=expvar([[0.05, 0.75, 0.25, 0.5], 0.25], [64, 0]),
    amp=0.55 * P[1, var([0.75, 1], 8), 1, [var([0.5, 1], 16), 1]] * expvar([1, 1, 0], 256)
) + (-5,var([2,4,6],[3,1]))

g3 >> sawbass(P[4,-4].reverse(), sus=0.5, dur=PDur(3,8), chop=4, amp=1 * var([1, 0], [28, 4, 31, 1, 56, 8]), bpf=6000)

b1 >> jbass(dur=1, lpf=PWhite(500, 1000), lpr=0.8, amp=P[0.5, 1] * var([1, 0], [128, 64, 64, 32, 128, 64]))
b1.follow(g2)

bp >> blip(dur=2, delay=P[0, 0.5], tremolo=4, room=1, mix=0.5, lpf=400, lpr=0.5, amp=3 * expvar([0.25, 1], 128))

print(Samples)

nb >> play('b', dur=8, amp=0.85)

jj >> sawbass(
    dur=var([0.25, [0.5, 0.25, 0.25, 0.25], 0.25, 0.25], 32),
    chop=4,
    drive=P[0, P[0.01, 0], 0.5, P[0, 0, 0.1, 0]] * 0,
    formant=1, 
    room=P[1, 0, 0, 0], mix=0.25, 
    sus=var([1.5, 2], 32),
    hpf=P[1, [0.25, 0.75, 1, 0.85], 0.75, 0.5,  1, 0.75, 1, [0.5, 0.75, 0.5, 1]] * expvar([250, 3500], 32),
    hpr=expvar([0.25, 0.1], [56, 8]),
    amp=0.6 * P[[var([0.25, 1], 32), PWhite(0.25, 1)], P[0.5, 1, 1, PWhite(0.5, 1)], 1, var([0.75, 1], 8)] * 0.
)


# btw just watching you do your magic is very enlightening haha

# thanks. I find it's more comfortable to code if you make your keyboard repeat speed faster, and response speed lower
# oh yea. just adjusted my keyboard! thanks for the tip
# makes you fasteerrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr

# now if only my brain could keep up...
# <3

# with practice xD

uu >> play('u', dur=4, delay=0.5, amp=1 * expvar([0.5, 1], 128) * var([0, 1], [64, 128, 32, 64, 64, 128]))

Group(cl, sn, sr, x1, v1, h1).stop()

db >> dab(dur=0.5, tremolo=1, lpf=100, bedn=P[-0.25, 0, 0], lpr=0.8, amp=P[1, P[0.75, 0.25, 0.15, 0.5]] * 1)
bk >> bass(dur=1, sus=P[0.2, 0.1], hpf=250, hpr=0.9, amp=1 * var([1, 0], [64, 64, 64, 32, 128, 64]))

v8 >> play('V', sample=1, dur=bv.dur, amp=0.85) 
bv >> play('V', rate=2, drive=0.25, dur=[1] * 7 + [0.5, 0.5], sample=1, lpf=0, hpf=120, hpr=0.15, amp=0.25 * 0)
v5 >> play('v', dur=1, delay=0.5, amp=P[0.35, 0.25])

sh >> play('s', pan=PWhite(-0.75, 0.75), lpf=expvar([2000, 5000], [64, 0]), lpr=0.25, dur=0.25, amp=expvar([1, 0, 0], [8, 8, 0]) * 0.5)
cl >> play('H', echo=P[0, 0, 0.25, 0.5,  0.25, 0, 0, 0.25], echotime=PStep(4,0.25), sample=var([2, 1], [28, 4, 7, 1, 56, 8]), dur=0.5, amp=P[0, 1] * 0.33 * var([0, 1], [64, 128, 64, 32, 32, 64, 128, 256]))
sn >> play('I', dur=x1.dur * 2, lpf=5000, lpr=0.5, amp=1.25 * var([1, 0], [64, 32, 128, 64, 256, 128]))
sr >> play('~', dur=0.25, pan=PWhite(-0.75, 0.75), amp=P[1, 0.75] * expvar([0, 2, 0], [64, 0, 32]))
x1 >> play('x', dur=P[2, 1, 1], sample=2, lpf=var([800, 500, 700, 350, 200], 32), lpr=expvar([1, 0.3], [64, 32, 128, 64]), delay=0, amp=P[1, 1, 1, 1] * 1.25)
v1 >> play('[vvv]', dur=x1.dur, sus=0.15, delay=P[0, 0.5, 0, 0.75], amp=P[0, [0, 0, [0, 1], 1], 0, [0, 1]] * 0.85 * var([1, 0], [256, 64, 128, 32])) 
h1 >> play('-', pan=PWhite(-0.5, 0.5), sample=2, dur=0.5, delay=0.5, amp=P[0.1, 0.5] * var([1, 0], [[28, 31, 64, 31, 56], [4, 1, 32, 1, 8]]) * var([1, 0], [64, 32, 128, 64, 128, 64]) * var([1, 0], [256, 128]))

sj >> play('S', dur=0.5, amp=P[[0.5, 0.35], 1] * 1.15 * var([1, 0], [28, 4, 31, 1, 7, 1, 7, 1, 7, 1, 3, 1, 3, 1, 3, 1, 3, 1]))

Group(sn, sr, x1, v1, h1, sh, cl, yi, h2).stop()

# reversed hihat :)

# i've got to take off 

# Maaster() is a lovely thing

# for sure. you've ...eh.. MASTERED it.

# i'll see myself out.

in# yo, check this out

Master().rate = 1

Master().hpf = 0


# not really, Crash Server guys are much more pro, but THANKSSSS <3

# ok, thanks for jamming! See ya later peace!

Master().lpr = P[0.15, 0.25]

 
  # a minute

# yeah, me too, watch this

# you got more control with amp, yea

# hehe, I basically just use timevars to turn the sound on and off

h2 >> play('-', rate=-1, dur=1, delay=-0.05, amp=0.95 * var([0, 1], [64, 32, 128, 64, 128, 64]) * var([1, 0], [256, 128]))

yi >> play('t', sample=2, rate=1, lpf=3800, lpr=0.75, tremolo=4, dur=2, delay=P[0, 0.5], amp=1)

tt >> play('ktrr',
    sample=1, dur=0.25,
    lpf=P[800, 900, [500, 1200], [450, 600, 700, 500]] * expvar([0.75, 1.5], [60, 4]),
    lpr=expvar([0.5, 0.25], [2, 0]),
    amp=1.25 * var([1, 0], [3, 1, 2, 2, 6,2 ,4, 2, 3, 1, 2, 3, 2, 2, 1, 1]) * var([0, 1], [64, 128, 32, 64, 128, 256]) * 0.5
)

xo >> play('X', sample=1, dur=1, hpf=120, hpr=0.2, amp=1.25)

ml >> play('V', sample=2, dur=0.25, lpf=expvar([200, 150], [2, 0]), lpr=expvar([1, 0.75], [1, 0]), amp=expvar([0.25, 1], [1, 0]))

ml.lpf=6000
ml.lpr=1

Group(v8, bv, v5).stop()

fh >> play(var(['n', 't'], [7, 1, 3, 1, 4, 2, 2, 1, 2, 1, 3]), sample=1, rate=P[1, 1.05, 1.1, 1], lpf=var([5000, 4000, 3000, 2500], 32), lpr=0.25, dur=0.25, amp=expvar([0.95, 0], [128, 0]) * 1.25)

