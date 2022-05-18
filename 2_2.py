# Given a string, return the length of the string using recursion. 
def str_len(s):
    if(s == ''):return 0
    return 1 + str_len(s[1:])

str = input('Enter a string:')
print(str_len(str))