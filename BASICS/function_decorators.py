def outer_function(msg):    
    def inner_function():
        print(msg)
    
    return inner_function

def decorator_function(original_function):
    def wrapper_function():
        print(f"Our wrappper executed before {original_function.__name__}")
        return original_function()
    return wrapper_function

def display():
    print("The display fucntion just ran")

decorated_function = decorator_function(display)
decorated_function()


def func_one(wrapper):
    print("This is the decorator function")
    print("i want to see whats going to happen")
    return wrapper

@func_one
def func_two():
    print("Lets see what happens")

func_two()

print("\n")

def my_decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Decorator modification")
        return original_function(*args, **kwargs)
    return wrapper_function

@my_decorator_function
def addition(a, b):
    return a + b

print(addition(10, 20))