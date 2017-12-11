def is_palindrome(n):
    s=str(n)
    s1=s[::-1]
    if s==s1:
        return n

list1=list(filter(is_palindrome,range(1,1000)))
print(list1)