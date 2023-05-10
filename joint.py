from dorna2 import Dorna
import time


def home():
    robot = Dorna()
    ip = "dorna"
    port = 443
    robot.connect(ip, port)
    print("Conectando")
    if not robot.connect(ip):
        print("not connected")
    else:
    	print("connected")


    print(robot.get_all_joint())



    #print(robot.sys())


    #robot.play(timeout=-1, cmd="joint", j0=180, j1=180, j2=-142, j3=135, j4=0, id=10)
    #print(robot.recv())




    robot.close()


if __name__ == '__main__':
    home()
#    main()
