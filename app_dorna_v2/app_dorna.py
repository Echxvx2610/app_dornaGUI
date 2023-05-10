#packages
import threading
import PySimpleGUI as sg
#from my_thread import principal
import time
from threading import *
#from p30538 import p30538
#from p30538_1A import p30538
#from p8678_a0 import p8678
from dorna_home_v2 import homming
from dorna_return_v2 import back
from dorna_zero_v2 import cero
from stop_v2 import stop
#from p31516 import p31516



#sys
def dorna_arm():
    #sg.theme_previewer() #ver paleta de temas
    sg.theme('GrayGrayGray')  # texto random para seleccionar tema al azar
    
    #***************************************************************\\FUNCIONES//************************************************************************************************
    def simulation():
        for i in range(10):
            time.sleep(1)
            print(i)
            if i == 9:
                window ['-TEXTBOX-'].update('Zero set Finalizado' + '\n' ,append=True)
    
    
    
    
    #****************************************VARIABLES************************************
    
    
    #********************************************************\\APP START//************************************************************************************************
    setup=[
        [sg.Push() ,sg.Text('Seleccione un Programa' ,text_color='Black') ,sg.Push()] ,
        [sg.Push() ,
        sg.Combo(
            # Lista de programa
             [
                 ['30538-1A'],
                 ['8678-1A'] ,
                 ['9104-1A'] ,
                 ['26156-1E'] ,
                 ['31516-1A']
            ] ,enable_events=True ,key='-COMBO-' ,size=(20 ,1)),sg.Push()] ,
        [sg.Text('Velocidad' ,text_color='Black')] ,
        [sg.Slider((0.0 ,500.0) ,resolution=0.1 ,tick_interval=250 ,orientation='h' ,default_value=0 ,s=(15 ,15) ,
                   key='-V-' ,enable_events=True) ,sg.Button('Set-V' ,key='-SETV-')] ,
        [sg.Text('Acceleracion' ,text_color='Black')] ,
        [sg.Slider((0 ,1000) ,tick_interval=2500 ,orientation='h' ,default_value=0 ,s=(15 ,15) ,key='-A-' ,
                   enable_events=True) ,sg.Button('Set-A' ,key='-SETA-')] ,
        [sg.Text('Torque' ,text_color='Black')] ,
        [sg.Slider((0 ,5000) ,tick_interval=2500 ,orientation='h' ,default_value=0 ,s=(15 ,15) ,key='-TQ-' ,
                   enable_events=True) ,sg.Button('Set-TQ' ,key='-SETTQ-')] ,
        [sg.Text('Tiempo Goma_ch' ,text_color='Black')] ,
        [sg.Slider((0 ,1) ,resolution=0.1 ,tick_interval=25 ,orientation='h' ,default_value=0 ,s=(15 ,15) ,
                   key='-GOMACH-' ,enable_events=True) ,sg.Button('Set-GCH' ,key='-SETGCH-')] ,
        [sg.Text('Tiempo Goma_gd' ,text_color='Black')] ,
        [sg.Slider((0 ,1) ,resolution=0.1 ,tick_interval=25 ,orientation='h' ,default_value=0 ,s=(15 ,15) ,
                   key='-GOMAG-' ,enable_events=True) ,sg.Button('Set-GG' ,key='-SETGG-')]
        ]
    

    display=[[sg.Text('Mensajes',key='-MENSAJES-',text_color='Black')],
             [sg.Multiline("" ,size=(57 ,10) ,no_scrollbar=False ,enable_events=True ,key='-TEXTBOX-')],
             [sg.HSeparator()],
             [
              sg.Button('Start' ,button_color=('Green3' ,'White') ,size=(10 ,2),border_width=10,mouseover_colors=('white','Green3'),expand_y=True,key='-START-') ,
              sg.Button('Stop' ,button_color=('white' ,'Orange') ,size=(10 ,2),border_width=10,mouseover_colors=('white','Orange') ,key='-STOP-'),
              sg.Button('Reset' ,button_color=('white' ,'Red') ,size=(10 ,2),border_width=10,mouseover_colors=('white','Red') ,key='-RESET-'),
              sg.Button('Quit' ,button_color=('Black' ,'Yellow') ,size=(10 ,2),border_width=10,mouseover_colors=('Black','Yellow') ,key='-QUIT-')
              ],
             [
              sg.Button('Zero Set',button_color=('white' ,'Blue1') ,size=(10 ,2),border_width=10,mouseover_colors=('white','Blue1') ,key='-ZERO-'),
              sg.Button('Inicializar Robot',button_color=('white' ,'SeaGreen') ,size=(10 ,2),border_width=10,mouseover_colors=('white','SeaGreen') ,key='-INICIALIZAR-'),
              sg.Button('Reposo',button_color=('white' ,'firebrick1') ,size=(10 ,2),border_width=10,mouseover_colors=('white','firebrick1') ,key='-REPOSO-')
              ]
             ]
             #[sg.Canvas(size=(410,300),background_color= 'black')]]
             #[sg.Image(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_dorna\img\dorna_ghost.png',key='-IMAGE-')]]  # 'dorna.gif',key='-IMAGE-')]]

    layout=[
        [sg.Column(setup),  # sg.vtop para tomar toda la columna y recorrerla hacia arriba
         sg.VSeparator(),
         sg.vtop(sg.Column(display,element_justification='c'))]]


    window = sg.Window('Dorna Arm',
                       layout,
                       element_justification='c',
                       icon= r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_dorna\img\dorna_mini.ico',
                       titlebar_icon= r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_dorna\img\dorna_mini.ico',resizable=True,size=((700,550)),finalize=True)
    window.set_min_size((250,550))
    

    #***************************************************************\\Bucle corre app//************************************************************************************************
    while True:
        event ,values=window.read()
        if event in (None ,'Cancel' ,'-QUIT-'): 
            break

        # window.Element('-IMAGE-').UpdateAnimation('dorna.gif',time_between_frames=60)

        #****************************************************************\\Eventos y valores de Sliders//******************************************************************************************************
        if event == '-V-':
            spd=values ['-V-']
            #print('V:' ,spd)
        if event == '-A-':
            accel=values ['-A-']
            #print('A:' ,accel)
        if event == '-TQ-':
            torq=values ['-TQ-']
            #print('TQ:' ,torq)
        if event == '-GOMACH-':
            goma_ch=values ['-GOMACH-']
            #print('Time Goma ch:' ,goma_ch)
        if event == '-GOMAG-':
            goma_g=values ['-GOMAG-']
            #print('Time Goma gd:' ,goma_g)

        # if event in '-V-' and '-A-' and '-TQ-':
        #    p = p8678(v=values['-V-'],a=values['-A-'],tq=values['-TQ-'],t1='0.5',t2='0.5')

        #***************************************************************\\Zero en Sliders//********************************************************************************************************************
        if event == '-SETV-':
            window ['-V-'].update(0)
            print('V:' ,values ['-V-'])
        if event == '-SETA-':
            window ['-A-'].update(0)
            print('A:' ,values ['-A-'])
        if event == '-SETTQ-':
            window ['-TQ-'].update(0)
            print('TQ:' ,values ['-TQ-'])
        if event == '-SETGCH-':
            window ['-GOMACH-'].update(0)
            print('Goma Ch:' ,values ['-GOMACH-'])
        if event == '-SETGG-':
            window ['-GOMAG-'].update(0)
            print('Goma Gd:' ,values ['-GOMAG-'])

        #*************************************************************\\Obtener valor de Combo(lista de programas)//**********************************************************************************************
        if event in '-COMBO-':
            if values ['-COMBO-'] == ['30538-1A']:
                window ['-TEXTBOX-'].update('Ensamble 30538-1A seleccionado' + '\n' ,append=True) 
            elif values ['-COMBO-'] == ['8678-1A']: 
                window ['-TEXTBOX-'].update('Ensamble 8678-1A seleccionado' + '\n' ,append=True) 
            elif values ['-COMBO-'] == ['9104-1A']: 
                window ['-TEXTBOX-'].update('Ensamble 9104-1A seleccionado' + '\n' ,append=True) 
            elif values ['-COMBO-'] == ['26156-1E']: 
                window ['-TEXTBOX-'].update('Ensamble 26156-1E seleccionado' + '\n' ,append=True) 
            elif values ['-COMBO-'] == ['31516-1A']: 
                window ['-TEXTBOX-'].update('Ensamble 31156-1A seleccionado' + '\n' ,append=True) 

        #***************************************************************\\Seleccion de programas//**********************************************************************************************
        if event == '-START-':
            if values ['-COMBO-'] == ['30538-1A']:
                hilo2=threading.Thread(target=simulation)
                hilo2.start()
                window ['-TEXTBOX-'].update('Zero set Iniciado' + '\n' ,append=True)
            elif values ['-COMBO-'] == ['8678-1A']:
                simulation()
            elif values ['-COMBO-'] == ['9104-1A']:
                simulation()
            elif values ['-COMBO-'] == ['26156-1E']:
                #def ejecuta_hilo():
                 #    principal()
                hilo = threading.Thread(target=principal)
                hilo.start()
                window ['-TEXTBOX-'].update('Zero set Iniciado' + '\n' ,append=True)
            elif values ['-COMBO-'] == ['31516-1A']:
                ensamble=p31516(v=spd ,a=accel ,tq=torq ,t=goma_ch ,t2=goma_g)
                print(ensamble.info_ensamble())

                # print(ensamble.info_ensamble())
                # hilo = Thread(target=p31516(v=spd,a=accel,tq=torq,t=goma_ch,t2=goma_g))
                # hilo.start()
        if event == '-ZERO-':
            cero()
            
        if event == '-INICIALIZAR-':
            homming()
            
        if event == '-REPOSO-':
            back()
        
                  
    # fin del bucle
    window.close()


if __name__=='__main__':
    dorna_arm()

