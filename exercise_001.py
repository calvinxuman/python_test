# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
L1=list(range(1,6))
num=0
for i in L1:
    for j in L1:
        for k in L1:
            if i!=j and j!=k and i!=k:
                print(i,j,k)
                num+=1
print(num)