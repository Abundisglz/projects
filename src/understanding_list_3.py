print ("\n\t hoy trabajare cin listas otra vez :(")
magicians =["harry","ron","hermione","snape","voldemort"]
print (magicians)
print ("\n\timprimir mal cada dato")
print (magicians[0],magicians[1],magicians[2],magicians[3],magicians[4])
print ("\n\timprimir bien cada dato")
for magician in magicians:#poner el singular de la lista
    print(magician,end=" ")#imprime en la misma linea
print()
for magician in magicians:
    print(f"{magician.title()} ese fue un gran hechizo")#imprime en la misma linea
    print(f"no puedo esperar a ver tu proximo hechizo {magician.upper()}\n")#imprime en la misma linea
print ("gracias a todos. Fue un gran espectaculo")
