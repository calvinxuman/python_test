# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# L1=list(range(1,1000))
# L2=[x * x for x in range(1,1000)]
# for i in L1:
#     a=i + 100
#     b=i + 268
#     if a in L2 and b in L2:
#         print(i)

# 假设该数为 x。
# 1、则：x + 100 = n2, x + 100 + 168 = m2
# 2、计算等式：m2 - n2 = (m + n)(m - n) = 168
print([n**2-100 for m in range(168) for n in range(m) if(m+n)*(m-n)==168])

