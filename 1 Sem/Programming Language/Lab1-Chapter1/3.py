n = int(input("Enter a number: "))
bits = int(input("Enter number of bits for representation: "))
mask = (1 << bits) - 1
def complement_operations(n, mask):
    # One's complement
    ones = ~n & mask
    # Two's complement
    twos = ones + 1
    print("\nOriginal number:", n, "Binary:", bin(n))
    print("One's complement:", ones, "Binary:", bin(ones))
    print("Two's complement:", twos, "Binary:", bin(twos))
complement_operations(n, mask)
