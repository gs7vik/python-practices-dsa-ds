# x =[1,2,3]
# x =-[x] wrong syntax
# print(x)

x=[1]
y=2
x.append(-y)
print(x)
while x:
    x.pop()

print(x)
