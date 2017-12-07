import requests
import unittest
import json


class get_advertisement(unittest.TestCase):
    def setUp(self):
        print("start test advertisement")
        pass

    def  test_get_advertisement(self):
        self.url='http://10.100.60.222:80/galaxy/advertisement/selectAdvertisementOrRecommend'
        self.headers = {"Content-Type": "application/json"}
        r=requests.get(self.url,headers=self.headers)
        response=r.json()
        pictrue1=response['advertList'][0]['imgUrl']
        pictrue2 = response['advertList'][1]['imgUrl']
        pictrue3 = response['advertList'][2]['imgUrl']
        self.assertEqual(pictrue1,'http://www.cx9z.com/advert/zulin.png')
        self.assertEqual(pictrue2, 'http://www.cx9z.com/advert/tingche.png')
        self.assertEqual(pictrue3, 'http://www.cx9z.com/advert/daba.png')

    def tearDown(self):
        print("end test advertisement")
        pass

if __name__=='__main__':
    unittest.main()

