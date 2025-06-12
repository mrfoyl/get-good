import multiprocessing

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_range(start_end):
    start, end = start_end
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    return primes

def list_primes_parallel(up_to):
    cpu_count = multiprocessing.cpu_count()
    print(f"Using {cpu_count} CPU cores")

    # Split the range [2..up_to+1) into chunks for each CPU core
    chunk_size = (up_to // cpu_count) + 1
    ranges = [(i, min(i + chunk_size, up_to + 1)) for i in range(2, up_to + 1, chunk_size)]

    with multiprocessing.Pool(cpu_count) as pool:
        results = pool.map(check_range, ranges)

    # Flatten the list of primes from all chunks
    primes = [prime for sublist in results for prime in sublist]

    print(f"\nPrime numbers up to {up_to}:")
    for prime in sorted(primes):
        print(prime)

if __name__ == "__main__":
    try:
        limit = int(input("Enter an upper limit to find prime numbers: "))
        list_primes_parallel(limit)
    except ValueError:
        print("❌ Please enter a valid integer.")
