# Entender diccionarios
# Crear un diccionario de motocicletas
motocicletas = {'honda': 2024, 'yamaha': 2023, 'suzuki': 2022}
print(motocicletas)
# Agregar una motocicleta
motocicletas['ducati'] = 2025
print(motocicletas)
# Cambiar el valor de una motocicleta
motocicletas['yamaha'] = 2024
print(motocicletas)
# Comprobar si existe una clave usando in
print('honda' in motocicletas)
print('bmw' in motocicletas)
# Obtener un valor usando get()
print(motocicletas.get('honda'))
print(motocicletas.get('bmw'))
# Obtener un valor predeterminado si no existe la clave
print(motocicletas.get('bmw', 'No encontrada'))
# Eliminar una motocicleta usando pop()
motocicleta_eliminada = motocicletas.pop('suzuki')
print(motocicleta_eliminada)
print(motocicletas)
# Contar los elementos del diccionario
print(len(motocicletas))
# Crear un diccionario vacio
motocicletas_2 = {}
print(motocicletas_2)
# Agregar elementos al diccionario vacio
motocicletas_2['kawasaki'] = 2023
motocicletas_2['bmw'] = 2024
print(motocicletas_2)
# Crear un diccionario de precios
precios_productos = {'manzana': 10.0, 'platano': 15.0, 'naranja': 12.0}
nombre_producto = input("Escribe el nombre del producto:").strip().lower()
# Buscar un producto en el diccionario
if nombre_producto in precios_productos:
    print("Precio:", precios_productos.get(nombre_producto))
else:
    print("Producto no encontrado")
# Cambiar el precio de un producto
precios_productos['manzana'] = 12.0
print(precios_productos)
# Recorrer el diccionario y mostrar claves y valores
for producto, precio in precios_productos.items():
    print(producto, precio)
# Mostrar solamente las claves
print(precios_productos.keys())
# Mostrar solamente los valores
print(precios_productos.values())