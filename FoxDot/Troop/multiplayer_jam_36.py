# hexadecinal bpm? :P

Clock.bpm = 133

print(Clock.bpm)

p1 >> play('[m|t2|]', dur=0.25, lpf=expvar([2000, 5000], [128, 0]), amp=P[[1, 0.75], [0.5, 0.5]] * var([0, 1], [64, 32, 128, 64, 64, 128, 64]))
p2 >> play('mv^', sample=1, dur=1, amp=var([1, 0], [[128, 64, 256], [64, 32, 128]]))
p3 >> play('Hn', sample=1, lpf=expvar([2000, 5000], [128, 0]), dur=8, delay=0.5, amp=var([0, 0.2], 128))

sn >> play('I.v.', dur=2, delay=1, amp=var([0, 1], [[128, 64], [64, 32]]))
kd >> play('Xx', sample=1, dur=1, amp=P[1, 0.85] * expvar([0, 1], 512))

k1 >> play("V.O.", lpf=500, lpr=0.5, amp=var([0, 1], [[256, 128], [128, 64]]) * 0.05)

b1 >> sawbass(
    [var([2, 0, -1, -2], [[16, 32], [8, 16]]),var([0, 1, 2], 8),var([1, 0]),[var([0, 1, -1], [64, 32]), 2]],
    dur=PDur(4,8),
    sus=2,
    chop=2, shape=[[var([.25, 0], [64, [128, 64]]), 0], var([0, 0.15], [8, 4]), 0, [0, var([0, 0.15, 0.3], 128)]], 
    lpf=[500, 1250, 300], lpr=[expvar([0.5, 0.25], 32), 0.25, sinvar([0.15, 0.5], 64), [0.25, var([0.5, 0.25], [64, 32])], 0.75],
    amp=0.00
)

c1 >> play(".(...~)", amp=expvar([0, 1], 256))
