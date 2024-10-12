class Student:
    
    def public_method(self):
        print("Inside public method")
        
    def _private_method(self):
        print("Inside a private method..you have to use single underscore in the front")
        
    def __very_private(self):
        print("inside a very private method")   
        
        
obj = Student()
# print(obj.__very_private_var)  # Raises AttributeError
# obj.__very_private_method()    # Raises AttributeError

#Name Mangling
# But you can still access it using the mangled name:

obj._Student__very_private() 