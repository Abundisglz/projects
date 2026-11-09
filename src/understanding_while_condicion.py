"""
Realizar un programa en el que el usuario deba ingresar el pin de acceso
si el pin es correcto entonces el mensaje debe decir:
'ingreso autorizado'
'bienvenido a la upv'
si el pin es incorrecto; intentos restantes #'
si el usuario ha ingresado mas de tres veces el pin incorrecto entonces el mensaje debe decir:
'pin incorrecto, cuenta bloqueada
"""
PIN_CORRECTO = "1234"
MAX_INTENTOS = 3
intentos = 0
aceso = False
while intentos <MAX_INTENTOS:
    Pin_user=input("teclea el pin:")
    if Pin_user == PIN_CORRECTO:
        print("ingreso autorizado")
        aceso = True
        break
    intentos += 1
    restantes = MAX_INTENTOS - intentos
    if restantes > 0:
        print(f"pin incorrecto, intentos restantes {restantes}")
    else:
        print("pin incorrecto, cuenta bloqueada temporalmente")
if aceso:
    print("bienvenido a la upv")


