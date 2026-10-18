""" Portada
Nombre: Angel Abundis, Matricula: 2630351, Grupo: 1-3
"""
"""Resumen ejecutivo
 Planteamiento de problema:En este problema dominare el uso de strings en Python
 creación, lectura, indexación, slicing, concatenación, búsqueda, reemplazo, división,
 unión y formato de texto. Además, que pueda validar y transformar entradas de usuario 
 Solucion propuesta: Estudiar los metodos de strings y aplicarlos en este programa que me permitira
 manipular cadenas de texto.
 Publico:Carlos tovar (profe charly mercury)
 """
#Problem 1:full name formatter(name+initials)
full_name = input("Inserta tu nombre completo:")
print (full_name)
print(full_name.strip())
print(full_name.lower())
print(full_name.title())
first_letter = " ".join(word[0]for word in full_name.split())
print (first_letter)
#problem 2:simple email validator (structure + domain)
email_text = input("Inserta tu correo:")
if email_text.count("@") == 1:
    print("valid email: True")
else:
    print("valid email: False")
if " " in email_text or email_text.strip() == "":
    print("valid email: False")
print(f"cuantos arrobas hay en el correo @:{email_text.count('@')}")
#Problem 3: Palindrome checker (ignoring spaces and case)

word_palindrome = input("Inserta una palabra para verificar si es un palindromo:").lower()
if word_palindrome.replace(" ", "")== word_palindrome.replace(" ", "")[::-1] :
    print("Es un palindromo")
else:
    print("No es un palindromo")
# Problem 4: Sentence word stats (lengths and first/last word)
words = input("Escribe una oracion:")
print(words.lstrip())
print(words.rstrip())
words = words.strip()
word = words.split()
num_words = len(word)
print (f"word count:{num_words}")
print(f"first word:{word[0]}")
print(f"last word:{word[-1]}")
"""
   min busca el valor mas pequeño 
   key len hace que cuente letra por letra de las palabras si yo
   no lo usara contaria el valor unicode
"""
print(f"shortest word:{min(word,key=len)}")
print(f"longest word:{max(word,key=len)}")
#7.5 Problem 5: Password strength classifier
password = str(input("Escribe tu contraseña:"))
uppercase = False
lowercase = False
number = False 
character_special = False
if " " in password:
    print("invalide password")
else:
    counter_letter_password = len(password)
    for letter in password:
        if letter.isupper():
            uppercase = True
        elif letter.islower:
            lowercase = True
        elif letter.isdigit():
            number = True
        else :
            character_special = True    
    if 8 > counter_letter_password or password == password.lower():
        print("Your password is weak")
    elif 8<=counter_letter_password and uppercase and lowercase and number:
        print("Your password is medium")
    elif 8<=counter_letter_password and uppercase and lowercase and number and character_special:
        print("Your password is strong")
#7.6 Problem 6: Product label formatter (fixed-width text)
product = (input("Escribe el nombre del producto:")) 
price = (input("Teclea el precio:"))
if product.strip() != "" and price.isnumeric():
    product_and_price = f"{product}|${price}"
    print(product_and_price)
    product_and_price = product_and_price[:30]
    product_and_price =product_and_price + " " * (30 - len(product_and_price))
    print(f"'{product_and_price}'")
else:
    print ("invalide text")