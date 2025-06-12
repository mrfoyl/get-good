import time
import multiprocessing
from tqdm import tqdm

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

def check_range(start, end):
    return [num for num in range(start, end) if is_prime(num)]

# ✅ This is the fix — top-level function instead of lambda
def process_range(args):
    return check_range(*args)

def list_primes_parallel(up_to):
    cpu_count = multiprocessing.cpu_count()
    print(f"\nUsing {cpu_count} CPU cores to calculate primes up to {up_to}...")

    chunk_size = max(10_000, up_to // (cpu_count * 4))
    ranges = [(i, min(i + chunk_size, up_to + 1)) for i in range(2, up_to + 1, chunk_size)]

    start_time = time.time()

    primes = []
    with multiprocessing.Pool(cpu_count) as pool:
        for result in tqdm(pool.imap_unordered(process_range, ranges), total=len(ranges), desc="Processing", unit="chunk"):
            primes.extend(result)

    elapsed = time.time() - start_time
    print(f"\n✅ Found {len(primes)} prime numbers up to {up_to}.")
    print(f"⏱️ Calculation took {elapsed:.2f} seconds.")

if __name__ == "__main__":
    try:
        limit = int(input("Enter an upper limit to find prime numbers: "))
        list_primes_parallel(limit)
    except ValueError:
        print("❌ Please enter a valid integer.")
