import time
from iridis import benchmark


@benchmark
def add(a, b):
    return a + b


result, execution_time = add(5, 3)
print(f"Result: {result}, Execution time: {execution_time:.6f} seconds")
