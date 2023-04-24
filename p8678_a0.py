#from dorna2 import dorna
import time
import stop
import threading


# from test_p import puntos
def p8678(self, v, a, tq, t1, t2):
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
        p1 = robot.play(track=True, cmd="lmove", rel=0, x=468.000, y=32.700, z=152.750, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=201)
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

        p2 = robot.play(track=True, cmd="lmove", rel=0, x=468.000, y=28.800, z=152.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=206)
        p2.complete(time_out=0)
        d2 = robot.play(track=True, cmd="output", out5=1, id=207)
        d2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=208)
        print("punto 2")
        robot.play(track=True, cmd="lmove", rel=0, x=468.000, y=28.800, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=209)
        robot.play(track=True, cmd="lmove", rel=0, x=468.000, y=24.600, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=210)
        p3 = robot.play(track=True, cmd="lmove", rel=0, x=468.000, y=24.600, z=152.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=211)
        p3.complete(time_out=0)
        d3 = robot.play(track=True, cmd="output", out5=1, id=212)
        d3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=213)
        print("punto 3")
        robot.play(track=True, cmd="lmove", rel=0, x=468.000, y=24.600, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=214)

    # puntos de ensamble PCB1
    # 1-s11
        # S11-1
        robot.play(track=True, cmd="lmove", rel=0, x=412.729, y=33.176, z=152.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=215)
        g1_1 = robot.play(track=True, cmd="lmove", rel=0, x=412.729, y=33.176, z=150.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=216)
        g1_1.complete(time_out=0)
        d4_1 = robot.play(track=True, cmd="output", out5=1, id=217)
        d4_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=218)
        robot.play(track=True, cmd="lmove", rel=0, x=412.729, y=33.176, z=152.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=219)
        # S11-2
        robot.play(track=True, cmd="lmove", rel=0, x=407.146, y=33.21, z=152.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=220)
        g2_1 = robot.play(track=True, cmd="lmove", rel=0, x=407.146, y=33.21, z=150.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=221)
        g2_1.complete(time_out=0)
        d5_1 = robot.play(track=True, cmd="output", out5=1, id=222)
        d5_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=223)
        robot.play(track=True, cmd="lmove", rel=0, x=407.146, y=33.21, z=152.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=224)
    # 1-S10
        # S10-1
        robot.play(track=True, cmd="lmove", rel=0, x=394.186, y=33.205, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=225)
        g3_1 = robot.play(track=True, cmd="lmove", rel=0, x=394.186, y=33.205, z=150.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=226)
        g3_1.complete(time_out=0)
        d6_1 = robot.play(track=True, cmd="output", out5=1, id=227)
        d6_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=228)
        robot.play(track=True, cmd="lmove", rel=0, x=394.186, y=33.205, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=229)
        # S10-2
        robot.play(track=True, cmd="lmove", rel=0, x=388.54, y=33.19, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=230)
        g4_1 = robot.play(track=True, cmd="lmove", rel=0, x=388.54, y=33.19, z=150.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=231)
        g4_1.complete(time_out=0)
        d7_1 = robot.play(track=True, cmd="output", out5=1, id=232)
        d7_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=233)
        robot.play(track=True, cmd="lmove", rel=0, x=388.54, y=33.19, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=234)
    # 1-S8
        # S8-1
        robot.play(track=True, cmd="lmove", rel=0, x=372.011, y=50.339, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=235)
        g5_1 = robot.play(track=True, cmd="lmove", rel=0, x=372.011, y=50.339, z=150.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=236)
        g5_1.complete(time_out=0)
        d8_1 = robot.play(track=True, cmd="output", out5=1, id=237)
        d8_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=238)
        robot.play(track=True, cmd="lmove", rel=0, x=372.011, y=50.339, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=239)
        # S8-2
        robot.play(track=True, cmd="lmove", rel=0, x=366.329, y=50.34, z=152.720, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=240)
        g6_1 = robot.play(track=True, cmd="lmove", rel=0, x=366.329, y=50.34, z=150.720, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=241)
        g6_1.complete(time_out=0)
        d9_1 = robot.play(track=True, cmd="output", out5=1, id=242)
        d9_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=243)
        robot.play(track=True, cmd="lmove", rel=0, x=366.329, y=50.34, z=152.720, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=244)
    # 1-S9
        # S9-2
        robot.play(track=True, cmd="lmove", rel=0, x=366.329, y=33.953, z=152.720, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=245)
        g7_1 = robot.play(track=True, cmd="lmove", rel=0, x=366.329, y=33.953, z=150.720, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=245)
        g7_1.complete(time_out=0)
        d10_1 = robot.play(track=True, cmd="output", out5=1, id=246)
        d10_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=247)
        robot.play(track=True, cmd="lmove", rel=0, x=366.329, y=33.953, z=152.720, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=248)
        # S9-1
        robot.play(track=True, cmd="lmove", rel=0, x=372.186, y=33.966, z=152.720, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=249)
        g8_1 = robot.play(track=True, cmd="lmove", rel=0, x=372.186, y=33.966, z=150.720, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=250)
        g8_1.complete(time_out=0)
        d11_1 = robot.play(track=True, cmd="output", out5=1, id=251)
        d11_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=252)
        robot.play(track=True, cmd="lmove", rel=0, x=372.186, y=33.966, z=152.720, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=253)
    # 1-S7
        # S7-1
        robot.play(track=True, cmd="lmove", rel=0, x=371.213, y=17.725, z=152.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=254)
        g9_1 = robot.play(track=True, cmd="lmove", rel=0, x=371.213, y=17.725, z=150.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=255)
        g9_1.complete(time_out=0)
        d12_1 = robot.play(track=True, cmd="output", out5=1, id=256)
        d12_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=256)
        robot.play(track=True, cmd="lmove", rel=0, x=371.213, y=17.725, z=152.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=258)
        # S7-2
        robot.play(track=True, cmd="lmove", rel=0, x=365.500, y=17.740, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=259)
        g10_1 = robot.play(track=True, cmd="lmove", rel=0, x=365.500, y=17.740, z=149.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=260)
        g10_1.complete(time_out=0)
        d13_1 = robot.play(track=True, cmd="output", out5=1, id=261)
        d13_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=262)
        robot.play(track=True, cmd="lmove", rel=0, x=365.500, y=17.740, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=263)

    # puntos de ensamble PCB2
    # 2-s8
        # S8-2
        robot.play(track=True, cmd="lmove", rel=0, x=365.150, y=-4.194, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=264)
        g1_2 = robot.play(track=True, cmd="lmove", rel=0, x=365.150, y=-4.194, z=149.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=265)
        g1_2.complete(time_out=0)
        d4_2 = robot.play(track=True, cmd="output", out5=1, id=266)
        d4_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=267)
        robot.play(track=True, cmd="lmove", rel=0, x=365.150, y=-4.194, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=268)
        # S8-1
        robot.play(track=True, cmd="lmove", rel=0, x=370.685, y=-4.185, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=269)
        g2_2 = robot.play(track=True, cmd="lmove", rel=0, x=370.685, y=-4.185, z=149.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=270)
        g2_2.complete(time_out=0)
        d5_2 = robot.play(track=True, cmd="output", out5=1, id=271)
        d5_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=272)
        robot.play(track=True, cmd="lmove", rel=0, x=370.685, y=-4.185, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=273)
    # 2-S9
        # S9-2
        robot.play(track=True, cmd="lmove", rel=0, x=365.545, y=-20.765, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=274)
        g3_2 = robot.play(track=True, cmd="lmove", rel=0, x=365.545, y=-20.765, z=149.478, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=275)
        g3_2.complete(time_out=0)
        d6_2 = robot.play(track=True, cmd="output", out5=1, id=276)
        d6_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=277)
        robot.play(track=True, cmd="lmove", rel=0, x=365.545, y=-20.765, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=278)
        # S9-1
        robot.play(track=True, cmd="lmove", rel=0, x=371.177, y=-20.756, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=279)
        g4_2 = robot.play(track=True, cmd="lmove", rel=0, x=371.177, y=-20.756, z=149.476, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=280)
        g4_2.complete(time_out=0)
        d7_2 = robot.play(track=True, cmd="output", out5=1, id=281)
        d7_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=282)
        robot.play(track=True, cmd="lmove", rel=0, x=371.177, y=-20.756, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=283)
    # 2-S10
        # S10-2
        robot.play(track=True, cmd="lmove", rel=0, x=387.284, y=-20.747, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=284)
        g5_2 = robot.play(track=True, cmd="lmove", rel=0, x=387.284, y=-20.747, z=149.686, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=285)
        g5_2.complete(time_out=0)
        d8_2 = robot.play(track=True, cmd="output", out5=1, id=286)
        d8_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=287)
        robot.play(track=True, cmd="lmove", rel=0, x=387.284, y=-20.747, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=288)
        # S10-1
        robot.play(track=True, cmd="lmove", rel=0, x=393.063, y=-20.780, z=151.600, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=289)
        g6_2 = robot.play(track=True, cmd="lmove", rel=0, x=393.063, y=-20.780, z=149.671, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=290)
        g6_2.complete(time_out=0)
        d9_2 = robot.play(track=True, cmd="output", out5=1, id=291)
        d9_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=292)
        robot.play(track=True, cmd="lmove", rel=0, x=393.063, y=-20.780, z=151.600, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=293)
    # 12-S11
        # S11-2
        robot.play(track=True, cmd="lmove", rel=0, x=406.245, y=-21.477, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=294)
        g7_2 = robot.play(track=True, cmd="lmove", rel=0, x=406.245, y=-21.477, z=149.914, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=295)
        g7_2.complete(time_out=0)
        d10_2 = robot.play(track=True, cmd="output", out5=1, id=296)
        d10_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=297)
        robot.play(track=True, cmd="lmove", rel=0, x=406.245, y=-21.477, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=298)
        # S11-1
        robot.play(track=True, cmd="lmove", rel=0, x=411.703, y=-21.441, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=299)
        g8_2 = robot.play(track=True, cmd="lmove", rel=0, x=411.703, y=-21.441, z=150.111, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=300)
        g8_2.complete(time_out=0)
        d11_2 = robot.play(track=True, cmd="output", out5=1, id=301)
        d11_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=302)
        robot.play(track=True, cmd="lmove", rel=0, x=411.703, y=-21.441, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=303)
    # 2-S7
        # S7-1
        robot.play(track=True, cmd="lmove", rel=0, x=370.243, y=-36.759, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=304)
        g9_2 = robot.play(track=True, cmd="lmove", rel=0, x=370.243, y=-36.759, z=149.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=305)
        g9_2.complete(time_out=0)
        d12_2 = robot.play(track=True, cmd="output", out5=1, id=306)
        d12_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=307)
        robot.play(track=True, cmd="lmove", rel=0, x=370.243, y=-36.759, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=308)
        # S7-2
        robot.play(track=True, cmd="lmove", rel=0, x=364.477, y=-36.765, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=309)
        g10_2 = robot.play(track=True, cmd="lmove", rel=0, x=364.477, y=-36.765, z=149.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=310)
        g10_2.complete(time_out=0)
        d13_2 = robot.play(track=True, cmd="output", out5=1, id=311)
        d13_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=312)
        robot.play(track=True, cmd="lmove", rel=0, x=364.477, y=-36.765, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=313)

    # puntos de ensamble PCB3
    # 3-s8
        # S8-1
        robot.play(track=True, cmd="lmove", rel=0, x=369.868, y=-59.661, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=314)
        g1_3 = robot.play(track=True, cmd="lmove", rel=0, x=369.868, y=-59.661, z=149.423, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=315)
        g1_3.complete(time_out=0)
        d4_3 = robot.play(track=True, cmd="output", out5=1, id=316)
        d4_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=317)
        robot.play(track=True, cmd="lmove", rel=0, x=369.868, y=-59.661, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=318)
        # S8-2
        robot.play(track=True, cmd="lmove", rel=0, x=364.115, y=-59.687, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=319)
        g2_3 = robot.play(track=True, cmd="lmove", rel=0, x=364.115, y=-59.687, z=149.442, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=320)
        g2_3.complete(time_out=0)
        d5_3 = robot.play(track=True, cmd="output", out5=1, id=321)
        d5_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=322)
        robot.play(track=True, cmd="lmove", rel=0, x=364.115, y=-59.687, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=323)
    # 3-S9
        # S9-2
        robot.play(track=True, cmd="lmove", rel=0, x=364.968, y=-76.217, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=324)
        g3_3 = robot.play(track=True, cmd="lmove", rel=0, x=364.968, y=-76.217, z=149.42, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=325)
        g3_3.complete(time_out=0)
        d6_3 = robot.play(track=True, cmd="output", out5=1, id=326)
        d6_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=327)
        robot.play(track=True, cmd="lmove", rel=0, x=364.968, y=-76.217, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=328)
        # S9-1
        robot.play(track=True, cmd="lmove", rel=0, x=370.639, y=-76.225, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=329)
        g4_3 = robot.play(track=True, cmd="lmove", rel=0, x=370.639, y=-76.225, z=149.794, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=330)
        g4_3.complete(time_out=0)
        d7_3 = robot.play(track=True, cmd="output", out5=1, id=331)
        d7_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=332)
        robot.play(track=True, cmd="lmove", rel=0, x=370.639, y=-76.225, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=333)
    # 3-S10
        # S10-2
        robot.play(track=True, cmd="lmove", rel=0, x=386.806, y=-76.230, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=334)
        g5_3 = robot.play(track=True, cmd="lmove", rel=0, x=386.806, y=-76.230, z=149.802, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=335)
        g5_3.complete(time_out=0)
        d8_3 = robot.play(track=True, cmd="output", out5=1, id=336)
        d8_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=337)
        robot.play(track=True, cmd="lmove", rel=0, x=386.806, y=-76.230, z=151.500, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=338)
        # S10-1
        robot.play(track=True, cmd="lmove", rel=0, x=392.306, y=-76.234, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=339)
        g6_3 = robot.play(track=True, cmd="lmove", rel=0, x=392.306, y=-76.234, z=150.023, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=340)
        g6_3.complete(time_out=0)
        d9_3 = robot.play(track=True, cmd="output", out5=1, id=341)
        d9_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=342)
        robot.play(track=True, cmd="lmove", rel=0, x=392.306, y=-76.234, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=343)
    # 3-S11
        # S11-2
        robot.play(track=True, cmd="lmove", rel=0, x=405.530, y=-77.359, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=344)
        g7_3 = robot.play(track=True, cmd="lmove", rel=0, x=405.530, y=-77.359, z=150.405, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=345)
        g7_3.complete(time_out=0)
        d10_3 = robot.play(track=True, cmd="output", out5=1, id=346)
        d10_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=347)
        robot.play(track=True, cmd="lmove", rel=0, x=405.530, y=-77.359, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=348)
        # S11-1
        robot.play(track=True, cmd="lmove", rel=0, x=411.078, y=-77.330, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=349)
        g8_3 = robot.play(track=True, cmd="lmove", rel=0, x=411.078, y=-77.330, z=150.402, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=350)
        g8_3.complete(time_out=0)
        d11_3 = robot.play(track=True, cmd="output", out5=1, id=351)
        d11_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=352)
        robot.play(track=True, cmd="lmove", rel=0, x=411.078, y=-77.330, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=353)
    # 3-S7
        # S7-1
        robot.play(track=True, cmd="lmove", rel=0, x=369.827, y=-92.328, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=354)
        g9_3 = robot.play(track=True, cmd="lmove", rel=0, x=369.827, y=-92.328, z=149.944, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=355)
        g9_3.complete(time_out=0)
        d12_3 = robot.play(track=True, cmd="output", out5=1, id=356)
        d12_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=357)
        robot.play(track=True, cmd="lmove", rel=0, x=369.827, y=-92.328, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=358)
        # S7-2
        robot.play(track=True, cmd="lmove", rel=0, x=364.148, y=-92.317, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=359)
        g10_3 = robot.play(track=True, cmd="lmove", rel=0, x=364.148, y=-92.317, z=149.939, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=360)
        g10_3.complete(time_out=0)
        d13_3 = robot.play(track=True, cmd="output", out5=1, id=361)
        d13_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=362)
        robot.play(track=True, cmd="lmove", rel=0, x=364.148, y=-92.317, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=363)

    # puntos de ensamble PCB4
    # 4-s8
        # S8-1
        robot.play(track=True, cmd="lmove", rel=0, x=369.799, y=-115.038, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=364)
        g1_4 = robot.play(track=True, cmd="lmove", rel=0, x=369.799, y=-115.038, z=149.936, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=365)
        g1_4.complete(time_out=0)
        d4_4 = robot.play(track=True, cmd="output", out5=1, id=366)
        d4_4.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=367)
        robot.play(track=True, cmd="lmove", rel=0, x=369.799, y=-115.038, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=368)
        # S8-2
        robot.play(track=True, cmd="lmove", rel=0, x=364.122, y=-115.039, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=369)
        g2_4 = robot.play(track=True, cmd="lmove", rel=0, x=364.122, y=-115.039, z=149.939, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=360)
        g2_4.complete(time_out=0)
        d5_4 = robot.play(track=True, cmd="output", out5=1, id=361)
        d5_4.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=362)
        robot.play(track=True, cmd="lmove", rel=0, x=364.122, y=-115.039, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=363)
    # 4-S9
        # S9-2
        robot.play(track=True, cmd="lmove", rel=0, x=364.956, y=-131.352, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=364)
        g3_4 = robot.play(track=True, cmd="lmove", rel=0, x=364.956, y=-131.352, z=149.958, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=365)
        g3_4.complete(time_out=0)
        d6_4 = robot.play(track=True, cmd="output", out5=1, id=366)
        d6_4.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=367)
        robot.play(track=True, cmd="lmove", rel=0, x=364.956, y=-131.352, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=368)
        # S9-1
        robot.play(track=True, cmd="lmove", rel=0, x=370.580, y=-131.366, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=369)
        g4_4 = robot.play(track=True, cmd="lmove", rel=0, x=370.580, y=-131.366, z=149.929, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=370)
        g4_4.complete(time_out=0)
        d7_4 = robot.play(track=True, cmd="output", out5=1, id=371)
        d7_4.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=372)
        robot.play(track=True, cmd="lmove", rel=0, x=370.580, y=-131.366, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=373)
    # 4-S10
        # S10-2
        robot.play(track=True, cmd="lmove", rel=0, x=386.707, y=-132.230, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=374)
        g5_4 = robot.play(track=True, cmd="lmove", rel=0, x=386.707, y=-132.230, z=150.463, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=375)
        g5_4.complete(time_out=0)
        d8_4 = robot.play(track=True, cmd="output", out5=1, id=376)
        d8_4.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=377)
        robot.play(track=True, cmd="lmove", rel=0, x=386.707, y=-132.230, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=378)
        # S10-1
        robot.play(track=True, cmd="lmove", rel=0, x=392.352, y=-132.227, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=379)
        g6_4 = robot.play(track=True, cmd="lmove", rel=0, x=392.352, y=-132.227, z=150.454, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=380)
        g6_4.complete(time_out=0)
        d9_4 = robot.play(track=True, cmd="output", out5=1, id=381)
        d9_4.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=382)
        robot.play(track=True, cmd="lmove", rel=0, x=392.352, y=-132.227, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=383)
    # 4-S11
        # S11-2
        robot.play(track=True, cmd="lmove", rel=0, x=405.478, y=-132.849, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=384)
        g7_4 = robot.play(track=True, cmd="lmove", rel=0, x=405.478, y=-132.849, z=150.932, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=385)
        g7_4.complete(time_out=0)
        d10_4 = robot.play(track=True, cmd="output", out5=1, id=386)
        d10_4.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=387)
        robot.play(track=True, cmd="lmove", rel=0, x=405.478, y=-132.849, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=388)
        # S11-1
        robot.play(track=True, cmd="lmove", rel=0, x=411.017, y=-132.834, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=389)
        g8_4 = robot.play(track=True, cmd="lmove", rel=0, x=411.017, y=-132.834, z=151.118, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=390)
        g8_4.complete(time_out=0)
        d11_4 = robot.play(track=True, cmd="output", out5=1, id=391)
        d11_4.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=392)
        robot.play(track=True, cmd="lmove", rel=0, x=411.017, y=-132.834, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=393)
    # 4-S7
        # S7-1
        robot.play(track=True, cmd="lmove", rel=0, x=369.805, y=-147.930, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=394)
        g9_4 = robot.play(track=True, cmd="lmove", rel=0, x=369.805, y=-147.930, z=150.239, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=395)
        g9_4.complete(time_out=0)
        d12_4 = robot.play(track=True, cmd="output", out5=1, id=396)
        d12_4.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=397)
        robot.play(track=True, cmd="lmove", rel=0, x=369.805, y=-147.930, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=398)
        # S7-2
        robot.play(track=True, cmd="lmove", rel=0, x=364.102, y=-147.352, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=399)
        g10_4 = robot.play(track=True, cmd="lmove", rel=0, x=364.102, y=-147.352, z=150.251, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=400)
        g10_4.complete(time_out=0)
        d13_4 = robot.play(track=True, cmd="output", out5=1, id=401)
        d13_4.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=402)
        robot.play(track=True, cmd="lmove", rel=0, x=364.102, y=-147.352, z=152.000, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=403)

        stby()
        # robot.play(track=True,cmd="lmove", rel=0, x=459.000, y=20.000, z=298.000, a=-0, b=0, vel=spd, accel=acel, jerk=torq, id=264)
        time.sleep(t)
        time.sleep(1)

        unload()

        #    robot.play(cmd="alarm",alarm=1, queue=1)
        # robot.close()


if __name__ == '__main__':
    p8678()
