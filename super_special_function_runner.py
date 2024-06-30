
import time

def run_and_analyze(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f'start time:\t{start}\nend time:\t{end}\ntotal time:\t{end - start}')
    return wrapper
