# app_dornaGUI
App GUI para robot dorna 2 (desarollada con python,pysimplegui)

La Utilidad que se le dio al robot dorna fue apoyando en el proceso de frabicacion de PCB's SMD,colocando goma en la base de componentes SMD "pesados" que pueden moverse o caerse del PCB en el proceso final de Coccion de la soldadura
Dicha app funciona de la siguiente forma:
Se generan los "programas" o scripts que utilizara el robot dorna,desde la GUI se selecciona el programa,se definen los parametros de Velocidad,Aceleracion,Torque,Tiempos de goma y empieza la ejecucion de dicho programa,los programas en si consisten en
coordenadas y llamadas a la API de Dorna 2, tambien se aplica el uso de hilos o pools de hilos para poder ejecutar un script en "segundo plano" y poder seguir controlando la GUI.
