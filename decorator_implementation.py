from functools import wraps

def satvik(f):
    try:
        @wraps(f)
        def wrapper(*args, **kwargs):
            print("Calling decorated function")
            # print(f"calling decorated function {f.__name__}")
            raise ArithmeticError("simply putting/raising arithemetic error here ")
            return f(*args, **kwargs)
        return wrapper
    except Exception as e:
        print("error is: "+str(e))

@satvik(1,2,3)
def say_hello():
    """This function says hello."""
    print("Hello!")

say_hello()
print(say_hello.__name__)  # Outputs: wrapper
print(say_hello.__doc__)   # Outputs: None
print(say_hello.__module__)  # Outputs: __main__ (correct, but other metadata is lost)

# say_hello(1,23,name="astbik")