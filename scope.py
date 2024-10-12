x='global x'
def fun():
    
    global x
    x=x+'a'
    print(x)

fun()
print(x)