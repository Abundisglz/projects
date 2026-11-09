datos_ingrsados= []
counter=0
suma=0.0
while True:
    imports=input("introduce un importe, si desea salir teclear exit:").lower().replace(" ","")
    try:
        imports = float(imports)
        suma+=imports
        datos_ingrsados.append(imports) 
        counter+=1
    except:
        if imports in "exit":
            print("")
        else:
            print("el dato ingresado es incorrecto")
    if imports == "exit":
        print (f"estos son los datos que ingresaste:{datos_ingrsados}")
        print(f"la suma de tus datos es:{suma}")
        print(f"La cantidad de datos ingresados es:{counter}")
        print(f"El dato minimo ingresado es:{min(datos_ingrsados)}")
        print(f"El dato maximo ingresado es:{max(datos_ingrsados)}")
        break