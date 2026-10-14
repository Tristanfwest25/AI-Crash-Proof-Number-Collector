# Collects 3 numbers entered one at a time and outputs the number collected, the sum, and the average. 

try:
    num1 = int(input("Enter Number 1: "))
except ValueError: 
    #Each exception is handled by using 0 as the default value.
    print("Invalid input. Using 0 instead.")
    num1 = 0
    
try:
    num2 = int(input("Enter Number 2: "))
except ValueError:
    #Each exception is handled by using 0 as the default value.
    print("Invalid input. Using 0 instead.")
    num2 = 0

try:
    num3 = int(input("Enter Number 3: "))
except ValueError:
    #Each exception is handled by using 0 as the default value.
    print("Invalid input. Using 0 instead.")
    num3 = 0
    
total = num1 + num2 + num3
average = total / 3
print(f"Your Numbers: {num1}, {num2}, {num3}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")
    
