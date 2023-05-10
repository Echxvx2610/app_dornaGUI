from dorna2 import dorna
import time


def main():
    robot = dorna()
    ip = "dorna"
    port = 443
    robot.connect(ip, port)
    print("Conectado")

    # print("Esperando entrada input0 para iniciar")
    # robot.wait(in0=1)
    # print( "espera por 2 segundos")
    # time.sleep(2)
    #spd = 50
    #acel = 1000
    #torq = 4000

    #robot.play(cmd="jmove", j0=0, j1=0, j2=0, j3=0, j4=0, vel=spd, accel=acel, jerk=torq, id=12)
    #robot.jmove(track=True, j0=0, j1=0, j2=0, j3=0, j4=0, vel=spd, accel=acel, jerk=torq, id=12)

    spd = 180
    acel = 1000
    torq = 4000


    for i in range(3):
        # movimento simple
        robot.play_script("deposito.txt")
        # robot.play(cmd="lmove", rel = 1, z=100*(-1)**(i+1), vel=100, accel=1000, jerk=4000, id=1)
#        robot.play(cmd="lmove", rel=0, x=367.601, y=51.692, z=280.000, a=3.616, b=-90, vel=spd, accel=acel,
#                   jerk=torq, id=1)
#       robot.play(cmd="lmove", rel=0, x=367.598, y=51.691, z=264.000, a=3.611, b=-90, vel=spd, accel=acel,
 #                  jerk=torq, id=2)
 #       time.sleep(2)
#        robot.play(cmd="output", out1=1, id=1000)
#        time.sleep(2)
#        robot.play(cmd="output", out1=0, id=1000)
#        print("deposito 1")
#        time.sleep(2)
#        robot.play(cmd="lmove", rel=0, x=367.599, y=51.691, z=280.000, a=3.616, b=-90, vel=spd, accel=acel,
#                   jerk=torq, id=3)
        # robot.wait(1)
        #time.sleep(2)
#        robot.play(cmd="lmove", rel=0, x=389.927, y=-150.939, z=280.000, a=3.607, b=-90, vel=spd, accel=acel,
#                   jerk=torq, id=4)
        # robot.wait(1)
        #time.sleep(2)
#        robot.play(cmd="lmove", rel=0, x=389.927, y=-150.94, z=264.000, a=3.602, b=-90, vel=spd, accel=acel,
#                   jerk=torq, id=5)
#        time.sleep(2)
#        robot.play(cmd="output", out1=1, id=102)
#        time.sleep(2)
#        robot.play(cmd="output", out1=0, id=102)
#        print("deposito 2")
#        time.sleep(2)
#        robot.play(cmd="lmove", rel=0, x=389.93, y=-150.941, z=280.000, a=3.611, b=-90, vel=spd, accel=acel,
#                   jerk=torq, id=6)
        # robot.wait(id=i+1,stat=2)
#        time.sleep(2)
        print("movimiento ", i, " completo")

        #posicion wait
        robot.play(cmd="jmove", j0=0, j1=100, j2=-90, j3=0, j4=-90, vel=50, accel=acel,
                   jerk=torq, id=200)
        time.sleep(5)

    robot.close()


if __name__ == '__main__':
    main()
