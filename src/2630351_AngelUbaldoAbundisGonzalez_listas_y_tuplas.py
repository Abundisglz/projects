
# Name: Angel Ubaldo Abundis Gonzalez
# Student ID: 2630351
# Group: 1-3
# Executive Summary
# In this work I use lists, tuples and dictionaries in Python.
# Lists can store items and we can add or remove elements.
# Tuples store values that cannot be changed after they are created.
# Dictionaries store information using keys and values.
# The six problems use collections for products, points and student grades.
# I also use them to count words and manage contacts.
# Each problem has inputs, outputs, validations and test cases.
# These exercises help me understand how collections work.
# Good practices
# Use lists when you need to add or remove items.
# Use tuples for data that should not change, like coordinates.
# Use dictionaries to search for information by a key.
# Avoid changing a list while going through it with a for loop.
# Use clear names for dictionary keys and messages.
# Problem 1: Product list with list
# Description: This program creates a product list and adds a new item.
# It also counts the items and checks if a product is in the list.
# Inputs: Initial products separated by commas, a new product and a search product.
# Outputs: Items list, total items and found item.
# Validations: Inputs cannot be empty and the initial list must have products.
# Test cases:
# 1) Normal: apple,banana,orange; add grape and search apple.
# 2) Border: One product in the initial list.
# 3) Error: Empty initial list or empty product name.
initial_items_text = input("Enter the initial products separated by commas:")
new_item = input("Enter a new product:")
search_item = input("Enter a product to search:")
if initial_items_text.strip() == "" or new_item.strip() == "" or search_item.strip() == "":
    print("Error: invalid input")
else:
    items_list = initial_items_text.split(",")
    items_list = [item.strip() for item in items_list if item.strip() != ""]
    new_item = new_item.strip()
    search_item = search_item.strip()
    if len(items_list) == 0:
        print("Error: invalid input")
    else:
        items_list.append(new_item)
        is_in_list = search_item in items_list
        print("Items list:", items_list)
        print("Total items:", len(items_list))
        print("Found item:", is_in_list)
# Problem 2: Points and distances with tuples
# Description: This program creates two points using tuples.
# It calculates the distance and the midpoint between the points.
# Inputs: Four coordinates x1, y1, x2 and y2.
# Outputs: Point A, Point B, distance and midpoint.
# Validations: All coordinates must be valid numbers.
# Test cases:
# 1) Normal: Point A (1,2) and point B (4,6).
# 2) Border: Both points are (0,0).
# 3) Error: A coordinate is not a number.
x1_text = input("Enter x1:")
y1_text = input("Enter y1:")
x2_text = input("Enter x2:")
y2_text = input("Enter y2:")
if x1_text.replace(".","",1).replace("-","",1).isdigit() and y1_text.replace(".","",1).replace("-","",1).isdigit() and x2_text.replace(".","",1).replace("-","",1).isdigit() and y2_text.replace(".","",1).replace("-","",1).isdigit():
    x1 = float(x1_text)
    y1 = float(y1_text)
    x2 = float(x2_text)
    y2 = float(y2_text)
    point_a = (x1, y1)
    point_b = (x2, y2)
    distance = ((x2-x1)**2+(y2-y1)**2)**0.5
    midpoint = ((x1+x2)/2,(y1+y2)/2)
    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance,2))
    print("Midpoint:", midpoint)
else:
    print("Error: invalid input")
# Problem 3: Product catalog with dictionary
# Description: This program stores products and their prices in a dictionary.
# It calculates the total price when the product exists.
# Inputs: Product name and quantity.
# Outputs: Unit price, quantity and total price.
# Validations: Product name cannot be empty, quantity must be positive
# and the product must exist in the dictionary.
# Test cases:
# 1) Normal: apple with quantity 3.
# 2) Border: banana with quantity 1.
# 3) Error: Unknown product or invalid quantity.
product_prices = {"apple":10.0,"banana":15.0,"orange":12.0,"grape":20.0}
product_name = input("Enter the product name:").strip().lower()
quantity_text = input("Enter the quantity:")
if quantity_text.isdigit():
    quantity = int(quantity_text)
    if product_name == "" or quantity <= 0:
        print("Error: invalid input")
    elif product_name in product_prices:
        unit_price = product_prices[product_name]
        total_price = unit_price * quantity
        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", total_price)
    else:
        print("Error: product not found")
else:
    print("Error: invalid input")
# Problem 4: Student grades with dict and list
# Description: This program stores student grades in a dictionary.
# It calculates the average and checks if the student passed.
# Inputs: Student name.
# Outputs: Grades, average and passed status.
# Validations: Name cannot be empty, student must exist and grades
# must not be empty before calculating the average.
# Test cases:
# 1) Normal: Angel has grades 90, 85 and 80.
# 2) Border: Maria has an average of 70.
# 3) Error: Student name does not exist.
grades = {"Angel":[90.0,85.0,80.0],"Maria":[70.0,70.0,70.0],"Carlos":[60.0,65.0,55.0]}
student_name = input("Enter the student name:").strip().title()
if student_name == "":
    print("Error: invalid input")
elif student_name in grades:
    grades_list = grades[student_name]
    if len(grades_list) == 0:
        print("Error: no grades available")
    else:
        average = sum(grades_list)/len(grades_list)
        is_passed = average >= 70.0
        print("Grades:", grades_list)
        print("Average:", round(average,2))
        print("Passed:", is_passed)
else:
    print("Error: student not found")
# Problem 5: Word frequency counter
# Description: This program separates a sentence into words.
# It counts the frequency of each word and finds the most common one.
# Inputs: A sentence.
# Outputs: Words list, frequencies and most common word.
# Validations: Sentence cannot be empty and the word list must have items.
# Simple punctuation marks are removed before counting.
# Test cases:
# 1) Normal: cat dog cat bird cat.
# 2) Border: One word.
# 3) Error: Empty sentence.
sentence = input("Enter a sentence:")
if sentence.strip() == "":
    print("Error: invalid input")
else:
    sentence = sentence.lower()
    sentence = sentence.replace(",","")
    sentence = sentence.replace(".","")
    sentence = sentence.replace("!","")
    sentence = sentence.replace("?","")
    sentence = sentence.replace(";","")
    sentence = sentence.replace(":","")
    words_list = sentence.split()
    if len(words_list) == 0:
        print("Error: no words found")
    else:
        freq_dict = {}
        for word in words_list:
            if word in freq_dict:
                freq_dict[word] = freq_dict[word]+1
            else:
                freq_dict[word] = 1
        most_common_word = max(freq_dict,key=freq_dict.get)
        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)
# Problem 6: Contact list with dictionary
# Description: This program manages contacts using a dictionary.
# It can add, search or delete a contact.
# Inputs: Action, contact name and phone number when adding a contact.
# Outputs: A message showing the result of the action.
# Validations: Action must be ADD, SEARCH or DELETE, name cannot be empty
# and phone cannot be empty when adding a contact.
# Test cases:
# 1) Normal: ADD a new contact.
# 2) Border: SEARCH an existing contact.
# 3) Error: DELETE a contact that does not exist.
contacts = {"Angel":"8344280024","Mi ex":"8344274696","Alison":"8342818270"}
action_text = input("Enter an action (ADD, SEARCH or DELETE):").strip().upper()
if action_text == "ADD" or action_text == "SEARCH" or action_text == "DELETE":
    name = input("Enter the contact name:").strip()
    if name == "":
        print("Error: invalid input")
    elif action_text == "ADD":
        phone = input("Enter the phone number:").strip()
        if phone == "":
            print("Error: invalid input")
        else:
            contacts[name] = phone
            print("Contact saved:", name, phone)
    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts.get(name))
        else:
            print("Error: contact not found")
    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")
else:
    print("Error: invalid input")
# 8. CONCLUSIONS
# I learned that lists, tuples and dictionaries have different uses.
# Lists let us add and remove items when we need to.
# Tuples are useful for data that should not change, like coordinates.
# Dictionaries help us find information using a key.
# A dictionary can also store lists, like the grades of students.
# These collections help organize information in different programs.
# It is important to check the inputs to avoid errors.
# 9. REFERENCES
# 1) Python documentation - Lists
# https://docs.python.org/3/tutorial/introduction.html#lists
# 2) Python documentation - Data Structures
# https://docs.python.org/3/tutorial/datastructures.html
# 3) Python documentation - Tuples and Sequences
# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# 4) Python documentation - Dictionaries
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# 5) Python documentation - Built-in Functions
# https://docs.python.org/3/library/functions.html
# 6) Python documentation - Errors and Exceptions
# https://docs.python.org/3/tutorial/errors.html
# GitHub repository:https://github.com/Abundisglz/projects