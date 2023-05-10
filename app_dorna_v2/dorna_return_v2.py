from dorna2 import Dorna
import time

def back():
    robot = Dorna()
    ip = "dorna"
    port = 443
    robot.connect(ip, port)
    print("Conectado....")
    print("Robot regresando a home....")

    spd = 50
    acel = 1000
    torq = 4000

    robot.play(track=True, cmd="jmove", j1=180, j2=-142, j3=135, j4=0, vel=spd, accel=acel, jerk=torq, id=12)
    robot.play(track=True, cmd="jmove", j0=180, vel=spd, accel=acel, jerk=torq, id=11)
    time.sleep(2)
    robot.set_motor(0)
    print("Robot regreso a Home....\n")

    robot.close()

if __name__ == "__main__":
    back()

