motorcycle=['honda', 'yamaha', 'suzuki']
print(motorcycle)
motorcycle.append('ducati')
print(motorcycle)
motorcycle_2=[]
print(motorcycle)
mototorcycle = "ducati"
motorcycle_2.append(mototorcycle)
print(motorcycle_2)
motorcycle_2.append('kawasaki')
motorcycle_2.append('harley-davidson')
motorcycle_2.append('bmw')
print(motorcycle_2)
motorcycle = "meimei"
print(motorcycle_2)
motorcycle_3=['ducati', 'kawasaki', 'harley-davidson', 'bmw']
print ("\nLista original de motocicletas:")
print(motorcycle_3)
motorcycle_3.insert(0, 'suzuki')
#metodo pop
print ("\n\tAqui aprendi a utilizar el metodo pop".upper())
motorcycle_4=['ducati', 'kawasaki', 'harley-davidson', 'bmw']
print (motorcycle_4)
deleted_motorcycle = motorcycle_4.pop()#se guarda en la variable el elemento eliminado
print (f"Se elimino la motocicleta: {deleted_motorcycle}")
#ordenar listas variable.sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print (cars)
cars.sort()#ordena la lista de manera permanente en orden alfabetico
print (cars)
cars.sort(reverse=True)#ordena la lista de manera permanente en orden alfabetico inverso
print (cars)