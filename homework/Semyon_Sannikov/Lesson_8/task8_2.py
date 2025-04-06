import sys

sys.set_int_max_str_digits(1000000)  

def generation():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


n_values = [5, 200, 1000, 100000]
fib_gen = generation()
results = {}
index = 0


for number in fib_gen:
    if index in n_values:
        results[index] = number
        if len(results) == len(n_values):
            break
    index += 1

for n in n_values:
    if n == 100000:
        num_str = str(results[n])
        chunk_size = 1000
        print(f"F({n}) = ")
        for i in range(0, len(num_str), chunk_size):
            print(num_str[i:i + chunk_size])
    else:
        print(f"F({n}) = {results[n]}")
