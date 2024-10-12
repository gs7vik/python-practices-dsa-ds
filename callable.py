class Callable:
    def __call__(self,x):
        return x*2*4
    
x=Callable()
res=x(2)
print(res)

#you use callable when you want an object to behave as a function 
