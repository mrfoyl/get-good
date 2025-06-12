import time
import multiprocessing

def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_range(start_end):
    start, end = start_end
    return [num for num in range(start, end) if is_prime(num)]

def list_primes_parallel(up_to):
    cpu_count = multiprocessing.cpu_count()
    print(f"\nUsing {cpu_count} CPU cores to calculate primes up to {up_to}...")

    # Split workload into optimal chunks
    chunk_size = max(10_000, up_to // cpu_count)
    ranges = [(i, min(i + chunk_size, up_to + 1)) for i in range(2, up_to + 1, chunk_size)]

    start_time = time.time()

    with multiprocessing.Pool(cpu_count) as pool:
        results = pool.map(check_range, ranges)

    primes = [prime for sublist in results for prime in sublist]
    end_time = time.time()

    elapsed = end_time - start_time

    print(f"\n✅ Found {len(primes)} prime numbers up to {up_to}.\n")
    # Optional: print the primes
    # print(*sorted(primes), sep="\n")
    print(f"⏱️ Calculation took {elapsed:.3f} seconds.")

if __name__ == "__main__":
    try:
        limit = int(input("Enter an upper limit to find prime numbers: "))
        list_primes_parallel(limit)
    except ValueError:
        print("❌ Please enter a valid integer.")
