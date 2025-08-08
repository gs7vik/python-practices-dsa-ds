try:
    a= 1
    print("a is 1")
except Exception as e:
    print("a not accessible")
    
print(a) #1

try:
    b = 2 
    print(" b is 2")
except Exception as e:
    print("b value not foud")
finally:
    print("This will always execute")
