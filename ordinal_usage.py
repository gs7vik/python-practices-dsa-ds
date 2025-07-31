#ordinal usage for converting alphabetical order to ordinal numbers
print(ord('a'))
print(ord('b'))
print(ord('a')-ord('a')+1)  # This will give you 1 for 'a', 2 for 'b', etc.

#convert ordinal numbers back to letters
ord_nums = [0,1,2,3,25]
letters = [chr(ord('a') + i) for i in ord_nums] 
print(letters)
