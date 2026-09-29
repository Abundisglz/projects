import random 
J=int(input("cuantoss numero quieres generar:"))
while J > 0:
    i = random.randint(1, 6780)
    print(i)
    J = J - 1
    if J == 0:
        h=input("deseas generar mas numeros? (si/no):")
        if h == "si":
            j = int(input("cuantos numeros quieres generar:"))