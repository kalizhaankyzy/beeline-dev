# Given an integer, return true if the integer is a palindrome.
def isPalindrome(n):
    n_rev=0
    temp = n
    while n>0:
        n_rev = n_rev*10 + n%10
        n = n//10
    if(temp==n_rev):return True
    return False

n = int(input('Enter the number:'))
print(isPalindrome(n))