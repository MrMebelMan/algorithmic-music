Clock.clear()
Clock.reset()

Clock.bpm = 125
Root.default = -2
Scale.default = "minor"

Scale.default.set(Pvar([Scale.minor,Scale.],[128,64,64,128,64,64,128,128]))

#no sound ok

#But this should work. I used it in my own stuff, got it from there

note=PRand(Scale.default)
notes = [-2, -2, var([-3, -2], [64, 32, 64]),  -2, [-2, var([-2, -3])], var([-2, -3, -4], 32)]
chords = [(0,2),(-1,1),(0,2),(1,3)]

var.brk = var([1, 0], [[31, 28, 31, 56], [1, 4, 1, 8]])

print(SynthDefs)

kk >> klank(dur=0.25, sus=[0.15, 0.5, 0.25], amp=[[0.05, 0.15], 0.1] * 0.05)

nl >> nylon(
    notes,
    pan=PWhite(-0.5, 0.5),
    room=expvar([0, 1], [128, 0]), mix=[0.15, [0.15, 0.05], 0.15, 0.15],
    dur=[[0.25, var([0.25, 0.5], [28, 4])], 0.25, 0.25],
    sus=[[1, 0.85], 0.25, var([0.25, 0.75], [[128, 32], [64, 16]]), [0.5, var([0.5, 0.25], [64, 128, 64])]],
    drive=P[0, 0.025, [0.04, 0.035]] * var([0, 1], [[128, 64], [32, 32]]),
    amp=P[1, 0.95, expvar([0.25, 0.75], 128)] * 0.00
)
sh >> play('s', dur=1, amp=expvar([1, 0], [4, 0]) * var([0, 0.5], [128, [256, 64]])).every(16, 'stutter', 2, amp=0.35)

cl >> play('H', room=expvar([0, 1], [128, 0]), mix=0.25, sample=1, dur=var([32, 16, 8], [128, [32, 64]]), delay=0.5, lpf=1500, amp=0.3)

u1 >> play('u', room=1, mix=0.25, dur=2, amp=expvar([0, 0.5], [64, 128, 128]) * var.brk)
h1 >> play('S', dur=1, amp=P[1, 0.85] * var([0, 0.25], [[128, 64], [64, 32, 64]]) * var.brk)
h2 >> play('-', sample=var([2, 1], 128), dur=[1] * 15 + [0.25, 0.75], delay=0.5, amp=var([0, 0.75], [64, 128, [64, 128], 256]))

h3 >> play(':', dur=0.25, amp=expvar([1, 0.25], 1/3) * var([0.4, 0], [[256, 128], [64, 32]]) * h2.amp)

m1 >> play('m', dur=var([4, 2, 1], [[64, 128], [64, 32], [128, 256]]), delay=0, bend=-0.25, benddelay=0.25, lpf=350, lpr=0.5, hpf=var([190, 130], [128, 32]), hpr=0.25, amp=P[1, 0.85] * 0.7 * var.brk)
#m1.dur=1
#m1.amp=P[1, 1, 1, 1] * 1.25 * var.brk
kd >> play('X', dur=m1.dur, delay=m1.delay, lpf=200, sample=var([2, 2], [256, [64, 128]]), amp=expvar([0, 0.35, 0.35], 128) * var.brk)
sn >> play('I', dur=m1.dur * 4, delay=0, amp=0.3)
m2 >> play('m', rate=1, sample=0, lpf=400, dur=m1.dur, delay=0.5, amp=P[var([1, 0], [64, 32]), 1, 1, 0] * var([0, 0.25, 0.5], [128, 32, 64, 64]))
# }:D
nn >> play('[ns]', pan=PWhite(-0.5, 0.5), rate=[0.75, 0.85, 0.75, 0.75], dur=0.125, lpf=expvar([1000, 1000, 5000], [[32, 32, 32, 64], [32, 32, 32, 64], 0]), lpr=0.25, amp=P[1, [0.85, 0.75, 0.95, 0.25]] * 0.5 * var.brk)
tt >> play('t', sample=1, dur=0.25, lpf=[var([1200, 1050], 4), [1200, 1000], [1200, var([700, 1300], 64), 1300, 800], var([1200, 1000], 8)], lpr=0.5,
    amp=P[
        [1, 0.75], [0.5, 0.75], [0.25, 0.5], 0.75,  [0.85, 0.5], var([0, 0.5], [128, [64, 32]]), [var([0, 0.75], 128), 0.5], expvar([0, 0.5], 128)
    ].reverse() * var([0.25, 0.5], [[128, 64], [256, 128]])
)

Group(sh, nn, cl, u1, h1, h2, h3, m1, kd, sn, nl, tt, m2, ws).stop()

bg >> bug(dur=1, sus=0.5, drive=0.05, lpf=300, lpr=0.25, tremolo=4, hpf=200, hpr=0.25, amp=expvar([0, 1], [128, 0]))
ws >> varsaw(oct=4.7,
    hpf=expvar([100, 350], [128, 0]), hpr=0.25,
    drive=expvar([0.01, 0.08], [128, 64]) * 0, dur=0.5,
    bend=0 * P[var([0, -0.05], 128), [0, -0.1, 0, 0]],
    benddelay=var([0.15, 0.75, 0.25, 0.5], 32),
    amp=P[1.1, 1] * 0.6
)

print(SynthDefs)


s1 >> donk(notes,dur=8,echo=1/2,room=1/3,mix=1/3,pan=(-2/3,2/3),amplify=2/4,amp=(1*var.intro)+(1*var.brk1)+(1*var.brk2))
t1 >> donk(notes,oct=6,dur=PDur(3,5),echo=1/2,formant=1,room=2/3,mix=1/3,pan=(-2/3,2/3),amplify=2/5,amp=(1*var.bldup1)+(1*var.drop1)+(1*var.bldup2)+(1*var.drop2))

s2 >> karp((notes,note),oct=PRand([6,7]),dur=PDur(5,8),sus=1,formant=linvar([0,3],16),room=2/3,mix=1/3,amplify=PRand([1/3,amp=1)

s3 >> prophet(chords,oct=var([5,6],[24,8]),sus=1/2,formant=2,lpf=800,room=1/3,mix=1/4,amplify=1/6,amp=1).offbeat()

s4 >> sitar(var([chords,P[:2]],4),oct=PRand([5,6]),dur=1/4,delay=var([[0,0,1/4],[0,1/2,1/4]],16),lpf=linvar([800,2000],[24,8]),pan=[-2/3,2/3],amplify=2/4,amp=(1*var.brk1)+(1*var.bldup1)+(1*var.brk2)+(var.bldup2))

s5 >> nylon(notes,oct=4,dur=PRand([PDur(3,5),1,2,4],1),amplify=2/4,amp=(1*var.drop1)+(1*var.drop2))

s6 >> nylon(chords,oct=PRand([5,6]),dur=PRand([1/2,1,2],1/2),pan=[-2/3,2/3],amplify=2/6,amp=(1*var.drop1)+(1*var.drop2))

s7 >> pulse(note,oct=6,dur=1/2,sus=1/8,echo=PRand([0,1/4,1/2,1],1),room=2/3,mix=1/2,amplify=2/5,amp=(1*var.drop1)+(1*var.drop2))


# There is no difference, but to have 2 makes it easier to work a dynamic for one instrument, while implementing
#this dynamic into the whole composition

# that will be but if you do on of them 1/2 your will have half. I use amp for on/off 0 and 1, while tuning
# the instrument volume with amplify

# Stopp and start over

# practically, what is the difference between amplify=[1, 0] and amp=[1, 0] ?


var.intro = var([1,0,0,0,0,0,0,0],[128,64,64,128,64,64,128,128])
var.brk1 = var([0,1,0,0,0,0,0,0],[128,64,64,128,64,64,128,128])
var.bldup1 = var([0,0,1,0,0,0,0,0],[128,64,64,128,64,64,128,128])
var.drop1 = var([0,0,0,1,0,0,0,0],[128,64,64,128,64,64,128,128])
var.brk2 = var([0,0,0,0,1,0,0,0],[128,64,64,128,64,64,128,128])
var.bldup2 = var([0,0,0,0,0,1,0,0],[128,64,64,128,64,64,128,128])
var.drop2 = var([0,0,0,0,0,0,1,0],[128,64,64,128,64,64,128,128])
var.outro = var([0,0,0,0,0,0,0,1],[128,64,64,128,64,64,128,128])

print(SynthDefs)


