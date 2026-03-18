n = int(input("Enter how many numbers: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("\nOriginal list:", numbers)
unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)