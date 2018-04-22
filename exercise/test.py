#!/usr/bin/python
# *-*coding:utf-8*-*


# def login_1(username,passwd):
#     global login_status
#     l1 = []
#     with open('users1',r) as f:
#         for i in f.readlines():
#             l1.append(i)
#     if username == l1[0] and passwd == l1[1]:
#         login_status = True

# def login_2(username,passwd):
#     global login_status
#     l2 = []
#     with open('users2',r) as f:
#         for i in f.readlines():
#             l2.append(i)
#     if username == l2[0] and passwd == l2[1]:
#         login_status = True

def login(func):
    def warrper(*args,**kw):
        global login_status
        if not login_status:
            username = input('请输入用户名：')
            passwd = input('请输入密码：')
            l1 = []
            with open('users1', 'r') as f:
                for i in f.readlines():
                    l1.append(i.rstrip('\n'))
            if username == l1[0] and passwd == l1[1]:
                print('登陆成功！')
                login_status = True
                return func(*args, **kw)
            else:
                print('用户名或密码不正确！')
                return None
        else:
            return func(*args, **kw)
    return warrper

@login
def home():
    print('Welcome to home ....')

@login
def finance():
    print('Welcome to finance ....')

@login
def book():
    print('Welcome to book ....')

login_status = False
print('1:home\n2:finance\n3:book')
while True:
    choose=input('请选择需要浏览的版块：')
    if int(choose) == 1:
        home()
    elif int(choose) == 2:
        finance()
    elif int(choose) == 3:
        book()