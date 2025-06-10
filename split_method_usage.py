st = "hello world, this is a test"

#split syntax
#split(separator, maxsplit)
#separator: the character to split the string by (default is whitespace)
#maxsplit: the maximum number of splits to do (default is -1, which means "all occurrences")
#note: method does not modify the original string, it returns a new list and this method is applicable to only strings
x = st.split() #by default, splits by whitespace
y = st.split(",")  # splits by comma



print(x) # Output: ['hello', 'world,', 'this', 'is', 'a', 'test']
print(y) # Output: ['hello world', ' this is a test']
print(type(x)) #<class 'list'>