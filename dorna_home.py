from dorna2 import Dorna
import time

def home():
    robot = Dorna()
    ip = "dorna"
    port = 443
    robot.connect(ip, port)
    print("Conectado")

    #mensa = robot.msg.get()
    #print(mensa)
    
    print(robot.sys())



    #z1 = \
    robot.play(timeout=-1, cmd="joint", j0=180, j1=180, j2=-142, j3=135, j4=0, id=10)
    print(robot.recv())
    #z1.complete()


    print(" ")
    print(robot.sys)
    if robot.sys["j0"] >= 179.9:
        if robot.sys["j1"] >= 179.9:
            if robot.sys["j2"] <= -141.9 and robot.sys["j2"] >= -142.1:
                if robot.sys["j3"] >= 134.9:
                    if robot.sys["j4"] <= 0.01:
                        print("set complete")

                        #cmd = {"cmd": "motor", "motor": 1, "id": 100}
                        m1 = robot.play(track=True, cmd="motor", motor=1, id=100)
                        m1.complete()
                        print("motor encendido")
                        time.sleep(1)
                        spd = 50
                        acel = 1000
                        torq = 4000

                        # robot.play(cmd="jmove", j0=0, j1=0, j2=0, j3=0, j4=0, vel=spd, accel=acel, jerk=torq, id=12)
                        #robot.jmove(track=True, j0=0, j1=0, j2=0, j3=0, j4=0, vel=spd, accel=acel, jerk=torq, id=12)



                    else:
                        print("J4 not set")
                else:
                    print("J3 not set")
            else:
                print("J2 not set")
        else:
            print("J1 not set")
    else:
        print("J0 not set")


    robot.close()


if __name__ == '__main__':
    home()
#    main()
