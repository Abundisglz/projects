# Problem 1: Product list with list
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
