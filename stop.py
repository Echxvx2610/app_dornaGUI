#from dorna2 import dorna

v_s=1

def stop():
    global v_s
    v_s = 0
    print(v_s)
    # return s
    robot = dorna()
    ip = "dorna"
    port=443
    robot.connect(ip,port)

    robot.play(cmd="halt", id=1, accel=7.5)
    robot.play(track=True, cmd="alarm", alarm=1)
    #paro.complete()
    print("robot Detenido")

#
# robot.play_script("stop.txt")
    robot.close()


def reset():
    global v_s
    v_s = 1
    print(v_s)
    robot = dorna()
    ip = "dorna"
    port = 443

    robot.connect(ip, port)
    robot.play(track=True, cmd="alarm", alarm=0)
    #r.complete()
    #robot.play_script("reset.txt")

    robot.close()
