import pygame
import serial
import time

# CAMBIA COM4 por el puerto de tu ESP32
esp32 = serial.Serial("COM4", 115200, timeout=0.1)

# Esperar a que la ESP32 reinicie
time.sleep(3)

pygame.init()

pantalla = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Control de motores ESP32")

ejecutando = True

try:
    while ejecutando:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    ejecutando = False

        teclas = pygame.key.get_pressed()

        # Motor izquierdo: W y D
        if teclas[pygame.K_w] and not teclas[pygame.K_d]:
            izquierda = 1
        elif teclas[pygame.K_d] and not teclas[pygame.K_w]:
            izquierda = -1
        else:
            izquierda = 0

        # Motor derecho: flechas arriba y abajo
        if teclas[pygame.K_UP] and not teclas[pygame.K_DOWN]:
            derecha = 1
        elif teclas[pygame.K_DOWN] and not teclas[pygame.K_UP]:
            derecha = -1
        else:
            derecha = 0

        # Enviar instrucciones a la ESP32
        comando = f"{izquierda},{derecha}\n"
        esp32.write(comando.encode())

        time.sleep(0.05)

finally:
    esp32.write(b"0,0\n")
    esp32.close()
    pygame.quit()