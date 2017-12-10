# -*-coding:UTF-8 -*-
from functools import reduce

def str2float(s):
    if '.' not in s:
        return int(s)
    else:
        s1=s.split(sep='.')[0]
        s2=s.split(sep='.')[1]
        l=len(s2)
        n1=reduce(lambda x1,x2:10*x1+x2,[int(i) for i in s1])
        n2=reduce(lambda x1,x2:10*x1+x2,[int(i) for i in s2])/(10**l)
        return n1+n2
str1=input('input a float number:')
print(str2float(str1))

