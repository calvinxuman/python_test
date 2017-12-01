# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
L1 = list(range(1,13))
L2 = [31,28,31,30,31,30,31,31,30,31,30,31]
date = input('请输入年月日(如20171102)：\n')
year = int(date[0:4])
month = int(date[4:6])
day = int(date[6:8])
count1 = 0
count2 = 0
for i in range(len(L1)):
    if L1[i] < month :
        count1 +=  L2[i]
if year % 4 == 0 and year % 100 != 0 and month > 2:
    count2 = count1 + day + 1
else:
    count2 = count1 + day
print('今天是第',count2,'天')

