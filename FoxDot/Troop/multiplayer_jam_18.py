# AFK 5 min
# Oooonnneee gooooood spliiiiifffff!
# :D


Clock.bpm = 150 # }:D

Scale.default = "minor"

print(Samples)

print(SynthDefs)

print(Scale.minor)

note=Pvar([[0,1,2,1,4,3,0,1],[0,1,4,5,0,2,3,6]],256)

s1 >> dub(note,oct=(4,5),dur=8,chop=PRand([4,8,16],[4,16,8]),drive=2/3,formant=PRand([1,3,5],PRand(8)),pan=linvar([-2/3,2/3],4),amplify=2/8)

s2 >> donk(note,dur=1/4,shape=linvar([1/3,3/4]),formant=1,lpf=expvar([300,1200],16),amplify=2/3)

s3 >> donk(note,oct=6,dur=1/4,shape=linvar([1/3,3/4]),formant=7,room=2/3,mix=1/2,amplify=2/6 * var.brk)

s4 >> space([0,1,0,3,0,5,0,2],oct=4,dur=1,sus=1/2,lpf=500formant=linvar([0,3],var([4,2,6])),amplify=2/3).offbeat()

b1 >> play("..o[.o]..o.",rate=linvar([1,3],var([4,16,8,2,32]),sample=-1,lpf=900,amplify=2/3 * var.brk)

# I think that's because of the nested var

b2 >> play("..i.",lpf=expvar([900,2000],16),amplify=2/3 * var.brk)

z4 >> sitar(note, oct=(3,[4,5]), dur=PDur(5,8,0,1), lpf=900).unison(3)



ra >> arpy(note,dur=[8, 8, 16], tremolo=2, amp=0.75)
kl >> klank(0, dur=var([8, 4, 2], [128, 64, [32, 64]]), oct=var([5, 4.9, 4.8, 4.7, 4.6], [64, 32, 32, [16, 8, 8]]), amp=0.35) #.stop()
fl >> pluck(var([-3, -2, 0], [64, 32, 32]), dur=1, delay=0.5, lpf=300, amp=2)
sh >> play('s',
    pan=PWhite(-0.5, 0.5),
    dur=[0.125,0.25,0.5,0.125,0.25],
    lpf=[PWhite(5000, 3000), [2500, PWhite(500, 1500)], [1800, 2000, 1000], [750, 500, 1250]],
    amp=expvar([1, 0], 16) * var([1, 0], [16, 32]) * 1.75
)


h1 >> play('-', sample=2, room=1.25, mix=0.3, dur=0.25, amp=expvar([1, 0], 4) * var([1, 0], [4, 12]))
ee >> play('e', room=1, mix=0.15, dur=0.25,
    lpf=[[300, 200, 800, 1200], [500, PWhite(500, 1500)], 750, [500, 700, 1000]],
    amp=P[1, 0.5, var([1, 0.25], [64, 32]), 1] * var([2.5, 0], [[128, 256], [64, 128]])
)

ee.stop()

rs >> play('I', dur=var([8, 4], [256, 128]), room=1, mix=0.5, amp=var([1, 0], [512, [64, 128, 256]]))
cb >> play('T', sample=var([0, 1], 128), rate=0.95, room=1, mix=0.45, dur=31, delay=0.75, amp=0.75)

var.brk = var([1, 0], [[256, 128, 64], [128, 64, 32]])

tm >> play('m', dur=1, lpf=var([500, 650, 800, 450], [16, [8, 8, 32, 32]]),
    amp=Pvar(
        [
            P[1.75],
            P[var([0, 1], 64), var([0, 1], 64), 0, 0,  1, 1, 0, 0]
        ], [256, 128]
    ) * 2 * var.brk
)
t2 >> play('m', dur=1, delay=0.5, lpf=300, amp=P[0, 1, 0, var([0, 1], [128, 128, 8, 8, 8, 8])] * var([1, 0], [[256, 64, 128], [128, 32, 64]]) * var.brk)
m2 >> play('r', sample=var([0, 1], [128, 64, 64, 64]), dur=[0.5, 0.25, 0.25], lpf=P[[500, 1250], [2000, 300, 500, 600], [300, PWhite(300, 1000)]] * 1, amp=3 * var.brk)

g1 >> growl(dur=[8,16,4], lpf=linvar([800,2000],24), oct=(linvar([3,3.5],128),4), pan=(-1,0,1), amp=0.5, rate=0.5).stop()

z3 >> play("M...", dur=4, rate=0.5)
z1 >> play("v..(...v)", dur=2, lpf=480, room=1, mix=linvar([0.7,0.5],[24,0]))
z2 >> dbass(note, dur=[6,2], lpf=400, sus=z2.dur, oct=(4,5), echo=[0.5,1,1.25], bend=PStep(4,2,0), hpf=40, benddelay=PWhite(0.5,0.8), amp=0.5) + var([0,PRand(-2,2)],[6,2])

