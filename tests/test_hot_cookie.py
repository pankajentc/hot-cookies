import unittest
from cookie import get_hot_cookie


class BasicTestSuite(unittest.TestCase):

    def test_get_hot_cookie(self):
        active_cookies = get_hot_cookie("test.csv", "2018-12-09")
        self.assertEqual(str(active_cookies), 'AtY0laUfhglK3lC7')

    def test_get_hot_cookie_multiple(self):
        active_cookies = get_hot_cookie("test.csv", "2018-12-08")
        self.assertMultiLineEqual(str(active_cookies), "4sMM2LxV07bPJzwf\n SAZuXPGUrfbcn5UA\n fbcn5UAVanZf6UtG")



if __name__ == '__main__':
     unittest.main()
