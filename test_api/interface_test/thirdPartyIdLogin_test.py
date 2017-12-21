#coding:utf-8
import requests
import xlrd
import unittest

class ThirdLogin():
    def __init__(self,unionedId,equipment):
        self.unionedId = unionedId
        self.equipment = equipment

    def third_party_login(self):
        self.base_url = 'http://10.100.70.222:80/galaxy/user/thirdPartyIdLogin'
        self.postdata = {'unionedId':self.unionedId,'equipment':self.equipment}
        response = requests.post(self.base_url,data=self.postdata).json()['msg']
        return response

class TestThirdLogin(unittest.TestCase):
    list_unionedId = []
    list_equipment = []
    dict_parameters = {'unionedId': list_unionedId, 'equipment': list_equipment}

    @classmethod
    def setUpClass(cls):
        data = xlrd.open_workbook(
            r'C:\Users\Administrator\PycharmProjects\python_test\test_api\test_case\login_testcase.xlsx')
        table = data.sheet_by_name('thirdPartyIdLogin')
        for i in table.col_values(5, 2):
            TestThirdLogin.list_unionedId.append(str(i))
        for j in table.col_values(6, 2):
            TestThirdLogin.list_equipment.append(str(j))
        # print(TestThirdLogin.dict_parameters)

    def test_thirdlogin_001(self):
        '''未更换设备，已绑定第三方'''
        self.thirdlogin_001 = ThirdLogin(TestThirdLogin.dict_parameters['unionedId'][0],
                                    TestThirdLogin.dict_parameters['equipment'][0])
        self.thirdlogin_result_001 = self.thirdlogin_001.third_party_login()
        print('test_thirdlogin_001的测试参数为：\n unionedId:' + TestThirdLogin.dict_parameters['unionedId'][0]
              + '\nequipment:' + TestThirdLogin.dict_parameters['equipment'][0])
        self.assertEqual('登录成功',self.thirdlogin_result_001)

    def test_thirdlogin_002(self):
        '''更换设备，已绑定第三方'''
        self.thirdlogin_002 = ThirdLogin(TestThirdLogin.dict_parameters['unionedId'][1],
                                    TestThirdLogin.dict_parameters['equipment'][1])
        self.thirdlogin_result_002 = self.thirdlogin_002.third_party_login()
        print('test_thirdlogin_002的测试参数为：\n unionedId:' + TestThirdLogin.dict_parameters['unionedId'][1]
              + '\nequipment:' + TestThirdLogin.dict_parameters['equipment'][1])
        self.assertEqual('设备不一致，需要发送验证码，调用发送验证码接口',self.thirdlogin_result_002)

    def test_thirdlogin_003(self):
        '''未绑定第三方'''
        self.thirdlogin_003 = ThirdLogin(TestThirdLogin.dict_parameters['unionedId'][2],
                                    TestThirdLogin.dict_parameters['equipment'][2])
        self.thirdlogin_result_003 = self.thirdlogin_003.third_party_login()
        print('test_thirdlogin_003的测试参数为：\n unionedId:' + TestThirdLogin.dict_parameters['unionedId'][2]
              + '\nequipment:' + TestThirdLogin.dict_parameters['equipment'][2])
        self.assertEqual('需要绑定手机号',self.thirdlogin_result_003)

    def test_thirdlogin_004(self):
        '''unionedId为空'''
        self.thirdlogin_004 = ThirdLogin(TestThirdLogin.dict_parameters['unionedId'][3],
                                    TestThirdLogin.dict_parameters['equipment'][3])
        self.thirdlogin_result_004 = self.thirdlogin_004.third_party_login()
        print('test_thirdlogin_004的测试参数为：\n unionedId:' + TestThirdLogin.dict_parameters['unionedId'][3]
              + '\nequipment:' + TestThirdLogin.dict_parameters['equipment'][3])
        self.assertEqual('唯一标识为空',self.thirdlogin_result_004)

    def test_thirdlogin_005(self):
        '''equipment为空'''
        self.thirdlogin_005 = ThirdLogin(TestThirdLogin.dict_parameters['unionedId'][4],
                                    TestThirdLogin.dict_parameters['equipment'][4])
        self.thirdlogin_result_005 = self.thirdlogin_005.third_party_login()
        print('test_thirdlogin_005的测试参数为：\n unionedId:' + TestThirdLogin.dict_parameters['unionedId'][4]
              + '\nequipment:' + TestThirdLogin.dict_parameters['equipment'][4])
        self.assertEqual('设备不一致，需要发送验证码，调用发送验证码接口',self.thirdlogin_result_005)


    def test_thirdlogin_006(self):
        '''SQL注入登录'''
        self.thirdlogin_006 = ThirdLogin(TestThirdLogin.dict_parameters['unionedId'][5],
                                         TestThirdLogin.dict_parameters['equipment'][5])
        self.thirdlogin_result_006 = self.thirdlogin_006.third_party_login()
        print('test_thirdlogin_006的测试参数为：\n unionedId:' + TestThirdLogin.dict_parameters['unionedId'][5]
              + '\nequipment:' + TestThirdLogin.dict_parameters['equipment'][5])
        self.assertEqual('设备不一致，需要发送验证码，调用发送验证码接口', self.thirdlogin_result_006)

    def tearDown(self):
        print('该用例测试完成')



if __name__ == '__main__':
    unittest.main()
