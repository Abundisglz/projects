sum=0.0
menssage = """
    sistema gestor de acumulacion de valores
    La creatividad esta en tus manos.
    En todo momento, si quieres salir del programa
    puedes tipear q,e,quit,exit
    """
while True:
    value_txt = input(menssage).lower().replace(" ","")

    if value_txt in ['q','e','exit','quit']:
        break
    
