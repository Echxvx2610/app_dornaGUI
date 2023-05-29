import threading
import time



class p31516:
    def __init__(self,v=0,a=0,tq=0,t=0.0,t2=0.0):
        self.v = v
        self.a = a
        self.tq = tq
        self.t = t
        self.t2 = t2

    def info_ensamble(self):
        return self.v,self.a,self.tq,self.t,self.t2
    
#print(ensamble.info_ensamble())

if __name__=='__main__':
    p31516()