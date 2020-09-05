# By BBScar, KittyCLock, RanggaPurAji

Clock.bpm = 130

# lolololol

Clock.set_time(0)

# Love you guys, thanks and yes, later

# later guys, stay healthy, peace and love from Yogyakarta

# peace and love from Prague!



         .```.   _.''..
        ;     ```      ``'.
        :  o               `.
        / >,:                \
       /.'   `'.,             :
      /'         ;.   .       ;
     /          ;  \ ;     ; /
                `..;\:     :'
               __||   `...,'
              `-,  )   ||
               /.^/ ___||
                   '---,_\    APTERYX
                      (/ `\




# me too, i need some cig now

# guys thanks again, i learnt so much from this. Sure man, this is nice jam, you guys are awesome


# ev
eryone allright??? so sorryyyyyyyYyyyyyyyy i didnt know , dang it dang it

# that was something

# "end it gracefully"

# guys thanks so much, pardon that last boom

# thank you @KittyClock

# also sorry @BBScar, 

# <3

Scale.default = Scale.indian

scale = Scale.default
note = PRand(scale,seed=7)

bassline=[0,-2,0,3,1,5,7,-1]
bassline2=[0,0,1,7]
var.brks=var([1,0],[28,4,30,2,14,2,12,4])

s1 >> dub(bassline,oct=4,dur=2,sus=P[2, 1, 1, [0.5, 1]],formant=1,chop=2,pan=(-2/3,2/3),amplify=2/5,amp=1)

s2 >> sawbass(Pvar([bassline2,note],[8,4]),oct=4,dur=2,coarse=3,shape=linvar([0,1/3],[8,0]),pan=PSine(32),amplify=4/5,amp=1).offbeat()

s3 >> rave(Pvar([[0,1],[0,7],[0,3],[0,5]]),dur=1/4,sus=1/4,formant=expvar([0,4],[[4,0],[8,0],[16,0],[4,0],[28,0],[4,0]]),lpf=linvar([400,1200],[32,0]),pan=(-2/3,2/3),amplify=PRand([1/8,3/8],[16,8,12,4,8,32,28]),amp=1)

s4 >> bell(bassline2,oct=5,dur=var([8,8,8,PSum(7,2)],[8,8,4,4]),echo=1/2,room=3/4,mix=1/3,amplify=2/5,amp=1)

print(SynthDefs)

#haha, a pleasure Rangga, anytime

#Yes, you got us here....thanks...I missed the jams soo much

# anyway, I gotta go eat with my gf, thanks for the jam!

# Thank you too RanngaPurAji!!!!

# yes yes yes!!! slow down, and cool this down a bit

# yahoooo



# It was fun!

# let's try to end the music gracefully for the nice recording


# guys, thank you so much. this is the best jam so far, it's been awhile, I learnt something again hahahaha

b1 >> play("m",dur=PRand([1/2,1,2],[1/2,1,2,8,16]),delay=[0,1/2,0,1/4,0,0,1/2],sample=var([1,2,3],[2,4,8,2,12,8,4]),rate=PRand([2/3,1,2],var.brks),amplify=3/5*var.brks,amp=1)

b2 >> play("-",dur=[1, 0.5, [0.5, 1, 0.5, 0.5]], amplify=3/4*var.brks,amp=1) 

k1 >> play('x', sample=0, dur=P[2, 1, 1],
    rate=var([0.95, 1, 1.05, 0.98], [16, 8]),
    bend=var([-0.25, 0, 0.15, 0, 0.25, 0], 32),
    amp=P[
        [var([0.25, 1], 4), 0.5, 0.25, 0.75],
        expvar([0.15, 1], [32, 0]) * P[var([0.5, 0.25, 1, 0.75], 64), 0.25, 0.75, 0.75],
        [var([0.75, 0, 1, 0.5, 0.25, 0.35], [16, 8]), expvar([1, 0.5], [16, 0]), var([0.5, 0, 1, 1], 8), 1],
        expvar([0.15, 0.5], 2)
    ] * var([1, 0], [31, 1, 28, 4]) * var([1.25, 0], [256, 128])
) #.stop()

k1.amp=P[[1.25, 1], 0.15, [0.5, 0.25, 1, 0.5], [0.25, 0.5, 0.25, 0.75]]

h1 >> play('t', sample=P[var([0, 1], [64, 32, 64]), var([2, 0, 1], [16, 32, 32]), 1, 1], dur=0.25, lpf=expvar([0.5, 1.1], [128, 0]) * expvar([5000, [1500, 2500, 2000, 1000]], 1), lpr=0.25, amp=expvar([0.5, 1], 1) * var([0, 0.5], [32, 128, 32, 64, 64, 256]) * P[1, var([1, 0], [64, 32, 16, 16]), 1, 1, var([0, 1], 128), var([0, 1], [64, 128, 256]), 1, var([0, 1], 8)])

h2 >> play('-', sample=2, dur=8, delay=0.5, amp=var([0.5, 0], [32, 64, 32, 32, 128, 32, 128, 64]))

cl >> play('H', sample=1, dur=8, delay=1, amp=0.75 * sn.amp)
sn >> play('o', dur=8, amp=expvar([0, 0, 0.4], [[64, 128], 128, 0]))

kd >> play('v', rate=0.9, dur=4, sus=var([0.15, 0.05, 0.1], [64, 32]), lpf=expvar([800, 200], [32, 0]), lpr=0.25, amp=var([0.85, 0], [31, 1, 28, 4]) * 1).every(127, 'stutter', 2)
k2 >> play('X', rate=0.7, dur=8, sample=1, lpf=600, lpr=0.25, hpf=var([110, 80, 120, 90, 100, 70], [64, 128, 128]), hpr=0.25, amp=kd.amp).every(127, 'stutter', 2)

# hahahhah

Group(kd, cl, sn, h1, b2).stop()

sr >> play('I', dur=1, amp=P[[0.25, 1, 0.5, 0.75], PWhite(0.25, 1), P[1, PWhite(0.5, 1)], PWhite(0.25, 0.75)] * var([0, 1.25], [[28, 3, 7, 7, 56], [4, 1, 1, 1, 8]]))

rc >> play('~', dur=0.5, amp=P[[0.5, 0.75], 1] * expvar([0, 0, 1.25], [[128, 64], [128, 64], 0]))

cr >> play('null', dur=1, sample=P[var([1, 0, 2, 3], 32), [var([1, 0, 2], 8), 2, 0], [3, 0, 1], [2, 4, 6]], lpf=expvar([1000, 4000, 5000], [128, 64, 0]), amp=P[1, [0, 0.25, 0, 0.5], [0.75, 1], [0.25, 0.5, 0.25, 0.75]] * 0.75)

Group(cr, h2, h1, rc, k2).stop()

ss >> play('S', dur=0.5, lpf=expvar([3000, 8000], [128, 0]), amp=P[0.85, [0.25, 0.35, 0.25, 0.25]] * var([0, 1], [32, 64, 32, 32, 32, 128])).stop()

print(Samples)


r3 >> star(bassline,dur=4,amp=0.4,sus=[0.5,0.25,1],chop=[3,3,2,4],hpf=300, hpr=0.5, pan=[0,1,-1,0,0.5,-0.5], oct=[3,4,4,6,5]).stop()

r4 >> pluck(bassline,dur=4, delay= 0.25,amp=0.25,sus=[0.5,0.25,1],hpf=300, hpr=0.5, pan=[1,-1,0,0.5,-0.5], oct=[4,6,5]).every(32, 'stutter', 2).stop()

r5 >> bell(bassline,dur=8,amp=0.25,hpf=300,sus=[0.25,1,0.5], hpr=0.5, chop=[2,2,4], oct=[1], pan=[-1,1,0]).every(64, 'stutter', 2).stop()

r2 >> play('n',dur=PDur([3,3,5,3,4,6],[8,16]),amp=0.125,pan=[0,-0.5,0.5,1,-1],sample=0).every(32, 'stutter', 2)

r2.stop()

# yeahhhhh hahaha
