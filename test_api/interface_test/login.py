# *-* coding:utf-8 *-*
import requests
import unittest
import xlrd


class Login(object):
    def __init__(self, phone, password, equipment):
        self.phone = phone
        self.password = password
        self.equipment = equipment

    def loginTest(self):
        longurl = 'http://www.cx9z.com' + '/galaxy/user/login' + '?phone=' + self.phone + '&password=' + self.password + '&equipment=' + self.equipment
        response = requests.post(longurl).json()['msg']
        return response


class LoginTest(unittest.TestCase):
    def setUp(self):
        pass
        # data=xlrd.open_workbook(r'C:\Users\Administrator\PycharmProjects\python_test\test_api\test_case\login_testcase.xlsx')
        # table=data.sheet_by_name('Sheet1')



    def testLogin_001(self):
        # 未更换设备且用户名密码正确
        self.login_001 = Login('13207140256', '8f7f8aca7230e2bbf851189f8da681e3443200fb','5F46ABD0E6674F48859F8FCA025B6F69')
        print('The Login_001 parameter is \n phone:' + self.login_001.phone + '\n password:' + self.login_001.password + '\n equipment:' + self.login_001.equipment)
        self.result_001 = self.login_001.loginTest()
        self.assertEqual('登陆成功', self.result_001)

    def testLogin_002(self):
        # 未更换设备，密码错误
        self.login_002 = Login('13207140256', '111111','5F46ABD0E6674F48859F8FCA025B6F69')
        print( 'The Login_002 parameter is \n phone:' + self.login_002.phone + '\n password:' + self.login_002.password + '\n equipment:' + self.login_002.equipment)
        self.result_002 = self.login_002.loginTest()
        self.assertEqual('密码错误', self.result_002)

    def tearDown(self):
        print('test have done!')


if __name__ == '__main__':
    unittest.main()
