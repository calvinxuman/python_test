# -*-coding:UTF-8 -*-


def findminandmax(L):
    if len(L) == 0:
        return (None, None)
    else:
        min = L[0]
        max = L[0]
        for i in L:
            if i < min:
                min = i
            if i > max:
                max = i
        return (min, max)


print(findminandmax([]))
