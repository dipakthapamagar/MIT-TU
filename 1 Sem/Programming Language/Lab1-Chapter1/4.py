bin1 = input("Enter first binary number: ")
bin2 = input("Enter second binary number: ")
num1 = int(bin1, 2)
num2 = int(bin2, 2)
print(f"{bin1} -> {num1}")
print(f"{bin1} -> {num2}")
add_result = num1 + num2
sub_result = num1 - num2
print("\nAddition:")
print("Decimal:", add_result)
print("Binary:", bin(add_result))  
print("\nSubtraction:")
print("Decimal:", sub_result)
print("Binary:", bin(sub_result ))
