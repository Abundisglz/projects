reprobada=input(f"¿Reprobaste la materia? (si/no): ")
reprobada = reprobada.lower().strip()
if reprobada == "si":
    print("El arturo se paso de lanza por una tarea me puso 54.")
elif reprobada == "no":
    print("¡Bien hecho! Sigue así.")
else:
    print("tu dato es incorrecto")

