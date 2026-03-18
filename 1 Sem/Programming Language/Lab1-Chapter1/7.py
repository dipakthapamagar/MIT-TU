print("Input like 3+5j")
num1 = complex(input("Enter first complex number (a+bj): "))
num2 = complex(input("Enter second complex number (a+bj): "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 #division by zero gives error
print("\nResults:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")