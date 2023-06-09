from dorna2 import Dorna
import time
#import stop
#import threading


# from test_p import puntos
def p8678(v, a, tq, t1, t2):
    '''
    p8678:
        Es el programa principal del ensamble de goma.haciendo referencia al No.PCB
        Aqui se crea una instancia de la clase Dorna() de la libreria local dorna2
        
        --Parametro de entrada
            v = velocidad
            a = aceleracion
            tq = torque
            t1 = tiempo de goma chica
            t2 = tiempo de goma grande
            ang = valor de angulo(constante)
            ** Aunque que no necesariamente se necesitan valores de entrada si no que se puede con valores prederminado
            del mismo robot
        
        --Instancia dorna
            ip = "dorna"
            port = 443
            
        --Informacion I/O (input/output)
            Inputs:
                in4 = Boton de emergencia
                in3 = Sensor deteccion de PCB
            Outputs:
                out5 = Dispensador de goma
                out2 = Clamp Conveyor
                out1 = stopper
                out3 = Linea de SMEMA
                
    
    '''
    robot = Dorna()
    ip = "dorna"
    port = 443
    robot.connect(ip, port)
    print("Conectado")
    
    spd = v
    acel = a
    torq = tq
    t = t2
    ang = 2.385
    print("spd:", spd, "acel:", acel, "torq:", torq, "t", t)
    
    def boton_stop():
        '''
        Funcion para detener Dorna:
            Evalua mediante .probe(),si mediante el modulo de I/O la entrada 4 es igual a 1
            de ser asi el robot se detiene y entra en un modo de emergencia o alarma...    
            
            Para continuar operando la entrada 4, debe tener un valor de 0;
            
            **nota: la entrada o input hace referencia al boton de emergencia
             
        '''
        robot.probe(index=4, val=1)
        #robot.wait(in4=1)
        robot.play(cmd="halt", id=1, accel=7.5)
        robot.play(cmd="alarm", alarm=1)
        robot.set_output(index=5, val=0, queue=1)
        #robot.play(out5=0)
        print("Robot stop, paro de emergencia presionado")

        robot.wait(in4=0)
        robot.play(cmd="alarm", alarm=0)
        print("robot run")

    def load():
        '''
        Funcion para detectar la carga de PCB:
            -valida el estado del stoper y el clamp del conveyor
            -
        
        '''
        if robot.get_input(index=1) == 1 and robot.get_input(index=2) == 0:  # validamos que el stoper este arriba y clamp abierto robot.sys["in1"] robot.sys["in2"]
            robot.probe(index=3, val=1)# esperamos tarjeta en els ensor
            #robot.wait(in3=1)
            #robot.play(timeout=-1, cmd="output", out3=0, id=50)
            robot.set_output(index=3, val=0, id=50)
            #sm = robot.play(track=True, cmd="output", out3=0, id=50)  # abrimos la linea de SMEMA, cancelamos comunicacion NEXT
            #sm.complete()
            robot.sleep(val=1)
            #time.sleep(1)
            robot.set_output(index=2, val=1, id=51)
            #robot.play(timeout=0, cmd="output", out2=1, id=51)  # Cerramos clamp
            #cload = robot.play(track=True, cmd="output", out2=1, id=51)  # Cerramos clamp
            #cload.complete()
            robot.sleep(val=0.5)
            #time.sleep(0.5)
            robot.set_output(index=1, val=0, id=52)
            #robot.play(timeout=0, cmd="output", out1=0, id=52)  # bajamos stopper
            #cstp = robot.play(track=True, cmd="output", out1=0, id=52)  # bajamos stopper
            #cstp.complete()
        else:
            stp()
            

    def unload():
        '''
        Funcion de descarga de PCB:
            -valida el estado del stopper y el clamp del conveyor
        
        '''
        
        if robot.get_input(index=1) == 0:  # validamos stopper abajo    robot.sys["in1"]
            cunld = robot.play(track=True, cmd="output", out2=0, id=60)  # abrimos clamp
            cunld.complete()
            u_sm = robot.play(track=True, cmd="output", out3=1, id=61)  # cerramos linea de SMEMA, habilitamos comunicacion NEXT
            u_sm.complete()
            robot.wait(in3=0)  # esperamos sensor este libre, salga pcb
            time.sleep(3)
            ustp = robot.play(track=True, cmd="output", out1=1, id=62)  # subimos stopper
            ustp.complete()
        else:
            print("Error el stopper esta arriba")
            # unload()

    def stp():
        robot.play(timeout=-1,cmd="output", out1=1, id=53)
        robot.play(timeout=-1, cmd="output", out2=0, id=54)
        robot.sleep(val=1)
        if robot.get_input(index=3) == 1:
            load()

    def stby():
        robot.play(timeout=0-1, cmd="lmove", rel=0, x=459.000, y=6.000, z=298.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=100)
        
    while robot.get_input(index=4) == 0:
        load()
        stby()
        time.sleep(t)
        # puntos de prueba iniciales
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=32.700, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=200)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=32.700, z=152.750, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=201)
        print(robot.sys)
        d1 = robot.play(timeout=-1, cmd="output", out5=1, id=202)
        print(d1)
        time.sleep(t)
        robot.play(timeout=-1,cmd="output", out5=0, id=203)
        print("punto 1")
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=32.700, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=204)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=28.800, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=205)
#PUNTO 2
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=28.800, z=152.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=206)
        robot.play(timeout=-1, cmd="output", out5=1, id=207)
        time.sleep(t)
        robot.play(timeout=-1,cmd="output", out5=0, id=208)
        print("punto 2")
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=28.800, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=209)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=24.600, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=210)
 #PUNTO 3
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=24.600, z=152.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=211)
        robot.play(timeout=-1, cmd="output", out5=1, id=212)
        time.sleep(t)
        robot.play(timeout=-1,cmd="output", out5=0, id=213)
        print("punto 3")
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=24.600, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=214)

    # puntos de ensamble PCB1
    # 1-L4
        # L4-1
        robot.play(timeout=-1, cmd="lmove", rel=0, x=408.394, y=47.117, z=152.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=215)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=408.394, y=47.117, z=150.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=216))
        robot.play(timeout=-1, cmd="output", out5=1, id=217)
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=218)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=408.394, y=47.117, z=152.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=219)

    # 1-C25
        # C25-1
        robot.play(timeout=-1, cmd="lmove", rel=0, x=387.153, y=38.054, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=225)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=387.153, y=38.054, z=150.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=226)
        robot.play(timeout=-1, cmd="output", out5=1, id=227)
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=228)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=387.153, y=38.054, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=229)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=382.22, y=40.983, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=230)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=382.22, y=40.983, z=150.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=231)
        robot.play(timeout=-1, cmd="output", out5=1, id=232)
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=233)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=382.22, y=40.983, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=234)

    # puntos de ensamble PCB2
    # 2-L4
        # L4-1
        robot.play(timeout=-1, cmd="lmove", rel=0, x=408.718, y=-9.391, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=264)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=408.718, y=-9.391, z=149.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=265)
        robot.play(timeout=-1, cmd="output", out5=1, id=266)
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=267)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=408.718, y=-9.391, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=268)

    # 2-c25
        # C25-1
        robot.play(timeout=-1, cmd="lmove", rel=0, x=388.424, y=-19.273, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=274)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=388.424, y=-19.273, z=149.478, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=275)
        robot.play(timeout=-1, cmd="output", out5=1, id=276)
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=277)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=388.424, y=-19.273, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=278)
        # C25-2
        robot.play(timeout=-1, cmd="lmove", rel=0, x=382.629, y=-15.636, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=279)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=382.629, y=-15.636, z=149.476, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=280)
        robot.play(timeout=-1, cmd="output", out5=1, id=281)
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=282)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=382.629, y=-15.636, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=283)

    # puntos de ensamble PCB3
    # 3-L4
        # L4-1
        robot.play(timeout=-1, cmd="lmove", rel=0, x=407.456, y=-66.422, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=314)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=407.456, y=-66.422, z=149.423, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=315)
        robot.play(timeout=-1, cmd="output", out5=1, id=316)
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=317)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=407.456, y=-66.422, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=318)

    # 3-C25
        # C25-1
        robot.play(timeout=-1, cmd="lmove", rel=0, x=387.472, y=-75.453, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=324)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=387.472, y=-75.453, z=149.42, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=325)
        robot.play(timeout=-1, cmd="output", out5=1, id=326)
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=327)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=387.472, y=-75.453, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=328)
        # C25-2
        robot.play(timeout=-1, cmd="lmove", rel=0, x=381.033, y=-71.95, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=329)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=381.033, y=-71.95, z=149.794, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=330)
        robot.play(timeout=-1, cmd="output", out5=1, id=331)
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=332)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=381.033, y=-71.95, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=333)

        stby()
        time.sleep(t)
        time.sleep(1)
        unload()

if __name__ == '__main__':
    robot = Dorna()
    robot.connect(host = "localhost", port = 443)
    p8678(40,1000,2500,0.5,0.5)
    robot.close()
