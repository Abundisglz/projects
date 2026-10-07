#Todavia no crearemos listas
#range() es un metodo built-in que nos permite crear una secuencia de numeros
first_ten_numbers = range(1,11) #Es de tipo range, no es una lista
for value in range(1,6):#ciclo for que itera sobre un rango de numeros del 1 al 5
    print(value)
a=int(input("ingrese el numero inicial: "))
b=int(input("ingrese el numero final: "))
b+=1
for value in range(a,b):#ciclo for que itera sobre un rango de numeros del a al b
    print(value)
numbers = list(range(0,10))#crea una lista de numeros del 0 al 9
print(numbers)
#numeros pares
even_numbers = list(range(0,10,2))#crea una lista de numeros pares del 2 al 10
print(even_numbers)
odd_numbers = list(range(1,10,2))#crea una lista de numeros impares del 1 al 9
print(odd_numbers)
