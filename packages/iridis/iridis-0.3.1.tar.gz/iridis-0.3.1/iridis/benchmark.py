import time


def benchmark(f: callable):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = f(*args, **kwargs)  # Call the original function
        end_time = time.perf_counter()

        return result, end_time - start_time

    return wrapper
