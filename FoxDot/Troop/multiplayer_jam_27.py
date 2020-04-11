Clock.bpm = 133
Scale.default = "minor"

print(Samples)

print(SynthDefs)

var.brk = var([1, 0], [[32, 31, 28, 56], [0, 1, 4, 8]])

s1 >> dbass(P[:8],oct=var([5,6],[6,2]),dur=PRand([1/2,PDur(3,5)],4),sus=1/4,formant=linvar([0,2],[6,2]),pan=PWhite(-2/3,2/3),amplify=PRand([0,1/3],4))


p1 >> play("-.--.--.", sample=5, pshift=var([0,2,4,0],[4,4,2,2]), lpf=P[[1000, 2500], 5000, 3500] * 1, amp=[[1, 0.8], 0.85, 1, 0.9], amp=var.brk)

k2 >> sawbass([0,2,4,0], dur=4, shape=.1, chop=1, hpf=linvar([400,1200],16), amp=var.brk)

c1 >> play("(Vv)(o.)O(.o-*)", sample=[1,2,3], amp=var([1, 0], [[128, 64, 256], [64, 32, 128]]))

p2 >> bug(dur=0.5,
    oct=6,
    drive=[0.15, 0.25, 0.25, [0.25, 0.3]],
    lpf=P[[500, 1500, 300, 700], 750, 1000, 1250] * 0.5,
    lpr=expvar([1, 0.5], [32, 64, 8, 8, 64, 128]),
    amp=P[0.75, [1, var([0, 1], 128)], 0.75, 0.5, [1, 0.25]] * var([0.15, 0], [[256, 128, 64], [128, 64, 32]])
)
tm >> play('m', dur=0.25, lpf=P[500, 750, 250, 400] * 0.75, amp=P[0, 0, var([0, 0.5], 64), var([0, 1], 64),  0.25, var([1, 0.5], 128), 0.75, var([0.5, 1], 128)] * 1.75 * var.brk) 
rs >> play('I', dur=var([4, 2, 1], [64, 128, 64]), room=1, mix=0.15, amp=P[1, [0.85, 0.75]] * expvar([0.15, 1], [128, 64, 128]))
su >> play('u', dur=rs.dur, delay=0.5, amp=P[0, 1, 0, 0,  0, [0, 1], 0, 0] * var([0.25, 0, 0.5], [64, 32]))
h1 >> play('-', sample=var([2, 1, 0], [128, 64, 32]), dur=1, room=0.75, mix=0.15, delay=0.5, amp=P[1.75, 1.5] * var([0, 1], [[64, 32], [[128, 32], [64, 128]]]))
ss >> play('S', sample=0, room=1, mix=0.2, dur=1, amp=var([0, 1], [128, 64, 32, 128, 256, 64, 32, 32]))

