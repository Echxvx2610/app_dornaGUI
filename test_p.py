from dorna2 import dorna
import time

robot = dorna()


def puntos(spd, acel, t):
    self_t = t
    self_spd = spd
    self_acel = acel

    p1 = robot.play(track=True, cmd="lmove", rel=0, x=314.052, y=3.638, z=189.950, a=-1.224, b=-89.955, vel=self_spd, accel=self_acel, jerk=4000, id=200)
    print(robot.sys)
    p1.complete(time_out=0)
    print("comm complete")
    #   robot.wait(id=200, stat=2)
    d1 = robot.play(track=True, cmd="output", out5=1, id=201)
    d1.complete()
    print(d1.complete())
    time.sleep(self_t)
    robot.play(cmd="output", out5=0, id=202)
    print("punto 1")
    robot.play(track=True, cmd="lmove", rel=0, x=314.052, y=3.638, z=192.500, a=-1.213, b=-89.966, vel=self_spd, accel=self_acel, jerk=4000, id=203)
    robot.play(track=True, cmd="lmove", rel=0, x=314.044, y=1.819, z=192.500, a=-1.213, b=-89.966, vel=self_spd, accel=self_acel, jerk=4000, id=204)
    p2 = robot.play(track=True, cmd="lmove", rel=0, x=314.044, y=1.819, z=189.950, a=-1.213, b=-89.966, vel=self_spd, accel=self_acel, jerk=4000, id=205)
    p2.complete(time_out=0)
    d2 = robot.play(track=True, cmd="output", out5=1, id=206)
    d2.complete()
    time.sleep(self_t)
    robot.play(cmd="output", out5=0, id=207)
    print("punto 2")
    #    robot.play(cmd="lmove", rel=0, x=314.044, y=1.819, z=192.500, a=-1.213, b=-89.966, id=208)
    robot.play(cmd="lmove", rel=0, x=314.044, y=1.819, z=194.500, a=-1.213, b=-89.966, vel=self_spd, accel=self_acel, jerk=4000, id=208)
    time.sleep(self_t)
