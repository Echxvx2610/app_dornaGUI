#from dorna2 import dorna
import time
import stop
import threading


# from test_p import puntos
def p31516(self, v, a, tq, t1, t2):
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
    dZ = 2.5

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
            print("Error el stopper esta arriba")
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
        robot.play(track=False, cmd="lmove", rel=0, x=467.721, y=-19.573, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=200)
        p1 = robot.play(track=True, cmd="lmove", rel=0, x=467.721, y=-19.573, z=152.000-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=201)
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
        robot.play(track=True, cmd="lmove", rel=0, x=467.721, y=-19.573, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=204)
        robot.play(track=True, cmd="lmove", rel=0, x=467.721, y=-23.714, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=205)

        p2 = robot.play(track=True, cmd="lmove", rel=0, x=467.721, y=-23.714, z=152.000-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=206)
        p2.complete(time_out=0)
        d2 = robot.play(track=True, cmd="output", out5=1, id=207)
        d2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=208)
        print("punto 2")
        robot.play(track=True, cmd="lmove", rel=0, x=467.721, y=-23.714, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=209)
        robot.play(track=True, cmd="lmove", rel=0, x=467.728, y=-26.984, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=210)
        p3 = robot.play(track=True, cmd="lmove", rel=0, x=467.728, y=-26.984, z=152.000-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=211)
        p3.complete(time_out=0)
        d3 = robot.play(track=True, cmd="output", out5=1, id=212)
        d3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=213)
        print("punto 3")
        robot.play(track=True, cmd="lmove", rel=0, x=467.728, y=-26.984, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=214)

    # puntos de ensamble PCB1
    # C132
        # C132-1
        robot.play(track=True, cmd="lmove", rel=0, x=353.633, y=35.361, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=215)
        g1_1 = robot.play(track=True, cmd="lmove", rel=0, x=353.633, y=35.361, z=148.700-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=216)
        g1_1.complete(time_out=0)
        d4_1 = robot.play(track=True, cmd="output", out5=1, id=217)
        d4_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=218)
        robot.play(track=True, cmd="lmove", rel=0, x=353.633, y=35.361, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=219)
        # C132-2
        robot.play(track=True, cmd="lmove", rel=0, x=344.448, y=35.366, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=220)
        g2_1 = robot.play(track=True, cmd="lmove", rel=0, x=344.448, y=35.366, z=148.700-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=221)
        g2_1.complete(time_out=0)
        d5_1 = robot.play(track=True, cmd="output", out5=1, id=222)
        d5_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=223)
        robot.play(track=True, cmd="lmove", rel=0, x=344.448, y=35.366, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=224)
    # L68
        # L68-1
        robot.play(track=True, cmd="lmove", rel=0, x=315.776, y=-9.003, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=225)
        g3_1 = robot.play(track=True, cmd="lmove", rel=0, x=315.776, y=-9.003, z=148.915-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=226)
        g3_1.complete(time_out=0)
        d6_1 = robot.play(track=True, cmd="output", out5=1, id=227)
        d6_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=228)
        robot.play(track=True, cmd="lmove", rel=0, x=315.776, y=-9.003, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=229)
        # L68-2
        robot.play(track=True, cmd="lmove", rel=0, x=315.770, y=-16.176, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=230)
        g4_1 = robot.play(track=True, cmd="lmove", rel=0, x=315.770, y=-16.176, z=148.915-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=231)
        g4_1.complete(time_out=0)
        d7_1 = robot.play(track=True, cmd="output", out5=1, id=232)
        d7_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=233)
        robot.play(track=True, cmd="lmove", rel=0, x=315.770, y=-16.176, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=234)
    # L38
        # L38-1
        robot.play(track=True, cmd="lmove", rel=0, x=338.818, y=-58.319, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=235)
        g5_1 = robot.play(track=True, cmd="lmove", rel=0, x=338.818, y=-58.319, z=148.900-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=236)
        g5_1.complete(time_out=0)
        d8_1 = robot.play(track=True, cmd="output", out5=1, id=237)
        d8_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=238)
        robot.play(track=True, cmd="lmove", rel=0, x=338.818, y=-58.319, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=239)
        # L38-2
        robot.play(track=True, cmd="lmove", rel=0, x=348.079, y=-54.830, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=240)
        g6_1 = robot.play(track=True, cmd="lmove", rel=0, x=348.079, y=-54.830, z=148.900-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=241)
        g6_1.complete(time_out=0)
        d9_1 = robot.play(track=True, cmd="output", out5=1, id=242)
        d9_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=243)
        robot.play(track=True, cmd="lmove", rel=0, x=348.079, y=-54.830, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=244)
    # L29
        # L29-1
        robot.play(track=True, cmd="lmove", rel=0, x=342.009, y=-77.065, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=245)
        g7_1 = robot.play(track=True, cmd="lmove", rel=0, x=342.009, y=-77.065, z=148.900-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=245)
        g7_1.complete(time_out=0)
        d10_1 = robot.play(track=True, cmd="output", out5=1, id=246)
        d10_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=247)
        robot.play(track=True, cmd="lmove", rel=0, x=342.009, y=-77.065, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=248)
        # L29-2
        robot.play(track=True, cmd="lmove", rel=0, x=329.870, y=-85.329, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=249)
        g8_1 = robot.play(track=True, cmd="lmove", rel=0, x=329.870, y=-85.329, z=148.900-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=250)
        g8_1.complete(time_out=0)
        d11_1 = robot.play(track=True, cmd="output", out5=1, id=251)
        d11_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=252)
        robot.play(track=True, cmd="lmove", rel=0, x=329.870, y=-85.329, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=253)
    # L27
        # L27-1
        robot.play(track=True, cmd="lmove", rel=0, x=352.962, y=-102.883, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=254)
        g9_1 = robot.play(track=True, cmd="lmove", rel=0, x=352.962, y=-102.883, z=149.150-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=255)
        g9_1.complete(time_out=0)
        d12_1 = robot.play(track=True, cmd="output", out5=1, id=256)
        d12_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=256)
        robot.play(track=True, cmd="lmove", rel=0, x=352.962, y=-102.883, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=258)
        # L27-2
        robot.play(track=True, cmd="lmove", rel=0, x=342.436, y=-113.014, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=259)
        g10_1 = robot.play(track=True, cmd="lmove", rel=0, x=342.436, y=-113.014, z=149.150-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=260)
        g10_1.complete(time_out=0)
        d13_1 = robot.play(track=True, cmd="output", out5=1, id=261)
        d13_1.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=262)
        robot.play(track=True, cmd="lmove", rel=0, x=342.436, y=-113.014, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=263)

    # C126
        # C126-1
        robot.play(track=True, cmd="lmove", rel=0, x=354.568, y=-98.572, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=264)
        g1_2 = robot.play(track=True, cmd="lmove", rel=0, x=354.568, y=-98.572, z=149.150-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=265)
        g1_2.complete(time_out=0)
        d4_2 = robot.play(track=True, cmd="output", out5=1, id=266)
        d4_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=267)
        robot.play(track=True, cmd="lmove", rel=0, x=354.568, y=-98.572, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=268)
        # C126-2
        robot.play(track=True, cmd="lmove", rel=0, x=354.993, y=-89.773, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=269)
        g2_2 = robot.play(track=True, cmd="lmove", rel=0, x=354.993, y=-89.773, z=149.150-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=270)
        g2_2.complete(time_out=0)
        d5_2 = robot.play(track=True, cmd="output", out5=1, id=271)
        d5_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=272)
        robot.play(track=True, cmd="lmove", rel=0, x=354.993, y=-89.773, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=273)
    # C705
        # C705-1
        robot.play(track=True, cmd="lmove", rel=0, x=354.996, y=-87.479, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=274)
        g3_2 = robot.play(track=True, cmd="lmove", rel=0, x=354.996, y=-87.479, z=149.100-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=275)
        g3_2.complete(time_out=0)
        d6_2 = robot.play(track=True, cmd="output", out5=1, id=276)
        d6_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=277)
        robot.play(track=True, cmd="lmove", rel=0, x=354.996, y=-87.479, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=278)
        # C705-2
        robot.play(track=True, cmd="lmove", rel=0, x=354.426, y=-79.264, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=279)
        g4_2 = robot.play(track=True, cmd="lmove", rel=0, x=354.426, y=-79.264, z=149.100-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=280)
        g4_2.complete(time_out=0)
        d7_2 = robot.play(track=True, cmd="output", out5=1, id=281)
        d7_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=282)
        robot.play(track=True, cmd="lmove", rel=0, x=354.426, y=-79.264, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=283)
    # C709
        # C709-1
        robot.play(track=True, cmd="lmove", rel=0, x=355.129, y=-76.932, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=284)
        g5_2 = robot.play(track=True, cmd="lmove", rel=0, x=355.129, y=-76.932, z=149.100-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=285)
        g5_2.complete(time_out=0)
        d8_2 = robot.play(track=True, cmd="output", out5=1, id=286)
        d8_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=287)
        robot.play(track=True, cmd="lmove", rel=0, x=354.129, y=-76.932, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=288)
        # C709-2
        robot.play(track=True, cmd="lmove", rel=0, x=355.115, y=-68.392, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=289)
        g6_2 = robot.play(track=True, cmd="lmove", rel=0, x=355.115, y=-68.392, z=149.100-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=290)
        g6_2.complete(time_out=0)
        d9_2 = robot.play(track=True, cmd="output", out5=1, id=291)
        d9_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=292)
        robot.play(track=True, cmd="lmove", rel=0, x=355.115, y=-68.392, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=293)
    # C704
        # C704-1
        robot.play(track=True, cmd="lmove", rel=0, x=357.503, y=-51.883, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=294)
        g7_2 = robot.play(track=True, cmd="lmove", rel=0, x=357.503, y=-51.883, z=149.100-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=295)
        g7_2.complete(time_out=0)
        d10_2 = robot.play(track=True, cmd="output", out5=1, id=296)
        d10_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=297)
        robot.play(track=True, cmd="lmove", rel=0, x=357.503, y=-51.883, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=298)
        # C704-2
        robot.play(track=True, cmd="lmove", rel=0, x=363.103, y=-52.186, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=299)
        g8_2 = robot.play(track=True, cmd="lmove", rel=0, x=363.103, y=-52.186, z=149.100-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=300)
        g8_2.complete(time_out=0)
        d11_2 = robot.play(track=True, cmd="output", out5=1, id=301)
        d11_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=302)
        robot.play(track=True, cmd="lmove", rel=0, x=363.103, y=-52.186, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=303)
    # C228
        # C228-1
        robot.play(track=True, cmd="lmove", rel=0, x=360.819, y=-62.426, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=304)
        g9_2 = robot.play(track=True, cmd="lmove", rel=0, x=360.819, y=-62.426, z=149.300-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=305)
        g9_2.complete(time_out=0)
        d12_2 = robot.play(track=True, cmd="output", out5=1, id=306)
        d12_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=307)
        robot.play(track=True, cmd="lmove", rel=0, x=360.819, y=-62.426, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=308)
        # C228-2
        robot.play(track=True, cmd="lmove", rel=0, x=369.716, y=-62.881, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=309)
        g10_2 = robot.play(track=True, cmd="lmove", rel=0, x=369.716, y=-62.881, z=149.300-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=310)
        g10_2.complete(time_out=0)
        d13_2 = robot.play(track=True, cmd="output", out5=1, id=311)
        d13_2.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=312)
        robot.play(track=True, cmd="lmove", rel=0, x=369.716, y=-62.881, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=313)
    # L120
        # L120-1
        robot.play(track=True, cmd="lmove", rel=0, x=365.402, y=-71.230, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=314)
        g1_3 = robot.play(track=True, cmd="lmove", rel=0, x=365.402, y=-71.230, z=149.400-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=315)
        g1_3.complete(time_out=0)
        d4_3 = robot.play(track=True, cmd="output", out5=1, id=316)
        d4_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=317)
        robot.play(track=True, cmd="lmove", rel=0, x=365.402, y=-71.230, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=318)
        # L120-2
        robot.play(track=True, cmd="lmove", rel=0, x=370.011, y=-82.974, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=319)
        g2_3 = robot.play(track=True, cmd="lmove", rel=0, x=370.011, y=-82.974, z=149.400-dZ, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=320)
        g2_3.complete(time_out=0)
        d5_3 = robot.play(track=True, cmd="output", out5=1, id=321)
        d5_3.complete()
        time.sleep(t)
        robot.play(cmd="output", out5=0, id=322)
        robot.play(track=True, cmd="lmove", rel=0, x=370.011, y=-82.974, z=154.700, a=ang, b=0, vel=spd, accel=acel, jerk=torq, id=323)
    # fin de referencias

        stby()
        # robot.play(track=True,cmd="lmove", rel=0, x=459.000, y=20.000, z=298.000, a=-0, b=0, vel=spd, accel=acel, jerk=torq, id=264)
        time.sleep(t)
        time.sleep(1)

        unload()

        #    robot.play(cmd="alarm",alarm=1, queue=1)
        # robot.close()


if __name__ == '__main__':
    p31516()
