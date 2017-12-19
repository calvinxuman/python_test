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
    list_phone = []
    list_password = []
    list_equipment = []
    dict_parameter = {'phone': list_phone, 'password': list_password, 'equipment': list_equipment}
    @classmethod
    def setUpClass(cls):
        data = xlrd.open_workbook(
            r'C:\Users\Administrator\PycharmProjects\python_test\test_api\test_case\login_testcase.xlsx')
        table = data.sheet_by_name('login')
        for i in table.col_values(5, 3):
            if i != '':
                LoginTest.list_phone.append(str(i))
        for j in table.col_values(6, 3):
            if j != '':
                LoginTest.list_password.append(str(j))
        for k in table.col_values(7, 3):
            if k != '':
                LoginTest.list_equipment.append(str(k))
        print(LoginTest.dict_parameter)

    def test_login_001(self):
        # 未更换设备且用户名密码正确
        self.login_001 = Login(LoginTest.dict_parameter['phone'][0],
                               LoginTest.dict_parameter['password'][0],
                               LoginTest.dict_parameter['equipment'][0])
        print('The Login_001 parameter is \n phone:' + self.login_001.phone + '\n password:' +
              self.login_001.password + '\n equipment:' + self.login_001.equipment)
        self.result_001 = self.login_001.login_test()
        self.assertEqual('登陆成功', self.result_001)

    def test_login_002(self):
        # 未更换设备，密码错误
        self.login_002 = Login(LoginTest.dict_parameter['phone'][1],
                               LoginTest.dict_parameter['password'][1],
                               LoginTest.dict_parameter['equipment'][1])
        print('The Login_002 parameter is \n phone:' + self.login_002.phone + '\n password:' +
               self.login_002.password + '\n equipment:' + self.login_002.equipment)
        self.result_002 = self.login_002.login_test()
        self.assertEqual('密码错误', self.result_002)

    def test_login_003(self):
        # 手机号未注册
        self.login_003 = Login(LoginTest.dict_parameter['phone'][2],
                               LoginTest.dict_parameter['password'][2],
                               LoginTest.dict_parameter['equipment'][2])
        print('The Login_003 parameter is \n phone:' + self.login_003.phone + '\n password:' +
               self.login_003.password + '\n equipment:' + self.login_003.equipment)
        self.result_003 = self.login_003.login_test()
        self.assertEqual('手机号未注册', self.result_003)

    def tearDown(self):
        pass
        print('done')


if __name__ == '__main__':
    unittest.main()
