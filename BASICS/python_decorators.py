def my_logger(original_function):
    import logging
    logging.basicConfig(filename=f"{original_function.__name__}.log", level=logging.INFO)
    
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args} and kwargs: {kwargs}")
        return original_function(*args, **kwargs);
    
    return wrapper

def my_timer(original_function):
    import time
    
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{original_function.__name__} ran in {t2} seconds")
        return result 
    return wrapper


@my_logger
def addition(a, b):
    return a + b

print(addition(20,30))

@my_timer
def printer():
    for _ in range(10000000):
        ...
printer()