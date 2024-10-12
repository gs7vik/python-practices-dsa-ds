from fuzzywuzzy import fuzz

#fuzzy search can be thought of as an advanced keyword search where people might 
#pronunce incorrect spelling of a word and fuzzy search can handle that 
# str1="this is a cat"
# str2="this isnt a cat" fuzzy matching fails to catch the semantics 

str1="marco fernandez"
str2="marco s"   
print(fuzz.ratio(str1, str2))  #outputs 0 


# smtr1="this"
# str2="h"   
# print(fuzz.ratio(str1, str2))  #outputs 40

# str1="this"
# str2="hi"   
# print(fuzz.ratio(str1, str2))  #outputs 67

# str1="T"
# str2="t"   
# print(fuzz.ratio(str1, str2))  #outputs 0