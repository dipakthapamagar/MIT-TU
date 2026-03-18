n = int(input("Enter how many numbers: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
cube_numbers = list(map(lambda x: x**3, numbers))
print("\nOriginal list:", numbers)
print("Cubes of list element:", cube_numbers)