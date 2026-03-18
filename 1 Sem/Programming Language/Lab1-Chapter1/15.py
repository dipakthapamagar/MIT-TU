n = int(input("Enter how many numbers: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("\nOriginal list:", numbers)
print("Even numbers:", even_numbers)