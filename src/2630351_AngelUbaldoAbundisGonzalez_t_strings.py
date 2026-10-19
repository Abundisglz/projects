"""Name: Angel Abundis, Student ID: 2630351, Group: 1-3"""
"""Executive Summary
In this activity I will practice using strings in Python.
Strings are used to store and work with text.
I will use methods to change letters, remove spaces and split words.
I will also use indexing, slicing and f-strings.
These tools help us organize and display information.
I will make six small programs to practice these topics.
I will also check some user inputs with simple conditions.
"""
# Best practices:
# Use strip() to remove extra spaces.
# Use lower() when comparing text without caring about uppercase letters.
# Use string methods to make working with text easier.
# Check user input before using it.
# Use clear messages so the user knows what to enter.
# Strings cannot be changed directly, so methods return a new string.
# Problem 1: Full name formatter (name + initials)
# Description: This program shows different ways to format a full name.
# Inputs: The user's full name.
# Outputs: The original name, name without extra spaces, lowercase,
# title case, and the initials.
# Validations: The name should not be empty after removing extra spaces.
# Test case 1-Normal: "Angel Abundis"
# Expected result: Shows the name and the initials A A.
# Test case 2-Border: "Angel"
# Expected result: Shows the name and the initial A.
# Test case 3-Error: An empty input.
# Expected result: The program does not have a specific empty-input check.
full_name = input("Enter your full name: ")
print(full_name)
print(full_name.strip())
print(full_name.lower())
print(full_name.title())
first_letter = " ".join(word[0]for word in full_name.split())
print(first_letter)
# Problem 2: Simple email validator (structure + domain)
# Description: This program checks how many @ symbols are in an email.
# Inputs: An email address.
# Outputs: Whether the email is valid and the number of @ symbols.
# Validations: Checks that there is one @ and no spaces.
# Test case 1 - Normal: "angel@gmail.com"
# Expected result: Shows valid email: True.
# Test case 2 - Border: "a@b"
# Expected result: Shows valid email: True because the code only checks @.
# Test case 3 - Error: "angel gmail.com"
# Expected result: Shows valid email: False.

email_text = input("Enter your email: ")
if email_text.count("@") == 1:
    print("Valid email: True")
else:
    print("Valid email: False")
if " " in email_text or email_text.strip() == "":
    print("Valid email: False")
print(f"Number of @ symbols in the email: {email_text.count('@')}")


# Problem 3: Palindrome checker (ignoring spaces and case)
# Description: This program checks if a word is a palindrome.
# Inputs: A word or phrase.
# Outputs: A message saying if it is a palindrome.
# Validations: The program converts the input to lowercase and ignores spaces.
# Test case 1 - Normal: "Anita lava la tina"
# Expected result: It is a palindrome.
# Test case 2 - Border: "oso"
# Expected result: It is a palindrome.
# Test case 3 - Error: An empty input.
# Expected result: The current code treats it as a palindrome.

word_palindrome = input("Enter a word to check if it is a palindrome: ").lower()
if word_palindrome.replace(" ", "")== word_palindrome.replace(" ", "")[::-1] :
    print("It is a palindrome")
else:
    print("It is not a palindrome")


# Problem 4: Sentence word stats (lengths and first/last word)
# Description: This program gets information about the words in a sentence.
# Inputs: A sentence.
# Outputs: The sentence without spaces at the beginning or end,
# the word count, the first and last word, and the shortest and longest words.
# Validations: The program removes extra spaces before splitting the sentence.
# Test case 1 - Normal: "Python is easy"
# Expected result: Shows 3 words, first word Python, last word easy.
# Test case 2 - Border: "Hello"
# Expected result: Shows 1 word.
# Test case 3 - Error: An empty sentence.
# Expected result: The program can cause an error when accessing the first word.

words = input("Enter a sentence: ")
print(words.lstrip())
print(words.rstrip())
words = words.strip()
word = words.split()
num_words = len(word)
print(f"Word count: {num_words}")
print(f"First word: {word[0]}")
print(f"Last word: {word[-1]}")

"""
   min finds the smallest value.
   key=len makes it compare the length of each word.
   Without it, it would compare the words in a different way.
"""

print(f"Shortest word: {min(word,key=len)}")
print(f"Longest word: {max(word,key=len)}")


# Problem 5: Password strength classifier
# Description: This program checks some characteristics of a password.
# Inputs: A password.
# Outputs: A message about the password strength.
# Validations: The program checks for spaces and the password length.
# Test case 1 - Normal: "Angel123"
# Expected result: The program checks the password strength.
# Test case 2 - Border: "Angel1"
# Expected result: Shows that the password is weak.
# Test case 3 - Error: A password with spaces.
# Expected result: Shows an invalid password message.
password = str(input("Enter your password: "))
uppercase = False
lowercase = False
number = False
character_special = False
if " " in password:
    print("Invalid password")
else:
    counter_letter_password = len(password)
    for letter in password:
        if letter.isupper():
            uppercase = True
        elif letter.islower:
            lowercase = True
        elif letter.isdigit():
            number = True
        else:
            character_special = True
    if 8 > counter_letter_password or password == password.lower():
        print("Your password is weak")
    elif 8<=counter_letter_password and uppercase and lowercase and number and not character_special:
        print("Your password is medium")
    elif 8<=counter_letter_password and uppercase and lowercase and number and character_special:
        print("Your password is strong")
# Problem 6: Product label formatter (fixed-width text)
# Description: This program puts a product name and price together.
# Inputs: The product name and its price.
# Outputs: A label that is cut or padded to 30 characters.
# Validations: The product name cannot be empty and the price must contain numbers.
# Test case 1 - Normal: Product "Notebook", price "50".
# Expected result: Shows the product and price in a label.
# Test case 2 - Border: Product "Pen", price "1".
# Expected result: Shows the label with spaces added at the end.
# Test case 3 - Error: An empty product name or a price with letters.
# Expected result: Shows an invalid text message.

product = (input("Enter the product name: "))
price = (input("Enter the price: "))
if product.strip() != "" and price.isnumeric():
    product_and_price = f"{product}|${price}"
    print(product_and_price)
    product_and_price = product_and_price[:30]
    product_and_price = product_and_price + " " * (30 - len(product_and_price))
    print(f"'{product_and_price}'")
else:
    print("Invalid text")


# Conclusions
# In this activity I practiced different ways to work with strings.
# I learned how to change text to lowercase and title case.
# I also used split(), join(), strip(), and slicing.
# These methods can help when working with names, emails and other text.
# I practiced using conditions to check what the user enters.
# I can use these string methods in other Python programs too.


# References
# 1. Python Documentation - Text Sequence Type: str
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
#
# 2. Python Documentation - String Methods
# https://docs.python.org/3/library/stdtypes.html#string-methods
#
# 3. Python Documentation - Built-in Functions
# https://docs.python.org/3/library/functions.html
#
# 4. Python Tutorial - More on Strings
# https://docs.python.org/3/tutorial/introduction.html#strings
#
# 5. Python Tutorial - Input and Output
# https://docs.python.org/3/tutorial/inputoutput.html
#
# GitHub repository URL:https://github.com/Abundisglz/projects/blob/main/src/2630351_AngelUbaldoAbundisGonzalez_t_strings.py