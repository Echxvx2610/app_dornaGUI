#from dorna2 import dorna
import time

def cero():
    robot = dorna()
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

    st1=robot.play(track=True,cmd="jmove",j0=0,vel=spd,accel=acel,jerk=torq,id=11)
    st1.complete()
    st2=robot.play(track=True,cmd="jmove",j1=0,j2=0,j3=0,j4=0,vel=spd,accel=acel,jerk=torq,id=12)
    st2.complete()
    #robot.jmove(track=True, j0=0.01, j1=0.01, j2=0.01, j3=0.01, j4=0, vel=50, accel=1000, jerk=4000)

    robot.close()


if __name__ == '__main__':
    cero()
#    main()
