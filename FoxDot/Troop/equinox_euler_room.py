Clock.bpm=var([133,250],[512,inf], start=now)

Clock.bpm=200


var.brk = var([1, 0], [31, 1, 28, 4, [56, 32, 56, ], [8, 0]])
var.bassl = var([0,2,0,-2,0,2,0,7])

note=PRand(Scale.default)

gS=Group(s1,s2,s3,s4,s5,s6).stop()

s1 >> blip(var.bassl,oct=6,dur=1/4,echoshape=1/3,drive=1/8,lpf=linvar([300,2000],16),amplify=2,amp=1*var.brk)



var.d = [1] * int(var([7, 15, 3], [64, 64, 32])) + [[0.5, 0.5, 0.25], [0.5, 0.5, 0.75]]

bd >> play('V', sample=2, dur=1, lpf=P[1500, 500] * 6, lpr=0.25, amp=P[1, [[0.95, 0.85], 0.75]]).stop()
od >> play('V', dur=var.d, rate=1.25, drive=0.25, lpf=0, hpf=120, hpr=0.25, amp=P[1, 1] * 5)
kd >> play('X', sample=1, dur=var.d, amp=[1, 0.9])
h1 >> play('-', sample=2, dur=1, delay=0.5, amp=var([1, 0], [[64, 32, 128], [32, 32, 64]]))
sn >> play('O', dur=0.25, amp=P[[1, 0, 0, 0.25], 0.85, [0.5, 0, 0.25, 0], [0.25, 0, [0, 0.5], [0, 0.75]], [0.85, 0.5, 0.75, 1]] * var([0.5, 0], 128))
rc >> play('~', dur=0.5, amp=expvar([0, 0, 1], [32, 64, 0]))



op >> play('T[mm]', 
    amp=linvar([0,0.5],)*var.brk, 
    room=linvar([0,10],32), 
    mix=0.2, 
    echo=0.02, 
    echotime=4, 
    dur=P[8, 4, 2]).every(16, 'stutter', 2, lpf=1200, lpr=0.35).every(16, 'alt', '*[mm]')
    

fade=var([1,0],[64,inf],start=now)

xx >> sawbass(P[0,2,4,6,8,1]-4
    , dur=7, chop=18, room=0.6
    , lpf=4000, echo=1
    , amp=1
    ).every(16,'mirror')

xy >> space(P[0,0,4,5,9]+3
    , dur=[3,5,4,6,2], chop=7, echo=0.2
    , room=0.8, sus=4, lpf=var(8000,2000)
    , amp=1
    ).every(8,'stutter').every(16,'mirror')

xz >>play("XXvvoooovvwer  VMM-- --   mm    "
    , pan=PSine(5)
    , lpf=var([1000,2000],32)
    , amp=1, chop=P[6,8,12,17,23]
    ).every(16,'stutter').every(32,'mirror')

sb >> sawbass(
    dur=0.25,
    hpf=P[200, 500, [850, 2000], [300, 1500], var([300, 280, 250, 230, 220], [64, 32]), var([500, 250, 200, 700], 8), [250, 200, 180],  [[500, 300, 200], var([200, 500, 300, 800], 16), 210, 220]] * 0.5,
    hpr=expvar([0.5, 0.25], [16, 32, 32, 8]),
    lpf=2500, lpr=0.15,
    drive=P[[0, 0.05], 0.03, 0.02, var([0, 0.05], [[128, 64], [64, 128]]),  [var([0, 0.05], 128), var([0.03, 0.15], [128, 64, 32])], 0, 0, 0] * 0,
    amp=P[1, 0.85, [0.9, 0.3], 0.5] * 0
)

sh >> play('s',
    pan=PWhite(-0.75, 0.75),
    dur=0.25,
    amp=[[1, 0.75], 0.5, 0.25, 1] *  var([0, 1], [[64, 32, 128], [128, 64, 256]]) # * expvar([1, 0.15], [[4, 16], [8, 0]]) * 1
)

tt >> play('t', dur=0.25, lpf=[[1500, 1000], 2000, 1350], lpr=0.25, amp=P[[0.25, 0.75, 0.25, 0.5], 0, 0, 0, 0.25, 0.5, 0.75, 1] * 0)

rs >> play('I', dur=var([8, 4, 2, 1, 2], 64), room=1, mix=0.15, amp=expvar([0, 0, 1, 1], [[32, 64], 32, [64, 128], 0]))


kd >> play('X', dur=1, sample=var([1, 2], [128, 256]), lpf=250, amp=[1, 1, 1, 1] * var([1.1, 0], [[256, 128, 64], [128, 64, 32]]) * var.brk)
h1 >> play('-', dur=1, delay=0.5, sample=2, amp=var([1, 0], [[64, 32, 128], [32, 64]]) * kd.amp * var.brk)

cl >> play('*', dur=8, delay=0.5, amp=var([0.5, 0], [128, 64, 32, 32]))

bp >> blip(dur=1, delay=0.5, amp=P[1, 0, 0, 0] * expvar([0, 0.85], 128) * 0)
bd >> play('V', sample=1, dur=1, lpf=P[650, 610], lpr=0.25, amp=P[1, [0.95, 0.85]] * var.brk * 0)
rk >> play('X', sample=2, rate=-1, dur=1, amp=var([0, 1], [63, 1]))

@next_bar
def stahp():
    Group(rs, h1, cl, bp, bd, rk, sh, kd, rc).stop()
    Group(bd,od, kd, h1, sn, rc).stop()

p0 >> play('X', 
    pan=[-1,1], 
    amp=linvar([0.0,0.75],4), 
    dur=2, 
    echo=0.02, 
    echotime=4,
    spin=4,
    chop=4,
    sus=2,
    mix=0.2,
    room=linvar([0,1],8)*PWhite(0.2,4)).every(4, 'stutter', 3, lpf=1500, lpr=0.45).every(8, 'alt', '*')

s0 >> sinepad(var.bassl, lpf=expvar([0,1],24)*var([1500,2500],16)*expvar([1,0],24), amp=linvar([1.5,0.25], 64)*var.brk, pan=[-1, 1], dur=1, echo=0.02, mix=0.25, sus=4)

lol hap
####################

print(SynthDefs)

print(Samples)

print(Attributes)

Server.add_forward("localhost", 12345)


