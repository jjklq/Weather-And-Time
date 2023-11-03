import time

def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.4f} seconds")
        return result
    return wrapper

@calculate_execution_time
def add(a: int, b: int) -> int:
    return a + b

result = add(1, 2)
print(result)
