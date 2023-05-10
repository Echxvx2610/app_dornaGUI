from dorna2 import Dorna
import time

def back():
    robot = Dorna()
    ip = "dorna"
    port = 443
    robot.connect(ip, port)
    print("Conectado")

    print(robot.sys)

    spd = 50
    acel = 1000
    torq = 4000

    #robot.play_script("zero.txt")

    #tr = robot.socket_loop()
    #print(tr)

    st2=robot.play(track=True,cmd="jmove",j1=180,j2=-142,j3=135,j4=0,vel=spd,accel=acel,jerk=torq,id=12)
    st2.complete()
    st1 = robot.play(track=True, cmd="jmove", j0=180, vel=spd, accel=acel, jerk=torq, id=11)
    st1.complete()

    #robot.jmove(track=True, j0=0.01, j1=0.01, j2=0.01, j3=0.01, j4=0, vel=50, accel=1000, jerk=4000)

    robot.close()


if __name__ == '__main__':
    back()
#    main()
