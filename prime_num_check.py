n = 51
a  = []
def isPrime(num):
    if num <=1 :
        return False
    isPrime = True
    for i in range(2, num): #checks if the number is divisible by numbers  other than 1 or the number itself . #checking till sqrt(num) will be more optimal
        
        
        if num%i == 0:
            isPrime = False
    return isPrime   
    
for i in range(1,51):
    x = isPrime(i)
    if x:
        a.append(i)
        
        
print(a)

#print all twin primes
for i in range(len(a)-1):
    if a[i+1] - a[i] == 2:
        print(a[i],a[i+1])
    