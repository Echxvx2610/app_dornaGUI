from dorna2 import Dorna
v_s=1

def stop():
    global v_s
    v_s = 0
    print(v_s)
    robot = Dorna()
    ip = "dorna"
    port=443
    robot.connect(ip,port)
    robot.play(cmd="halt", id=1, accel=7.5)
    robot.play(track=True, cmd="alarm", alarm=1)
    print("robot Detenido")
    robot.close()


def reset():
    global v_s
    v_s = 1
    print(v_s)
    robot = Dorna()
    ip = "dorna"
    port = 443
    robot.connect(ip, port)
    robot.play(track=True, cmd="alarm", alarm=0)
    print("robot reseteado!")
    
    robot.close()
