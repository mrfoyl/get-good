import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def list_primes(up_to):
    print(f"Prime numbers up to {up_to}:")
    for num in range(2, up_to + 1):
        if is_prime(num):
            print(num)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 prime_calculator.py <upper_limit>")
    else:
        try:
            limit = int(sys.argv[1])
            list_primes(limit)
        except ValueError:
            print("Please provide a valid integer.")
