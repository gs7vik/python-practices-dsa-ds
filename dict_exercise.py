keys = ['a', 'b', 'c']
values = [1, 2, 3]
# Output: {'a': 1, 'b': 2, 'c': 3}
empty_dict = {}
for k,v in zip(keys, values):
    empty_dict[k] = v
print(empty_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}