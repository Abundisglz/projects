#problema 1
"""
temp_c=float(input("Teclea la temperatura en grados celcius:"))
temp_f = temp_c * 9 / 5 + 32
temp_k = temp_c + 273.15
if temp_k < 0.0:
    print (f"la temperatura es alta:{temp_c>=30}")
    print(f"temperatura en farenhein:{temp_f}")
    print(f"temperatura en kelvin{temp_k}")

"""
""" 
#problema 2
pago = float(input("teclea cuanto se paga por hora:"))
print("si trabajaste cuarenta horas y veinte minutos teclea 40.20 la hora seria el numero entero y los minutos como decimales")
horas_trab=float(input("teclea las horas trabajadas:"))
pago_total = pago*horas_trab
horas_extras = horas_trab-40
pago_horas_extras= pago * horas_extras * 1.5 + pago_total
if horas_trab <= 40:
    print("Tu pago es regular")
    print(f"tu pago es de{pago_total}")
else:
    print ("Tu pago es overtime")
    print (f"Tu pago total es:{pago_horas_extras}")
    print (f"se hicieron horas extras:{horas_trab> 40}")
    print(f"las horas extras son:{horas_trab-40}")
"""
"""
problema 3
cliente =str(input("Teclea yes si es estudiante o senior:").lower().strip())
purchase_total =float(input("costo del producto:"))
if cliente == "yes" and cliente == "no" and purchase_total <=0:
    cliente_con_descuento = False
    cliente_con_descuento = cliente == "yes"
    su_compra_merece_descuento = False
    su_compra_merece_descuento = purchase_total >= 1000
    print(f"Merece descuento:{su_compra_merece_descuento or cliente_con_descuento}") 
    if cliente_con_descuento or su_compra_merece_descuento:
        purchase_total = purchase_total*.9
        print(f"Su compra es de:${purchase_total}")
    else:
        print(f"Su compra es de:${purchase_total}")
else:
    print("Error: Cliente no válido o compra no válida.")
    """
#problema 4
num_1=int(input("Teclea un numero:"))
num_2=int(input("Teclea otro numero:"))
num_3=int(input("Teclea otro numero:"))
suma = num_1 + num_2 + num_3
avarage = suma / 3
valor_max = max(num_1,num_2,num_3)
valor_min = min(num_1,num_2,num_3)
par = (num_1%2==0) and (num_2%2==0) and (num_3%2==0)
print(f"La suma es: {suma}")
print(f"El promedio es: {avarage}")
print(f"El valor maximo es: {valor_max}")
print(f"El valor minimo es: {valor_min}")
print(f"¿Los tres números son pares? {par}")