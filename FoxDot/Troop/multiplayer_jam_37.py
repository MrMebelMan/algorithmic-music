from pythonosc.udp_client import SimpleUDPClient
ip = "127.0.0.1"
port = 12345
client = SimpleUDPClient(ip,port)  # Create client
def mean(numbers):
    return float(sum(numbers))/max(len(numbers),1)
def oscMsg():
    bpm = float(60/Clock.bpm) 
    val0 = float(Clock.bpm)             
    val1 = mean(Master().amp)  
    val2 = mean(Master().amplify)
    val3 = mean(Master().freq)
    val4 = mean(Master().dur)
    val5 = mean(Master().oct)
    client.send_message("/vizart",[val0,val1,val2,val3,val4,val5])
    Clock.future(,lambda:oscMsg())
oscMsg()

print(Clock.beat)

Clock.set_time(0)

print(SynthDefs)

print(Clock.beat)

Clock.bpm = 133

var.pat = P[28, 4, 8, 8, 6, 2, 16, 8, 8]

var.dur = P[[31, 31, 28, 28, 56, 56], [1, 1, 4, 4, 8, 8]]
var.brk = var([1, 0], var.dur)

so >> pluck(
    var([0, -0.5], 512),
    dur=PDur(4, 12),
    room=0.5, mix=[0, 0.1, [0, 0.2], 0],
    sus=[2, 1, 1, 1],
    chop=4,
    hpf=[[200, 300, 400], [600, 250], [300, 600, 1200], 800],
    hpr=[0.25, 0.5, 0.25, 0.25],
    lpf=[
        [var([5000, 1500, 1000], [64, 32, [32, 64]]), 2500, 6000], 4500, var([6000, 4000], 8), var([3000, 3500, 2500, 1500], 64),
        [2500, 1500, 1000, 500], 3500, [1000, var([500, 2500, 350, 3000], [64, 32])], 1250,
    ], lpr=expvar([0.5, 0.25], 32),
    amp=P[[1, 0.5], 0.75, 1, 1] * var([1, 0], var.pat) * 0.15
)
sb >> sawbass(
    so.degree,
    dur=PDur(4, 8),
    sus=1,
    chop=4,
    lpf=[[5000, 4000, 2500], [3500, 4000], [4500, 2500], [2500, 3500, 500, 1750]], lpr=expvar([0.5, 0.25], [16, 16, 32]),
    hpf=[[500, 300, 250, 600], 750, [300, 300, 400, 500], 450], hpr=expvar([0.25, 0.5], 64),
    amp=1 * var([0, 1], var.pat) * 0.1
)

k1 >> play('X', room=0.75, mix=0.2, sample=var([1, 2], [[[256, 64, 32], 128], 128]), dur=1, lpf=var([400, 850], 128), lpr=0.5, hpf=var([135, 110, 90, 120], [[128, 32], [64, 32, 64]]), hpr=0.25, amp=expvar([0.5, 0.8], 128) * var.brk * 2.75)

k2 >> play('X', sample=1, dur=k1.dur, delay=0.5, lpf=700, lpr=0.25, amp=P[1, 0, [1, 0.9], 0.25] * k1.amp * var([0.75, 0], [256, 256, 128, 128]) * var.brk)
#k2.stop()

tt >> play('t', sample=2, lpf=P[5000, [8500, 4000, 4500], [7500, 4250, 4750], [5500, 3750, 6000]], amp=P[[0.25, 0.5], 0, [0, 0, 0, 1], 0, [0.25, 0.3], 1, [0.5, 0.75, 0, 0.5], [0.75, 0.5, 0.75, 0.85]] * var([0, 2], [[128, 64, 32], [64, 128]]) * 1.5)
cl >> play('H', sample=1, dur=var([8, 4], [128, 64]), delay=0.5, amp=var([0, 0.35], [128, [64, 128, 256], 32, 64, 32, 32]) * 1.5)
h1 >> play('-', dur=k1.dur, delay=0.5, amp=P[1, [1, 0.9]] * var([1, 0], [[128, 256, 64, 64, 32], [64, 128, 64]]) * 1.75)
h2 >> play('-', sample=var([2, 1], [128, [64, 32]]), dur=0.25, amp=P[0.15, [0, 0.25], 0.5, [0, 0, 0, 1],  [0.25, 0, 0.25, 0.15], [0.15, 0.15, 0.2, 0.25], 0, 0] * var([1.75, 0], [[64, 128, 32], 128, [32, 256], 64, 128, 128]) * 1.5)

jb >> jbass(var([2, 0, 1, 3, 1.5, 0, 0], 64), dur=k1.dur, chop=[4, 4, 4, var([2, 4], [[128, 64], [64, 32]])], hpf=[60, [var([70, 50], [128, 64]), [60, 65]], var([70, 60], 128), var([70, 60, 55], 128)], hpr=0.25, amp=P[1.45, [1, 0.85, 1, 0.9]] * expvar([0.85, 0.20], 1/4) * var.brk * var([0, 0.4], [512, 256]) * k1.amp)
br >> bass(
    P[-0.5, 0.25, 0, [1, 0]],
    dur=0.25,
    hpf=var([130, [120, 90], 100, [120, 80], 110, 90, 80], 4),
    hpr=0.3,
    lpf=P[850, 150, 700, [150, var([250, 500], 128)]], lpr=0.75,
    sus=[2, 0.5, 0.5, 0.5],
    chop=[4, 4, 4, [4, 2]],
    amp=P[[[1, 1.1], 1, 1, 1], [0.5, 0.25]] * 1 * var([0, [0.5, 0.75], 1], [[128, 128, 64], [64, 128], [64, 128]]) * var.brk
)

rr >> play('I', sample=[var([0, 1, 2], 64), var([1, 2]), [var([2, 1], [128, 64]), 0], 0, [0, 2]], pan=PWhite(-0.5, 0.5), room=1, mix=[0.1, 0], dur=0.25, amp=P[var([0, 1], 512), var([0, 0.5, 0.25, 0, 0.75], 128), [0, var([1, 0], [64, 32])], 0, [1, 0.75], [0, 1], [0.25, [0, 1]], [0.5, 0.75, 0.25, 0.25]] * var([0, 1], [256, 256, 128, 64, 64, 128, 32, 32]))

bg >> blip(-0.15, dur=1, delay=0.5, oct=4.7, elay=0.5, bend=-0.25, benddelay=0.75, hpf=[150, 140, 150, 155], hpr=[0.33, 0.5], amp=P[2.25, [2, 2.15]] * var.brk * expvar([0, 0, 1, 1], [[128, 256], 128, 256, 0]) * 0.5)

r2 >> play('I', sample=var([0, 2], [[128, 64, 64], [256, 128, [128, 64]]]), dur=1, room=1, mix=0.25, lpf=250, lpr=0.25, amp=var([0, 2], [[128, 64], [256, 128, 256]]))
r3 >> play('I', sample=r2.sample, dur=r2.dur, delay=0.5, room=1, mix=0.25, lpf=250, lpr=0.25, amp=P[[var([0, 1], [64, [32, 64]]), 1], 0, 0, 0] * 0.25 * r2.amp)

print(SynthDefs)
 
t1 >> dub(P[-2,3,3,3,0],oct=6,dur=8,echo=1/2,chop=16,shape=1/9,lpf=[[400,800,1000],[1200,600,900],[450,850,1500],350],room=1/3,mix=1/2,pan=(-2/3,2/3),amplify=2/5,amp=expvar([0, 1, 1], [64, 64, 128]))

t2 >> blip(PSine(4)+P[:2]+[0,1,0,-2,5,7,0],oct=4.25,dur=1/4,echo=1/2,shape=2/5,drive=0,lpf=sb.lpf * 0.25,lpr=[0.5, 0.25, 0.75, 0.75],pan=PWhite(-1,1),amplify=var([2/5,0],24,8),amp=var([1, 0], [[[32, 256], 256, 64], [128, 256, 64]]))

t3 >> creep(jb.degree,oct=PRand([4,5],1/2),dur=1/2,sus=1,delay=[0,1],echo=6/5,shape=3/7,chop=3,bend=1,lpf=PWhite(800,2000),lpr=linvar([1/7,1],32),room=1/3,mix=1/2,amplify=[3/7] * 7 + [[0.75, 0.5]],amp=var([1, 0], var.pat))

t4 >> klank(PRand([-1,0,1,2]),oct=4,dur=32,drive=2/4,lpf=var([0,linvar([400,3000],4)],4),amplify=var([0,linvar([0,3/5],4)],64),amp=var([0, 1], var.pat))

t5 >> noise((-12,0),oct=(4,PRand([6,7,8])),atk=PRand([2,3,4]),dur=PRand([4,6,8,12,16,32],16),sus=PRand([4,6,8,12,16]),echo=PRand([0,1/2,5/7,3/4,1]),slide=PWhite(1/2,2),lpf=sinvar([400,[800,2400,1200,900,750]],[2,3,4,6,8,12]),room=2/3,mix=1/2,amplify=4/7,amp=1)

@next_bar
def stahp():
    Group(r3, h2, cl, tt, t2, bg).stop()
    Group(r3, h1, h2, cl).stop()
    Group(tt, t2, bg, k2).stop()
    Group(r2, r3, rr).stop()
    Group(t5, t4, t3).stop()
    Group(t1, t2).stop()
    Group(kd, k1, jb, br).stop()
    
print(Clock)

print(Attributes)

