player = ["jason","benjamin","bryian","shecid","allison","wendy"]
print("lista original",player)
#slicing
print(player[3:6]) #imprime desde el indice 3 hasta el 5
print(player[-3:6]) #imprime desde el indice -3 hasta el 5
print(player[3:]) #imprime desde el indice 3 hasta el final
print(player[:3]) #imprime desde el inicio hasta el indice 2    
a=3
b=6
print(player[a:b]) #imprime desde el indice 3 hasta el 5
my_food = ["pizza","hamburguesa","hot dog","tacos","sushi"]
my_friend_food = my_food #copia de la lista de manera erronea
my_friend_food_2 = my_food[:] #copia de la lista de manera correcta
my_friend_food_3 = my_food.copy() #copia de la lista de manera correcta
my_friend_food_4 = list(my_food) #copia de la lista de manera correcta