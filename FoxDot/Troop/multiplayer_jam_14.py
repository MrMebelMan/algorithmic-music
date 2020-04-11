Clock.bpm = 180

print(SynthDefs)

print(Samples)

print(Attributes)

###############################


# that's just variable definition, for some reason you should put .var in front of it, so the changes are applied to all the playes that use it

# :D thanks

# but the break that you created was dope af

var.brk = var([1,0], [[31, 28],[1, 4]])

sh >> play('s', dur=[1] * 7 + [0.5, 0.5] + [0.25] * 4 + [0.25, 0.75, 0.5, 0.5], amp=var([1, 0], [[64, 128], [32, 64]]))
ab >> play('(qt)kk', dur=0.5, rate=[-1, 1, 0.85, 0.75], room=[1, 0], mix=0.25, bend=[-0.25, 0], amp=0.25)
fl >> feel(dur=8, sus=9, tremolo=4, amp=2.5)

bb >> play('X', dur=[2, [0.5, 1], 0.25, 0.75, [1, 2]], amp=0.85 * var.brk * var([1, 0], [[64, 128], [128, 64, 256]]))

h1 >> play('~', dur=0.5, amp=expvar([0, 1], [64, 0]) * var.brk)
rs >> play('I.oo[td].vu', rate=[1, 0.95, [1.1, 1]], dur=0.25, amp=0.85 * var.brk)

bd >> play('V', sample=1, dur=1, amp=1 * var.brk)
sb >> play('V', sample=1, dur=1, delay=0.5, amp=P[1, [0, var([0, 1], [[128, 64], [64, 32]])], [0, 0, 0, 1], 0] * var.brk * var([1, 0], [[64, 128, 256], [32, 64, 128]]))

cl >> play('*', dur=1, delay=0.75, amp=1.5 * var.brk)
h2 >> play(':', dur=1, delay=0.5, amp=1.5 * var.brk)
sn >> play('O', dur=[2] * 15 + [0.5, 0.5], amp=0.3 * var.brk)

# nice <3

# thanks!

@next_bar
def stop():
    Group(cl, h2, sn).stop()
    Group(sh, bb, h1).stop()
    Group(rs, cl).stop()
    Group(sb, ex).stop()
    Group(bd, l3, od).stop()

n0 >> play('h', dur=PDur(var(5,8),8), echo=0.02, lpf=sinvar([2000,3000],[2/3,8]),lpr=0.25, amp=sinvar([0.25,0.45],[[255,127],0,0,0,0]) * var.brk* linvar([1,0],64), pan=[-1,1]).every(4, 'stutter', spin=64)

od >> play('z', dur=PDur(3,8), bend=-1, shape=[0.15, [0.25, 0.1]], rate=expvar([0,2],[[255,127],0,0,0,0]), lpf=expvar([150, 800], [1/3, 4]), amp=expvar([1,0],[[255,127],0,0,0,0]) * var.brk*linvar([1,0],128))

l3 >> play('T', dur=PDur(1,3), amp=linvar([1,0],16), room=sinvar([0,1],[[255,64],1,4])).every(2, 'stutter', 3, hpr=0.25).stop()

ex >> play('V', dur=PDur(var([3,5],8),16), amp=var([0, 0.35], [[64, 128], [128, 64, 32, 256]]) *var.brk*linvar([1,0],32), lpf=var([300,800],8)*linvar([1,0],32), lpr=0.25).every(2, 'stutter',sample=[-1,1]).stop()

e3 >>

#


# dayum, forgot to record

# lemme start over

# AHHH

# sounds nice, right?

# I think we should be using moar breaks

# less is more sometimes

# wall of sound is great too, but breaks make it spicey
