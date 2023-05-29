from dorna2 import Dorna
import time
#import stop
#import threading


# from test_p import puntos
def p31974(v, a, tq, t1, t2):
   # self.v = v
   # self.a = a
   # self.t = tq
   # self.t1 = t1
   # self.t2 = t2

    robot = Dorna()
    ip = "dorna"
    port = 443
    robot.connect(ip, port)
    print("Conectado")
   # print(stop.v_s)

    #   print(robot.sys)

    # spd = 300
    spd = v
    # acel = 1500
    acel = a
    # torq = 4000
    torq = tq
    t = t2
    ang = 2.385
    print(spd)
    print(acel)
    print(torq)
    print(t)

    def boton_stop():
        robot.probe(index=4, val=1)
        #robot.wait(in4=1)
        robot.play(cmd="halt", id=1, accel=7.5)
        robot.play(cmd="alarm", alarm=1)
        robot.set_output(index=5, val=0, queue=1)
        #robot.play(out5=0)
        print("robot stop, paro de emergencia presionado")

        robot.wait(in4=0)
        robot.play(cmd="alarm", alarm=0)
        print("robot run")

    def load():
        if robot.get_input(index=1) == 1 and robot.get_input(index=2) == 0:  # validamso que el stoper este arriba y clamp abierto robot.sys["in1"] robot.sys["in2"]
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

            # load()

    def unload():
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
            print("error el stopper esta arriba")
            # unload()

    def stp():
        robot.play(timeout=-1,cmd="output", out1=1, id=53)
       # stp1 = robot.play(track=True, cmd="output", out1=1, id=53)
        #stp1.track_cmd()
        #stp1.complete()
        robot.play(timeout=-1, cmd="output", out2=0, id=54)
        #clmp = robot.play(track=True, cmd="output", out2=0, id=54)
        #clmp.track_cmd()
        #clmp.complete()
        robot.sleep(val=1)
        if robot.get_input(index=3) == 1:
        #robot.probe(index=3, val=1)# esperamos tarjeta en els ensor
            load()

    def stby():
        robot.play(timeout=0-1, cmd="lmove", rel=0, x=459.000, y=6.000, z=298.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=100)
        #w = robot.play(track=True, cmd="lmove", rel=0, x=459.000, y=6.000, z=298.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=100)
        #w.complete()
#    thread = threading.Thread(target=boton_stop)
#    thread.start()
    while robot.get_input(index=4) == 0:
        #robot.sys["in4"]
        # if robot.sys["in3"] == 0:
        load()

        # robot.play(track=True, cmd="lmove", rel=0, x=459.000, y=6.000, z=298.000, a=2.85, b=0, vel=spd, accel=acel, jerk=torq, id=264)
        stby()
        time.sleep(t)
        # puntos de prueba iniciales
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=32.700, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=200)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=32.700, z=152.750, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=201)
        #p1.complete()
        print(robot.sys)
        #    print("comm complete")
        #
        d1 = robot.play(timeout=-1, cmd="output", out5=1, id=202)
        #d1.complete()

        print(d1)
        time.sleep(t)
        robot.play(timeout=-1,cmd="output", out5=0, id=203)
        print("punto 1")
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=32.700, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=204)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=28.800, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=205)
#PUNTO 2
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=28.800, z=152.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=206)
        #p2.complete(time_out=0)
        robot.play(timeout=-1, cmd="output", out5=1, id=207)
        #d2.complete()
        time.sleep(t)
        robot.play(timeout=-1,cmd="output", out5=0, id=208)
        print("punto 2")
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=28.800, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=209)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=24.600, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=210)
 #PUNTO 3
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=24.600, z=152.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=211)
        #p3.complete(time_out=0)
        robot.play(timeout=-1, cmd="output", out5=1, id=212)
        #d3.complete()
        time.sleep(t)
        robot.play(timeout=-1,cmd="output", out5=0, id=213)
        print("punto 3")
        robot.play(timeout=-1, cmd="lmove", rel=0, x=468.000, y=24.600, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=214)

    # puntos de ensamble PCB1
    # 1-L4
        # L4-1
        robot.play(timeout=-1, cmd="lmove", rel=0, x=408.394, y=47.117, z=152.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=215)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=408.394, y=47.117, z=150.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=216)
        #g1_1.complete(time_out=0)
        robot.play(timeout=-1, cmd="output", out5=1, id=217)
        #d4_1.complete()
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=218)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=408.394, y=47.117, z=152.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=219)

    # 1-C25
        # C25-1
        robot.play(timeout=-1, cmd="lmove", rel=0, x=387.153, y=38.054, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=225)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=387.153, y=38.054, z=150.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=226)
        #g3_1.complete(time_out=0)
        robot.play(timeout=-1, cmd="output", out5=1, id=227)
        #d6_1.complete()
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=228)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=387.153, y=38.054, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=229)
        # C25-2
        robot.play(timeout=-1, cmd="lmove", rel=0, x=382.22, y=40.983, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=230)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=382.22, y=40.983, z=150.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=231)
        #g4_1.complete(time_out=0)
        robot.play(timeout=-1, cmd="output", out5=1, id=232)
        #d7_1.complete()
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=233)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=382.22, y=40.983, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=234)

    # puntos de ensamble PCB2
    # 2-L4
        # L4-1
        robot.play(timeout=-1, cmd="lmove", rel=0, x=408.718, y=-9.391, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=264)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=408.718, y=-9.391, z=149.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=265)
        #g1_2.complete(time_out=0)
        robot.play(timeout=-1, cmd="output", out5=1, id=266)
        #d4_2.complete()
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=267)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=408.718, y=-9.391, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=268)

    # 2-c25
        # C25-1
        robot.play(timeout=-1, cmd="lmove", rel=0, x=388.424, y=-19.273, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=274)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=388.424, y=-19.273, z=149.478, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=275)
        #g3_2.complete(time_out=0)
        robot.play(timeout=-1, cmd="output", out5=1, id=276)
        #d6_2.complete()
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=277)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=388.424, y=-19.273, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=278)
        # C25-2
        robot.play(timeout=-1, cmd="lmove", rel=0, x=382.629, y=-15.636, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=279)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=382.629, y=-15.636, z=149.476, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=280)
        #g4_2.complete(time_out=0)
        robot.play(timeout=-1, cmd="output", out5=1, id=281)
        #d7_2.complete()
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=282)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=382.629, y=-15.636, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=283)

    # puntos de ensamble PCB3
    # 3-L4
        # L4-1
        robot.play(timeout=-1, cmd="lmove", rel=0, x=407.456, y=-66.422, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=314)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=407.456, y=-66.422, z=149.423, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=315)
        #g1_3.complete(time_out=0)
        robot.play(timeout=-1, cmd="output", out5=1, id=316)
        #d4_3.complete()
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=317)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=407.456, y=-66.422, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=318)

    # 3-C25
        # C25-1
        robot.play(timeout=-1, cmd="lmove", rel=0, x=387.472, y=-75.453, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=324)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=387.472, y=-75.453, z=149.42, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=325)
        #g3_3.complete(time_out=0)
        robot.play(timeout=-1, cmd="output", out5=1, id=326)
        #d6_3.complete()
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=327)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=387.472, y=-75.453, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=328)
        # C25-2
        robot.play(timeout=-1, cmd="lmove", rel=0, x=381.033, y=-71.95, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=329)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=381.033, y=-71.95, z=149.794, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=330)
        #g4_3.complete(time_out=0)
        robot.play(timeout=-1, cmd="output", out5=1, id=331)
        #d7_3.complete()
        time.sleep(t)
        robot.play(timeout=-1, cmd="output", out5=0, id=332)
        robot.play(timeout=-1, cmd="lmove", rel=0, x=381.033, y=-71.95, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=333)

        stby()
        # robot.play(track=True,cmd="lmove", rel=0, x=459.000, y=20.000, z=298.000, a=-0, b=0, vel=spd, accel=acel, jerk=torq, id=264)
        time.sleep(t)
        time.sleep(1)

        unload()

        #    robot.play(cmd="alarm",alarm=1, queue=1)
        # robot.close()


if __name__ == '__main__':
    robot = Dorna()
    robot.connect(host = "localhost", port = 443)
    p8678(40,1000,2500,0.5,0.5)
    robot.close()
