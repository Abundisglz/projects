# Problem 1: Temperature converter
# This program converts Celsius to Fahrenheit and Kelvin.
# It also checks if the temperature is high.
# Inputs: Temperature in Celsius.
# Outputs: Fahrenheit, Kelvin and high temperature status.
# Validations: Kelvin cannot be below zero.
# Test cases:
# 1) Normal: 25 Celsius.
# 2) Border: 30 Celsius.
# 3) Error: -300 Celsius.
temperature_c = float(input("Teclea la temperatura en grados celcius:"))
temperature_f = temperature_c * 9 / 5 + 32
temperature_k = temperature_c + 273.15
if temperature_k < 0.0:
    print("Error: invalid input")
else:
    print(f"la temperatura es alta:{temperature_c >= 30}")
    print(f"temperatura en farenhein:{temperature_f}")
    print(f"temperatura en kelvin{temperature_k}")
# Problem 2: Work hours and overtime payment
# This program calculates the payment for the hours worked.
# Extra hours are paid with an extra 50 percent.
# Inputs: Hourly payment and hours worked.
# Outputs: Regular payment, overtime payment and extra hours.
# Validations: Hours worked should not be negative.
# Test cases:
# 1) Normal: 35 hours.
# 2) Border: 40 hours.
# 3) Error: Negative hours.
hourly_pay = float(input("teclea cuanto se paga por hora:"))
print("si trabajaste cuarenta horas y veinte minutos teclea 40.20 la hora seria el numero entero y los minutos como decimales")
hours_worked = float(input("teclea las horas trabajadas:"))
total_pay = hourly_pay * hours_worked
overtime_hours = hours_worked - 40
overtime_pay = hourly_pay * overtime_hours * 1.5 + total_pay
if hours_worked <= 0 or hourly_pay <= 0:
    print("Error: invalid input")
else:
    if hours_worked <= 40:
        print("Tu pago es regular")
        print(f"tu pago es de{total_pay}")
    else:
        print("Tu pago es overtime")
        print(f"Tu pago total es:{overtime_pay}")
        print(f"se hicieron horas extras:{hours_worked > 40}")
        print(f"las horas extras son:{hours_worked - 40}")
# Problem 3: Discount eligibility
# This program checks if a customer can get a discount.
# The discount is 10 percent if one of the conditions is true.
# Inputs: Customer answer and purchase total.
# Outputs: Discount status and final purchase price.
# Validations: The customer answer and purchase total must be valid.
# Test cases:
# 1) Normal: Student answers yes and buys for 500.
# 2) Border: Purchase total is 1000.
# 3) Error: Invalid customer answer.
customer = str(input("Teclea yes si es estudiante o senior:").lower().strip())
purchase_total = float(input("costo del producto:"))
if customer == "yes" and customer == "no" and purchase_total >= 0:
    customer_discount = False
    customer_discount = customer == "yes"
    purchase_discount = False
    purchase_discount = purchase_total >= 1000
    print(f"Merece descuento:{purchase_discount or customer_discount}")
    if customer_discount or purchase_discount:
        purchase_total = purchase_total * 0.9
        print(f"Su compra es de:${purchase_total}")
    else:
        print(f"Su compra es de:${purchase_total}")
else:
    print("Error: Cliente no válido o compra no válida.")
# Problem 4: Basic statistics
# This program works with three integers.
# It calculates the sum, average, maximum, minimum and checks if all are even.
# Inputs: Three integers.
# Outputs: Sum, average, maximum, minimum and even status.
# Validations: The inputs must be integers.
# Test cases:
# 1) Normal: 2, 4, 6.
# 2) Border: 0, 0, 0.
# 3) Error: A decimal number instead of an integer.
number_1 = int(input("Teclea un numero:"))
number_2 = int(input("Teclea otro numero:"))
number_3 = int(input("Teclea otro numero:"))
if number_1 <= 0 or number_2 <= 0 or number_3 <= 0:
    print("Error: invalid input")
else:
    total_sum = number_1 + number_2 + number_3
    average = total_sum / 3
    maximum_value = max(number_1, number_2, number_3)
    minimum_value = min(number_1, number_2, number_3)
    all_even = (number_1 % 2 == 0) and (number_2 % 2 == 0) and (number_3 % 2 == 0)
    print(f"La suma es: {total_sum}")
    print(f"El promedio es: {average}")
    print(f"El valor maximo es: {maximum_value}")
    print(f"El valor minimo es: {minimum_value}")
    print(f"¿Los tres números son pares? {all_even}")
# Problem 5: Loan eligibility
# This program checks if a person can get a loan.
# It uses income, monthly debt and credit score.
# Inputs: Monthly income, monthly debt and credit score.
# Outputs: Debt ratio and eligibility status.
# Validations: Income must be above zero and debt and score cannot be negative.
# Test cases:
# 1) Normal: Income 10000, debt 2000 and score 700.
# 2) Border: Income 8000, debt 3200 and score 650.
# 3) Error: Income is zero.
monthly_income = float(input("Teclea tu ingreso mensual: "))
monthly_debt = float(input("Teclea tu deuda mensual: "))
credit_score = int(input("Teclea tu puntaje crediticio: "))
if monthly_income <= 0 or monthly_debt <= 0 or credit_score <= 0:
    print("Error: invalid input")
else:
    debt_ratio = monthly_debt / monthly_income
    eligible = monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650
    print("Debt ratio:", debt_ratio)
    print("Eligible:", eligible)
# Problem 6: Body Mass Index
# This program calculates the BMI using weight and height.
# It checks if the person is underweight, normal weight or overweight.
# Inputs: Weight in kilograms and height in meters.
# Outputs: BMI and weight category.
# Validations: Weight and height must be above zero.
# Test cases:
# 1) Normal: 70 kg and 1.75 m.
# 2) Border: BMI is 25.
# 3) Error: Height is zero.
weight_kg = float(input("Teclea tu peso en kilogramos: "))
height_m = float(input("Teclea tu estatura en metros: "))
bmi = weight_kg / (height_m ** 2)
if weight_kg <= 0 or height_m <= 0:
    print("Error: invalid input")
else:
    underweight = bmi < 18.5
    normal_weight = 18.5 <= bmi < 25.0
    overweight = bmi >= 25.0
    print(f"Tu BMI es: {round(bmi, 2)}")
    print(f"¿Tienes bajo peso? {underweight}")
    print(f"¿Tienes peso normal? {normal_weight}")
    print(f"¿Tienes sobrepeso? {overweight}")   
# 8. CONCLUSIONS
# I learned that int and float are useful for doing different calculations.
# Integers are for whole numbers and floats can have decimal numbers.
# Comparisons give True or False, and we can use them with if to make decisions.
# It is important to check the values entered by the user to avoid errors.
# I learned how to use and, or and not to combine different conditions.
# These things are useful in programs about payments, discounts and loans.
# I also learned that we need to check values before doing calculations.
# 9. REFERENCES
# 1) Python documentation - Numeric Types
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 2) Python documentation - Boolean Type
#    https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
# 3) Python documentation - Expressions and operators
#    https://docs.python.org/3/reference/expressions.html
# 4) Python documentation - Built-in Functions
#    https://docs.python.org/3/library/functions.html
# 5) Python documentation - Errors and Exceptions
#    https://docs.python.org/3/tutorial/errors.html
# GitHub repository URL:https://github.com/Abundisglz/projects