def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def compute_factorials(*args):
    for num in args:
        fact = factorial(num)
        if fact is None:
            print(f"Factorial not defined for negative number {num}")
        else:
            print(f"Factorial of {num} ({num}!) is {fact}")
n = int(input("How many numbers do you want to enter? "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
compute_factorials(*numbers)