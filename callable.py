class Callable:
    def __call__(self,x):
        return x*2*4
    
x=Callable()
res=x(2)
print(res)

#you use callable when you want an object to behave as a function 
#this concept is used in decorators
#for example

class Decorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self,*args,**kwargs):
        print(f"Calling {self.func.__name__}")
        return self.func(*args, **kwargs)

@Decorator
def greet(name):
    print(f"Hello, {name}")

greet("Alice")