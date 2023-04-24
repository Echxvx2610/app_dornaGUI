import tkinter as tk
from tkinter import ttk
from dorna_home import home
from dorna_zero import cero
from dorna_return import back
#from main import main
from stop import stop, reset
#from tt import main
from p8678_a0 import p8678
from p30538_1A import p30538
from p31516_1A import p31516
import threading
import queue
#from dorna2 import dorna
from concurrent import futures


thread_pool_executor = futures.ThreadPoolExecutor(max_workers=10)
global robot
class Application(tk.Frame):


    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.place(relwidth=1, relheight=1)
        self.create_widgets()
#boton de inicio de robot
    def create_widgets(self):
        self.t_on = tk.Button(self, fg="blue", font="Arial 12 bold")
        self.t_on["text"] = "Inicializar Robot"
        self.t_on["command"] = self.say_hi
        self.t_on.place(x=20, y=20, width=140, height=50)

# boton de retorno a oringen o reposo
        self.back_origen = tk.Button(self,fg="blue", font="Arial 12 bold")
        self.back_origen["text"] = "Reposo"
        self.back_origen["command"]=self.back
        self.back_origen.place(x=190, y=20, width=100, height=50)

## boton de zero set, robot se va a coordenas 0 en todos los ejes
        self.zero_set = tk.Button(self, bg="Orange", font="Arial 12 bold")
        self.zero_set["text"] = "Zero set"
        self.zero_set["command"] = self.z_set
        self.zero_set.place(x=320, y=20, width=100, height=50)

## LIsta de programas
        self.titulobox = tk.Label(text="Seleccione un Programa", font="Arial 12")
        self.titulobox.place(x=20, y=100)

        self.sec = ttk.Combobox(self, values=["6187-1B","8678_1A","30538-1A","31516-1A"], font="Arial 12")
        self.sec.place(x=10, y=130,width=200, height=25)

## paramentros de robot
    #velocicad
        self.titulospeed = tk.Label(text="Velocidad", font="Arial 12")
        self.titulospeed.place(x=20, y=165)

        spd = tk.DoubleVar()

        self.speed = tk.Scale(orient='horizontal', length=200, from_=1.0, to=500.0, variable=spd, resolution=1, showvalue=0)
        self.speed.place(x=10,y=190, height= 25)
        self.speed.set(50)


        self.speedbox = tk.Label(textvariable=spd, font="Arial 12")
        self.speedbox.place(x=140, y=165, width=50)


    #Aceleracion
        self.tituloacel = tk.Label(text="Aceleracion", font="Arial 12")
        self.tituloacel.place(x=20, y=225)

        acel = tk.DoubleVar()

        self.acel = tk.Scale(orient='horizontal', length=200, from_=1.0, to=10000.0, variable=acel, resolution=1,
                              showvalue=0)
        self.acel.place(x=10, y=250, height=25)
        self.acel.set(1000)

        self.acelbox = tk.Label(textvariable=acel, font="Arial 12")
        self.acelbox.place(x=140, y=225, width=50)

    #Torque
        self.titulotorque = tk.Label(text="Torque", font="Arial 12")
        self.titulotorque.place(x=20, y=275)

        tor = tk.DoubleVar()

        self.torque = tk.Scale(orient='horizontal', length=200, from_=1.0, to=50000.0, variable=tor, resolution=1,
                             showvalue=0)
        self.torque.place(x=10, y=300, height=25)
        self.torque.set(5000)

        self.torquebox = tk.Label(textvariable=tor, font="Arial 12")
        self.torquebox.place(x=140, y=275, width=50)

    #tiempo Goma Chica
        self.t1label = tk.Label(text = "Tiempo Goma Chica", font = "Arial 12")
        self.t1label.place(x=20, y=325)

        t1 = tk.DoubleVar()

        self.t1scale = tk.Scale(orient='horizontal', length=200, from_=0.1, to=2.0, variable=t1, resolution=0.1, showvalue=0)
        self.t1scale.place(x=10, y=350, height=25)
        self.t1scale.set(0.5)
        self.t1box = tk.Label(textvariable=t1, font="Arial 12")
        self.t1box.place(x=180, y=325)

    # tiempo Goma Grande
        self.t2label = tk.Label(text="Tiempo Goma Grande", font="Arial 12")
        self.t2label.place(x=20, y=375)

        t2 = tk.DoubleVar()

        self.t2scale = tk.Scale(orient='horizontal', length=200, from_=0.1, to=2.0, variable=t2, resolution=0.1,
                                showvalue=0)
        self.t2scale.place(x=10, y=400, height=25)
        self.t2scale.set(1)
        self.t2box = tk.Label(textvariable=t2, font="Arial 12")
        self.t2box.place(x=180, y=375)


    # text box
        self.titulobox = tk.Label(text="Mensajes", font="Arial 12")
        self.titulobox.place(x=450, y=25)

        self.scrollcaja = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.caja = tk.Text(width=50, height=20, yscrollcommand=self.scrollcaja.set)
        self.caja.place(x=450, y=50)
        self.caja.configure(yscrollcommand = self.scrollcaja.set)
        #mensaje(self)

        #self.caja.insert(robot.sys())

## Boton de inicio de programa
        self.run = tk.Button(self, font="Arial 12 bold", fg="green", bd=2)
        self.run["text"]= "START"
        self.run["command"]= self.inicio
        v_run = "Running..."
        #self.run.pack(after=self.sec, padx='6 0')
        self.run.place(x=250, y=100, width=100, height=50)

##Boton de paro de robot
        self.stop = tk.Button(self,font="Arial 12 bold", fg="yellow",bg="red", bd=4)
        self.stop["text"]="STOP"
        self.stop["command"]= self.alto
        v_alto = "Robot Detenido"
        self.stop.place(x=30, y=445, width=100, height=50)

# boton de reset alarm
        self.reset = tk.Button(self, font="Arial 12 bold", fg="blue", bg="gray", bd=4)
        self.reset["text"] = "RESET"
        self.reset["command"] = self.r_set
        self.reset.place(x=150, y=445, width=100, height=50)

###boton de salir
        self.quit = tk.Button(self, text="QUIT",
                              fg="red",
                              font="Arial 12 bold",
                              command=root.destroy)
        self.quit.place(x=280, y=445, width=50, height=50)
# Seleccion de programa a correr
    def inicio(self):
        reset()
        #self.mensaje("Running...")
        if self.sec.get() == "8678_1A":
            thread_pool_executor.submit(p8678(self,self.speed.get(),self.acel.get(),self.torque.get(),self.t1scale.get(),self.t2scale.get()))
           #                      kwargs={'thread_queue':q})

            #p1 = threading.Thread(p8678(self,self.speed.get(),self.acel.get(),self.torque.get(),self.t1scale.get(),self.t2scale.get()),
            #                      kwargs={'thread_queue':q})
            #p1.setDaemon(True)
            #p1.start()
            self.after(100, self.listen_result)

        elif self.sec.get() == "6187-1B":
            thread_pool_executor.submit(p8678(self, self.speed.get(), self.acel.get(), self.torque.get(), self.t1scale.get(), self.t2scale.get()))
            #p2 = threading.Thread(p8678(self, self.speed.get(), self.acel.get(), self.torque.get(), self.t1scale.get(), self.t2scale.get()))
            #p2.setDaemon(True)
            #p2.start()

        elif self.sec.get() == "30538-1A":
            thread_pool_executor.submit(p30538(self, self.speed.get(), self.acel.get(), self.torque.get(), self.t1scale.get(), self.t2scale.get()))
            #p2 = threading.Thread(p8678(self, self.speed.get(), self.acel.get(), self.torque.get(), self.t1scale.get(), self.t2scale.get()))
            #p2.setDa
        elif self.sec.get() == "31516-1A":
            thread_pool_executor.submit(p31516(self, self.speed.get(), self.acel.get(), self.torque.get(), self.t1scale.get(), self.t2scale.get()))

        else:
            print(" ")

    def listen_result(self):
        try:
            res = q.get(0)
            #print(res)
            #self.mensaje(res)
            #self.text_label.config(text=res)

        except q.empty():
            self.after(100, self.listen_result)




# orden de hacer home al robot
    def say_hi(self):
        home()
        #print("Robot Encendido")

    def alto(self):
        stop()
        #self.mensaje("Robot Detenido")
        self.caja.insert(tk.END,"Robot detenido\n")
        #print("robot se ha detenido")

    def back(self):
        back()
        self.caja.insert(tk.END,"robot en origen\n")


    def r_set(self):
        reset()
        self.caja.insert(tk.END,"Robot habilitado\n")


    def z_set(self):
        cero()
        self.caja.insert(tk.END,"Robot en Zero\n")

    def setting(self):
        speed = self.speed.get()
        acele = self.acel.get()
        torq = self.torque.get()
        tc = self.t1scale.get()
        tg = self.t2scale.get()
        return speed,acele,torq,tc,tg



root = tk.Tk()
root.title("Robot para goma SMT")
root.geometry('900x600')
root.resizable(0,0)
#thread = threading.Thread(target=Application)
#thread.start()
# Barra de mensase inferior
#def mensaje(self):
        #self.status=tk.Label(self, text=txt, bd=1, relief='sunken', anchor='w', font="curiel 12")
        #self.status.place(x=0, y=500,width=800, height=30)
        #print("programa iniciado")
#    global robot
#    robot = dorna()
#    ip = "dorna"
#    port = 443
#    robot.connect(ip, port)
#    while True:
#        if not robot.msg.empty():
#            self.caja.insert(tk.END,robot.msg.get())

q = queue.Queue()

app = Application(master=root)

app.mainloop()