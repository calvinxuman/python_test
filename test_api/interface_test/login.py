# *-* coding:utf-8 *-*
import requests
import unittest
import xlrd


class Login(object):
    def __init__(self, phone, password, equipment):
        self.phone = phone
        self.password = password
        self.equipment = equipment

    def login_test(self):
        longurl = 'http://10.100.70.222' + '/galaxy/user/login' + '?phone=' + self.phone + '&password=' + \
                  self.password + '&equipment=' + self.equipment
        response = requests.post(longurl).json()['msg']
        return response


class LoginTest (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        list_phone = []
        list_password = []
        list_equipment = []
        dict_parameter = {'phone': list_phone, 'password': list_password, 'equipment': list_equipment}
        data = xlrd.open_workbook(
            r'C:\Users\Administrator\PycharmProjects\python_test\test_api\test_case\login_testcase.xlsx')
        table = data.sheet_by_name('login')
        for i in table.col_values(5, 3):
            if i != '':
                list_phone.append(i)
        for j in table.col_values(6, 3):
            if j != '':
                list_password.append(j)
        for k in table.col_values(7, 3):
            if k != '':
                list_equipment.append(k)
        print(dict_parameter['phone'][2])

    def test_login_001(self):
        # 未更换设备且用户名密码正确

        self.login_001 = Login('13207140256',
                               '8f7f8aca7230e2bbf851189f8da681e3443200fb', '5A9E2398DC25406E9A41F7B283E1A3FE')
        print('The Login_001 parameter is \n phone:' + self.login_001.phone + '\n password:' +
              self.login_001.password + '\n equipment:' + self.login_001.equipment)
        self.result_001 = self.login_001.login_test()
        self.assertEqual('登陆成功', self.result_001)

    def test_login_002(self):
        # 未更换设备，密码错误
        self.login_002 = Login('13207140256',
                               '111111', '5A9E2398DC25406E9A41F7B283E1A3FE')
        print('The Login_002 parameter is \n phone:' + self.login_002.phone + '\n password:' +
               self.login_002.password + '\n equipment:' + self.login_002.equipment)
        self.result_002 = self.login_002.login_test()
        self.assertEqual('密码错误', self.result_002)

    def test_login_003(self):
        # 手机号未注册
        self.login_003 = Login('13307140256',
                               '222222', '5A9E2398DC25406E9A41F7B283E1A3FE')
        print('The Login_003 parameter is \n phone:' + self.login_003.phone + '\n password:' +
               self.login_003.password + '\n equipment:' + self.login_003.equipment)
        self.result_003 = self.login_003.login_test()
        self.assertEqual('手机号未注册', self.result_003)

    def tearDown(self):
        pass
        print('done')


if __name__ == '__main__':
    unittest.main()
