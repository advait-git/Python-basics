import time
# over here we are making a decorator for calculating the time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result=func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer #this is the decorator
def example_function(n):
    time.sleep(n)
example_function(2)