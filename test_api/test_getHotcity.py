import requests
import unittest

class test_getHotCity(unittest.TestCase):
    def setUp(self):
        print('start test get hotcity')


    def test_getHotCity(self):
        self.url='http://www.cx9z.com/galaxy/dicChina/getHotCity'
        self.headers='{"Content-Type": "application/json"}'
        r=requests.get(self.url,self.headers)
        response=r.json()
        hotcity1=response['hotCity']
        expect_hotcity=['北京', '天津', '上海', '南京', '杭州', '厦门', '青岛', '武汉', '长沙', '广州', '深圳', '成都']
        self.assertEqual(expect_hotcity,hotcity1)

    def tearDown(self):
        print('end test get hotcity')

if __name__=='__main__':
    unittest.main()