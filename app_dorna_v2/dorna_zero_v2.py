from dorna2 import Dorna
import time

def cero():
    robot = Dorna()
    ip = "dorna"
    port = 443
    robot.connect(ip, port)
    print("Conectado...")

    spd = 50
    acel = 1000
    torq = 4000

    # Motion 1
    # start = time.time()
    st1 = robot.play(timeout=-1,cmd="jmove", id=11, j0=0, vel=spd, accel=acel, jerk=torq)
    time.sleep(1)
    print("Robot en movimiento...")

    #Motion 2
    st2 = robot.play(timeout=-1, track=True, cmd="jmove", j1=0, j2=0, j3=0, j4=0, vel=spd, accel=acel, jerk=torq, id=12)
    time.sleep(1)
    print("Movimiento completado..\n")
    # robot.jmove(track=True, j0=0.01, j1=0.01, j2=0.01, j3=0.01, j4=0, vel=50, accel=1000, jerk=4000)

    robot.close()

if __name__ == "__main__":
    cero()