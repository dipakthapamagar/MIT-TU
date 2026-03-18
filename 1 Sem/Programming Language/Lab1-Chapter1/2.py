a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
def bitwise_operations(a, b):
    print("\nBitwise AND:", a & b, "Binary Format Result: ",  bin(a & b))
    print("Bitwise OR:", a | b, "Binary Format Result: ",  bin(a | b))
    print("Bitwise XOR:", a ^ b, "Binary Format Result: ",  bin(a ^ b))
bitwise_operations(a, b)
