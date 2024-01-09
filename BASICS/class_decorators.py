class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        print("The call method executed this")
        return self.original_function(*args, **kwargs)

@decorator_class
def addition(a, b):
    return a + b

print(addition(10, 30))