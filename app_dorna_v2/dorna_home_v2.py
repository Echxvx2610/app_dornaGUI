from dorna2 import Dorna
import time

def homming():
    robot = Dorna()
    ip = "dorna"
    port = 443
    robot.connect(ip, port)
    print("Conectado")

    print(" ")
    joints = robot.get_all_joint()
    print(f'Posicion de joints:{joints}')
    if joints[0] >= 179.9:
        if joints[1] >= 179.9:
            if joints[2] <= -141.9 and joints[2] >= -142.1:
                if joints[3] >= 134.9:
                    if joints[4] <= 0.01:
                        print("set complete")

                        # cmd = {"cmd": "motor", "motor": 1, "id": 100}
                        robot.set_motor(1)
                        print("Motor encendido...\n")
                        time.sleep(1)
                        spd = 50
                        acel = 1000
                        torq = 4000
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

if __name__ == "__main__":
    homming()


