import unittest
from active_cookie import get_hot_cookie


class BasicTestSuite(unittest.TestCase):

    def test_get_hot_cookie(self):
        active_cookies = get_hot_cookie("test.csv", "2018-12-09")
        self.assertEqual(str(active_cookies), 'AtY0laUfhglK3lC7')


if __name__ == '__main__':
     unittest.main()
