print("\nExpression: x + y * 3 ** 2 // 2")
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
result = x + y * 3 ** 2 // 2
step1 = 3 ** 2       # Exponentiation first
step2 = y * step1    # Multiplication next
step3 = step2 // 2   # Floor division
step4 = x + step3    # Addition last
print("Step 1 (3 ** 2):", step1)
print("Step 2 (y * 3 ** 2):", step2)
print("Step 3 ((y * 3 ** 2) // 2):", step3)
print("Step 4 (x + (y * 3 ** 2) // 2):", step4)
print("\nFinal Result:", result)
