# I can just use the current date to calculate age 
import datetime

# Program 1. Display name four times
name = input("Enter your name: ")
print((name + " ") * 4)

print("---")

# Program 2. Name and age after 20 years
age = int(input("Enter your age: "))
print(name + " will be " + str(age + 20) + " in twenty years.")

print("---")

# Program 3. Sum, Difference, Product, and Quotient
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2 if num2 != 0 else "Cannot divide by zero")

print("---")

# Program 4. Year you turn 100
current_year = datetime.datetime.now().year
year_100 = current_year + (100 - age)
print(name + ", you will turn 100 in the year " + str(year_100))