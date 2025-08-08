x = {'dav': 1, 'dave': 2, 'david': 3, 'daveed': 4}

x['sat'] = 5



del x['sat']
print(x)

#2 

text = "apple banana apple orange banana apple"
words = text.split()

print(words)
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word,0)+1
    
# print(word_freq)

#3
student_grades = {"Alice": "A", "Bob": "B", "Charlie": "A"}

invert_dict = {}

for k,v in student_grades.items(): 
    if v not in invert_dict:
        invert_dict[v] =[]
    invert_dict[v].append(k)




    
print(invert_dict)

# s='hel'
# s[2] = '1' 
# print(s) # This wil throw an error because strings are immutable

ex_tuple = (1, 2, 3, 4, 5)
ex_list = [1, 2, 3, 4, 5]

ex_list[0] = 10  # This is allowed
ex_tuple[0] = 10  # This will raise a TypeError because tuples are immutable