L1=list(range(1,6))
num=0
for i in L1:
    for j in L1:
        for k in L1:
            if i!=j and j!=k and i!=k:
                print(i,j,k)
                num += 1