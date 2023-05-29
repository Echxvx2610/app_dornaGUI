'''
# import module
from threading import *
import time


# creating a function
def thread_1():
    for i in range(5):
        print('this is non-daemon thread')
        time.sleep(2)


# creating a thread T
T = Thread(target=thread_1)

# starting of thread T
T.start()

# main thread stop execution till 5 sec.
time.sleep(1)
print('main Thread execution')
print(time.perf_counter())
print(time.localtime())

'''

#utilizamos Triple comilla para comentar varias lineas de codigo


from threading import *
import time

stop_principal = False

def principal():
    def second_plane():
        for i in range(11):
            print(i)
            time.sleep(1)
            if i==10:
                print('Second plane completed')

    hilo = Thread(target=second_plane,daemon=True) #si daemon is True,el hilo secundario se detiene cuando el hilo principal se termina de ejecutar,en este caso como solo imprimimos un texto el paro fue inmediato
    hilo.start()
    #hilo.join()
    time.sleep(11) #se detiene el hilo secundario hasta que se termina de ejecutar el hilo principal,pasando los 11 segundos
    print('First plane returned')

#al trabajar con hilos el script principal es el hilo principal, cuando creamos un hilo secundario se ejecutara y regresaremos al hilo principal, en pocas palabras no podremos utilizar el hilo principal hasta que termine el secundario
# si deseamos lo contrario detener el secundario o seguir utilizando el principal tenemos que definir al hilo secundario como un hilo deamon(deamon=True)

if __name__=="__main__":
    principal()