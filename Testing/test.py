import unittest
import main
# import script

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 10)

    def test_do_stuff2(self):
        test_param = 'hfgdf'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    # def test_check(self):
    #     check_num = 15
    #     res = main.check(check_num)
    #     self.assertEqual(res, 30)


if __name__ == '__main__' :
    unittest.main()