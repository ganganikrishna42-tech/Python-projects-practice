prime_num = [int(input("Enter a number:")) for i in range(int(input("Enter the size of the array:")))]
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
prime_numbers = [x for x in prime_num if is_prime(x)]
print("\nThe prime numbers in the array are:\n", prime_numbers)