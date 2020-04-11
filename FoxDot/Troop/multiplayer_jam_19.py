
# AFK 5 min 

Clock.bpm = 133

Scale.default = "minor"

print(Samples)

print(SynthDefs)

print(Attributes)

print(Scale.minor)


da >> play('O o Ooo', pan=PWhite(-0.75, 0.75), 
            lpf=PWhite(100,5000), amp=0.85,
            room=0.8, mix=PWhite(0,1))

di >> play('T tt', sample=[1,2,3,4], amp = 0.70, lpf=PWhite(500,1000),
           rate=linvar([1,4],8))

do >> play('dodo', dur=[1,2,2,2], echo = 2, echotime= 0.25, rate=[1,-0.5],
            lpf = PWhite(200,5000), lpr = [0.8, 1])

# AFK for 10 mins

ra >> play('([X [sd] ][X ])', dur=2)

ru >> play('raph', dur=[2,2,1,1,4])

ri >> play('glass of wine', sample=[[0, 2, 2, 3], 1, [0, 1, 2, 3], var([0, 1, 2, 3], 8)], rate=[0.5,1, 1], dur=0.25, lpf=PWhite(2000, 5000), amp = [0.2, 0.4, 0.5, 0.7, 0.8]).stop()

vu >> play('m', sample=[0,1,2,3], dur=var([2,4], 8))

da >> play('')


# There are multiple timevars:
# var (square)
# linvar (linear)
# sinvar (sine)
# expvar (exponential)
# var([1, 0], [8, 4]) will cycle between 1 and 0. 1 for 8 beats, 0 for 4 beats
# useful for turning the things on and off when using as amp=var([1, 0], ...)

# '|o2| will play the 'o' sample number 2
# '(Xo)T' will play XT, oT, XT, oT ....
# '[--]' will play the - sample twice

p2 >> play('X ', amp=var([1, 0], [64, 32]))

var.brk = var([1, 0], [[31, [28, 56], 31, 28, [32, 56], [32, 31]], [1, [4, 8], 1, 4, [0, 8], [0, 1]]])
dd >> play('d', sample=[0, var([0, 1], [[128, 256], [64, 128]]), var([0, 1], [[512, 256], [128, 64]]), 0], dur=[0.5, 0.25, 0.25], lpf=[PWhite(500, 2500), 3000, 1500, 2500], amp=var([1.5, 0], [[512, 256, 256], [128, 64, 64]]))
h1 >> play('-', dur=1, delay=0.5, amp=var([1.85, 0], [[128, 64], [64, 32]]) * var.brk)
h2 >> play('-', room=1, mix=0.25, dur=0.25, sample=2, lpf=[PWhite(1000, 3500), PWhite(2000, 5000)], amp=var([0, 1], [64, 128, 32, 32, 128]) * expvar([1.5, 0], 1/3) * var.brk)
pd >> pads([0, 1, -1, -1], dur=[8, 8, 16], tremolo=2, amp=0.85)
tw >> twang(0, dur=[0.5, 0.25, 0.25], sus=0.25, lpf=[[1500, PWhite(500, 1250)], [1000, 1250, 950, 700], [1750, 800, 1200]], lpr=0.25, amp=1)
sb >> sawbass(
    [var([0, -1, -2, 4, 3], 32), 1, var([2, 0, 1, -1, -2], [16, 8]), 1, 4, 3, 0, 1],
    dur=0.5, lpf=[400, [200, 300, 800], 500, 350], amp=0
)
rs >> play('I', sample=1, room=1, mix=0.25, dur=2, amp=var([2, 0], [[64, 128], [32, 64]]) * var.brk)
fh >> play(':', dur=0.25, lpf=1500, lpr=0.25, amp=var([1.5, 0], [[256, 128], [64, 32]]) * var.brk)
bd >> play('V', sample=var([0, 1, 2], [128, 128, 64]), dur=1, lpf=var([500, 750, 600, 450, 800], [32, 8, 8, 64, 32, 32]), amp=var([0.85, 0], [[512, 256], [64, 32]]) * var.brk)
sb >> play('V', sample=bd.sample, dur=1, delay=0.5, lpf=300,
    amp=P[
        var([1, 0], [[256, [128, 64, 32]], [128, 64, 32]]), var([0, 1], [[64, 128], [32, [8, 16], [8, 16]]]), 0, var([0, 1], [[16, 8], [8, 4]]),
        var([1, 0], 512), var([0, 1], [64, 32, 32, 16, 8, 8]), var([0, 1], 128), var([0, 1], [[64, [32, 64, 128]]])
    ] * var([0.5, 0], [[256, 128], [64, 32]]) * bd.amp
)
rr >> play('!', room=1, mix=0.5, sample=1, dur=8, amp=0.15)
rv >> rave(-2, dur=0.25, sus=1, drive=0.05, hpf=expvar([2000, 3000], 8), hpr=0.25, amp=P[1, [0, 0.85], 1, 1] * var([0.45, 0], [512, 256]) * var.brk)
kk >> play('X', sample=1, dur=1, lpf=500, amp=var([0, 1], [[256, 128, 64, 64], [[128, 64], 128]]) * var.brk) 
bp >> blip(var([-2, [0, 1, 2], -1, -2.5], [64, 32, 32, 16, 16, 8, 8, 8, 8]), dur=1, sus=2, delay=0.5, tremolo=2, amp=var([0.75, 0], [[256, 128], [64, [32, 64]]]))

Group(bd, sb, kk).stop()

# StageLimiter.activate(2)
# execute this ^ in the supercollider console to enable sidechaining

