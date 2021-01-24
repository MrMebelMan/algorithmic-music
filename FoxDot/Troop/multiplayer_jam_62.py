# By KittyClock and Madman9

var.brk = var([1, 0], [[28, 31, 56], [4, 1, 8]]) * 1

# I multiply drum's amp with it, so it stops after 28, goes silent for 4 and then again loud
# same for 31, 1 and 56, 8


x2 >> play('x', sample=(0, 1), dur=[1] * 7 + [0.5, 0.5], amp=1.25 * var([1, 1, 0], 32) * var.brk).stop()

h1 >> play('-', echo=P[0.25, 0, 0, 0], sample=2, dur=1, delay=0.5, amp=var([0, 1], [32, 64, 64, 128, 64])).stop()

oo >> play('o', dur=var([8, 4, 2], [64, 128, 32, 32]), delay=P[0, var([0, 0.5], [128, 64])], amp=0.45).stop()
cl >> play('H', sample=1, dur=1, amp=P[0, 1] * 0.35 * var([1, 0], [64, 128, 128])).stop()

# now yes a little bit better 

# if it's not playable anymore, we can stop if you want

# I enjoy it -- just that my PC started becoming glitchy and the sound too. 

tt >> play('t', sample=[1, 0, var([2, 0], 8), [2, 0]], dur=0.25, lpf=2500, lpr=0.25, amp=P[1, 1, 0, var([0, 1], 8), PWhite(0.5, 1)] * 1).stop() # 0 to 

vv >> play('V', sample=2, sus=0.05, dur=P[0.5, 0.25, 0.25], lpf=expvar([500, 3000], [128, 0]), lpr=0.25, amp=expvar([0.15, 1], [1, 0]) * 1.35 * var.brk)

# well, foxdot is not good for drones, but there are some trick. Yes that goes from low to top playing on three notes for example. 

# I guess we can stop here for now

# continuous bass?

# I guess we should ask in the group about it, I'm not sure how to make it long and getting louder

# I think atk parameter is attack, so you can probably do a long attack, but I'm not sure if bass synth has it

# looks like jbass has, I think I got it

bk >> sawbass(dur=8, sus=8, atk=8, lpf=500, lpr=0.25, room=1, mix=0.2, amp=0.75)

# any idea  hot to create a continusly rasing bass sound ..that goes from 
xx >> play ('@', sample=[1,2], dur=4, amp=expvar([0, 1, 1], 64)).stop()

xz >> play(P["x-@%"].amen(), amp=0.5).every(4, "reverse").stop()

x3 >> play('X', sample=2, dur=1, amp=P[1, 0.5] * 1.25).stop()

bs >> bass(dur=0.25, sus=1,
    chop=var([4, 2], [28, 4]),
    hpf=P[expvar([800, 150], [32, 0]), 250, 600, var([400, 200], 2)],
    hpr=expvar([0.05, 0.25], [4, 0]), amp=1 * 0.15
)

cp >> play('H', room=PWhite(0.25, 1), mix=PWhite(0, 0.15), sample=2, dur=0.25,
    amp=var([1, 0], [3, 1, 2, 2, 4, 2, 5, 3, 3, 1, 3, 2]) * expvar([0.25, 1], [4, 8, 2, 4, 0]) * 0.5
)


dr >> play("x--@", dur=var([2, 0.25], [3, 1, 4, 2]), sample=[1,2,4])
dd >> play('~', dur=0.25, amp=expvar([0, 0, 1], [32, 32, 0])) # this will go silent for 32, then gradually go from 0 to 1 for 32, then drop to 0 immediately


