class dividebyxero(BaseException): #for creating a custom exception you have to define it as a class and then inherit Exception super class 
    pass 

'''
Directly inheriting from BaseException is rare and generally not recommended for custom exceptions 
because it includes exceptions that are not intended for normal error handling.
'''
try:
    num=5/0
except:
    raise dividebyxero("not possible")