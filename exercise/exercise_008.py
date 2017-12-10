def is_palindrome():
    n=1
    while True:
        s=str(n)
        s1=s[::-1]
        if s==s1:
            yield n
        n+=1

j=20
for i in is_palindrome():
    print(i)
    j -= 1
    if j < 1 :
        break