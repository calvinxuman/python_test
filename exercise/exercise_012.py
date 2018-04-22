# -*-  conding:utf-8 -*-
# 题目：判断101-200之间有多少个素数，并输出所有素数。
#
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
j = 0
L = []
for num in range(101, 201):
    for i in range(2, num):
        if num%i == 0:
            j += 1
    if j == 0:
        L.append(num)
    else:
        j = 0
print(len(L))
print(L)