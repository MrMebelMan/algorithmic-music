Clock.bpm = 133 * 2


print(sorted(SynthDefs)) # <3

print(Samples)

print(sorted(Attributes))

print(Clock.bpm)
print(Scale.default)

Scale.default = 'chromatic'

var.chords = var([[1, 0.5], 4, var([3, 2, 1], 64)])
var.brk = var([1, 0], [31, 1, 28, 4, 56, 8, 31, 1, 32, 0, 32, 0, 31, 1])


a1 >> sitar(var.chords + [0, 2, 4, 6], dur=1/2, amp=1/2 * var.brk, fmod=5, lpf=linvar([0, 8000], 8))
b1 >> sawbass(var.chords, dur=4, amp=P[0.85, 0.75] * var.brk, tremolo=var([0, 2], [128, [64, 32]]), pan=linvar([-1, 0, 1], 8),crush=8) 

a2 >> blip(
    var.chords + PRand([-2, 0, 2, 4, 6]),
    dur=1/4,
    lpf=P[1250, 800, [400, 600, 900, 1200], [2000, 1500, 1000]],
    lpr=expvar([0.25, 0.5], 8),
    drive=P[[0, 0.25], 0, [0, 0.2], 0.45] * 0,
    amp=P[1, [0.5, 1], [1, 1, var([0, 1], 128), var([0, 1], [64, 32])], 1] * 1.25 *  var.brk
)


a3 >> play(
    "[zzZzZSSS]",
    pan=PWhite(-0.85, 0.85),
    sample=P[var([0, 2, 3, 1, 1], [64, 32, 16, 8, 8]), [0, var([2, 0, 1], 64), 2, 1], 0, [0, 1]].reverse(),
    hpf=expvar([[200, 500, 1000], 2000], [[128, 4, 8, 32, 64, 128], 0]),
    hpr=expvar([0.25, 1], 1/3),
    dur=[var([1, 0.5], 256), var([1, 0.5], 256), [0.5, 0.25], [0.5, 0.75]],
    amp=expvar([0, 1], [[64, [128, 32]], [128, 256]]),
    drive=[expvar([0, 0.5], 1/3), [0, 0.25], 0.2, 0.15],
    crush=var([0, 20], [16, 4, [4, 5, 6], 4, 16, 32]),
    lpf=P[
        var([5000, 3000, 500, 1250], [8, 8, 16, 16, 64, 46]),
        2500,
        1500,
        var([500, 1000, 1250, 1500], [64, 32, 32])
     ],
     lpr=expvar([0.25, 0.75], [[16, 32], [4, 8, 16, 32]]),
).rarely("stutter", int(var([8, 4, 2], [64, 32, 64, 32, 32]))).solo(0)


# the more you modify the sound variations, the better it sounds

# I'm not sure how bitcrush works tbh
# try it

# sure! Thanks for playing!
# Got to go


# wait, z was amazing, let's shape it

a4 >> play("|V2|u..", amp=0.75 * var.brk, sample=[var([0, 1, 2], [16, 32]), PRand(7)])

# feel free to change others' code and introduce your own sounds

# hangdrum?

sh >> play('s', dur=0.5, pan=PWhite(-0.85, 0.85), hpf=expvar([5000, 200], [128, 0]), hpr=0.25, amp=P[[PWhite(0.25, 1), 1], 0.85, 1, [1, 0.95]] * 3 * var.brk)

print(Clock)

e4.stop()

e3.stop()

####################################################


@next_bar:
def stop_some():
    Group(rs, sp, dk).stop()



Master().hpf = 250

Master().hpf = 0


rs >> play('I',
    pan=PWhite(-0.75, 0.75),
    room=1, mix=0.3,
    dur=1,
    lpf=7000, lpr=0.25,
    amp=P[[0.15, 0.2], [0.15, 0.1, 0.15, 0.15]] * expvar([0, 0, 10], [[32, 64, 32, 128], [128, 64, 32], 0])
)
sp >> sinepad(
    -0.5,
    dur=P[
        0.25, 0.25, 0.25, 0.25,
        0.25, 0.25, 0.25, 0.25
    ] * 2,
    lpf=P[
        [2000, 500], 750, 250, 1000,
        var([750, 1000, 1200], 32), 400, 300, 800,
    ],
    lpr=0.25,
    sus=[1, 0.5, 0.85, 0.25],
    drive=[var([0.05, 0.15], [128, 64, 32, 32, 64, 64]), var([0.05, 0.1], [64, 128]), 0.05, var([0.05, 0.08], [[128, 64], [64, 32]])],
    hpf=P[[100, 150], var([250, 300, 200], [16, 8, 8]), var([350, 300]), var([250, 300, 150], [64, 32])], hpr=P[0.5, 0.25, 0.75, 0.25],
    amp=P[[1, 0.75], 1, 1, [0.75, 1],  1, 1, 1, [1, 0.5]] * var([0.5, 0], 256) * var.brk
)
dk >> donk(dur=0.5, lpf=[1500, 500, 250, 750], amp=P[1, 0, 0.25, 0,  1, 0.5, 0, 0] * var([0, 1], [[64, 128, 256], [64, 128, 256, 32, 32]]) * var.brk)
sb >> sawbass(
    dur=0.25,
    oct=[5, 5.1, 5, [5, 4.8]],
    hpf=[500, 250, 850, [500, 300, 600, 250], [250, 1000], [1200, 800, 500, 1000]],
    hpr=0.25,
    bend=[0, -0.25, 0, [0, -0.15]],
    amp=P[1, [0, 1], [0.25, 1]] * expvar([2.85, 0.75], [[512, 256], [128, 64]])
)
h1 >> play('-', dur=0.25, lpf=P[[300, 500, 700], [150, 200, 300]] * 15, amp=P[1, 1, 0.5, 0.75] * var([1, 0], [[128, 256, 512], [64, 128]]))

kd >> play('X', dur=2, sample=1, lpf=2000, lpr=0.25, amp=1.5 * var.brk)
sk >> play('X', dur=2, sample=1, delay=1, lpf=250, amp=P[[1, 0, 0, 0], [[0, 0.5], 0.25, 0, 0], 0, 0] * var([0, kd.amp], [[64, 64, 32], [128, 64, 64]]))

rs.stop()


kd.stop()
sk.stop()
sp.stop()
dk.stop()

sb.stop()

print(SynthDefs)

bg >> bug(0, dur=0.5, drive=[0.05, 0.025, 0.05, 0.08], lpf=P[[500, 1000], 650, 300] * expvar([0, 5], [256, 0]), amp=P[1, 0.85, [0.5, 0.75]] * expvar([0, 5.5], [256, 0]))
tt >> play('n', pan=PWhite(-0.5, 0.5), sample=[var([1, 2, 3], [[64, 16], [32, 8, 8]]), var([3, 2], 64), var([2, 1, 0, 2], [128, 64, 32, 32, 64, 64])], dur=[1, 0.5, 0.5], amp=P[1, 1, 1, 1] * 1.5)

# i am living with my machine pal. take care!!

# <3

Master().lpf = 0

@nextBar
def run_that_function_to_make_some_move_bitches():
    Clock.bpm += 2
    Scale.default = "major"


e1 >> play("V", dur=4, pan = (-1,1) , amp=P[var([[0.25, 0], [0.5, 0.75]], [[256, 128, 64], [128, 64, 32]]), linvar([0.5,0.8],4)] * var.brk)

e2 >> play("x---m[--]h[---]",amp=linvar([0,1.4],16) * var.brk).every(16,"amen")

e3 >> rave(amp=0.5 * var.brk, rate=3 , formant = 1, tremeolo = 2, slide =3, lpf = sp.lpf)

e4 >> play("2" , mix=2 , rate =1 , room=2, amp =var([0, 1.5], [[128, 64], [64, 128, 32]]), dur = 16, sus =4 , delay =0.5)

e5 >> ambi(sb.pitch, amp = 1.8 * var.brk, lpf = sb.lpf, dur = sp.dur)


m1 >> karp(P*(0,-2,-4), room=1, mix=.6, amp=var([1,0],4) * var.brk)





