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
        longurl = 'http://10.100.70.220:8080' + '/galaxy/user/login' + '?phone=' + self.phone + '&password=' + \
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
        for i in table.col_values(5, 2):
            if i != '':
                LoginTest.list_phone.append(str(int(i)))
            else:
                LoginTest.list_phone.append('')
        for j in table.col_values(6, 2):
            if j != '':
                LoginTest.list_password.append(str(j))
            else:
                LoginTest.list_password.append('')
        for k in table.col_values(7, 2):
            if k != '':
                LoginTest.list_equipment.append(str(k))
            else:
                LoginTest.list_equipment.append('')
        # print(LoginTest.dict_parameter)

    def test_login_001(self):
        '''未更换设备且用户名密码正确'''
        self.login_001 = Login(LoginTest.dict_parameter['phone'][0],
                               LoginTest.dict_parameter['password'][0],
                               LoginTest.dict_parameter['equipment'][0])
        print('The Login_001 parameter is \n phone:' + self.login_001.phone + '\n password:' +
              self.login_001.password + '\n equipment:' + self.login_001.equipment)
        self.result_001 = self.login_001.login_test()
        self.assertEqual('登陆成功', self.result_001)

    def test_login_002(self):
        '''未更换设备，密码错误'''
        self.login_002 = Login(LoginTest.dict_parameter['phone'][1],
                               LoginTest.dict_parameter['password'][1],
                               LoginTest.dict_parameter['equipment'][1])
        print('The Login_002 parameter is \n phone:' + self.login_002.phone + '\n password:' +
               self.login_002.password + '\n equipment:' + self.login_002.equipment)
        self.result_002 = self.login_002.login_test()
        self.assertEqual('密码错误', self.result_002)

    def test_login_003(self):
        '''手机号未注册'''
        self.login_003 = Login(LoginTest.dict_parameter['phone'][2],
                               LoginTest.dict_parameter['password'][2],
                               LoginTest.dict_parameter['equipment'][2])
        print('The Login_003 parameter is \n phone:' + self.login_003.phone + '\n password:' +
               self.login_003.password + '\n equipment:' + self.login_003.equipment)
        self.result_003 = self.login_003.login_test()
        self.assertEqual('手机号未注册', self.result_003)

    def test_login_004(self):
        '''更换设备且用户名密码正确'''
        self.login_004 = Login(LoginTest.dict_parameter['phone'][3],
                               LoginTest.dict_parameter['password'][3],
                               LoginTest.dict_parameter['equipment'][3])
        print('The Login_004 parameter is \n phone:' + self.login_004.phone + '\n password:' +
               self.login_004.password + '\n equipment:' + self.login_004.equipment)
        self.result_004 = self.login_004.login_test()
        self.assertEqual('设备不一致，需要发送验证码，调用发送验证码接口', self.result_004)

    def test_login_005(self):
        '''更换设备,密码错误'''
        self.login_005 = Login(LoginTest.dict_parameter['phone'][4],
                               LoginTest.dict_parameter['password'][4],
                               LoginTest.dict_parameter['equipment'][4])
        print('The Login_005 parameter is \n phone:' + self.login_005.phone + '\n password:' +
               self.login_005.password + '\n equipment:' + self.login_005.equipment)
        self.result_005 = self.login_005.login_test()
        self.assertEqual('密码错误', self.result_005)


    def test_login_006(self):
        '''SQL注入登录'''
        self.login_006 = Login(LoginTest.dict_parameter['phone'][5],
                               LoginTest.dict_parameter['password'][5],
                               LoginTest.dict_parameter['equipment'][5])
        print('The Login_006 parameter is \n phone:' + self.login_006.phone + '\n password:' +
               self.login_006.password + '\n equipment:' + self.login_006.equipment)
        self.result_006 = self.login_006.login_test()
        self.assertEqual('密码错误', self.result_006)

    def test_login_007(self):
        '''手机号为空'''
        self.login_007 = Login(LoginTest.dict_parameter['phone'][6],
                               LoginTest.dict_parameter['password'][6],
                               LoginTest.dict_parameter['equipment'][6])
        print('The Login_007 parameter is \n phone:' + self.login_007.phone + '\n password:' +
               self.login_007.password + '\n equipment:' + self.login_007.equipment)
        self.result_007 = self.login_007.login_test()
        self.assertEqual('账号,密码不可为空', self.result_007)

    def test_login_008(self):
        '''密码为空'''
        self.login_008 = Login(LoginTest.dict_parameter['phone'][7],
                               LoginTest.dict_parameter['password'][7],
                               LoginTest.dict_parameter['equipment'][7])
        print('The Login_008 parameter is \n phone:' + self.login_008.phone + '\n password:' +
               self.login_008.password + '\n equipment:' + self.login_008.equipment)
        self.result_008 = self.login_008.login_test()
        self.assertEqual('账号,密码不可为空', self.result_008)

    def tearDown(self):
        pass
        print('done')


if __name__ == '__main__':
    unittest.main()
