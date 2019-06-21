from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """收藏列表"""

    def setUp(self):
        self.url = url + "/app/book/collect-list"

    def test_1(self):
        data = {'page_num': '',
                'page_size': '',
                'deviceid': '',
                'channel': '',
                'from': '',
                'version': '',
                'access_token': '',
                'access_type': '',
                'sign': ''}
        res = requests.get(url=self.url, params=data)
        print(res.text)
        self.assertTrue(u"1123" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
