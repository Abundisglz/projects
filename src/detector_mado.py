"""Programa para detectar un mando de PS4 y enviar las velocidades de los joysticks a un ESP32"""
#Aqui mando a llamar las librerias necesarias
import pygame
import time
import serial

# inicializo las librerias de pygame y el modulo de joysticks
pygame.init()
pygame.joystick.init()

#Esta es la conexion con la esp32 (benja busca cual es el puerto de tu lap y cambialo en donde dice com10)
ESP32 = serial.Serial("COM10", 115200, timeout=0.1)
#defino la variable mando como none para que no haya ningun mando conectado al inicio
mando = None
#inicie un try para que en caso de que haya un error, se cierre la conexion con la esp32 y se cierre pygame
try:
    #Este while contine el codigo completo
    while True:
        #la linea 21 es para que pygame detecte el mando 
        pygame.event.pump()
        #detecta la cantidad de mandos conectados
        cantidad = pygame.joystick.get_count()
        #si hay un mando conectado y la variable mando es None, entonces se inicializa el mando y
        #se imprime el nombre del mando conectado
        if cantidad > 0 and mando is None:
            #se agrega el mando a la variable mando y se inicializa
            mando = pygame.joystick.Joystick(0)
            mando.init()
            #imprime el nombre del mando conectado
            print("MANDO CONECTADO:", mando.get_name())
        #detecta si se deconecto el mando
        elif cantidad == 0 and mando is not None:
            print("MANDO DESCONECTADO")
            mando = None
        #lee los valores de movimiento de los joysticks
        if mando is not None:
            eje_1 = int(mando.get_axis(1) * -10)
            eje_2 = int(mando.get_axis(3) * -10)
            eje_1 = max(-10, min(10, eje_1))
            eje_2 = max(-10, min(10, eje_2))
            #agrega zona muerta por si no movemos el control el robot este quieto
            if abs(eje_1) <= 1:
                eje_1 = 0

            if abs(eje_2) <= 1:
                eje_2 = 0
            #muestra en consola los valores de los joysticks    
            print("Joystick:", eje_1, eje_2)
            #envia los valores a la esp32 para enviarlos a los motores
            ESP32.write(f"{eje_1},{eje_2}\n".encode())
            #agregue una salida que es con el circulo y creo que en xbox es el B
            if mando.get_button(1):
                print("BOTON CIRCULO PRESIONADO")
                break
        else:
            #si no hay mando se queda quieto el robot
            ESP32.write(b"0,0\n")
finally:
    #detiene el robot y cierra la conexion con la esp32 y pygame
    ESP32.write(b"0,0\n")
    ESP32.close()
    pygame.quit()