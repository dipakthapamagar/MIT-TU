n = int(input("Enter how many numbers: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("\nNumbers in the list:", numbers)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)