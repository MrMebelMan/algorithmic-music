Clock.bpm = 125
Scale.default = "minor"
Root.default = -2

var.dp = P[[8, 16], [4, 8], 2,1, 3, 1, [6, 12], [2, 8], 5, 4, [4, 32], [2, 8, 16], 3, 2, 3, 1]
var.d2 = P[16, 8, 5, 3, [4, 8], [2, 16], [8, 32], [1, 8], 2, 3]

var.brk = var([1, 0], [31, 1, 31, 1, 28, 4])
var.mad = P[[0.25] * 4 + [0.125] * 8 + [0.5] * 4 + [1] * 56]

trk   = P[128,64,64,128,64,64,128,128]
in_   = P[1,0,0,0,0,0,0,0]
bldup = P[0,1,0,0,1,0,0,0]
brk   = P[0,0,1,0,0,1,0,0]
drp   = P[0,0,0,1,0,0,1,0]
out   = P[0,0,0,0,0,0,0,1]

tm >> play(var(['x', 'X'], [64, 128]), 
    sample=Pvar([(3, [1, 0]), P[0]], [64, 128]),
    rate=P[PRand([1,1,3/4,3/5]),var([4/5,3/5,6/5],32),var([2,1.5,1.25,1,1,1],64),var([2/3,1],128),var([7/5,1],[128,64]),PRand([1/3,1/2])],
    dur=1/4,
    bend=P[[-0.15, 0], 0, [0, 0.1, 0, 0.15], 0] * var([1, 0], 32),
    delay=[0,var([1/2, 0], [128, 64]),0,[0,1/4],0,PRand([0,1/4]),0,1/2],
    pshift=P[var([0, 1], [64, 32]),PRand([2/3,1,0,-1/5]),PRand([0,2/3,2/5,2]),var([-1/4, 0], [32, 64]),[1/3,2],var([1/7, 0],[32,64,128]),0],
    lpf=P[[var([300, 200, 400], 64), [500, 750, 500, var([1000, 500, 350], 64)], var([700,300],128), var([1200, 300])],[1200,300],[700,900],var([500, 250, 650], [64, 32])],
    lpr=P[[0.25, 0.75, 0.5, 0.75], [0.5, 0.25], [0.25, 0.5, .075, 0.85], [0.25, 0.5]] * 1.5,
    amplify=P[
        [1, 0.9],
        [var([0.5, 0.85], 64),0.85,PRand([0.75,1/4,2/3])],
        [PRand([2/3,1/4,1/7]),1/7],
        [[0.5, 0.25, 0.25], var([0.5, 0], 64), 0.85],2/3,1/3,[var([0.25, 0.5, 0.75], 128),1/2],
        [var([0.25, 0.5], 128),var([2/3,1/7,3/4],PRand([4,8,12,16,24,32,64])),1/3,2/5]
    ],
    amp=
)

#hey vlad how can I add amp to amplify?


kk >> play('x', rate=P[1.05, 1, 1.03, 0.98], sample=0, dur=1, lpf=0, amp=P[1, 0.85] * var([0, 1], P[256, 128, 128, 128, 64, 128] / 1.5) * var.brk)
kd >> play('X', dur=1, sample=1, cut=0.5, lpf=500, amp=expvar([0, 0, 0.75, 0.75], [128, [128, 64], 256, 0]) * var.brk)

rs >> play('I', dur=[1] * 126 + [0.5, 0.5, 0.5], amp=expvar([0, 0.5], [256, 0]))

tb >> play("S",
    dur=1/4,
    echo=[0,1/2,0,3/4],
    sample=var([3,4],PRand([1,2,4,8,16,32])),
    delay=1/2,lpf=P[2000,PRand([900,3000,1000]),2000],
    room=1/2,
    mix=1/3,
    pan=PWhite(-1,1),
    amplify=P[1/8,[0,2/3,1/6],1/4,0,1/8,linvar([1/2,3/4],4),[0,1/7,2/3]],
    amp=var([0, 1], [128, 256, 64, 128])
)

tg >> play("&",
    dur=[1/2,PDur(3,5),0,PDur(5,8)],
    pshift=P[-1,1/2,var([0,1,-1],PRand([2,4,8,12,16])),0,1],
    echo=1/2,
    amplify=P[0,1/3,3/4,0,1/5,1/7],
    amp=var([1, 0], [[128, 64, 256], [64, 32, 128]])
)

pc >> play("E",
    sample=Pvar([P[0], var([0, 1, 2, 0], [3, 1, 2, 2, 3, 1])], [64, 128]),
    dur=1/2,
    echo=PRand([0,1/2,PDur(3,5)]),
    lpf=linvar([800,1600],32),
    amplify=P[1/5,[0,1/3,1/4],0,PRand([1/8,0,2/5]),0,1/4,1/5,0],
    amp=expvar([0.25, 1], 256)
)

vr >> play("q",rate=var([1,2],64),pshift=var([0,-1],[14,2]),delay=Pvar([0,[0,1/2]],[[24,16],[8,16]]),sample=1,room=1/3,mix=1/2,lpf=linvar([800,2000],32),pan=PWhite(-1,1),amplify=P[3/7,4/7],amp=1)

vn >> play("Y",
    dur=PRand([1/4,1/2,1,2],[8,1,[15,7],4]),
    sample=PRand(1),
    rate=P[[2, 1], var([1, 2], 32), 1, 1],
    echo=[1/4,var([1/2,1/4],[32,64])], 
    echotime=1,
    lpf=expvar([[400, 500, 1000, [600, 1100]],1800],128), 
    lpr=0.25,
    room=P[2/3, var([0, 1/3], 128), 0], 
    mix=1/3,
    pan=[-2/3,0,2/3],
    amplify=1/9,
    amp=P[[1,0.9],[0.85,0.75]] * 1.75
)

oh >> play('-', dur=[1] * 15 + [[0.25, 0.5], [0.75, 0.5]], sample=2, delay=0.5, room=1, mix=0.15, amp=var([0.25, 0], [[128, 64], [64, 32]]) * var.brk)
sh >> play('s',
    dur=0.25,
    amp=P[
        [var([0, 0.5, 0.75], 256), 0.15], [0.25, 0.5], [0.5, 0.75], [var([0, 0.5], 128), 0.15],
        var([0.85, 0], [64, [32, 64]]), 0.65, var([0.45, 0.25, 0], 32), var([0.25, 0.5, 0.15, 0], [128, 64, 32]),
        [0, 0.25], [0.5, 0.75, 0.25, 0.15], [0.15, 0], [0.75, 0.5, 0.25, 0.5],
        [0.25, 0.15, 0, 0], [0.5, 0, 0.25, 0.15], [0.75, 0.5, 0.75, var([0, 1], 128)], [0.25, 0.15, 0.5, 0.75] 
    ] * expvar([0, 0.4], [128, 256]) * var.brk
)
st >> play('m', sample=0, dur=1, delay=0.5, lpf=P[var([300, 500, 600], 64), var([500, 300], 8), [250, var([500, 250], [128, 64, 32])], 300], lpr=0.5,
    amp=P[
        var([1, 0.5], 8), [var([0.25, 0], 64), var([0.5, 0.25, 0], 128)], 0, 0,
        [0, var([0.5, 0], 4)], 0, var([0, 0.5], 8), var([0.7, 0], 4)
    ] * expvar([0.25, 0.5], 256) * var([1, 0], [[128, 256], [64, 128]]) * var.brk
)

