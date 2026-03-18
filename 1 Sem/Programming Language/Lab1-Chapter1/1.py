a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
def display_result(x):
    print(f"\nInteger Number: {x}")
    print("Binary Representation: ", bin(x))
    print("Octal Representation: ", oct(x))
    print("Hexadecimal Representation: ", hex(x))
display_result(a)
display_result(b)
