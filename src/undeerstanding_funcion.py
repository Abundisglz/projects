"""
username = input("Escribe el nombre del usuario:")
def great_to_person(name):
    ""Esta función recibe un nombre y devuelve un saludo personalizado.""
    print(f"Hola: {name.title()}")
great_to_person(username)
"""
def create_full_name(first_name, middle_name, last_name):
    """Esta función recibe un nombre y un apellido y devuelve el nombre completo."""
    full_name = f"{first_name} {middle_name} {last_name}"
    print(full_name.title())
while True:
    exit = input("Si deseas salir teclea si si quiere continuar teclea no:").strip().lower()
    if exit == "si":
        break
    try:
        first_name = str(input("Escribe tu primer nombre:").strip())
        middle_name = str(input("Escribe tu segundo nombre:").strip())
        last_name = str(input("Escribe tus apellidos:").strip())
        create_full_name(first_name, middle_name, last_name)
    except ValueError:
        print("Dato no valido")
#Tarea - como se mezclan positional y keyword arguments
