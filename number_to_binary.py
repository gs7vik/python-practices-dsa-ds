n = -3
# m = 10
# print(bin(m).count('1')) #2  # prints the count of '1's in the binary representation of m
# print(bin(n)[2:])  # prints binary representation of n without '0b' prefix, good for production use
cnt = bin(n).count('1')  # counts the number of '1's in the binary representation
print(cnt)  #8 # prints the count of '1's in the binary representation
# #manually converting to binary
# n = 10
# binary = ''
# count_1 = 0
# if n == 0:
#     binary = '0'
# while n > 0:
#     binary = str(n % 2) + binary
#     if str(n%2) =='1':
#         count_1 = count_1 + 1
#     n = n//2
# print(binary)
# #the count_1 will give you the number of 1's in the binary representation

# s = 'aba'

# def pali(s):
#     # print(s[::-1])
#     return s[::-1]

# if s == pali(s):
#     print("pali")
# else:
#     print('not pali')