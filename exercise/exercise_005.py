# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
data=input('输入三个整数,用空格隔开：')
list1=data.split(' ')
# list2=[]
# for i in list1:
#      list2.append(int(i))
# list3=sorted(list2)
print(sorted(list1))