# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
#
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
def countBits(n):
    n = bin(int(n))
    sum = 0
    for i in range(2,len(n)):
        sum += int(n[i])
    return sum

print(countBits(0))#, 0);
print(countBits(4))#, 1);
print(countBits(7))#, 3);
print(countBits(9))#, 2);
print(countBits(10))#, 2);
print(countBits(1234))#, 5);

# def countBits(n):
#     return bin(n).count("1")