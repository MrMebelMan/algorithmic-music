Clock.bpm = 170

print(Samples)

print(SynthDefs)

print(Attributes)

e1 >> jbass(0, chop=var([16,32],16),lpf = 2000,amp=.5 * var.brk)
#fellas, i'm gonna go & sleep,it's 1 am in here, thanks for the best music!
# hooorayy

# got sound, Eylem?

note = PRand(Scale.minor)

# I got it to work!!!!

b1 >> play("@",rate=linvar([1,2],[2,4,8,1]),sample=1,formant=expvar([0,5],PRand(16)),amplify=expvar([0,1],[2,4,8,0,1]))

b2 >> play("<[ss].......><->",sample=3,amplify=2, echo=0.2).every(16,"stutter",2)

b3 >> play(".......\\",dur=8,sample=2,formant=2,room=1,mix=1/2,amplify=2/3)

s1 >> dirt([0,2,4,7,1],dur=var([PDur(3,5),1/4],PRand([1,2,4])),sus=1/8,room=3/4,mix=1/2,formant=linvar([0,7],PRand(7)),amplify=3/4)

s2 >> charm(s1.degree,oct=6,dur=PDur(3,5),sus=1/2,coarse=0,room=3/4,mix=1/2,hpf=800,formant=var([2,3,2,4],16),pan=[-2/3,2/3],amplify=1/5,amp=1)

s3 >> dbass((s1.degree,PRand(Scale.default)),oct=4,dur=8,chop=2,pan=(-2/3,2/3),amplify=2/5)

s4 >> arpy(note,oct=6,dur=PRand([1/4,1/2,1]),echo=6/5,formant=linvar([0,5],PRand([8,16,32,64])),amplify=Pvar([0,3/5],[32,64,128,256]))




print(Master().lpf)

# I don't get why Master().lpf values are changing

print(Master().hpf)

# I guess I should connect to the speakers instead of headphones
# in headphones it sounds ok

# :D

# I'm not alone, unfortunately

# there are some normies who wouldn't understand :D



Master().hpf = expvar([[125, 80], [180, 120], [800, 600]], [32, [32, 32, 64], 0])

Master().hpf = 0

Master().hpr = 0.5

Master().lpf = 0

Master().lpr = 0.5


nn >> play('n',
    rate=var([1, -1], [32, 64, 128, 8, 8, 4, 2, 2, 8]),
    sample=[[1, 0], 0, [2, 1, 1, 3]],
    dur=[0.5, 0.25, 0.25],
    amp=var([1, 0], [28, 4]) * expvar([0, 1], 128)
)
sh >> play('s', sample=1, dur=0.25, amp=expvar([2, 0], [4, 8]) * var([1, 0], [[64, 128], [32, 64]]))

ph >> play('y', sample=var([2, 3], [16, 8, 4, 4]), dur=var([2, 1], [64, 32]), amp=var([1, 0], [[128, 32, 8, 8], [64, 16, 32]]))
tb >> play('p', room=1, mix=expvar([0.1, 0.25], [64, 0]), dur=[1] * 7 + [0.5, 0.5], amp=var([0.75, 0], [[28, 64], [4, 32]]))
ml >> play('r', sample=[[0, 1], [0, 0, 1]], dur=[1/4, 1/8, 1/8], amp=P[0.55, 0.25, [0.75, 0.5]] * var([1, 0], [[31, 64], [1, [32, 64]]]))

bl >> blip(dur=1, lpf=500, amp=1)
bp >> blip(dur=1, delay=0.5, lpf=300, amp=[1, 0, 0])

# AFK 5 min

# AFK, distra



@next_bar
def off():
    Group(nn, sh, ph, tb, ml).stop()

var.brk = var([1, 0], [[31, 28, 31, 56], [1, 4, 1, 8]])

bd >> play('X', sample=1, dur=var([8, 4, 2, 1], [128, 64, 64, [128, 256]]), hpf=150, hpr=0.25, amp=0.75 * var.brk)
sb >> play('X', sample=1, dur=var([8, 4, 2, 1], [128, 64, 64, [128, 256]]), delay=0.5,
    amp=P[0, var([1, 0], [128, 64]), 0, var([1, 0], [8, 16, 32, 32]),  0, 1, 0, 0] * 0.5 * var.brk
)
kk >> play('X', sample=1, dur=1, delay=0.75, amp=P[0.5, 0] * bd.amp)

rs >> play('I', dur=[2] * 16 + [1] * 7 + [0.5, 0.5], amp=1.25)
sr >> play('o', dur=0.25, amp=P[[0.25, PWhite(0.3, 0.8)], [PWhite(0.5, 1), 0.75]] * var([0, 1], [[31, 28, 31, 56], [1, 4, 1, 8]]))
cl >> play('*', dur=var([4, 2], 64), delay=0.75, amp=1)
h1 >> play(':', sample=2, dur=1, delay=0.5, amp=var([1.25, 0], [[64, 128], [32, 64]]))

@next_bar
def off_bass():
    Group(bd, sb, kk, h1, cl).stop()

print(SynthDefs)


n0 >> play('!', amp=expvar([0,1],[[256,128],0,0,0])*var.brk, rate=expvar([0,2],[[256,128],0,0,0]), echo=0.25, room=expvar([0,1],[[256,128],0,0,0])).every(1, 'stutter').stop()

#^^^^:D

o0 >> play('V', dur=PDur(var([3,5],8),16), pan=0, amp=var.brk * expvar([0, 0, 1], [64, 128, 0]), sample=var([0, 1, 2],16), lpf=var([200,600],32), lpr=0.5, delay=6/5, coarse=0.75).offbeat().every(8, 'stutter')

# thanks
print(o0.pan)

# I think bass should be mono, panning doesn't sound very well
# but that's just me

#

od >> play('[- -]', drive=0.25, amp=var.brk*PWhite, spin=linvar([0,128],[[256,128],64,0,0]),rate=expvar([0,2],[[256,128],0,0,0]), echo=expvar([0,0.09],[[256,128],0,0,0])).every(2, 'stutter')

le >> play('.XE', dur=var.brk, amp=0.25*var.brk, lpf=300, lpr=0.25).offbeat()

xe >> sinepad(PStrum(var([2,0],[128,32])), amp=expvar([0,1],[[256,128],0,0,0])*var.brk, rate=var.rt*var.brk, dur=1/2, amplify=2, coarse=6/7, sus=1/7, drive=1, hpf=1500)

# only we two left, lol?

# kek

# fuuuuu

# I need more AFK time
# hopefully 2-3 mins

# sure, we can

# :thumbsup:

# multiply amp with my var.brk for synchronised breaks!

# are you going to save everything?

var.rt=expvar([0,2],[[256,128],0,0,0])

# I am getting "Buffer UGen channel mismatch: expected 1, yet buffer has 2 channels", how do i fix this in SC?
# it's ok


# Cool
