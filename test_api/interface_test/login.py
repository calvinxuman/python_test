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
        # self.login_001 = Login('13207140256', '8f7f8aca7230e2bbf851189f8da681e3443200fb', '5F46ABD0E6674F48859F8FCA025B6F69')
        # print('The test parameter is \n phone:'+self.login_001.phone + '\n password:' + self.login_001.password + '\n equipment:' +self.login_001.equipment)
        # self.result_001 = self.login_001.loginTest()

    def testLogin_001(self):
        self.login_001 = Login('13207140256', '8f7f8aca7230e2bbf851189f8da681e3443200fb',
                               '5F46ABD0E6674F48859F8FCA025B6F69')
        print(
            'The test parameter is \n phone:' + self.login_001.phone + '\n password:' + self.login_001.password + '\n equipment:' + self.login_001.equipment)
        self.result_001 = self.login_001.loginTest()
        self.assertEqual('登陆成功', self.result_001)

    def testLogin_002(self):
        self.login_002 = Login('13207140256', '8f7f8aca7230e2bbe851189f8da681e3443200fb',
                                   '5F46ABD0E6674F48859F8FCA025B6F69')
        print(
            'The test parameter is \n phone:' + self.login_002.phone + '\n password:' + self.login_002.password + '\n equipment:' + self.login_002.equipment)
        self.result_002 = self.login_002.loginTest()
        self.assertEqual('登陆成功', self.result_002)

    def tearDown(self):
        print('test have done!')


if __name__ == '__main__':
    unittest.main()
