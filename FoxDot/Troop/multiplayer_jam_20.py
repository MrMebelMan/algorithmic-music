Clock.bpm = 133

print(SynthDefs)

print(Samples)

print(Attributes)

Scale.default = 'minor'

var.brk = var([1, 0], [[31, 28, 32, 31], [1, 4, 0, 1]])

sw >> swell(dur=0.25,
    hpf=[[var([400, 200, 100, 800], [[64, 128], [32, 64]]), 300, 200], 250, [200, 150]],
    hpr=0.25,
    lpf=[[150, 200], 250, [300, 350, 400, 450]],
    formant=[0.45, 0, [0, 0.25], [0, 0.3, 0, 0]],    
    amp=1 * var.brk
)


#  I GGOTTA LEAVE
#YOU TOO <3
#ALRIGHT

h1 >> play(':', room=1, mix=0.25, dur=var([8, 1], [[256, 128], [128, 64]]), delay=0.5, amp=0.75)
h2 >> play('-', sample=2, rate=0.98, dur=0.25, amp=expvar([1, 0], 1/3) * var([1, 0], [[128, 64, 32], [64, 32, [128, 32]]]))


@next_bar
def stop_all():
    Group(mb, bd, sb, rb, e1, e7, e5).stop()
    Group(tm, bs, rs, ns).stop()


mb >> play('V', dur=0.25, lpf=P[[500, 400, 300], 250, 100, [50, 500]], amp=P[1, 0.75, 0.5, 0.25] * 1)

e1 >> play("X", dur=[1, 1, [1, [0.5, 0.25]], [1, [0.5, 0.75]]], lpf=6500, hpr=0.25, amp=linvar([0.4, 0.8], 8) * var.brk)

bd >> play('X', dur=1, sample=2, lpf=500, lpr=0.5, amp=var([1, 0], [[256, 128], [64, 32]]) * var.brk)
sb >> play('X', dur=1, delay=0.5, lpf=200, lpr=0.75, amp=P[0.5, 0, 0, 0] * var.brk * bd.amp)
rb >> play('X', sample=2, rate=-1, dur=1, amp=var([0, 1], [[31, 31, 31, 63], 1]))
sh >> play('s', dur=0.25,
    lpf=P[var([1000, 2500, 3500], [64, 32, 32, 32]), 2000, 1250, [PWhite(1000, 3000), 3000]] * expvar([1, 2], 128), lpr=0.35,
    amp=expvar([1, 0], [[8, 16, 8], 0]) * var([1, 0], [[256, 128, 64], [128, 64, 32]])
)
tm >> play('m', dur=0.25, lpf=4050, amp=P[0, [0.25, 0.75], [1, 0.5], 0] * var.brk * var([0, 1], [[256, 64], [128, 32]]))
ns >> play('n', pan=PWhite(-0.75, 0.75), sample=[0, 1, 3, 2, [0, 1], [1, 2, 0]], drive=var([0.15, 0.25, 0.5, 0.65], 64), dur=0.25, amp=var([1, 0], [[512, 256, 128], [128, 64, 32]]) * expvar([1, 0.15, 1, 0], 1/3))
rs >> play('I', room=1, mix=0.15, dur=2, amp=var([0, 3.5], [[256, 64, 32], [128, 64, 128]]))

Master().hpf = var([0, 400, 500, 650, 800], [56, 2, 2, 2, 2])
Master().hpf = 1150
Master().hpf = 0
Master().hpr = 0.25

Group(bd,rb,tm,rs,e4, e5,e7, e3).solo(0)

@nextBar
def update_to_techno():
    Clock.bpm -=4
    Scale.default = "minor"
    Root.default = 4 

# cool thank. later!

e5 >> play("x---[h--]m {x }", dur=0.5, amp=0.2 * var.brk* var([4,0]) ).every(16,"amen")

e6 >> feel(amp=expvar([1,2],8) * var.brk ,tremolo =3 , lpf = e3.lpf, rate=2 , cut=2, chop=1, dur= 0.25).stop()

e7 >> play("V", lpf=1800, lpr=0.5, amp=1 * var.brk, dur=4, delay= 0.5, rate=4)


print(sorted(Attributes))


Master().lpf = linvar([0,3000],[28,4])

Master().lpf = 0





