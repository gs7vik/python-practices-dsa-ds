# Create an empty stack using a list
stack = []

# Push operation
stack.append(10)
stack.append(20)

# Pop operation
item = stack.pop()  # Removes and returns the last item (20)
print(item)         # Output: 20

item = stack.pop()  # Removes and returns the next item (10)
print(item)         # Output: 10