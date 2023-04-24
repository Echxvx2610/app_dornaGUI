#from dorna2 import dorna
import time
import stop
import threading


# from test_p import puntos
def p30538(self, v, a, tq, t1, t2):
    self.v = v
    self.a = a
    self.t = tq
    self.t1 = t1
    self.t2 = t2

    robot = dorna()
    ip = "dorna"
    port = 443
    robot.connect(ip, port)
    print("Conectado")
    print(stop.v_s)

    #   print(robot.sys)

    # spd = 300
    spd = v
    # acel = 1500
    acel = a
    # torq = 4000
    torq = tq
    t = t2
    ang = 2.385
    dZ = 1.8

    print(spd)
    print(acel)
    print(torq)
    print(t)

    def boton_stop():
        robot.wait(in4=1)
        robot.play(cmd="halt", id=1, accel=7.5)
        robot.play(cmd="alarm", alarm=1)
        robot.play(out5=0)
        print("robot stop, paro de emergencia presionado")

        robot.wait(in4=0)
        robot.play(cmd="alarm", alarm=0)
        print("robot run")

    def load():
        if robot.sys["in1"] == 1 and robot.sys["in2"] == 0:  # validamso que el stoper este arriba y clamp abierto
            robot.wait(in3=1)  # esperamos tarjeta en els ensor
            sm = robot.play(track=True, cmd="output", out3=0, id=50)  # abrimos la linea de SMEMA, cancelamos comunicacion NEXT
            sm.complete()
            time.sleep(1)
            cload = robot.play(track=True, cmd="output", out2=1, id=51)  # Cerramos clamp
            cload.complete()
            time.sleep(0.5)
            cstp = robot.play(track=True, cmd="output", out1=0, id=52)  # bajamos stopper
            cstp.complete()
        else:
            stp()

            # load()

    def unload():
        if robot.sys["in1"] == 0:  # validamos stopper abajo
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
        stp1 = robot.play(track=True, cmd="output", out1=1, id=53)
        stp1.complete()
        clmp = robot.play(track=True, cmd="output", out2=0, id=54)
        clmp.complete()
        load()

    def stby():
        w = robot.play(track=True, cmd="lmove", rel=0, x=459.000, y=6.000, z=298.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=100)
        w.complete()

    thread = threading.Thread(target=boton_stop)
    thread.start()
    while robot.sys["in4"] == 0:
        # if robot.sys["in3"] == 0:
        load()

        # robot.play(track=True, cmd="lmove", rel=0, x=459.000, y=6.000, z=298.000, a=2.85, b=0, vel=spd, accel=acel, jerk=torq, id=264)
        stby()
        time.sleep(t)
        # puntos de prueba iniciales
        robot.play(track=False, cmd="lmove", rel=0, x=468.000, y=32.700, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=200)
        p1 = robot.play(track=True, cmd="lmove", rel=0, x=468.000, y=32.700, z=151.200-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=201)
        p1.complete()
        print(robot.sys)
        #    print("comm complete")
        #
        d1 = robot.play(track=True, cmd="output", out5=1, id=202)
        d1.complete()
        print(d1.complete())
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=203)
        print("punto 1")
        robot.play(track=True, cmd="lmove", rel=0, x=468.000, y=32.700, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=204)
        robot.play(track=True, cmd="lmove", rel=0, x=468.000, y=28.800, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=205)

        p2 = robot.play(track=True, cmd="lmove", rel=0, x=468.000, y=28.800, z=151.200-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=206)
        p2.complete(time_out=0)
        d2 = robot.play(track=True, cmd="output", out5=1, id=207)
        d2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=208)
        print("punto 2")
        robot.play(track=True, cmd="lmove", rel=0, x=468.000, y=28.800, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=209)
        robot.play(track=True, cmd="lmove", rel=0, x=468.000, y=24.600, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=210)
        p3 = robot.play(track=True, cmd="lmove", rel=0, x=468.000, y=24.600, z=151.200-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=211)
        p3.complete(time_out=0)
        d3 = robot.play(track=True, cmd="output", out5=1, id=212)
        d3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=213)
        print("punto 3")
        robot.play(track=True, cmd="lmove", rel=0, x=468.000, y=24.600, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=214)

    # puntos de ensamble PCB1
    # L608
        # L608-1
        robot.play(track=True, cmd="lmove", rel=0, x=334.438, y=12.581, z=152.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=215)
        g1_1 = robot.play(track=True, cmd="lmove", rel=0, x=334.438, y=12.581, z=148.860-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=216)
        g1_1.complete(time_out=0)
        d4_1 = robot.play(track=True, cmd="output", out5=1, id=217)
        d4_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=218)
        robot.play(track=True, cmd="lmove", rel=0, x=334.438, y=12.581, z=152.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=219)
        # L608-2
        robot.play(track=True, cmd="lmove", rel=0, x=342.174, y=12.581, z=152.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=220)
        g2_1 = robot.play(track=True, cmd="lmove", rel=0, x=342.174, y=12.581, z=148.869-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=221)
        g2_1.complete(time_out=0)
        d5_1 = robot.play(track=True, cmd="output", out5=1, id=222)
        d5_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=223)
        robot.play(track=True, cmd="lmove", rel=0, x=342.174, y=12.581, z=152.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=224)
    # C132
        # C132-1
        robot.play(track=True, cmd="lmove", rel=0, x=346.876, y=34.549, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=225)
        g3_1 = robot.play(track=True, cmd="lmove", rel=0, x=346.876, y=34.549, z=148.919-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=226)
        g3_1.complete(time_out=0)
        d6_1 = robot.play(track=True, cmd="output", out5=1, id=227)
        d6_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=228)
        robot.play(track=True, cmd="lmove", rel=0, x=346.876, y=34.549, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=229)
        # C132-2
        robot.play(track=True, cmd="lmove", rel=0, x=350.941, y=25.471, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=230)
        g4_1 = robot.play(track=True, cmd="lmove", rel=0, x=350.941, y=25.471, z=148.915-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=231)
        g4_1.complete(time_out=0)
        d7_1 = robot.play(track=True, cmd="output", out5=1, id=232)
        d7_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=233)
        robot.play(track=True, cmd="lmove", rel=0, x=350.941, y=25.471, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=234)
    # C566
        # C566-1
        robot.play(track=True, cmd="lmove", rel=0, x=350.943, y=23.360, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=235)
        g5_1 = robot.play(track=True, cmd="lmove", rel=0, x=350.943, y=23.360, z=148.933-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=236)
        g5_1.complete(time_out=0)
        d8_1 = robot.play(track=True, cmd="output", out5=1, id=237)
        d8_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=238)
        robot.play(track=True, cmd="lmove", rel=0, x=350.943, y=23.360, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=239)
        # C566-2
        robot.play(track=True, cmd="lmove", rel=0, x=350.934, y=14.582, z=152.720, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=240)
        g6_1 = robot.play(track=True, cmd="lmove", rel=0, x=350.934, y=14.582, z=148.939-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=241)
        g6_1.complete(time_out=0)
        d9_1 = robot.play(track=True, cmd="output", out5=1, id=242)
        d9_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=243)
        robot.play(track=True, cmd="lmove", rel=0, x=350.934, y=14.582, z=152.720, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=244)
    # C567
        # C567-1
        robot.play(track=True, cmd="lmove", rel=0, x=350.930, y=12.857, z=152.720, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=245)
        g7_1 = robot.play(track=True, cmd="lmove", rel=0, x=350.930, y=12.857, z=148.911-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=245)
        g7_1.complete(time_out=0)
        d10_1 = robot.play(track=True, cmd="output", out5=1, id=246)
        d10_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=247)
        robot.play(track=True, cmd="lmove", rel=0, x=350.930, y=12.857, z=152.720, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=248)
        # C567-2
        robot.play(track=True, cmd="lmove", rel=0, x=350.939, y=3.997, z=152.720, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=249)
        g8_1 = robot.play(track=True, cmd="lmove", rel=0, x=350.939, y=3.997, z=148.929-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=250)
        g8_1.complete(time_out=0)
        d11_1 = robot.play(track=True, cmd="output", out5=1, id=251)
        d11_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=252)
        robot.play(track=True, cmd="lmove", rel=0, x=350.939, y=3.997, z=152.720, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=253)
    # C709
        # C709-1
        robot.play(track=True, cmd="lmove", rel=0, x=359.113, y=-43.398, z=152.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=254)
        g9_1 = robot.play(track=True, cmd="lmove", rel=0, x=359.113, y=-43.398, z=149.100-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=255)
        g9_1.complete(time_out=0)
        d12_1 = robot.play(track=True, cmd="output", out5=1, id=256)
        d12_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=256)
        robot.play(track=True, cmd="lmove", rel=0, x=359.113, y=-43.398, z=152.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=258)
        # C709-2
        robot.play(track=True, cmd="lmove", rel=0, x=359.113, y=-52.153, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=259)
        g10_1 = robot.play(track=True, cmd="lmove", rel=0, x=359.113, y=-52.153, z=149.121-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=260)
        g10_1.complete(time_out=0)
        d13_1 = robot.play(track=True, cmd="output", out5=1, id=261)
        d13_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=262)
        robot.play(track=True, cmd="lmove", rel=0, x=359.113, y=-52.153, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=263)

    # C705
        # C705-1
        robot.play(track=True, cmd="lmove", rel=0, x=359.111, y=-54.098, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=264)
        g1_2 = robot.play(track=True, cmd="lmove", rel=0, x=359.111, y=-54.098, z=149.121-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=265)
        g1_2.complete(time_out=0)
        d4_2 = robot.play(track=True, cmd="output", out5=1, id=266)
        d4_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=267)
        robot.play(track=True, cmd="lmove", rel=0, x=359.111, y=-54.098, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=268)
        # C705-2
        robot.play(track=True, cmd="lmove", rel=0, x=359.113, y=-63.002, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=269)
        g2_2 = robot.play(track=True, cmd="lmove", rel=0, x=359.113, y=-63.002, z=149.092-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=270)
        g2_2.complete(time_out=0)
        d5_2 = robot.play(track=True, cmd="output", out5=1, id=271)
        d5_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=272)
        robot.play(track=True, cmd="lmove", rel=0, x=359.113, y=-63.002, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=273)
    # L27
        # L27-1
        robot.play(track=True, cmd="lmove", rel=0, x=367.744, y=-84.326, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=274)
        g3_2 = robot.play(track=True, cmd="lmove", rel=0, x=367.744, y=-84.326, z=149.560-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=275)
        g3_2.complete(time_out=0)
        d6_2 = robot.play(track=True, cmd="output", out5=1, id=276)
        d6_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=277)
        robot.play(track=True, cmd="lmove", rel=0, x=367.744, y=-84.326, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=278)
        # L27-2
        robot.play(track=True, cmd="lmove", rel=0, x=378.296, y=-74.437, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=279)
        g4_2 = robot.play(track=True, cmd="lmove", rel=0, x=378.296, y=-74.437, z=149.562-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=280)
        g4_2.complete(time_out=0)
        d7_2 = robot.play(track=True, cmd="output", out5=1, id=281)
        d7_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=282)
        robot.play(track=True, cmd="lmove", rel=0, x=378.296, y=-74.437, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=283)
    # C126
        # C126-1
        robot.play(track=True, cmd="lmove", rel=0, x=374.048, y=-71.734, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=284)
        g5_2 = robot.play(track=True, cmd="lmove", rel=0, x=374.048, y=-71.734, z=149.755-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=285)
        g5_2.complete(time_out=0)
        d8_2 = robot.play(track=True, cmd="output", out5=1, id=286)
        d8_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=287)
        robot.play(track=True, cmd="lmove", rel=0, x=374.048, y=-71.734, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=288)
        # C126-2
        robot.play(track=True, cmd="lmove", rel=0, x=374.050, y=-62.787, z=151.600, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=289)
        g6_2 = robot.play(track=True, cmd="lmove", rel=0, x=374.050, y=-62.787, z=149.512-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=290)
        g6_2.complete(time_out=0)
        d9_2 = robot.play(track=True, cmd="output", out5=1, id=291)
        d9_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=292)
        robot.play(track=True, cmd="lmove", rel=0, x=374.050, y=-62.787, z=151.600, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=293)
    # L120
        # L120-1
        robot.play(track=True, cmd="lmove", rel=0, x=374.046, y=-58.340, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=294)
        g7_2 = robot.play(track=True, cmd="lmove", rel=0, x=374.046, y=-58.340, z=149.513-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=295)
        g7_2.complete(time_out=0)
        d10_2 = robot.play(track=True, cmd="output", out5=1, id=296)
        d10_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=297)
        robot.play(track=True, cmd="lmove", rel=0, x=374.046, y=-58.340, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=298)
        # L120-2
        robot.play(track=True, cmd="lmove", rel=0, x=369.691, y=-47.514, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=299)
        g8_2 = robot.play(track=True, cmd="lmove", rel=0, x=369.691, y=-47.514, z=149.319-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=300)
        g8_2.complete(time_out=0)
        d11_2 = robot.play(track=True, cmd="output", out5=1, id=301)
        d11_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=302)
        robot.play(track=True, cmd="lmove", rel=0, x=369.691, y=-47.514, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=303)
    # L29
        # L29-1
        robot.play(track=True, cmd="lmove", rel=0, x=371.882, y=-40.096, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=304)
        g9_2 = robot.play(track=True, cmd="lmove", rel=0, x=371.882, y=-40.096, z=149.323-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=305)
        g9_2.complete(time_out=0)
        d12_2 = robot.play(track=True, cmd="output", out5=1, id=306)
        d12_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=307)
        robot.play(track=True, cmd="lmove", rel=0, x=371.882, y=-40.096, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=308)
        # L29-2
        robot.play(track=True, cmd="lmove", rel=0, x=383.247, y=-31.260, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=309)
        g10_2 = robot.play(track=True, cmd="lmove", rel=0, x=383.247, y=-31.260, z=149.558-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=310)
        g10_2.complete(time_out=0)
        d13_2 = robot.play(track=True, cmd="output", out5=1, id=311)
        d13_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=312)
        robot.play(track=True, cmd="lmove", rel=0, x=383.247, y=-31.260, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=313)
    # C208
        # C208-1
        robot.play(track=True, cmd="lmove", rel=0, x=390.600, y=-42.696, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=314)
        g1_3 = robot.play(track=True, cmd="lmove", rel=0, x=390.600, y=-42.696, z=149.566-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=315)
        g1_3.complete(time_out=0)
        d4_3 = robot.play(track=True, cmd="output", out5=1, id=316)
        d4_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=317)
        robot.play(track=True, cmd="lmove", rel=0, x=390.600, y=-42.696, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=318)
        # C208-2
        robot.play(track=True, cmd="lmove", rel=0, x=399.670, y=-42.695, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=319)
        g2_3 = robot.play(track=True, cmd="lmove", rel=0, x=399.670, y=-42.695, z=149.833-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=320)
        g2_3.complete(time_out=0)
        d5_3 = robot.play(track=True, cmd="output", out5=1, id=321)
        d5_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=322)
        robot.play(track=True, cmd="lmove", rel=0, x=399.670, y=-42.695, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=323)
    # L38
        # L38-1
        robot.play(track=True, cmd="lmove", rel=0, x=413.467, y=-48.937, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=324)
        g3_3 = robot.play(track=True, cmd="lmove", rel=0, x=413.467, y=-48.937, z=150.256-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=325)
        g3_3.complete(time_out=0)
        d6_3 = robot.play(track=True, cmd="output", out5=1, id=326)
        d6_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=327)
        robot.play(track=True, cmd="lmove", rel=0, x=413.467, y=-48.937, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=328)
        # L38-2
        robot.play(track=True, cmd="lmove", rel=0, x=415.232, y=-40.238, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=329)
        g4_3 = robot.play(track=True, cmd="lmove", rel=0, x=415.232, y=-40.238, z=150.270-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=330)
        g4_3.complete(time_out=0)
        d7_3 = robot.play(track=True, cmd="output", out5=1, id=331)
        d7_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=332)
        robot.play(track=True, cmd="lmove", rel=0, x=415.232, y=-40.238, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=333)
    # C704
        # C704-1
        robot.play(track=True, cmd="lmove", rel=0, x=415.232, y=-24.201, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=334)
        g5_3 = robot.play(track=True, cmd="lmove", rel=0, x=415.232, y=-24.201, z=150.265-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=335)
        g5_3.complete(time_out=0)
        d8_3 = robot.play(track=True, cmd="output", out5=1, id=336)
        d8_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=337)
        robot.play(track=True, cmd="lmove", rel=0, x=415.232, y=-24.201, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=338)
        # C704-2
        robot.play(track=True, cmd="lmove", rel=0, x=409.620, y=-24.197, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=339)
        g6_3 = robot.play(track=True, cmd="lmove", rel=0, x=409.620, y=-24.197, z=150.199-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=340)
        g6_3.complete(time_out=0)
        d9_3 = robot.play(track=True, cmd="output", out5=1, id=341)
        d9_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=342)
        robot.play(track=True, cmd="lmove", rel=0, x=409.620, y=-24.197, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=343)
    # fin de referencias

        stby()
        # robot.play(track=True,cmd="lmove", rel=0, x=459.000, y=20.000, z=298.000, a=-0, b=0, vel=spd, accel=acel, jerk=torq, id=264)
        time.sleep(t)
        time.sleep(1)

        unload()

        #    robot.play(cmd="alarm",alarm=1, queue=1)
        # robot.close()


if __name__ == '__main__':
    p30538()
