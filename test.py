from dorna2 import dorna
import time

def main():
    robot = dorna()
    ip = "169.254.48.61"
    port = 443
    robot.connect(ip, port)
    print("Conectado")

    print("Esperando entrada input0 para iniciar")
    robot.wait(in0=1)
    print( "espera por 2 segundos")
    time.sleep(2)

    for i in range(2):
        #movimento simple
        robot.play(cmd="lmove", rel = 1, z=100*(-1)**(i+1), vel=100, accel=1000, jerk=4000, id=1)
        robot.wait(id=i+1,stat=2)
        print("movimiento ",i," completo")
    robot.close()

# recibir mensajes del sistema robot
def main_sys():
    robot = dorna()
    ip = "169.254.48.61"
    port = 443
    robot.connect(ip, port)
    print("Conetado")

    start = time.time()
    while time.time() - start < 10:
        print(robot.sys)

    robot.close()
# recibir mensajes condicionado a una entrada
def main_msg():
    robot = dorna()

    ip = "169.254.48.61"
    port = 443
    robot.connect(ip, port)
    print("Conetado")

    start = time.time()
    while time.time() - start < 10:
        if not robot.msg.empty():
            msg = robot.msg.get()
            if "cmd" in msg and msg["cmd"]=="output":
                print(msg)

    robot.close()

if __name__ == '__main__':
    main()