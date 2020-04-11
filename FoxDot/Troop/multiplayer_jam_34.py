Clock.clear()
Clock.reset()

Clock.set_time(1024)

# drop material:
# n0 >> noise(note, amp=linvar([0.35,0],32) * var.brk, hpf=300, lpf=1500, lpr=0.35, hpr=0.45, shape=0, bend=-1, echo=0, chop=4, sus=2).every(32, 'stutter')
# or this?
#
Clock.bpm = 137

var.brk = var([1, 0], [31, 1, 28, 4])

def chill():
    jb >> jbass(dur=PDur(3, 8), oct=5, hpf=var([180, 150, 125, 100], [32, 32, 64, [64, 128]]), hpr=0.4, amp=P[[1, [2, 0.5]], 2] * expvar([0.15, 1, 1], [128, 128, 0]))
    kd >> play('X', sample=var([1, 2, 1, 0], 128), dur=1, lpf=600, lpr=1.1, amp=P[1.5, var([1.25, 1.5], [64, 128, 64, 64])] * var.brk)
    sb >> sawbass(bend=3.5, benddelay=var([0, 0.25, 0.5, 0.75], 32), dur=[0.25, 0.25, 0.5], drive=0, delay=0, amp=P[0.25, [0.85, 1]] * var([1, 0], [128, [64, 128]]))
    dd >> play('D', lpf=expvar([400, 900], [128, 0]), dur=[1] * 7 + [0.5, 0.5], amp=var([1.25, 0], [[128, 64], 32]))
    db >> play('V', sample=var([1, 2], [128, 256]), bend=-0.25, benddelay=[0.15, 0.25], lpf=400, dur=1, amp=P[1, 0.85] * var([1, 0], [[64, 64, 128], [128, 256]]))
    s2 >> play('v', sample=1, dur=0.25, amp=P[0, 1, var([0, 0.75], 128), 0] * 1 * db.amp)
    sh >> play('s', room=1, bend=[-0.5, -0.25], benddelay=0.25, mix=0.15, dur=1, delay=0.5, amp=var([0, 1], [[64, [32, 64]], [128, 64]]))
    hh >> play('t', sample=2, dur=0.25, amp=expvar([0.25, 1], 1/3) * sh.amp * expvar([0, 0, 1, 1], [32, [32, 64], [64, 128], 0]))
    cl >> play('H', room=1, mix=0.25, dur=var([16, 8, 4, 2, 1], 64), delay=0.5, amp=0.35)
    rs >> play('I', sample=1, dur=1, lpf=var([1150, 1000, 950], 128), amp=var([0, 1], [[32, 64, 128], [64, 128, 256]]))
    ki >> play('x', dur=1, delay=0.5, amp=P[1, [0.75, 0.25]] * expvar([0, 1.5], [128, 64, 32, 64, 32]))
    Group(k3, b4, b5, bs, tt).stop()
    Clock.schedule(overdrive, Clock.now() + 128)

Group(db, dd, jb, sb, s2, rs, ki, cl, h2, jb, kd, sh).stop()

Group(jb, sb).stop()

Group(jb, sb, dd, s2, ki).stop()

#############

def overdrive():
    k3 >> play('V', rate=var([0.89, 0.88, 0.865, 0.85], 128), sample=var([2, 1], [[512, 256], [128, 256]]), dur=[0.5, 0.5, 1], hpf=P[40, 45], hpr=[var([0.15, 0.25], [[128, 64], [64, 128, 256]]), var([0.25, 0.15], [[[64, 32], [128, 256]], [32, 64]])], lpf=[250, 350], amp=P[0.85, 1] * 1)
    b4 >> play('V', sample=var([0, 2], [256, 128]), rate=0.9, lpf=80, lpr=0.18, bend=0.25, benddelay=[0.75, var([0.5, 0.75], 64)], dur=[1, 0.5, 0.5], amp=1.13)
    b5 >> play('V', sample=1, rate=1, dur=1, delay=0.5, lpf=P[350, 500], lpr=0.5, amp=P[var([1, 0], [128, [32, 64]]), 0.25] * var([1, 0], [31, 1, 28, 5, 56, 8]))
    bs >> dub(dur=0.25, sus=[[0.75, var([0.65, 0.75], 128)], 0.25], amp=P[[0.78, 1], [0.5, 0.75]] * expvar([0, 0.6], 256) * var([0.85, 0.25, 0.75, 0.35], [64, 128]), hpf=P[var([95, 110, 125], 64), 220] * var([0, 0.25], [128, 256]), hpr=var([0.75, 0.25], [[31, 28, 56], [1, 4, 8]]))
    tt >> play('D', dur=0.25, sample=0,
        rate=P[1, [0.85, 1, 1, 1], [1, 1.05], [1, 1, 0.95, 1]],
        lpf=expvar([1200, 900], [[128, 64], 0]), lpr=0.35,
        amp=P[
            [0.75, 0.25], [0, var([0, 0.85], 32)], var([0, 0.5], [64, 128]), [0, 0, 0, var([0, 0.75], [[128, 32, 64], [64, 16, 128]])],
            0.75, 0.25, 0.5, [1, var([0, 1], [[128, 32], [256, 64]])]
        ] * expvar([1, 0.75, 1, 0], 256) # * var([1, 0, 1], [32, 64, [32, 64, 128], 16, 8, 2, 8, 2, 4, 128, 64])
    )
    Group(jb, sb, dd, s2, sh, hh, kd).stop()
    Clock.schedule(chill, Clock.now() + 32)

print(SynthDefs)

print(Samples)

print(Attributes)

h2 >> play('-', sample=2, room=1, mix=0.15, lpf=4500, lpr=0.25, dur=1, delay=0.5, amp=var([0, 1], [128, [64, 128]]))


overdrive()

chill()


s0 >> sinepad(amp=sinvar([0.25,0.75],[4,24]), 
    lpf=var([1500,800,0,0,0,800],[4,16,4,4]), 
    lpr=[0.45,0.35,0.25,0.25,0.25,0.25,0.45], 
    spin=4, 
    pan=[-1,1], 
    echo=linvar([0,0.35],4), 
    mix=0.2, 
    echotime=2, 
    room=0.75).every([4,32], 'stutter', var([3,2],1), mix=0.2, amp=0.5, room=expvar([0,1],[16,32])).stop() # this has one of the high pitched sounds, from the stutter
    
cb >> play('T[mm]', amp=linvar([0.5,0],16)*var.brk, dur=4, echo=0.02, drive=0.5, shape=P[0.25, 0.02]).every(4, 'alt', '*').stop() # this is the other from the echo=0.02

n0 >> noise(note, amp=linvar([0.35,0],32) * var.brk, hpf=300, lpf=2500, lpr=0.35, hpr=0.45, shape=0, bend=-1, echo=0, chop=4, sus=2, coarse=8, dur=4).every(32, 'stutter')



dl >> play('-', amp=0, dur=2)


# that was noise lol I hav ethe amp set 

# :O
# :D

# add more sample playerss!!

# something fast and high-pitched!

 #WOAH THAT'S GOOD
 

# GREAT FOR DROPS!


print(PZip([0,-1,0,1],[0,2]))

note=PZip([0,-1,0,1],[0,2])

s1 >> bell(note,oct=4,dur=PDur(3,5),sus=1/4,shape=2/3,bend=1,lpf=var([300,800]),pan=PWhite(-1,1),amplify=2/5,amp=[0.15, 0.1])

s2 >> rave(note,oct=6,dur=var([PDur(5,8),PDur(3,5)],[24,8]),sus=1/6,echo=1/2,formant=1,lpf=expvar([500,1600],[16,8,32,12,4,8]),amplify=2/5,amp=1*var.brk)

s3 >> 

#lol I accidently die sus to 


# Music Label?


